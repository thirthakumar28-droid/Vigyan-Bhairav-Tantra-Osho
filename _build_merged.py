#!/usr/bin/env python3
"""
Build a single merged HTML containing every Vigyan Bhairav Tantra technique
in Osho's book order.

Structure of the output:
  1.  Cover / master TOC
  2.  Preface              (= important-first-access-this.html  body)
  3.  About these techniques  (14 thematic intros, collapsible)
  4.  The 38 Osho chapters in order, each a section containing:
         · chapter title  (from canonical_112_sutras.json)
         · the 2..9 sutras in that chapter, in canonical order,
           with full commentary preserved from the thematic files
  5.  Appendix — Self-Discovery (= find-yourself.html body)
  6.  Footer

Output: vigyan-bhairav-tantra-complete-book.html
"""
import json, re, unicodedata, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT  = ROOT / 'vigyan-bhairav-tantra-complete-book.html'

# ──────────────────────────────────────────────────────────────────────
# 1.  Load canonical sutras
# ──────────────────────────────────────────────────────────────────────
canonical = json.loads((ROOT / 'canonical_112_sutras.json').read_text(encoding='utf-8'))


def normalize(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = (text.replace('&mdash;', ' ').replace('&ndash;', ' ')
                .replace('&nbsp;', ' ').replace('&rsquo;', "'")
                .replace('&lsquo;', "'").replace('&ldquo;', '"').replace('&rdquo;', '"')
                .replace('&amp;', '&'))
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = text.lower()
    text = re.sub(r'[^a-z ]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()


canonical_norm = [(normalize(s['sutra']), s) for s in canonical]


def find_sutra(text: str):
    norm = normalize(text)
    if not norm:
        return None
    for cnorm, cs in canonical_norm:
        if cnorm.startswith(norm[:60]) or norm.startswith(cnorm[:60]):
            return cs
    words = set(norm.split()[:14])
    best, score = None, 0.0
    for cnorm, cs in canonical_norm:
        cw = set(cnorm.split()[:14])
        if not cw: continue
        s = len(words & cw) / len(words | cw)
        if s > score: best, score = cs, s
    return best if score >= 0.45 else None


# ──────────────────────────────────────────────────────────────────────
# 2.  Parse thematic files
# ──────────────────────────────────────────────────────────────────────
HERO_RE  = re.compile(r'<header\s+class="hero">.*?</header>', re.DOTALL)
TECH_RE  = re.compile(r'<article\s+class="technique"[^>]*?data-tech="(\d+)"[^>]*>.*?</article>', re.DOTALL)
SUTRA_RE = re.compile(r'<blockquote\s+class="sutra"[^>]*>(.*?)</blockquote>', re.DOTALL)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.DOTALL)
EYEBROW_RE = re.compile(r'<div\s+class="eyebrow">.*?</div>', re.DOTALL)
JUMP_RE    = re.compile(r'<nav\s+class="jumplinks"[^>]*>.*?</nav>', re.DOTALL)
HOWTO_RE   = re.compile(r'<aside\s+class="howto-block">.*?</aside>', re.DOTALL)
BEGINNER_RE= re.compile(r'<aside\s+class="beginner-block">.*?</aside>', re.DOTALL)
GLOSSARY_RE= re.compile(r'<details\s+class="glossary-block">.*?</details>', re.DOTALL)
DISCLAIM_P_RE = re.compile(r'<p\s+class="disclaimer">.*?</p>', re.DOTALL)
SCRIPT_RE  = re.compile(r'<script[^>]*>.*?</script>', re.DOTALL)
STYLE_RE   = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL)
HEAD_RE    = re.compile(r'<head[^>]*>(.*?)</head>', re.DOTALL)
BODY_RE    = re.compile(r'<body[^>]*>(.*?)</body>', re.DOTALL)
MAIN_RE    = re.compile(r'<main[^>]*>(.*?)</main>', re.DOTALL)
H1_RE      = re.compile(r'<h1[^>]*>(.*?)</h1>', re.DOTALL)
LEDE_RE    = re.compile(r'<p\s+class="lede">(.*?)</p>', re.DOTALL)
META_RE    = re.compile(r'<p\s+class="meta">(.*?)</p>', re.DOTALL)


THEMATIC_FILES = sorted([
    f for f in ROOT.glob('vigyan-bhairav-*.html')
    if f.name not in ('vigyan-bhairav-find-yourself.html',
                      'vigyan-bhairav-tantra-complete-book.html')
])

themes = []          # {slug, title, lede, hero_html, techs:[…]}
all_techs = []       # flat list, every technique with its canonical num
local_to_canonical = {}   # ('breath', 4) → 4 (canonical sutra num)

for fp in THEMATIC_FILES:
    raw = fp.read_text(encoding='utf-8')
    slug = fp.stem.replace('vigyan-bhairav-', '').replace('-techniques', '')
    title = re.sub(r'\s*[—–-]\s*Vigyan Bhairav Tantra.*$', '',
                   (TITLE_RE.search(raw).group(1) if TITLE_RE.search(raw) else slug)).strip()
    title = html.unescape(title)

    hero_html = HERO_RE.search(raw).group(0) if HERO_RE.search(raw) else ''
    # Strip the per-file "Techniques in this file" jumplinks + per-file eyebrow.
    hero_html = JUMP_RE.sub('', hero_html)
    hero_html = EYEBROW_RE.sub('', hero_html)

    h1_m   = H1_RE.search(hero_html)
    lede_m = LEDE_RE.search(hero_html)
    file_h1   = (h1_m.group(1).strip() if h1_m else title)
    file_lede = (lede_m.group(1).strip() if lede_m else '')

    techs_in_file = []
    for tm in TECH_RE.finditer(raw):
        local = int(tm.group(1))
        block = tm.group(0)
        sutra_m = SUTRA_RE.search(block)
        sutra_raw = sutra_m.group(1) if sutra_m else ''
        match = find_sutra(sutra_raw)
        if not match:
            print(f"!! unmatched: {fp.name}  t{local}")
            continue

        # normalize chapter string (canonical JSON has stray \r\n in two entries)
        match = dict(match)
        match['chapter'] = re.sub(r'\s+', ' ', match['chapter']).strip()

        n = match['num']
        # Rewrite ids and references inside this block: t{local} → sutra-{n}
        new_block = block
        # data-tech
        new_block = re.sub(r'data-tech="\d+"', f'data-tech="{n}"', new_block)
        # data-fav="t{local}"
        new_block = re.sub(rf'data-fav="t{local}\b"', f'data-fav="sutra-{n}"', new_block)
        # id="t{local}" → id="sutra-{n}"
        new_block = re.sub(rf'\bid="t{local}"', f'id="sutra-{n}"', new_block)
        # href="#t{local}"
        new_block = re.sub(rf'href="#t{local}\b"', f'href="#sutra-{n}"', new_block)
        # "Technique X of 112" header → use canonical
        new_block = re.sub(r'<span>\s*Technique\s+\d+\s+of\s+112\s*</span>',
                           f'<span>Sutra {n} of 112</span>', new_block)

        rec = {
            'canonical': n,
            'chapter': match['chapter'],
            'short':   match['short'],
            'slug':    slug,
            'theme_title': file_h1,
            'html':    new_block,
        }
        techs_in_file.append(rec)
        all_techs.append(rec)
        local_to_canonical[(slug, local)] = n

    techs_in_file.sort(key=lambda t: t['canonical'])
    first_n = techs_in_file[0]['canonical'] if techs_in_file else 999

    # Build local→canonical mapping for this file, then rewrite any remaining
    # intra-file `#tN` cross-references in every technique block.
    file_map = {(slug, lo): ca for (s, lo), ca in local_to_canonical.items() if s == slug}
    def fix_local_links(html_text, smap=file_map, sl=slug):
        def _r(m):
            n = int(m.group(1))
            canon = smap.get((sl, n))
            return f'href="#sutra-{canon}"' if canon else m.group(0)
        return re.sub(r'href="#t(\d+)\b"', _r, html_text)
    for t in techs_in_file:
        t['html'] = fix_local_links(t['html'])
    hero_html = fix_local_links(hero_html)

    themes.append({
        'slug': slug,
        'title': file_h1,
        'lede': file_lede,
        'hero_html': hero_html,
        'first': first_n,
        'count': len(techs_in_file),
        'covers': sorted({t['canonical'] for t in techs_in_file}),
    })

themes.sort(key=lambda t: t['first'])
all_techs.sort(key=lambda t: t['canonical'])

# ── validate ──
present = {t['canonical'] for t in all_techs}
missing = sorted(set(range(1, 113)) - present)
assert not missing, f"missing sutras: {missing}"
assert len(all_techs) == 112, f"got {len(all_techs)}"
print(f"✓ all 112 sutras matched, {len(themes)} thematic groups, {len({t['chapter'] for t in all_techs})} Osho chapters")

# ──────────────────────────────────────────────────────────────────────
# 3.  Group by Osho chapter (preserving canonical order)
# ──────────────────────────────────────────────────────────────────────
chapters = []   # ordered list of {chapter_label, techs:[…]}
seen = []
for t in all_techs:
    ch = t['chapter']
    if ch not in seen:
        seen.append(ch)
        chapters.append({'chapter': ch, 'techs': []})
    chapters[-1]['techs'].append(t)

# ──────────────────────────────────────────────────────────────────────
# 4.  Pull the preface + self-discovery bodies
# ──────────────────────────────────────────────────────────────────────
preface_raw = (ROOT / 'important-first-access-this.html').read_text(encoding='utf-8')
preface_body = BODY_RE.search(preface_raw).group(1)
preface_body = SCRIPT_RE.sub('', preface_body)

selfdisc_raw = (ROOT / 'vigyan-bhairav-find-yourself.html').read_text(encoding='utf-8')
selfdisc_body = BODY_RE.search(selfdisc_raw).group(1)
selfdisc_body = SCRIPT_RE.sub('', selfdisc_body)

# strip any embedded progress-bar / floating control clusters / outer header.controls
for pat in (r'<div\s+class="progress"[^>]*>\s*</div>',
            r'<div\s+class="controls"[^>]*>.*?</div>',
            r'<nav\s+class="controls"[^>]*>.*?</nav>',
            r'<button[^>]*class="toc-toggle"[^>]*>.*?</button>',
            r'<main[^>]*>',           # stray opens
            r'</main>',               # stray closes (these files have unbalanced ones)
            r'<footer[^>]*>.*?</footer>',  # we provide our own footer
           ):
    preface_body  = re.sub(pat, '', preface_body, flags=re.DOTALL)
    selfdisc_body = re.sub(pat, '', selfdisc_body, flags=re.DOTALL)


# ──────────────────────────────────────────────────────────────────────
# 4b.  Rewrite cross-file links so they work in the merged document.
#      vigyan-bhairav-{slug}-techniques.html#tN  →  #sutra-M
#      vigyan-bhairav-{slug}-techniques.html      →  #about-{slug}
# ──────────────────────────────────────────────────────────────────────
def rewrite_links(text):
    def repl_anchor(m):
        slug, local = m.group(1), int(m.group(2))
        canon = local_to_canonical.get((slug, local))
        return f'#sutra-{canon}' if canon else m.group(0)
    text = re.sub(r"vigyan-bhairav-([a-z\-]+?)-techniques\.html#t(\d+)",
                  repl_anchor, text)
    text = re.sub(r"vigyan-bhairav-([a-z\-]+?)-techniques\.html",
                  lambda m: f'#about-{m.group(1)}', text)
    text = re.sub(r"important-first-access-this\.html", '#preface', text)
    text = re.sub(r"vigyan-bhairav-find-yourself\.html", '#self-discovery', text)
    text = re.sub(r"vigyan-bhairav-discover-yourself\.html", '#self-discovery', text)
    return text

preface_body  = rewrite_links(preface_body)
selfdisc_body = rewrite_links(selfdisc_body)
# Also rewrite within the about-cards (they include hero blocks with cross-links)
for th in themes:
    th['hero_html'] = rewrite_links(th['hero_html'])

# Final defensive sweep: any remaining `#tN` anchors are broken (point to local
# techniques that don't exist) — turn them into plain text.
def kill_dead_anchors(s):
    return re.sub(r'<a\s+href="#t\d+[^"]*"[^>]*>(.*?)</a>',
                  r'\1', s, flags=re.DOTALL)
preface_body  = kill_dead_anchors(preface_body)
selfdisc_body = kill_dead_anchors(selfdisc_body)
for th in themes:
    th['hero_html'] = kill_dead_anchors(th['hero_html'])
for t in all_techs:
    t['html'] = kill_dead_anchors(t['html'])

# Also collect each thematic file's CSS so we know we have full coverage.
# We'll use the breath file's CSS as the canonical theme, plus extras from others.
breath_raw = (ROOT / 'vigyan-bhairav-breath-techniques.html').read_text(encoding='utf-8')
canonical_style_inner = STYLE_RE.search(breath_raw).group(1)
canonical_style = '<style>\n' + canonical_style_inner + '\n</style>'

# Some files may have unique CSS for elements only they use; concatenate the rest
extra_styles = []
for fp in THEMATIC_FILES + [ROOT / 'important-first-access-this.html',
                            ROOT / 'vigyan-bhairav-find-yourself.html']:
    if fp.name == 'vigyan-bhairav-breath-techniques.html':
        continue
    raw = fp.read_text(encoding='utf-8')
    m = STYLE_RE.search(raw)
    if m:
        extra_styles.append(f'/* === styles from {fp.name} === */\n' + m.group(1))
extra_combined = '<style>\n' + '\n\n'.join(extra_styles) + '\n</style>'

# ──────────────────────────────────────────────────────────────────────
# 5.  Build the merged HTML
# ──────────────────────────────────────────────────────────────────────
def slug_chapter(label: str) -> str:
    s = re.sub(r'[\r\n]+', ' ', label).strip()
    s = re.sub(r'^\d+\.\s*', '', s)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    return s[:60]


# Master TOC ----------------------------------------------------------
toc_items = []
toc_items.append('<li><a href="#preface">Preface — Important: First Access This</a></li>')
toc_items.append('<li><a href="#about">About These Techniques (Category Overviews)</a></li>')
toc_items.append('<li class="toc-section">The 112 Techniques (in Osho\'s book order)</li>')
for ch in chapters:
    cid = 'ch-' + slug_chapter(ch['chapter'])
    nums = [t['canonical'] for t in ch['techs']]
    label = re.sub(r'[\r\n]+', ' ', html.unescape(ch['chapter'])).strip()
    rng = f"sutra {nums[0]}" if len(nums) == 1 else f"sutras {nums[0]}–{nums[-1]}"
    toc_items.append(
        f'<li><a href="#{cid}">{html.escape(label)}</a> '
        f'<span class="toc-meta">{rng} ({len(nums)})</span></li>'
    )
toc_items.append('<li><a href="#self-discovery">Appendix — Find Your Path (Self-Discovery)</a></li>')
TOC_HTML = '<ol class="master-toc">' + '\n'.join(toc_items) + '</ol>'

# About-These-Techniques section: 14 collapsible cards ----------------
about_cards = []
for th in themes:
    nums = th['covers']
    cid = f"about-{th['slug']}"
    rng = f"sutra {nums[0]}" if len(nums) == 1 else f"sutras {nums[0]}–{nums[-1]}"
    inner = th['hero_html']
    # the inner hero has its own <h1>, which we want demoted to h3 in this overview
    inner = re.sub(r'<h1\b', '<h3', inner, count=1)
    inner = re.sub(r'</h1>', '</h3>', inner, count=1)
    about_cards.append(f'''
<details class="about-card" id="{cid}">
  <summary><strong>{html.escape(th['title'])}</strong>
    <span class="card-meta">{rng} · {th['count']} techniques</span></summary>
  <div class="about-card-body">{inner}</div>
</details>''')


# Chapter sections ---------------------------------------------------
chapter_sections = []
for ch in chapters:
    cid   = 'ch-' + slug_chapter(ch['chapter'])
    label = re.sub(r'[\r\n]+', ' ', html.unescape(ch['chapter'])).strip()
    # canonical "chapter" looks like "3. Breath – A Bridge to the Universe"
    m = re.match(r'^(\d+)\.\s*(.*)$', label)
    if m:
        ch_num   = m.group(1)
        ch_title = m.group(2).strip()
    else:
        ch_num, ch_title = '', label
    nums = [t['canonical'] for t in ch['techs']]
    rng  = (f"Sutra {nums[0]}" if len(nums) == 1
            else f"Sutras {nums[0]}–{nums[-1]}")
    inner_techs = '\n'.join(t['html'] for t in ch['techs'])

    # Which thematic files do these techniques come from?
    contributing = sorted({t['slug'] for t in ch['techs']})
    contrib_links = ' · '.join(
        f'<a href="#about-{s}">{s}</a>' for s in contributing
    )
    chapter_sections.append(f'''
<section class="chapter" id="{cid}">
  <header class="chapter-head">
    <div class="eyebrow">Chapter {ch_num} · {rng} · {len(nums)} technique{'s' if len(nums)!=1 else ''}</div>
    <h2>{html.escape(ch_title)}</h2>
    <p class="chapter-meta">From thematic group{'s' if len(contributing)!=1 else ''}: {contrib_links}</p>
  </header>
  {inner_techs}
  <p class="back-to-top"><a href="#top">↑ Back to top</a></p>
</section>''')


# Some unifying styles in addition to the imported ones --------------
EXTRA_CSS = '''
<style>
/* === merged-book-only overrides === */
html{scroll-padding-top:80px}
.master-toc{list-style:none;padding-left:0;font-family:var(--sans);font-size:.95rem;line-height:1.85}
.master-toc li{padding:.15rem 0;border-bottom:1px dotted var(--rule)}
.master-toc li.toc-section{font-weight:700;color:var(--accent);
  border-bottom:1px solid var(--accent-soft);margin-top:1.2rem;padding:.4rem 0;
  font-size:.78rem;letter-spacing:.18em;text-transform:uppercase}
.master-toc a{color:var(--ink)}
.master-toc .toc-meta{color:var(--ink-faint);font-size:.8rem;margin-left:.4rem}

.book-cover{
  text-align:center;padding:5rem 1.5rem 4rem;
  border-bottom:1px solid var(--rule);margin-bottom:3rem;
}
.book-cover .eyebrow{font-family:var(--sans);font-size:.75rem;
  letter-spacing:.24em;text-transform:uppercase;color:var(--ink-faint)}
.book-cover h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.15;margin:1rem 0}
.book-cover .subtitle{color:var(--ink-soft);font-style:italic;margin:0 auto;max-width:36rem}
.book-cover .stats{margin-top:2rem;color:var(--ink-faint);font-family:var(--sans);font-size:.85rem}

.part-divider{
  margin:5rem auto 2rem;padding:1rem 0;border-top:1px solid var(--accent-soft);
  text-align:center;font-family:var(--sans);font-size:.78rem;letter-spacing:.2em;
  text-transform:uppercase;color:var(--accent);
}

.about-card{
  background:var(--bg-card);border:1px solid var(--rule);border-radius:8px;
  margin:1rem 0;padding:0;
}
.about-card>summary{
  list-style:none;cursor:pointer;padding:1rem 1.2rem;
  display:flex;justify-content:space-between;align-items:center;gap:1rem;
  font-family:var(--sans);font-size:1rem;
}
.about-card>summary::-webkit-details-marker{display:none}
.about-card>summary::after{content:"＋";color:var(--accent);font-size:1.2rem}
.about-card[open]>summary::after{content:"−"}
.about-card .card-meta{color:var(--ink-faint);font-size:.78rem;font-family:var(--sans)}
.about-card-body{padding:0 1.2rem 1.5rem;border-top:1px solid var(--rule)}
.about-card-body header.hero{padding:1.5rem 0 0;border:0;margin:0;text-align:left}
.about-card-body h3{font-size:1.4rem;margin:.6rem 0 1rem;color:var(--accent)}

.chapter{margin:0 0 4rem;padding:2rem 0 1rem;
  border-top:2px solid var(--accent-soft)}
.chapter-head{margin:0 0 2rem;text-align:center}
.chapter-head .eyebrow{font-family:var(--sans);font-size:.72rem;
  letter-spacing:.2em;text-transform:uppercase;color:var(--accent);margin-bottom:.6rem}
.chapter-head h2{font-size:clamp(1.4rem,3.4vw,2.2rem);margin:0 0 .8rem;
  line-height:1.2;color:var(--ink)}
.chapter-head .chapter-meta{font-family:var(--sans);font-size:.82rem;
  color:var(--ink-faint);margin:0}
.chapter-head .chapter-meta a{color:var(--accent-soft)}
.back-to-top{text-align:right;margin:2rem 0 0;font-family:var(--sans);font-size:.85rem}
.back-to-top a{color:var(--ink-faint);text-decoration:none}
.back-to-top a:hover{color:var(--accent)}

#master-toc-panel{
  position:fixed;top:0;right:-420px;width:min(420px,100vw);height:100vh;
  background:var(--bg-card);border-left:1px solid var(--rule);
  box-shadow:-12px 0 32px -16px rgba(0,0,0,.6);
  padding:5rem 1.5rem 2rem;overflow-y:auto;z-index:150;
  transition:right .35s cubic-bezier(.2,.7,.3,1);
}
#master-toc-panel.open{right:0}
#master-toc-panel h2{font-family:var(--sans);font-size:.85rem;
  letter-spacing:.18em;text-transform:uppercase;color:var(--ink-faint);
  margin:0 0 1rem}
#toc-overlay{
  position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:140;
  opacity:0;pointer-events:none;transition:opacity .3s}
#toc-overlay.open{opacity:1;pointer-events:auto}
.toc-toggle{
  position:fixed;top:1rem;left:1rem;z-index:160;
  background:var(--bg-card);border:1px solid var(--rule);
  border-radius:999px;padding:.55rem 1rem;
  font-family:var(--sans);font-size:.85rem;color:var(--ink-soft);
  cursor:pointer;box-shadow:var(--shadow);
  display:inline-flex;align-items:center;gap:.5rem;
}
.toc-toggle:hover{color:var(--accent);border-color:var(--accent-soft)}

/* tame the inner hero blocks once they're inside collapsed cards */
.about-card-body .meta{font-size:.8rem;color:var(--ink-faint)}

/* keep find-yourself self-contained */
#self-discovery{margin-top:5rem;padding-top:3rem;border-top:2px solid var(--accent-soft)}
#self-discovery h2.appendix-h{text-align:center;font-size:2rem;color:var(--accent)}

/* preface tweaks */
#preface{margin:0 auto 4rem}
#preface section{margin-top:2rem}
#preface .disclaimer-block{
  background:var(--bg-card);border:1px solid #c44;border-radius:8px;
  padding:1.5rem;margin:1rem 0}
</style>'''

JS = r'''
<script>
(function(){
  /* progress bar */
  var bar = document.getElementById('progress');
  function tick(){
    var s = window.scrollY,
        h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (h>0 ? (s/h*100):0) + '%';
  }
  window.addEventListener('scroll', tick, {passive:true});
  window.addEventListener('resize', tick);
  tick();

  /* theme toggle */
  var themes = ['near-black','pure-black','sepia','sepia-dark','high-contrast'];
  var t = document.getElementById('theme-toggle');
  if (t) t.addEventListener('click', function(){
    var cur = document.documentElement.getAttribute('data-theme') || 'near-black';
    var i = themes.indexOf(cur);
    var next = themes[(i+1) % themes.length];
    document.documentElement.setAttribute('data-theme', next);
    try{ localStorage.setItem('vbt-theme', next); }catch(e){}
  });
  try{
    var saved = localStorage.getItem('vbt-theme');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
  }catch(e){}

  /* master TOC drawer */
  var btn = document.getElementById('toc-toggle');
  var panel = document.getElementById('master-toc-panel');
  var overlay = document.getElementById('toc-overlay');
  function tocClose(){ panel.classList.remove('open'); overlay.classList.remove('open'); }
  function tocOpen(){  panel.classList.add('open');    overlay.classList.add('open'); }
  if (btn) btn.addEventListener('click', function(){
    panel.classList.contains('open') ? tocClose() : tocOpen();
  });
  if (overlay) overlay.addEventListener('click', tocClose);
  if (panel) panel.addEventListener('click', function(e){
    if (e.target.tagName === 'A') tocClose();
  });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') tocClose();
  });

  /* favourites — store sutra-N ids */
  function loadFavs(){ try{return JSON.parse(localStorage.getItem('vbt-favs')||'[]');}catch(e){return [];} }
  function saveFavs(f){ try{localStorage.setItem('vbt-favs', JSON.stringify(f));}catch(e){} }
  var favs = loadFavs();
  document.querySelectorAll('button.fav-btn[data-fav]').forEach(function(b){
    var id = b.getAttribute('data-fav');
    if (favs.indexOf(id) >= 0){ b.textContent='♥'; b.setAttribute('aria-pressed','true'); }
    b.addEventListener('click', function(){
      var i = favs.indexOf(id);
      if (i>=0){ favs.splice(i,1); b.textContent='♡'; b.setAttribute('aria-pressed','false'); }
      else     { favs.push(id);    b.textContent='♥'; b.setAttribute('aria-pressed','true');  }
      saveFavs(favs);
    });
  });
})();
</script>'''

PROGRESS = '<div class="progress" id="progress" aria-hidden="true"></div>'
CONTROLS = '''
<button class="toc-toggle" id="toc-toggle" aria-label="Open table of contents">
  ☰&nbsp; Contents
</button>
<div class="controls" role="toolbar" aria-label="Reading controls">
  <button id="theme-toggle" aria-label="Cycle theme">◐</button>
</div>
<div id="toc-overlay"></div>
<aside id="master-toc-panel" aria-label="Table of contents">
  <h2>Contents</h2>
  ''' + TOC_HTML + '''
</aside>'''

# Cover ----------------------------------------------------------------
COVER = f'''
<header class="book-cover" id="top">
  <div class="eyebrow">The Vigyan Bhairav Tantra · Osho's Book of Secrets</div>
  <h1>The Complete 112 Techniques</h1>
  <p class="subtitle">All 112 meditation methods Shiva gave to Devi —
  arranged in Osho's book order, with full commentary and practice notes.</p>
  <p class="stats">{len(chapters)} chapters · 112 sutras · {len(themes)} thematic groups · single-file offline edition</p>
</header>'''

# Preface --------------------------------------------------------------
PREFACE = f'''
<section id="preface">
  <p class="part-divider">Preface — First Access This</p>
  {preface_body}
</section>'''

# About-Section --------------------------------------------------------
ABOUT = f'''
<section id="about">
  <p class="part-divider">About These Techniques · Category Overviews</p>
  <p style="text-align:center;color:var(--ink-faint);font-style:italic;
            font-family:var(--sans);font-size:.92rem;max-width:44rem;margin:0 auto 2rem">
    The 112 sutras have traditionally been clustered by what kind of doorway they
    use — breath, sound, looking, etc. Tap any group below to read its overview,
    safety notes and "how to begin" guidance before practising.
  </p>
  {''.join(about_cards)}
</section>'''

# Body of all chapters -------------------------------------------------
CHAPTERS = f'''
<section id="chapters">
  <p class="part-divider">The 112 Techniques · In Osho's Book Order</p>
  {''.join(chapter_sections)}
</section>'''

# Self-discovery appendix ---------------------------------------------
SELF = f'''
<section id="self-discovery">
  <p class="part-divider">Appendix — Find Your Path</p>
  <h2 class="appendix-h">Self-Discovery: Which Door Suits You?</h2>
  {selfdisc_body}
</section>'''

FOOTER = '''
<footer style="text-align:center;padding:4rem 1.5rem;color:var(--ink-faint);
               font-family:var(--sans);font-size:.85rem;border-top:1px solid var(--rule);
               margin-top:5rem">
  <p>Vigyan Bhairav Tantra · Compiled single-file edition.</p>
  <p>Source talks: Osho, <em>The Book of Secrets</em>. Sanskrit text: ~5,000 yrs old.</p>
  <p><a href="#top" style="color:var(--accent)">↑ Return to top</a></p>
</footer>'''

merged_body = '\n'.join([PROGRESS, CONTROLS, '<main>',
                         COVER, PREFACE, ABOUT, CHAPTERS, SELF,
                         '</main>', FOOTER, JS])

# Build final document -------------------------------------------------
DOCUMENT = f'''<!DOCTYPE html>
<html lang="en" data-theme="near-black">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="All 112 meditation techniques from Osho's Vigyan Bhairav Tantra (The Book of Secrets), arranged in book order, with full commentary, practice instructions, and safety notes — single-file offline edition.">
<title>Vigyan Bhairav Tantra — The Complete 112 Techniques (Osho)</title>
{canonical_style}
{extra_combined}
{EXTRA_CSS}
</head>
<body>
{merged_body}
</body>
</html>
'''

OUT.write_text(DOCUMENT, encoding='utf-8')
size_kb = OUT.stat().st_size / 1024
print(f"\n→ wrote {OUT.name}   ({size_kb:.1f} KB,  {len(chapters)} chapters,  "
      f"{sum(len(c['techs']) for c in chapters)} techniques)")
