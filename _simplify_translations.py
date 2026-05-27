#!/usr/bin/env python3
"""
Post-process the Hindi and Kannada translated HTML files to use simpler,
everyday spoken language instead of the literary / over-Sanskritized forms
that Google Translate tends to produce.

Strategy
--------
- Open each translated HTML.
- Walk every visible text node (skipping <script>, <style>, <code>, <pre>).
- Apply a curated word->word replacement dictionary using a regex that
  requires the match to NOT be flanked by another Devanagari/Kannada
  letter, so we only replace standalone words and don't break compound
  inflected forms (e.g., "ತಂತ್ರವು" stays intact even if "ತಂತ್ರ" is in the dict).
- Also apply a few attribute-level replacements (title, alt, aria-label,
  the <title> tag, meta description) so headings/tooltips read naturally.
- Write the file back in place.

Principle: only replace words that have a clearly more common everyday
equivalent. Words that are already common in modern speech (अभ्यास, ज्ञान,
ಧ್ಯಾನ, ಅನುಭವ, etc.) are left alone.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).parent

SKIP_TAGS = {"script", "style", "noscript", "code", "pre"}
TEXT_ATTRS = ("title", "alt", "placeholder", "aria-label")

# ---------------------------------------------------------------------------
# Hindi: literary/Sanskritized -> everyday spoken
# ---------------------------------------------------------------------------
HI_REPLACEMENTS: dict[str, str] = {
    # Conjunctions / connectors
    "किन्तु": "लेकिन",
    "परन्तु": "लेकिन",
    "परंतु": "लेकिन",
    "एवं": "और",
    "तथा": "और",
    "अथवा": "या",
    "तत्पश्चात": "उसके बाद",
    "तदुपरांत": "उसके बाद",
    "पश्चात": "बाद",
    "तत्क्षण": "तुरंत",
    "पुनः": "फिर",
    "कदाचित": "शायद",
    "सम्भवतः": "शायद",
    "संभवतः": "शायद",
    # Quantifiers / intensifiers
    "अत्यन्त": "बहुत",
    "अत्यंत": "बहुत",
    "अत्यधिक": "बहुत ज़्यादा",
    "अधिकांश": "ज़्यादातर",
    "अधिकांशतः": "ज़्यादातर",
    "सर्वथा": "पूरी तरह",
    "सर्वदा": "हमेशा",
    "मात्र": "सिर्फ़",
    # "केवल" is fine, leave it
    "सम्पूर्ण": "पूरा",
    # "संपूर्ण" left alone — it's commonly used
    "पूर्णतः": "पूरी तरह",
    "सम्पूर्णतः": "पूरी तरह",
    "आंशिक": "थोड़ा",
    # Quality / difficulty
    "कठिन": "मुश्किल",
    "सरल": "आसान",
    "सुलभ": "आसान",
    "दुर्गम": "मुश्किल",
    "तीव्र": "तेज़",
    "तीव्रता": "तेज़ी",
    "मन्द": "धीमा",
    # Necessity / importance
    "आवश्यक": "ज़रूरी",
    "अनिवार्य": "ज़रूरी",
    "महत्त्वपूर्ण": "ज़रूरी",
    "महत्वपूर्ण": "ज़रूरी",
    "महत्त्व": "अहमियत",
    "महत्व": "अहमियत",
    "विशिष्ट": "ख़ास",
    # Spatial / positional
    "आन्तरिक": "अंदर का",
    "आंतरिक": "अंदर का",
    "बाह्य": "बाहर का",
    "भीतर": "अंदर",
    "अन्धकार": "अंधेरा",
    "अंधकार": "अंधेरा",
    "विपरीत": "उल्टा",
    # State / presence
    "उपस्थित": "मौजूद",
    "अनुपस्थित": "ग़ैर-हाज़िर",
    "विद्यमान": "मौजूद",
    "अभिव्यक्त": "ज़ाहिर",
    "अभिव्यक्ति": "ज़ाहिर होना",
    "प्रादुर्भाव": "शुरुआत",
    # Cause / effect
    "परिणाम": "नतीजा",
    "फलस्वरूप": "नतीजे में",
    "प्रभाव": "असर",
    "कारणवश": "वजह से",
    # Mind / thought
    "मनन": "सोच",
    "चिन्तन": "सोच",
    "चिंतन": "सोच",
    "जागृत": "जगा हुआ",
    # "जागरूक", "जागरूकता" — common modern Hindi, leave
    "सतर्क": "सावधान",
    # Action / handling
    "त्याग": "छोड़ना",
    "परित्याग": "छोड़ देना",
    "ग्रहण": "अपनाना",
    # State words
    "दशा": "हाल",
    # "अवस्था", "परिस्थिति" — commonly used, leave
    "गतिमान": "चलता हुआ",
    "अस्थिर": "हिलता हुआ",
    # Knowledge
    "विद्या": "जानकारी",
    "अविद्या": "अनजानापन",
    # Connection
    "सम्बद्ध": "जुड़ा हुआ",
    # Others
    "प्रथम": "पहला",
    "द्वितीय": "दूसरा",
    "तृतीय": "तीसरा",
}

# ---------------------------------------------------------------------------
# Kannada: literary/Sanskritized -> everyday spoken
# ---------------------------------------------------------------------------
KN_REPLACEMENTS: dict[str, str] = {
    # Conjunctions / connectors
    "ಪರಂತು": "ಆದರೆ",
    "ಕಿಂತು": "ಆದರೆ",
    "ತಥಾ": "ಮತ್ತು",
    "ಏವಂ": "ಮತ್ತು",
    "ಪುನಃ": "ಮತ್ತೆ",
    "ಸರ್ವದಾ": "ಯಾವಾಗಲೂ",
    "ಕದಾಪಿ": "ಎಂದಿಗೂ",
    "ಪಶ್ಚಾತ್": "ನಂತರ",
    # Quantifiers / intensifiers
    "ಅತ್ಯಂತ": "ತುಂಬಾ",
    "ಅತ್ಯಧಿಕ": "ತುಂಬಾ ಹೆಚ್ಚು",
    "ಅಧಿಕಾಂಶ": "ಹೆಚ್ಚಿನ",
    "ಪರಿಪೂರ್ಣ": "ಪೂರ್ತಿ",
    "ಸಂಪೂರ್ಣವಾಗಿ": "ಪೂರ್ತಿಯಾಗಿ",
    # "ಸಂಪೂರ್ಣ" left alone — widely used
    # Begin / end (and common verb inflections of ಪ್ರಾರಂಭ)
    "ಪ್ರಾರಂಭಿಸುತ್ತೀರಿ": "ಶುರು ಮಾಡುತ್ತೀರಿ",
    "ಪ್ರಾರಂಭಿಸುತ್ತೇನೆ": "ಶುರು ಮಾಡುತ್ತೇನೆ",
    "ಪ್ರಾರಂಭಿಸುತ್ತೇವೆ": "ಶುರು ಮಾಡುತ್ತೇವೆ",
    "ಪ್ರಾರಂಭಿಸುತ್ತಾರೆ": "ಶುರು ಮಾಡುತ್ತಾರೆ",
    "ಪ್ರಾರಂಭಿಸುತ್ತದೆ": "ಶುರುವಾಗುತ್ತದೆ",
    "ಪ್ರಾರಂಭಿಸುತ್ತವೆ": "ಶುರುವಾಗುತ್ತವೆ",
    "ಪ್ರಾರಂಭಿಸುವುದು": "ಶುರು ಮಾಡುವುದು",
    "ಪ್ರಾರಂಭಿಸುವುದಕ್ಕೆ": "ಶುರು ಮಾಡಲು",
    "ಪ್ರಾರಂಭಿಸುವ": "ಶುರು ಮಾಡುವ",
    "ಪ್ರಾರಂಭಿಸಬೇಡಿ": "ಶುರು ಮಾಡಬೇಡಿ",
    "ಪ್ರಾರಂಭಿಸಬೇಕು": "ಶುರು ಮಾಡಬೇಕು",
    "ಪ್ರಾರಂಭಿಸಲು": "ಶುರು ಮಾಡಲು",
    "ಪ್ರಾರಂಭಿಸಿದ": "ಶುರು ಮಾಡಿದ",
    "ಪ್ರಾರಂಭಿಸಿದರು": "ಶುರು ಮಾಡಿದರು",
    "ಪ್ರಾರಂಭಿಸಿ": "ಶುರು ಮಾಡಿ",
    "ಪ್ರಾರಂಭವಾಗುತ್ತದೆ": "ಶುರುವಾಗುತ್ತದೆ",
    "ಪ್ರಾರಂಭವಾಗುವ": "ಶುರುವಾಗುವ",
    "ಪ್ರಾರಂಭವಾಗಿಲ್ಲ": "ಶುರುವಾಗಿಲ್ಲ",
    "ಪ್ರಾರಂಭವಾಗಲು": "ಶುರುವಾಗಲು",
    "ಪ್ರಾರಂಭವಾದ": "ಶುರುವಾದ",
    "ಪ್ರಾರಂಭದಲ್ಲಿ": "ಶುರುವಿನಲ್ಲಿ",
    "ಪ್ರಾರಂಭದಿಂದ": "ಶುರುವಿನಿಂದ",
    "ಪ್ರಾರಂಭಕ್ಕೆ": "ಶುರುವಿಗೆ",
    "ಪ್ರಾರಂಭದ": "ಶುರುವಿನ",
    "ಪ್ರಾರಂಭ": "ಶುರು",
    "ಆರಂಭ": "ಶುರು",
    "ಸಮಾಪ್ತಿ": "ಮುಗಿಯುವುದು",
    "ಸಮಾಪ್ತ": "ಮುಗಿದಿದೆ",
    "ಮುಕ್ತಾಯ": "ಮುಗಿಯುವಿಕೆ",
    # Inner / outer adverb forms
    "ಆಂತರಿಕವಾಗಿ": "ಒಳಗಡೆ",
    "ಬಾಹ್ಯವಾಗಿ": "ಹೊರಗಡೆ",
    # Awareness adverb / verb forms
    "ಜಾಗೃತರಾಗಿರಲು": "ಎಚ್ಚರವಾಗಿರಲು",
    "ಜಾಗೃತರಾಗಿರಿ": "ಎಚ್ಚರವಾಗಿರಿ",
    "ಜಾಗೃತರಾಗಿ": "ಎಚ್ಚರವಾಗಿ",
    "ಜಾಗೃತರಾಗುವ": "ಎಚ್ಚರವಾಗುವ",
    # Thought variants
    "ಚಿಂತನೆಯಿಲ್ಲದೆ": "ಯೋಚನೆಯಿಲ್ಲದೆ",
    "ಚಿಂತನೆಯಲ್ಲಿ": "ಯೋಚನೆಯಲ್ಲಿ",
    "ಚಿಂತನೆಯಿಂದ": "ಯೋಚನೆಯಿಂದ",
    "ಚಿಂತನೆಗೆ": "ಯೋಚನೆಗೆ",
    "ಚಿಂತನೆಯ": "ಯೋಚನೆಯ",
    # Perfect / complete inflections
    "ಪರಿಪೂರ್ಣವಾಗಿ": "ಪೂರ್ಣವಾಗಿ",
    # Necessity / importance
    "ಆವಶ್ಯಕ": "ಬೇಕಾದ",
    "ಅವಶ್ಯಕ": "ಬೇಕಾದ",
    "ಅವಶ್ಯಕತೆ": "ಬೇಕು",
    "ಅನಿವಾರ್ಯ": "ಬೇಕೇಬೇಕು",
    "ಮಹತ್ವ": "ಮುಖ್ಯ",
    "ಮಹತ್ವದ": "ಮುಖ್ಯವಾದ",
    "ಮಹತ್ವಪೂರ್ಣ": "ಮುಖ್ಯ",
    "ವಿಶಿಷ್ಟ": "ವಿಶೇಷ",
    # Quality / difficulty
    "ಕಠಿಣ": "ಕಷ್ಟ",
    "ಕ್ಲಿಷ್ಟ": "ಕಷ್ಟ",
    "ಸಹಜ": "ಸುಲಭ",
    # Spatial
    "ಆಂತರಿಕ": "ಒಳಗಿನ",
    "ಬಾಹ್ಯ": "ಹೊರಗಿನ",
    "ಪೂರ್ವ": "ಮೊದಲು",
    # Mind / awareness
    "ಜಾಗೃತ": "ಎಚ್ಚರ",
    "ಜಾಗೃತಿ": "ಎಚ್ಚರ",
    "ಸಚೇತನ": "ಎಚ್ಚರವಾಗಿರುವ",
    "ಪ್ರಜ್ಞಾವಂತ": "ಎಚ್ಚರವಾಗಿರುವ",
    "ಚಿಂತನೆ": "ಯೋಚನೆ",
    "ಮನನ": "ಯೋಚನೆ",
    # Self / nature
    # "ಸ್ವಯಂ" left — modern usage common
    "ಸ್ವಭಾವ": "ಗುಣ",
    "ಸ್ವರೂಪ": "ರೂಪ",
    # Cause / effect
    "ಫಲ": "ಫಲಿತಾಂಶ",
    "ಪ್ರಭಾವ": "ಪರಿಣಾಮ",
    # State
    "ದಶೆ": "ಸ್ಥಿತಿ",
    # "ಪರಿಸ್ಥಿತಿ", "ಸ್ಥಿತಿ" — common, leave
    # Numbers
    "ಪ್ರಥಮ": "ಮೊದಲನೆ",
    "ದ್ವಿತೀಯ": "ಎರಡನೆ",
    "ತೃತೀಯ": "ಮೂರನೆ",
}

# ---------------------------------------------------------------------------
# Compile regexes once. Boundary = not flanked by another letter from the
# same script (Devanagari U+0900-U+097F or Kannada U+0C80-U+0CFF).
# ---------------------------------------------------------------------------
def compile_replacements(mapping: dict[str, str], script_range: str) -> list[tuple[re.Pattern, str]]:
    # sort keys longest-first so longer phrases match before their substrings
    entries = sorted(mapping.items(), key=lambda kv: -len(kv[0]))
    compiled = []
    for src, tgt in entries:
        pattern = re.compile(
            rf"(?<![{script_range}]){re.escape(src)}(?![{script_range}])"
        )
        compiled.append((pattern, tgt))
    return compiled


HI_PATTERNS = compile_replacements(HI_REPLACEMENTS, r"\u0900-\u097F")
KN_PATTERNS = compile_replacements(KN_REPLACEMENTS, r"\u0C80-\u0CFF")


def simplify_text(text: str, patterns: list[tuple[re.Pattern, str]]) -> str:
    if not text:
        return text
    for pat, tgt in patterns:
        text = pat.sub(tgt, text)
    # Apply Kannada stem-based rewrites for ಪ್ರಾರಂಭ family
    # (catches every inflected form in one shot, regardless of suffix).
    if patterns is KN_PATTERNS:
        # verb form "ಪ್ರಾರಂಭಿಸ-" = "to start (something)" -> "ಶುರು ಮಾಡ-"
        text = _KN_PRARAMBHA_ISA.sub(r"ಶುರು ಮಾಡ\1", text)
        # noun "ಪ್ರಾರಂಭ" with case markers/possessives -> "ಶುರು"
        # Captures Kannada vowel-signs/consonant-clusters that follow as the
        # case-marker tail. We just replace the stem ಪ್ರಾರಂಭ -> ಶುರು.
        text = _KN_PRARAMBHA_NOUN.sub(r"ಶುರು\1", text)
    return text


# Stem-based rewrites for Kannada ಪ್ರಾರಂಭ family.
# The verb "to start (something)": ಪ್ರಾರಂಭಿಸು + tense markers
_KN_PRARAMBHA_ISA = re.compile(r"(?<![\u0C80-\u0CFF])ಪ್ರಾರಂಭಿಸ([\u0C80-\u0CFF]*)")
# The noun "beginning" / verb "to begin" (intransitive ವಾಗು auxiliary): all suffixes
# This covers ಪ್ರಾರಂಭವಾಗ-, ಪ್ರಾರಂಭವಾದ-, ಪ್ರಾರಂಭವನ್ನು, ಪ್ರಾರಂಭದ-, ಪ್ರಾರಂಭವು, ಪ್ರಾರಂಭ
_KN_PRARAMBHA_NOUN = re.compile(r"(?<![\u0C80-\u0CFF])ಪ್ರಾರಂಭ([\u0C80-\u0CFF]*)")


def process_file(path: Path, patterns: list[tuple[re.Pattern, str]], label: str) -> None:
    print(f"\n=== Simplifying {label}: {path.name} ===")
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    # Text nodes
    text_changes = 0
    for s in list(soup.find_all(string=True)):
        # skip script/style/etc
        bad = False
        for parent in s.parents:
            if isinstance(parent, Tag) and parent.name in SKIP_TAGS:
                bad = True
                break
        if bad:
            continue
        original = str(s)
        new = simplify_text(original, patterns)
        if new != original:
            s.replace_with(NavigableString(new))
            text_changes += 1
    print(f"  text nodes changed: {text_changes}")

    # Attribute values
    attr_changes = 0
    for tag in soup.find_all(True):
        for a in TEXT_ATTRS:
            v = tag.get(a)
            if isinstance(v, str):
                new = simplify_text(v, patterns)
                if new != v:
                    tag[a] = new
                    attr_changes += 1
        if tag.name == "meta":
            v = tag.get("content")
            if isinstance(v, str):
                new = simplify_text(v, patterns)
                if new != v:
                    tag["content"] = new
                    attr_changes += 1
    print(f"  attribute values changed: {attr_changes}")

    # Application/json scripts: simplify the keys we previously translated
    json_changes = 0
    import json as _json
    for s in soup.find_all("script"):
        t = (s.get("type") or "").lower()
        if t != "application/json":
            continue
        raw = s.string or ""
        try:
            data = _json.loads(raw)
        except Exception:
            continue
        def walk(node):
            nonlocal json_changes
            if isinstance(node, dict):
                for k in list(node.keys()):
                    v = node[k]
                    if isinstance(v, str):
                        new = simplify_text(v, patterns)
                        if new != v:
                            node[k] = new
                            json_changes += 1
                    else:
                        walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(data)
        s.string = _json.dumps(data, ensure_ascii=False)
    print(f"  json string changes: {json_changes}")

    path.write_text(str(soup), encoding="utf-8")
    print(f"  wrote {path.name} ({path.stat().st_size:,} bytes)")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    targets = [
        ("hi", ROOT / "vigyan-bhairav-tantra-complete-book-hindi.html", HI_PATTERNS),
        ("kn", ROOT / "vigyan-bhairav-tantra-complete-book-kannada.html", KN_PATTERNS),
    ]
    for code, path, patterns in targets:
        if only and only != code:
            continue
        if not path.exists():
            print(f"  ! {path} missing, skipping")
            continue
        process_file(path, patterns, code)


if __name__ == "__main__":
    main()
