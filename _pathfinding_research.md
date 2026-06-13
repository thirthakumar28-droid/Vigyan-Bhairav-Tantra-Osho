# Pathfinding Research Dossier

**Purpose.** Evidence base for the self-diagnosis instrument in
`vigyan-bhairav-find-yourself.html` ("The Mirror"). It documents every
credible system humans use to (a) read a person's inner constitution and
(b) route them to a fitting contemplative practice — then synthesises them
into the consolidated matching model the quiz uses to recommend specific
Vigyan Bhairav Tantra (VBT) techniques.

**How to read the confidence tags.** Each system is tagged:
- **Canonical** — a primary traditional source states it directly.
- **Well-established** — broad scholarly/teaching consensus.
- **Heuristic** — useful routing rule, not validated science; used as a
  cross-check, never as the sole signal.
- **Contested** — has real academic critics; used with caution.

**Licensing note.** All external material below is paraphrased and kept under
30 consecutive words per source; sources are linked inline. Content was
rephrased for compliance with licensing restrictions.

---

## 0. The core problem this instrument solves

Most modern people answer "who are you?" from self-image (who they wish they
were, or who they were told to be), not from their actual nature. A good
diagnostic must therefore:

1. Ask about **behaviour under load**, not stated values — stress strips the
   persona and reveals the default. (This is why several questions probe "what
   do you *actually* do when stressed / unscheduled / triggered," not "what do
   you believe.")
2. Triangulate across **independent axes** so no single self-flattering answer
   dominates. The quiz measures temperament (the four yogas), energetic channel
   (body/mind/heart/energy), the gunas (mental quality), the doshas (bodily
   constitution), nervous-system state (the safety gate), plus light cross-checks
   (sensory orientation, attachment, intent).
3. Report **honest confidence** — high only when several independent axes
   converge on the same technique.

---

## 1. The Four Yogas — temperament → path

**Status: Canonical (Vivekananda, Sivananda) + Well-established.**

The four classical paths each suit a different dominant faculty. The mapping is
consistent across sources:

| Temperament (dominant faculty) | Path | What it does |
|---|---|---|
| Active / will-driven | **Karma yoga** | union through selfless action |
| Emotional / devotional | **Bhakti yoga** | union through love and surrender |
| Rational / intellectual | **Jnana yoga** | union through inquiry and discrimination |
| Meditative / mystical | **Raja yoga** | union through concentration and witnessing |

Sources:
- Sivananda: bhakti suits the devotional temperament where love predominates;
  raja suits the mystic temperament; jnana suits rational, bold-reasoning minds;
  the active temperament follows karma yoga. ([sivanandaonline.org](https://www.sivanandaonline.org/public_html/?cmd=displaysection&section_id=1190))
- North Central College course notes: meditative → raja, rational → jnana,
  active → karma, emotional → bhakti. ([noctrl.edu, via search snippet](http://bhoffert.faculty.noctrl.edu/RELG100/020.Hinduism.FourPathsOfYoga.html))
- Google Arts & Culture: karma engages the mind's active aspect; bhakti the
  emotional; raja the mystical; jnana the intellectual. ([artsandculture.google.com](https://artsandculture.google.com/story/QQURiPuOVM2eIw?hl=en))
- Vivekananda framing: bhakti is for hearts yearning for a personal relationship
  with the divine; jnana for those seeking through reason. ([philosophy.institute](https://philosophy.institute/indian-philosophy/vivekanandas-paths-spiritual-yoga/))

**Critical caveat (Sivananda's own teaching): the Yoga of Synthesis.** Sivananda
explicitly advocated blending all four paths according to temperament rather
than picking one and discarding the rest. ([scribd summary](https://www.scribd.com/document/331585327/The-Four-Paths-of-Yoga))
**Design implication:** report a *primary* and *secondary* path with percentages,
never a single exclusive label.

**Diagnostic questions that reveal path (used in the quiz):**
- Unscheduled free time → do you *do* (karma), *think/learn* (jnana),
  *connect* (bhakti), or *be alone in quiet* (raja)?
- The book that changes you → biography/how-to (karma), philosophy/science
  (jnana), poetry/novels (bhakti), sparse mystical writing (raja).
- Under stress → activate/take charge (karma), withdraw into quiet (raja),
  reach out/talk (bhakti), analyse/plan (jnana).

---

## 2. The Three Gunas — mental quality / what needs lifting

**Status: Canonical (Samkhya, Bhagavad Gita) + Well-established.**

The gunas describe the *quality* of mind-energy. They act on the mind first,
and the body follows. ([squarespace/What Are the Gunas](https://chartreuse-pear-6dfh.squarespace.com/blog/what-are-the-gunas))

| Guna | Quality | Behavioural markers |
|---|---|---|
| **Sattva** | clarity, harmony, balance | calm, reflective, compassionate, present, equanimous ([realitypathing](https://realitypathing.com/how-to-recognize-imbalances-in-your-guna/)) |
| **Rajas** | activity, passion, fire | restless, driven, ambitious, agitated, craving, over-doing |
| **Tamas** | inertia, heaviness, darkness | dull, heavy, foggy, numb, oversleeping, avoidant, stuck ([yogabasics](https://www.yogabasics.com/learn/the-3-gunas-of-nature.html)) |

**The key routing insight (not "what is your guna" but "what is in excess"):**
The practice should *counter the excess* guna.
- High **tamas** → do NOT add stillness/sleep; add fire, movement, light, sound
  first. (Sound/vibration lifts inertia; walking and energising practices clear
  it.)
- High **rajas** → cool and slow down; do less, not more; silence and gentle
  practice over intense concentration.
- High **sattva** → protect it; silence, nature, contemplative practice;
  the subtlest void/witnessing techniques become accessible.

Sources confirm conscious manipulation of the gunas moves one toward clarity
([yogabasics](https://www.yogabasics.com/learn/the-3-gunas-of-nature.html)); sattva
is the target state of balance and presence ([sagerountree](https://sagerountree.com/the-three-gunas-explained/)).

**Design implication (already in engine, retained):** the catalog tags each
technique with `liftsGuna` (the excess it counters), and the scorer rewards a
technique only when its `liftsGuna` matches the user's *dominant* (excess) guna
and that guna isn't sattva. This is the correct logic and the dossier confirms it.

---

## 3. The Doshas — bodily constitution / what the body needs

**Status: Canonical (Ayurveda: Charaka/Sushruta) + Well-established clinically.**

Prakriti questionnaires (AYUSH/CCRAS-aligned) assess body features, appetite,
sleep, energy, temperature preference, mood, and stress response across
~24–60 items. ([arxiv prakriti dataset](https://arxiv.org/html/2510.06262v1),
[yogachaitanya 60-Q quiz](https://yogachaitanya.com/ayurvedic-dosha-quiz/))

| Dosha | Elements | Traits | What meditation must do |
|---|---|---|---|
| **Vata** | air + ether | light, mobile, creative, cold, dry, irregular sleep, anxious-when-imbalanced, restless mind ([russellrowe](https://russellrowe.com/dosha-type-self-assessment-26.php)) | **Ground & warm**: steady breath, slow mindful walking, body-based, regular rhythm ([insighttimer/Inman](https://insighttimer.com/jessicainman/guided-meditations/types-of-meditation-for-the-different-ayurvedic-consitutions)) |
| **Pitta** | fire + water | sharp, hot, focused, intense, driven, vivid sleep, irritable-when-imbalanced | **Cool & soften**: surrender, compassion, water/heart practices; avoid fiery breath & intense concentration ([banyanbotanicals](https://www.banyanbotanicals.com/info/blog-the-banyan-insight/details/love-meditations-for-the-doshas/)) |
| **Kapha** | earth + water | steady, cool, slow, deep, heavy, sleeps deeply (sometimes too much), hard to anger | **Activate & lighten**: energising, light, lively practices, walking meditation, keep the mind alert ([kripalu](https://kripalu.org/resources/how-choose-meditation-practice-your-dosha), [fitsri](https://www.fitsri.com/articles/meditation-for-vata-pitta-kapha)) |

**Concrete dosha→practice guidance found:**
- Vata: grounding into the body — steady breath-based meditation or slow walks
  in nature. ([insighttimer/Inman](https://insighttimer.com/jessicainman/guided-meditations/types-of-meditation-for-the-different-ayurvedic-consitutions))
- Kapha: opposite qualities — light, lively, energising; walking meditation to
  clear the cobwebs. ([kripalu](https://kripalu.org/resources/how-choose-meditation-practice-your-dosha))
- Vata-Pitta: mindfulness, heart/throat-chakra focus, loving-kindness, yoga
  nidra, trataka balance Vata's restlessness and Pitta's intensity. ([kamaayurveda](https://www.kamaayurveda.com/uk/en_GB/vata-pitta-recommendations))
- Anxious/scattered minds: rhythmic sound/mantra creates focus. ([chakraserenity](https://chakraserenity.com/ayurvedic-practices/ayurvedic-meditation-techniques/))

**Design implication:** dosha drives `doshaGood`/`doshaBad`. A technique that
aggravates the body's baseline (e.g. fiery third-eye/kundalini work for a Pitta
or Vata system) must be *penalised*, which the engine does (`doshaBad` −16).
Distinguish **prakriti** (stable birth constitution) from **vikriti** (current
imbalance) — the quiz mixes both; treat the result as "current tendency."
([astrologyayurveda vikruti](https://astrologyayurveda.com/quizzes-booking/vikruti-quiz/))

---

## 4. Nervous-system state — the SAFETY GATE (most important addition)

**Status: Contested theory, but the clinical caution is Well-established.**

This is the single most defensible and most valuable part of the instrument.
Independent of *which* practice fits a person's temperament, some practices are
*unsafe as a first medicine* for a dysregulated nervous system, and the research
on adverse meditation effects is robust.

**The finding:** Standard, unmodified meditation can worsen symptoms for people
with trauma histories, ACEs, or PTSD — provoking activation, flashbacks,
emotional distress, or extended dissociation rather than calm. This calls for
screening and trauma-informed design. Sources:
- Meditation/mindfulness can produce adverse effects, especially in those with
  trauma histories or subclinical PTSD; careful screening is needed.
  ([drlesliekorn](https://drlesliekorn.com/research/meditation-adverse-effects-assessment/))
- Standard practice can worsen traumatic stress for a significant subgroup.
  ([aihcp](https://aihcp.net/2026/01/22/the-evolution-of-trauma-informed-mindfulness-neurobiology-adverse-effects-and-what-you-need-to-do/))
- Yoga nidra specifically can cause overwhelming flashbacks, distress, and
  extended dissociation if delivered carelessly. ([PubMed 39690521](https://pubmed.ncbi.nlm.nih.gov/39690521/))
- Unmodified mindfulness often triggers activation rather than calm for
  survivors. ([anniewright](https://anniewright.com/meditation-and-trauma-why-mindfulness-can-be-activating-and-what-to-do-instead/))

**Polyvagal framing (Contested but useful as a routing heuristic).** Porges'
model describes three autonomic states ([polyvagalinstitute](https://www.polyvagalinstitute.org/whatispolyvagaltheory)):

| State | Felt sense | What it needs | What to AVOID first |
|---|---|---|---|
| **Ventral vagal** | settled, safe, socially engaged | anything — full range available | — |
| **Sympathetic** | activated, fight/flight, anxious, racing | discharge then settle; grounding; gentle breath | intense concentration, kundalini/fire, breath-holding |
| **Dorsal vagal** | shut-down, frozen, numb, collapsed | gentle activation, sound, warmth, sensory re-entry, movement | void/emptiness, death-rehearsal, long silent sitting (deepens collapse) |

Problems arise when the system gets *stuck* — chronically activated (anxiety,
hypervigilance) or chronically collapsed (numbness, fatigue, disconnection).
([theholisticcare](https://www.theholisticcare.com/blog/nervous-system-regulation))

**Honest limitation:** polyvagal theory has academic critics
([polyvagalinstitute background+criticism](https://www.polyvagalinstitute.org/background)).
We use the *state* labels only as a routing/safety heuristic, not as settled
neuroscience. The underlying caution (don't hand intense dissolving practices to
a dysregulated person) is independently well-supported by the adverse-effects
literature above.

**Design implication (the gate):** `nervBad` carries a large penalty (−22), and
high-intensity techniques (intensity 3) are further penalised for sympathetic or
dorsal states. This is correct and should be the *hardest* constraint in the
scorer — it can override a strong temperament match, because safety precedes fit.

---

## 5. VBT technique families and which seeker they suit

**Status: Canonical structure (Kashmir Shaivism) + Osho's commentary.**

The VBT is a Shaiva tantra of the Kaula Trika tradition of Kashmir Shaivism;
its 112 dharanas include breath-awareness variants, concentration on body
centres, non-dual awareness, mantra, visualisation, and sense-based
contemplations. ([Wikipedia VBT](https://en.wikipedia.org/wiki/Vij%C3%B1%C4%81na_Bhairava_Tantra),
[shivashakti](https://shivashakti.com/vijnan.htm))

**Lakshmanjoo's upaya stratification** (which means suits which capacity) maps
neatly onto our intensity/readiness axis:
- **Anavopaya** (the "individual means") — breath, mantra recitation, focus on
  centres. The *entry level*; uses effort and supports. ([lakshmanjooacademy](https://www.lakshmanjooacademy.org/blog/introduction-and-approach-to-the-vijnana-bhairava-by-swami-lakshmanjoo))
- **Shaktopaya** (the "means of energy") — awareness/contemplation, the witnessing
  middle.
- **Shambhavopaya** (the "divine means") — void, instantaneous non-dual
  recognition. The *advanced* end; little support, requires stability.

**Design implication:** maps to the `intensity` field (1 = anava/entry,
2 = shakta/witnessing, 3 = shambhava/void & death). The scorer should keep
intensity-3 techniques away from beginners (thin data) and dysregulated systems.

**Osho's own typology (from this repo's source).** Osho repeatedly sorts people
into **active vs. passive** and **head vs. heart**, and frames bhakti as the
parallel road for heart-oriented people running alongside the dry attention
techniques for the scientifically-minded (AUDIT_REPORT.md, heart-file notes;
`_chapter_intros_README.md`). His active methods (Dynamic, Kundalini, Nataraj,
Nadabrahma) discharge accumulated energy *before* stillness — directly parallel
to the "lift tamas / discharge rajas first" logic. ([anandasarita](https://www.anandasarita.com/blog/Osho-meditations),
[shunspirit](https://shunspirit.com/article/what-is-meditation-by-osho))

---

## 6. Cross-check systems (Heuristic — secondary weight only)

### 6a. Buddhist personality types (Visuddhimagga / Asanga)
Three core temperaments with matched antidotes ([Sharon Salzberg](https://sharonsalzberg.squarespace.com/on-being-column/the-three-personality-types-of-buddhist-psychology),
[tricycle](https://tricycle.org/magazine/buddhist-personality-type/)):
- **Greed/passion type** (passionate, ambitious, pleasure-seeking) → antidotes
  that work *with* beauty and devotion rather than against it.
- **Aversion/hatred type** (critical, perfectionistic, sharp) → forgiveness,
  compassion, loving-kindness. ([againstthestream](https://www.againstthestream.com/dharma-talk-and-meditation-podcast/buddhist-personality-types))
- **Delusion/confusion type** (foggy, indecisive) → mindfulness, structure,
  inquiry to make contact with experience.

This independently corroborates the gunas (passion≈rajas, aversion≈pitta-fire,
delusion≈tamas) and the path map (aversion→bhakti/heart antidote).

### 6b. Meditation by personality / MBTI-style and arousal
- Anxious/perfectionistic people do better with short, *structured* guided
  practice than open silence; restless/high-energy people need movement or
  breath-counting *before* long stillness. ([mindtastik](https://mindtastik.com/meditation-techniques/what-is-the-best-mindfulness-practice-for-your))
- Three research-grounded families: focused attention, open monitoring,
  automatic self-transcending. ([psychologytoday](https://www.psychologytoday.com/nz/blog/the-meditating-mind/202106/what-type-meditation-is-best))

### 6c. Attachment style (Heuristic)
- Anxious attachment: hyperactivated nervous system, fear of abandonment,
  people-pleasing; meditation helps observe responses before the panic-pursuit
  cycle. ([ordinaryintrovert](https://ordinaryintrovert.com/meditation-for-anxious-attachment/),
  [berkeley](https://greatergood.berkeley.edu/article/item/how_to_heal_anxious_attachment_by_prioritizing_your_own_needs))
- Avoidant attachment: suppresses closeness; loving-kindness/devotional practice
  may feel difficult and should be approached gradually. ([positivepsychology](https://positivepsychology.com/avoidant-attachment-style-in-adults/))
- Attachment insecurity *moderates* emotional response to mindfulness vs.
  loving-kindness — i.e. the same practice lands differently by attachment style;
  another reason to keep attachment a light cross-check, not a driver.
  ([PubMed 35201791](https://pubmed.ncbi.nlm.nih.gov/35201791/))

### 6d. Sensory orientation (Heuristic)
Visual / auditory / kinesthetic preference gives a small nudge: kinesthetic →
body practices; auditory → sound/breath; visual → light/imagination. Weak signal,
small weight only.

---

## 7. SYNTHESISED MATCHING MODEL (what the quiz implements)

**Axes measured (independent so they can corroborate):**
1. **Path** (karma/bhakti/jnana/raja) — temperament. *Primary driver.*
2. **Energy channel** (body/mind/heart/energy) — the faculty the practice works through.
3. **Guna** (sattva/rajas/tamas) — the *excess* to counter.
4. **Dosha** (vata/pitta/kapha) — bodily baseline to heal, not aggravate.
5. **Nervous-system state** (ventral/sympathetic/dorsal) — the SAFETY GATE.
6. **Intent** (sleep/anxiety/anger/disconnect/focus/stuck/joy/grief/love/ego) —
   what they came for; routes the "for this situation, do this" block.
7. Light cross-checks: sensory, attachment.

**Scoring rule (weights reflect evidential strength):**
- Path match — strongest positive (top-path match large bonus). *Vedanta-grounded.*
- Energy-channel match — strong positive.
- Guna: reward only when the technique lifts the user's *excess* guna.
- Dosha: moderate reward for `doshaGood`; **large penalty for `doshaBad`**
  (aggravating the constitution).
- **Nervous system: largest penalty for `nervBad`; extra penalty for
  intensity-3 on sympathetic/dorsal.** Safety overrides fit.
- Intent: rewards techniques addressing the stated need.
- Sensory: small nudge only.

**Confidence rule:** high only when (a) coverage of questions is high, (b) the
margin between the top two paths is clear, and (c) ideally some deep-research
questions were answered. Single-signal matches must NOT report high confidence.
A clear primary + corroborating energy + a fired safety gate = trustworthy.
A narrow path margin on thin data = "tentative — answer more."

**The 21-day rule.** Present the top pick as "the strongest of several reasonable
doors," recommend trying it ~21 days, and tell the user to let their own
experience overrule the quiz. (This honesty is itself trauma-informed and matches
the Yoga-of-Synthesis caution against rigid single-path labelling.)

---

## 8. Known fidelity caveat on destination pages

Per `AUDIT_REPORT.md`, several technique pages contain fabricated "signs it's
working," a few silently altered sutras, and instructions that contradict Osho
(e.g. breath-stopping framed as a daily practice; "blink when you must" vs.
Osho's "do not blink"; a light/floating body-scan where Osho prescribes
heaviness/death). **Routing can be correct while the destination page still
carries embellishments.** The quiz should therefore (a) only link to techniques
whose sutra is *verbatim-faithful* per the audit where possible, and (b) frame
recommendations as starting points, not literal step-by-step authority.

**Techniques to prefer (audit-clean sutras):** breath gap/turning/third-eye
(t1, t2, t5), centering thread-of-light & look-lovingly (cen2/cen6),
witnessing self-remembering & middle-way (wit5/wit9), sound AUM & central-sound,
sensory become-the-taste, sleep-edge, heart peace/devotion.
**Techniques to flag/handle carefully (audit-altered or contradicted):**
fire/death-rehearsal (dth1 — strong + prerequisites Osho insists on),
seven-openings suffocation, "sit on buttocks" (page describes a different pose),
heart "being is love" framing. Keep these gated behind intensity + safety.

---

## 9. Source list (primary references used)

- Sivananda, *The Four Paths* — temperament→path. ([link](https://www.sivanandaonline.org/public_html/?cmd=displaysection&section_id=1190))
- Sivananda articles — four temperaments, Yoga of Synthesis. ([link](https://articles.sivananda.org/our-lineage-and-the-gurus-teaching/yoga-sadhana/))
- Vivekananda's paths (philosophy.institute). ([link](https://philosophy.institute/indian-philosophy/vivekanandas-paths-spiritual-yoga/))
- Google Arts & Culture, Four Paths. ([link](https://artsandculture.google.com/story/QQURiPuOVM2eIw?hl=en))
- Yoga Basics / Arhanta / realitypathing — gunas markers. ([link](https://www.yogabasics.com/learn/the-3-gunas-of-nature.html))
- Prakriti questionnaire (AYUSH/CCRAS) — dosha items. ([arxiv](https://arxiv.org/html/2510.06262v1))
- Kripalu / Insight Timer / Banyan / Kama Ayurveda / fitsri — dosha→practice. (links inline §3)
- Porges / Polyvagal Institute — autonomic states + criticism. ([link](https://www.polyvagalinstitute.org/whatispolyvagaltheory))
- Dr Leslie Korn / AIHCP / PubMed — meditation adverse effects, trauma. (links inline §4)
- Lakshmanjoo Academy — upaya stratification. ([link](https://www.lakshmanjooacademy.org/blog/introduction-and-approach-to-the-vijnana-bhairava-by-swami-lakshmanjoo))
- Wikipedia VBT; shivashakti — technique families. (links inline §5)
- Sharon Salzberg / Tricycle / Visuddhimagga — Buddhist types. (links inline §6a)
- positivepsychology / Berkeley GG / PubMed — attachment + meditation. (links inline §6c)
- This repo: `AUDIT_REPORT.md`, `canonical_112_sutras.json`,
  `_chapter_intros_README.md`, `_book_study_notes.md`.

*Content throughout was rephrased for compliance with licensing restrictions;
each external claim is attributed to its source.*
