#!/usr/bin/env python3
"""
Build a single merged HTML containing every Vigyan Bhairav Tantra technique
in Osho's book order.

Structure of the output:
  1.  Cover / master TOC
  2.  Preface              (= important-first-access-this.html body, with
                            the situation matcher, random button and safety
                            index stripped; an 8-question quiz inserted in
                            place of the random button)
  3.  The 39 Osho chapters in order, each a section containing:
         · chapter title  (from canonical_112_sutras.json)
         · Osho's framing for the chapter  (from _chapter_intros.json)
         · the 2..9 sutras in that chapter, in canonical order,
           with full commentary preserved from the thematic files
  4.  Appendix — Self-Discovery (= find-yourself.html body)
  5.  Footer

Output: vigyan-bhairav-tantra-complete-book.html
"""
import json, re, unicodedata, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT  = ROOT / 'vigyan-bhairav-tantra-complete-book.html'

# ──────────────────────────────────────────────────────────────────────
# 0.  Load chapter intros (paraphrased framings of each Osho chapter)
# ──────────────────────────────────────────────────────────────────────
chapter_intros_data = json.loads(
    (ROOT / '_chapter_intros.json').read_text(encoding='utf-8')
)
chapter_intros = {c['chapter']: c for c in chapter_intros_data['chapters']}

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

# Strip the three sections we no longer want in the merged book:
#   - the "Find a technique by what's happening in your life" matcher
#   - the "I can't decide — surprise me" random button
#   - the "Safety & Cautions Index" (its content lives in the disclaimer
#     and in each technique's own caution block already)
# We replace `random` with an 8-question quiz section further below.
for _strip_id in ('matcher', 'random', 'safety'):
    preface_body = re.sub(
        rf'<section\s+id="{_strip_id}"[^>]*>.*?</section>',
        '', preface_body, flags=re.DOTALL,
    )

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


# ──────────────────────────────────────────────────────────────────────
# 4c.  Build the 8-question recommendation quiz.
# Each option carries weights for some of the 15 categories. The category
# with the highest summed weight wins, and we recommend a representative
# sutra from that category (preferring an iconic hand-picked sutra when
# it is present in that category, otherwise falling back to the lowest
# canonical number in the slug).
# ──────────────────────────────────────────────────────────────────────

# Friendly display name + iconic sutra preference per slug.
CATEGORY_DISPLAY = {
    'breath':      'Breath',
    'centering':   'Centering',
    'sound':       'Sound & Mantra',
    'light':       'Light & Gazing',
    'witnessing':  'Witnessing',
    'negation':    'Self-Inquiry',
    'void':        'Emptiness & Void',
    'sensory':     'The Senses',
    'movement':    'Movement',
    'sleep':       'Sleep & Dream',
    'tantra':      'Tantric Union',
    'heart':       'Heart & Devotion',
    'death':       'Death Contemplation',
    'imagination': 'Imagination',
    'mind':        'Mind & Thought',
}

# Iconic sutras per category, by canonical number. If a preferred number
# is not actually present in that category, we fall back to the lowest
# canonical number in the slug.
PREFERRED_SUTRA = {
    'breath':      1,    # the gap between two breaths
    'centering':   27,   # lotus thread in the spinal column
    'sound':       38,   # intone "aum" slowly
    'light':       29,   # light rays from center to center up the spine
    'witnessing':  84,   # look into the blue sky beyond clouds
    'negation':    71,   # toss attachment for body aside
    'void':        58,   # before desire and before knowing
    'sensory':     22,   # while being caressed, enter the caress
    'movement':    24,   # in a moving vehicle, sway rhythmically
    'sleep':       75,   # at the point of sleep
    'tantra':      75,   # at the start of sexual union, attentive on the fire
    'heart':       12,   # devotion frees
    'death':       54,   # focus on fire rising through your form
    'imagination': 49,   # five-coloured circles of the peacock tail
    'mind':        61,   # let mind be before thought
}

# Build slug -> {nums: [...], rep_num: int, rep_short: str}
sutras_by_slug: dict = {}
for t in all_techs:
    sutras_by_slug.setdefault(t['slug'], []).append(t['canonical'])

short_by_num = {s['num']: s['short'] for s in canonical}

def representative(slug):
    nums = sorted(sutras_by_slug.get(slug, []))
    if not nums:
        return None
    pref = PREFERRED_SUTRA.get(slug)
    n = pref if pref in nums else nums[0]
    return n

# 8-question quiz definition. Each option's weights sum to ~3.
QUIZ_QUESTIONS = [
    {
        'q': 'When you sit down to meditate, what comes most naturally?',
        'options': [
            ('Following my breath',                              {'breath': 3}),
            ('Sitting still and feeling the body inside',        {'centering': 2, 'sensory': 1}),
            ('Watching thoughts pass by',                        {'witnessing': 2, 'mind': 1}),
            ('Listening — to silence or to a sound',             {'sound': 3}),
            ("I can't sit still — I want to move",               {'movement': 2, 'breath': 1}),
        ],
    },
    {
        'q': 'Which sense pulls you in most strongly?',
        'options': [
            ('Touch — texture, warmth, contact',                 {'sensory': 2, 'tantra': 1}),
            ('Sight — light, colour, beauty',                    {'light': 2, 'imagination': 1}),
            ('Hearing — music, voices, silence',                 {'sound': 3}),
            ('The feel of breath itself',                        {'breath': 3}),
            ('None — I live mostly in my head',                  {'mind': 2, 'witnessing': 1}),
        ],
    },
    {
        'q': "What's the deepest reason you came here?",
        'options': [
            ('Less anxiety, more calm',                          {'breath': 2, 'centering': 1}),
            ('More love, more connection',                       {'heart': 2, 'tantra': 1}),
            ('Insight — to see what is actually true',           {'witnessing': 2, 'negation': 1}),
            ('Rest, surrender, letting go',                      {'sleep': 2, 'void': 1}),
            ('To feel alive, present, awake',                    {'sensory': 2, 'movement': 1}),
        ],
    },
    {
        'q': 'How do you feel about the body?',
        'options': [
            ('It is the doorway I trust most',                   {'centering': 2, 'sensory': 1}),
            ('It is a vehicle for energy',                       {'tantra': 2, 'breath': 1}),
            ('I forget it is there',                             {'mind': 2, 'imagination': 1}),
            ('A burden I would like to transcend',               {'death': 2, 'void': 1}),
            ('I am at war with it',                              {'heart': 1, 'tantra': 1, 'negation': 1}),
        ],
    },
    {
        'q': 'When something painful arises inside, what happens?',
        'options': [
            ('I think about it endlessly',                       {'mind': 2, 'witnessing': 1}),
            ('I push it away or distract myself',                {'imagination': 1, 'sleep': 1, 'movement': 1}),
            ('I let myself feel it fully',                       {'heart': 2, 'sensory': 1}),
            ('I try to watch it from outside',                   {'witnessing': 3}),
            ('I want the self that suffers to dissolve',         {'void': 2, 'negation': 1}),
        ],
    },
    {
        'q': 'How do you feel about emptiness, silence, the unknown?',
        'options': [
            ('Frightening — I want to fill it',                  {'sensory': 1, 'heart': 1, 'sound': 1}),
            ('Peaceful — feels like home',                       {'void': 2, 'sleep': 1}),
            ('Curious but cautious — I want a guide',            {'witnessing': 2, 'light': 1}),
            ('I prefer richness, colour, energy',                {'tantra': 1, 'light': 1, 'imagination': 1}),
            ('I have not really tasted it',                      {'breath': 1, 'centering': 2}),
        ],
    },
    {
        'q': 'What dissolves "you" most easily, even briefly?',
        'options': [
            ('Music or chanting',                                {'sound': 3}),
            ('A vast view: sky, ocean, mountain',                {'light': 2, 'void': 1}),
            ('A long walk, a run, dance',                        {'movement': 3}),
            ('A lover\'s touch or gaze',                         {'tantra': 2, 'heart': 1}),
            ('Falling asleep',                                   {'sleep': 3}),
            ('A piercing question with no answer',               {'negation': 2, 'mind': 1}),
        ],
    },
    {
        'q': 'Tonight, before sleep, what would feel right?',
        'options': [
            ('Counting breaths',                                 {'breath': 3}),
            ('Imagining myself as light filling the room',       {'imagination': 2, 'light': 1}),
            ('Watching the dark behind closed eyes',             {'void': 2, 'light': 1}),
            ('Feeling the body sink, layer by layer',            {'centering': 2, 'sleep': 1}),
            ('Silently saying one word until it dissolves',      {'sound': 2, 'mind': 1}),
            ('Letting go of being someone',                      {'death': 2, 'negation': 1}),
        ],
    },
]

def build_quiz_html():
    blocks = []
    for qi, q in enumerate(QUIZ_QUESTIONS):
        opts = []
        for oi, (label, weights) in enumerate(q['options']):
            wjson = json.dumps(weights)
            inp_id = f'q{qi}_{oi}'
            opts.append(
                f'<label class="quiz-opt" for="{inp_id}">'
                f'<input type="radio" id="{inp_id}" name="q{qi}" '
                f'data-weights=\'{wjson}\' value="{oi}">'
                f'<span>{html.escape(label)}</span></label>'
            )
        blocks.append(
            f'<fieldset class="quiz-q" data-qi="{qi}">'
            f'<legend><span class="quiz-step">Question {qi+1} of {len(QUIZ_QUESTIONS)}</span> '
            f'{html.escape(q["q"])}</legend>'
            f'<div class="quiz-opts">{"".join(opts)}</div>'
            f'</fieldset>'
        )
    return '\n'.join(blocks)

# Per-category data the JS will use to render the recommendation.
quiz_category_meta = {}
for slug, display in CATEGORY_DISPLAY.items():
    n = representative(slug)
    if n is None:
        continue
    quiz_category_meta[slug] = {
        'display': display,
        'rep_num': n,
        'rep_short': short_by_num.get(n, ''),
        'rep_anchor': f'sutra-{n}',
        'about_anchor': f'about-{slug}',
    }

QUIZ_HTML = f'''
<section id="quiz">
  <h2>Find your starting technique &mdash; an 8-question quiz</h2>
  <p>Answer all eight honestly. The quiz will recommend one of the 112
  techniques that fits the way you already meet life. You can re-take it as
  often as you like.</p>
  <form id="quiz-form" class="quiz-block" novalidate>
    {build_quiz_html()}
    <div class="quiz-actions">
      <button type="button" class="quiz-btn" id="quiz-submit">See my technique &rarr;</button>
      <button type="button" class="quiz-btn quiz-btn-ghost" id="quiz-reset">Reset</button>
    </div>
    <p class="quiz-hint" id="quiz-hint" aria-live="polite"></p>
  </form>
  <div class="quiz-result" id="quiz-result" aria-live="polite" hidden></div>
  <script id="quiz-category-meta" type="application/json">{json.dumps(quiz_category_meta)}</script>
</section>'''

# Inject the quiz inside the preface, after the categories section
# (which is the natural place for the recommendation flow).
if '</section>' in preface_body and 'id="categories"' in preface_body:
    # Find the close of the categories section and insert the quiz after it.
    cats_close_pat = re.compile(
        r'(<section\s+id="categories"[^>]*>.*?</section>)', re.DOTALL,
    )
    m = cats_close_pat.search(preface_body)
    if m:
        preface_body = (preface_body[:m.end()] + '\n' + QUIZ_HTML
                        + preface_body[m.end():])
    else:
        preface_body = preface_body + '\n' + QUIZ_HTML
else:
    preface_body = preface_body + '\n' + QUIZ_HTML


def slug_chapter(label: str) -> str:
    s = re.sub(r'[\r\n]+', ' ', label).strip()
    s = re.sub(r'^\d+\.\s*', '', s)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    return s[:60]


# Master TOC ----------------------------------------------------------
toc_items = []
toc_items.append('<li><a href="#preface">Preface — Important: First Access This</a></li>')
toc_items.append('<li><a href="#quiz">Find your starting technique (8-question quiz)</a></li>')
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

# About-These-Techniques cards are intentionally not built. The
# "About These Techniques · Category Overviews" section was removed from
# the merged book per the project plan; the per-category hero blocks are
# left in their standalone thematic HTML files.


# Chapter sections ---------------------------------------------------
def render_chapter_intro(ch_num: str, ch_title: str) -> str:
    """Return the styled chapter-intro HTML block for the given chapter,
    or '' if no intro exists for it.

    The intro JSON has one entry per sutra-discourse chapter (the odd-
    numbered chapters 3, 5, ..., 79). Each summary already embeds one
    short attributed quote inline; we split it out into a styled
    blockquote so the framing reads cleanly.
    """
    try:
        n = int(ch_num)
    except (ValueError, TypeError):
        return ''
    entry = chapter_intros.get(n)
    if not entry:
        return ''
    summary = entry.get('summary', '').strip()
    quote   = entry.get('quote', '').strip()

    # Split the summary so the inline attributed quote becomes a callout.
    framing = summary
    if quote and quote in summary:
        # Split on the segment that introduces the quote.
        # Typical pattern: '... As Osho puts it: "QUOTE"'
        before_quote = summary.split(quote)[0]
        # Trim the trailing ': "', the words "As Osho puts it" etc.
        framing = re.sub(
            r'\s*(?:As Osho (?:puts it|says|notes|frames it|bluntly notes)[^"]*?)?[":\s]*$',
            '', before_quote,
        ).strip()
        if not framing:
            framing = before_quote.strip()

    framing_html = html.escape(framing).replace('\n', '<br>') if framing else ''
    quote_html   = html.escape(quote) if quote else ''

    parts = ['<aside class="chapter-intro" aria-label="Osho\'s framing for this chapter">']
    parts.append('<div class="chapter-intro-eyebrow">Osho\'s framing</div>')
    if framing_html:
        parts.append(f'<p class="chapter-intro-body">{framing_html}</p>')
    if quote_html:
        parts.append(
            '<blockquote class="chapter-intro-quote">'
            f'<p>{quote_html}</p>'
            '<cite>— Osho</cite>'
            '</blockquote>'
        )
    parts.append('</aside>')
    return '\n'.join(parts)


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

    # Note: the "From thematic groups: ..." line that used to live here is
    # removed — its anchors targeted the per-category overview cards which
    # are no longer part of the merged book.

    intro_block = render_chapter_intro(ch_num, ch_title)

    chapter_sections.append(f'''
<section class="chapter" id="{cid}">
  <header class="chapter-head">
    <div class="eyebrow">Chapter {ch_num} · {rng} · {len(nums)} technique{'s' if len(nums)!=1 else ''}</div>
    <h2>{html.escape(ch_title)}</h2>
  </header>
  {intro_block}
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

/* === chapter-intro (Osho's framing) === */
.chapter-intro{
  background:var(--bg-card);border:1px solid var(--rule);border-radius:8px;
  padding:1.4rem 1.6rem;margin:0 0 2.5rem;
  border-left:3px solid var(--accent);
}
.chapter-intro-eyebrow{
  font-family:var(--sans);font-size:.7rem;letter-spacing:.18em;
  text-transform:uppercase;color:var(--accent);margin-bottom:.7rem;
  font-weight:600;
}
.chapter-intro-body{
  font-family:var(--serif);font-size:1.02rem;line-height:1.7;
  color:var(--ink-soft);margin:0 0 1rem;
}
.chapter-intro-quote{
  margin:1rem 0 0;padding:.9rem 1.2rem;
  border-left:3px solid var(--accent-soft);background:transparent;
  font-style:italic;font-family:var(--serif);font-size:1.05rem;
  line-height:1.6;color:var(--ink);
}
.chapter-intro-quote p{margin:0 0 .4rem}
.chapter-intro-quote cite{
  display:block;font-style:normal;font-family:var(--sans);
  font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-faint);
}
@media print{
  .chapter-intro{break-inside:avoid;border-color:#888}
}

/* === quiz === */
#quiz{margin:3rem 0}
#quiz .quiz-block{
  background:var(--bg-card);border:1px solid var(--rule);border-radius:8px;
  padding:1.5rem 1.6rem;margin-top:1rem;
}
.quiz-q{
  border:0;border-top:1px solid var(--rule);
  padding:1.4rem 0 0;margin:1.4rem 0 0;
}
.quiz-q:first-of-type{border-top:0;padding-top:0;margin-top:0}
.quiz-q legend{
  font-family:var(--serif);font-size:1.08rem;line-height:1.45;
  color:var(--ink);padding:0;margin-bottom:.9rem;
}
.quiz-step{
  display:block;font-family:var(--sans);font-size:.7rem;
  letter-spacing:.18em;text-transform:uppercase;color:var(--accent);
  margin-bottom:.3rem;font-weight:600;
}
.quiz-opts{display:flex;flex-direction:column;gap:.45rem}
.quiz-opt{
  display:flex;gap:.7rem;align-items:flex-start;
  padding:.6rem .8rem;border:1px solid var(--rule);border-radius:6px;
  cursor:pointer;font-family:var(--sans);font-size:.93rem;line-height:1.4;
  color:var(--ink-soft);transition:border-color .15s, background .15s;
}
.quiz-opt:hover{border-color:var(--accent-soft);color:var(--ink)}
.quiz-opt input{margin-top:.25rem;accent-color:var(--accent)}
.quiz-opt:has(input:checked){
  border-color:var(--accent);background:var(--accent-soft);color:var(--ink);
}
.quiz-actions{
  display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.6rem;
  padding-top:1.4rem;border-top:1px solid var(--rule);
}
.quiz-btn{
  background:var(--accent);color:#fff;border:0;border-radius:6px;
  padding:.7rem 1.2rem;font-family:var(--sans);font-size:.9rem;
  font-weight:600;cursor:pointer;letter-spacing:.02em;
}
.quiz-btn:hover{filter:brightness(1.1)}
.quiz-btn-ghost{
  background:transparent;color:var(--ink-soft);
  border:1px solid var(--rule);
}
.quiz-btn-ghost:hover{color:var(--accent);border-color:var(--accent-soft)}
.quiz-hint{
  margin:1rem 0 0;font-family:var(--sans);font-size:.85rem;
  color:#c44;min-height:1.2em;
}
.quiz-result{
  margin-top:1.5rem;padding:1.5rem 1.6rem;background:var(--bg-card);
  border:1px solid var(--accent-soft);border-radius:8px;
  border-left:3px solid var(--accent);
}
.quiz-result .result-eyebrow{
  font-family:var(--sans);font-size:.72rem;letter-spacing:.18em;
  text-transform:uppercase;color:var(--accent);font-weight:600;
}
.quiz-result h3{
  font-family:var(--serif);font-size:1.35rem;margin:.4rem 0 .8rem;color:var(--ink);
}
.quiz-result .result-cat{
  font-family:var(--sans);font-size:.85rem;color:var(--ink-faint);
  margin:0 0 1rem;
}
.quiz-result .result-cta{
  display:inline-block;background:var(--accent);color:#fff;
  text-decoration:none;padding:.65rem 1.1rem;border-radius:6px;
  font-family:var(--sans);font-size:.9rem;font-weight:600;margin-top:.5rem;
}
.quiz-result .result-cta:hover{filter:brightness(1.1)}
.quiz-result .runners-up{
  margin-top:1.2rem;padding-top:1rem;border-top:1px solid var(--rule);
  font-family:var(--sans);font-size:.82rem;color:var(--ink-faint);
}
.quiz-result .runners-up strong{color:var(--ink-soft);font-weight:600}
@media(max-width:600px){
  #quiz .quiz-block{padding:1.2rem 1rem}
  .quiz-q legend{font-size:1rem}
  .quiz-opt{font-size:.9rem}
}
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

  /* 8-question quiz: score across the 15 categories, recommend a sutra */
  var quizForm   = document.getElementById('quiz-form');
  var quizMetaEl = document.getElementById('quiz-category-meta');
  if (quizForm && quizMetaEl) {
    var meta;
    try { meta = JSON.parse(quizMetaEl.textContent || '{}'); }
    catch(e) { meta = {}; }
    var submitBtn = document.getElementById('quiz-submit');
    var resetBtn  = document.getElementById('quiz-reset');
    var hintEl    = document.getElementById('quiz-hint');
    var resultEl  = document.getElementById('quiz-result');
    var totalQs   = quizForm.querySelectorAll('fieldset.quiz-q').length;

    function answeredCount(){
      var c = 0;
      for (var i = 0; i < totalQs; i++) {
        if (quizForm.querySelector('input[name="q' + i + '"]:checked')) c++;
      }
      return c;
    }

    function score(){
      var totals = {};
      var picks = quizForm.querySelectorAll('input[type="radio"]:checked');
      picks.forEach(function(inp){
        var w;
        try { w = JSON.parse(inp.getAttribute('data-weights') || '{}'); }
        catch(e) { w = {}; }
        Object.keys(w).forEach(function(k){
          totals[k] = (totals[k] || 0) + w[k];
        });
      });
      // Sort categories by score descending; preserve a stable order on ties.
      var ranked = Object.keys(totals).map(function(k){
        return {slug: k, score: totals[k]};
      }).sort(function(a, b){
        return b.score - a.score;
      });
      return ranked;
    }

    function renderResult(ranked){
      if (!ranked.length) {
        resultEl.hidden = true;
        return;
      }
      var top = ranked[0];
      var info = meta[top.slug];
      if (!info) {
        resultEl.hidden = true;
        return;
      }
      var html = '';
      html += '<div class="result-eyebrow">Your recommended starting place</div>';
      html += '<h3>Sutra ' + info.rep_num + ' — ' + escapeHtml(info.rep_short) + '</h3>';
      html += '<p class="result-cat">Category: <strong>' + escapeHtml(info.display) + '</strong> · '
            + 'score ' + top.score + '</p>';
      html += '<a class="result-cta" href="#' + info.rep_anchor + '">Read this technique &rarr;</a>';

      // Show up to 2 runners-up if they have non-zero score
      var runners = ranked.slice(1, 4).filter(function(r){
        return r.score > 0 && meta[r.slug];
      });
      if (runners.length) {
        var parts = runners.map(function(r){
          var m = meta[r.slug];
          return '<a href="#' + m.rep_anchor + '">'
               + escapeHtml(m.display) + ' (sutra ' + m.rep_num + ')</a>';
        });
        html += '<div class="runners-up"><strong>Also worth exploring:</strong> '
              + parts.join(' · ') + '</div>';
      }

      resultEl.innerHTML = html;
      resultEl.hidden = false;
      // Smooth-scroll the result into view.
      resultEl.scrollIntoView({behavior:'smooth', block:'center'});
    }

    function escapeHtml(s){
      return String(s == null ? '' : s)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    }

    if (submitBtn) submitBtn.addEventListener('click', function(){
      var done = answeredCount();
      if (done < totalQs) {
        hintEl.textContent = 'Please answer all '
          + totalQs + ' questions (you\u2019ve answered '
          + done + ').';
        // Find the first unanswered question and focus it.
        for (var i = 0; i < totalQs; i++) {
          if (!quizForm.querySelector('input[name="q' + i + '"]:checked')) {
            var fs = quizForm.querySelector('fieldset[data-qi="' + i + '"]');
            if (fs) fs.scrollIntoView({behavior:'smooth', block:'center'});
            break;
          }
        }
        resultEl.hidden = true;
        return;
      }
      hintEl.textContent = '';
      renderResult(score());
    });

    if (resetBtn) resetBtn.addEventListener('click', function(){
      quizForm.reset();
      hintEl.textContent = '';
      resultEl.hidden = true;
      resultEl.innerHTML = '';
      // Scroll back to the start of the quiz so the next attempt feels fresh.
      var quizSec = document.getElementById('quiz');
      if (quizSec) quizSec.scrollIntoView({behavior:'smooth', block:'start'});
    });

    // Live-update hint as the user picks options.
    quizForm.addEventListener('change', function(){
      var done = answeredCount();
      if (done === totalQs) {
        hintEl.textContent = 'All ' + totalQs + ' answered \u2014 click "See my technique".';
      } else {
        hintEl.textContent = '';
      }
    });
  }
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

# About-Section is intentionally removed: per the project plan, the
# "About These Techniques · Category Overviews" section is no longer part
# of the merged book. The category-overview cards previously generated
# from each thematic file's hero are not rendered.

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
                         COVER, PREFACE, CHAPTERS, SELF,
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
