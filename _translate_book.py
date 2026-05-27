#!/usr/bin/env python3
"""
Translate the visible text of vigyan-bhairav-tantra-complete-book.html
into Hindi (hi) and Kannada (kn), preserving all HTML structure,
CSS, JavaScript, attributes, anchors, and IDs.

Strategy
--------
1. Parse the HTML with BeautifulSoup using the html.parser (preserves
   whitespace and existing structure better than lxml for our purpose).
2. Walk every NavigableString that is NOT inside <script>, <style>,
   <code>, <pre>, or any element whose ancestor opted out via the
   `data-no-translate` attribute (we don't actually use this, but we
   skip script/style robustly).
3. Translate certain common attributes that hold visible text:
   - title, alt, placeholder, aria-label, content (only meta description /
     og:description / twitter:description), value (only on input[type=button|submit])
4. Translate the contents of <title> tag.
5. Update <html lang="..."> to the target language.
6. Inject a small CSS rule so Indic scripts use a comfortable font stack
   that doesn't break the existing serif aesthetic.
7. Do NOT touch:
   - JSON inside <script type="application/json"> (would break parsing
     unless we deeply translate the right keys; the user-visible mapping
     for those is rendered on screen via JS). We DO translate the values
     of `display` and `rep_short` because those are shown in the UI.
8. Batch translate strings (deep-translator GoogleTranslator handles
   roughly ~5000 chars per call). We chunk to ~4500 to be safe.
9. Cache identical strings so we don't translate "Read more" 200 times.

This script is idempotent on a fresh source file. Re-running just
overwrites the output.
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, NavigableString, Tag
from deep_translator import GoogleTranslator

ROOT = Path(__file__).parent
SRC = ROOT / "vigyan-bhairav-tantra-complete-book.html"

TARGETS = {
    "hi": ROOT / "vigyan-bhairav-tantra-complete-book-hindi.html",
    "kn": ROOT / "vigyan-bhairav-tantra-complete-book-kannada.html",
}

# Tags whose text content is NOT user-visible (do not translate inside)
SKIP_TAGS = {"script", "style", "noscript", "code", "pre"}

# Attributes that hold visible text and should be translated
TEXT_ATTRS = ("title", "alt", "placeholder", "aria-label")

# Indic-friendly font stack appended for hi/kn output
INDIC_FONT_OVERRIDE = """
/* === Indic script readability override (auto-injected) === */
:root { --indic-serif: "Noto Serif Devanagari", "Noto Serif Kannada",
                       "Tiro Devanagari Hindi", "Tiro Kannada",
                       "Iowan Old Style", "Palatino Linotype", Palatino,
                       "Hoefler Text", Georgia, serif; }
body, .sutra blockquote, p, h1, h2, h3, h4, h5, h6, li, dt, dd, blockquote,
figcaption, summary { font-family: var(--indic-serif) !important; }
""".strip()

INDIC_FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Noto+Serif+Devanagari:wght@400;500;600;700&'
    'family=Noto+Serif+Kannada:wght@400;500;600;700&display=swap" rel="stylesheet">'
)


def is_translatable_string(s: NavigableString) -> bool:
    """A string is translatable if it has any letters and is not inside a skipped tag."""
    text = str(s)
    if not text or text.isspace():
        return False
    # Must contain at least one letter (skip pure punctuation/numbers/symbols)
    if not re.search(r"[A-Za-z]", text):
        return False
    # Skip if any ancestor is a non-translatable tag
    for parent in s.parents:
        if isinstance(parent, Tag) and parent.name in SKIP_TAGS:
            return False
    return True


def collect_strings(soup: BeautifulSoup) -> list[NavigableString]:
    """All NavigableStrings in the document that should be translated."""
    out: list[NavigableString] = []
    for s in soup.find_all(string=True):
        if is_translatable_string(s):
            out.append(s)
    return out


def collect_attrs(soup: BeautifulSoup) -> list[tuple[Tag, str]]:
    """All (tag, attr_name) pairs whose value should be translated."""
    pairs: list[tuple[Tag, str]] = []
    for tag in soup.find_all(True):
        for a in TEXT_ATTRS:
            v = tag.get(a)
            if isinstance(v, str) and v.strip() and re.search(r"[A-Za-z]", v):
                pairs.append((tag, a))
        # meta description-style content
        if tag.name == "meta":
            name = (tag.get("name") or tag.get("property") or "").lower()
            if name in {
                "description",
                "og:description",
                "og:title",
                "twitter:description",
                "twitter:title",
            }:
                v = tag.get("content")
                if isinstance(v, str) and v.strip() and re.search(r"[A-Za-z]", v):
                    pairs.append((tag, "content"))
        # input[value] for buttons
        if tag.name == "input":
            t = (tag.get("type") or "").lower()
            if t in {"button", "submit", "reset"}:
                v = tag.get("value")
                if isinstance(v, str) and v.strip() and re.search(r"[A-Za-z]", v):
                    pairs.append((tag, "value"))
    return pairs


# JSON inside <script type="application/json"> — we will translate specific keys
JSON_TRANSLATE_KEYS = {"display", "rep_short"}


def collect_json_strings(soup: BeautifulSoup) -> list[tuple[Tag, list[tuple[list, str]]]]:
    """Return list of (script_tag, [(path, original_value), ...])."""
    results = []
    for s in soup.find_all("script"):
        t = (s.get("type") or "").lower()
        if t != "application/json":
            continue
        raw = s.string or ""
        try:
            data = json.loads(raw)
        except Exception:
            continue
        items: list[tuple[list, str]] = []

        def walk(node, path):
            if isinstance(node, dict):
                for k, v in node.items():
                    if k in JSON_TRANSLATE_KEYS and isinstance(v, str) and v.strip():
                        items.append((path + [k], v))
                    else:
                        walk(v, path + [k])
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, path + [i])

        walk(data, [])
        if items:
            results.append((s, data, items))
    return results


def chunked(seq: list[str], max_chars: int = 4500) -> Iterable[list[str]]:
    """Group strings so each batch joined with the SEP fits under max_chars."""
    SEP = "\n<<<__SEP__>>>\n"
    cur: list[str] = []
    cur_len = 0
    for s in seq:
        add = len(s) + len(SEP)
        if cur and cur_len + add > max_chars:
            yield cur
            cur, cur_len = [], 0
        cur.append(s)
        cur_len += add
    if cur:
        yield cur


def translate_unique(unique: list[str], target: str) -> dict[str, str]:
    """Translate a list of unique source strings; return source->target map."""
    SEP = "\n<<<__SEP__>>>\n"
    translator = GoogleTranslator(source="en", target=target)
    mapping: dict[str, str] = {}
    total = len(unique)
    done = 0
    for batch in chunked(unique, max_chars=4500):
        joined = SEP.join(batch)
        # retry up to 4 times
        last_err = None
        for attempt in range(4):
            try:
                out = translator.translate(joined)
                break
            except Exception as e:
                last_err = e
                time.sleep(1.5 * (attempt + 1))
        else:
            # If a whole batch fails, fall back to per-item with retries
            print(f"  ! batch failed ({last_err}); falling back to per-item", flush=True)
            out = None

        if out is None:
            parts = []
            for item in batch:
                for attempt in range(4):
                    try:
                        parts.append(translator.translate(item) or item)
                        break
                    except Exception:
                        time.sleep(1.5 * (attempt + 1))
                else:
                    parts.append(item)  # give up, keep original
        else:
            parts = out.split(SEP)
            if len(parts) != len(batch):
                # The separator got mangled by Google. Fall back per item.
                parts = []
                for item in batch:
                    for attempt in range(4):
                        try:
                            parts.append(translator.translate(item) or item)
                            break
                        except Exception:
                            time.sleep(1.5 * (attempt + 1))
                    else:
                        parts.append(item)

        for src, tgt in zip(batch, parts):
            mapping[src] = tgt.strip() if isinstance(tgt, str) else src
        done += len(batch)
        print(f"  translated {done}/{total}", flush=True)
    return mapping


def translate_document(target: str, out_path: Path) -> None:
    print(f"\n=== Translating to {target} -> {out_path.name} ===", flush=True)
    src_html = SRC.read_text(encoding="utf-8")
    soup = BeautifulSoup(src_html, "html.parser")

    # 1. Collect all source strings
    text_nodes = collect_strings(soup)
    attr_pairs = collect_attrs(soup)
    json_blobs = collect_json_strings(soup)

    sources: set[str] = set()
    for s in text_nodes:
        sources.add(str(s))
    for tag, a in attr_pairs:
        sources.add(tag.get(a))
    for _tag, _data, items in json_blobs:
        for _path, v in items:
            sources.add(v)

    unique = sorted(sources)
    print(f"  unique strings to translate: {len(unique)}", flush=True)

    # 2. Translate (cached by uniqueness)
    mapping = translate_unique(unique, target)

    # 3. Apply to text nodes
    for s in text_nodes:
        original = str(s)
        translated = mapping.get(original, original)
        if translated != original:
            s.replace_with(NavigableString(translated))

    # 4. Apply to attributes
    for tag, a in attr_pairs:
        original = tag.get(a)
        translated = mapping.get(original, original)
        if translated and translated != original:
            tag[a] = translated

    # 5. Apply to JSON blobs
    for tag, data, items in json_blobs:
        for path, original in items:
            translated = mapping.get(original, original)
            # navigate path and set
            node = data
            for step in path[:-1]:
                node = node[step]
            node[path[-1]] = translated
        new_json = json.dumps(data, ensure_ascii=False)
        tag.string = new_json

    # 6. Update lang attribute on <html>
    html_tag = soup.find("html")
    if html_tag:
        html_tag["lang"] = target

    # 7. Inject Indic font stack (link + override style)
    head = soup.find("head")
    if head:
        # font link
        link_soup = BeautifulSoup(INDIC_FONT_LINK, "html.parser")
        for el in list(link_soup.contents):
            head.append(el)
        # override style block
        style_tag = soup.new_tag("style")
        style_tag.string = INDIC_FONT_OVERRIDE
        head.append(style_tag)

    out_path.write_text(str(soup), encoding="utf-8")
    print(f"  wrote {out_path} ({out_path.stat().st_size:,} bytes)", flush=True)


def main():
    if not SRC.exists():
        print(f"Source not found: {SRC}", file=sys.stderr)
        sys.exit(1)

    only = sys.argv[1] if len(sys.argv) > 1 else None
    for code, out_path in TARGETS.items():
        if only and only != code:
            continue
        translate_document(code, out_path)


if __name__ == "__main__":
    main()
