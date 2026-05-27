# Concrete Plan of Edits — to deliver 112 unique, correctly-placed techniques

Source of truth: Osho's own *List of Meditations* appendix (Ch. 80) and the verbatim sutras as printed in *The Book of Secrets* (Part 1). The canonical 1-112 list with exact wording is in `.work/canonical_112.json`.

## Headline counts

- Current website entries: **104** spread across 15 category files
- Hard fabrications (sutra not in Osho's text — DELETE outright): **6**
- Heavily-corrupted paraphrases (real sutra, fix the wording): **4**
- Duplicate copies of the same canonical sutra (DELETE all but one): **21**
- Real Osho sutras currently represented in the repo: **77 of 112**
- Real Osho sutras MISSING from the repo entirely (must be ADDED): **35**

After applying this plan: 112 unique sutras across 15 category files, every sutra verbatim, every "Technique X of 112" badge using Osho's canonical numbering, and the 15 per-file counts that sum exactly to 112.

---
## A. DELETE

### A.1  Fabrications (sutra is not present in Osho's text at all)

These six lines did not come from *The Book of Secrets*. The fuzzy-match score against every one of the 112 canonical sutras is below 0.45 (sequence) AND below 0.30 (keyword Jaccard). The closest hit is shown only as a sanity check — none of them is actually a misspelling of that canonical sutra; they are independent inventions.

| File | Badge | Sutra in repo (excerpt) | Closest canonical (informational only) |
|---|---:|---|---|
| `vigyan-bhairav-centering-techniques.html` | 14 | _Or, feel your form as awareness — above, below, and through your heart — and let the form melt away. Your spinal column,_ | #14 "Put your awareness on your spine" (low confidence — true fabrication) |
| `vigyan-bhairav-death-techniques.html` | 81 | _In the certainty that the impermanent shall pass, rest in the permanent._ | #76 "Dissolve into darkness" (low confidence — true fabrication) |
| `vigyan-bhairav-heart-techniques.html` | 110 | _Feel love filling you from all sides, and become love itself._ | #80 "Imagine the whole world burning" (low confidence — true fabrication) |
| `vigyan-bhairav-heart-techniques.html` | 111 | _As you sing, or listen to music, enter the feeling totally — become the feeling._ | #33 "Look into the limitless sky" (low confidence — true fabrication) |
| `vigyan-bhairav-imagination-techniques.html` | 86 | _Imagine the unimaginable — the formless, the limitless, the infinite._ | #33 "Look into the limitless sky" (low confidence — true fabrication) |
| `vigyan-bhairav-imagination-techniques.html` | 87 | _Feel ‘I am’ without any content. Just the feeling of existence without any quality._ | #8 "Watch the turning point with devotion" (low confidence — true fabrication) |

### A.2  Duplicate copies (same canonical sutra appears in 2 or 3 files — keep only one)

After applying section C (rewrites to verbatim), pick the keeper using these tie-breakers, in order:
1. The copy that lives in the correct target category (column 3).
2. The copy whose wording is verbatim Osho.
3. The highest-confidence match.

| Canonical # | Short title | KEEP this copy | DELETE these copies |
|---:|---|---|---|
| 19 | Sit on your buttocks only | `centering` #19 | `sleep` #104, `void` #87 |
| 20 | Meditate in a moving vehicle | `centering` #20 | `sleep` #105 |
| 21 | Concentrate on a pain in your body | `centering` #21 | `sleep` #106 |
| 23 | Feel an object and become it | `void` #88 | `sensory` #67 |
| 28 | Imagine yourself losing all energy | `void` #85 | `centering` #11 |
| 29 | Devote yourself | `heart` #109 | `void` #86 |
| 47 | Use your name as a mantra | `sound` #47 | `imagination` #91 |
| 55 | Be aware of the gap between waking and sleep | **move** `witnessing` #55 → `sleep` | `heart` #108 |
| 56 | Think of the world as an illusion | `negation` #95 | `witnessing` #56 |
| 57 | Be undisturbed by desires | `witnessing` #57 | `mind` #106 |
| 58 | See the world as a drama | `witnessing` #58 | `mind` #107 |
| 62 | Use mind as the door to meditation | `mind` #108 | `heart` *(unnumbered)*, `sensory` #65 |
| 65 | Do not judge | **move** `mind` #109 → `negation` | `sensory` #68 |
| 72 | Feel the presence of the ever-living existence | `light` #72 | `centering` #10 |
| 79 | Focus on fire | `death` #79 | `light` #79 |
| 82 | Feel, don't think | **move** `void` #82 → `negation` | `mind` #92 |
| 85 | Thinking no thing | **move** `movement` #101 → `void` | `negation` #93 |
| 100 | Remain detached | `mind` #110 | `negation` #94 |
| 111 | Beyond knowing and not-knowing | `mind` #112 | `imagination` #90 |

---
## B. MOVE  (keeper from section A.2 is in the wrong category file)

| Canonical # | Short title | Currently in | MOVE TO |
|---:|---|---|---|
| 25 | Stop! | `death` #82 | **witnessing** |
| 26 | Face any desire | `sensory` #66 | **witnessing** |
| 31 | Look at an object as a whole | `imagination` #88 | **sensory** |
| 33 | Look into the limitless sky | `void` #89 | **light** |
| 51 | When joy arises, become it | `tantra` #51 | **heart** |
| 55 | Be aware of the gap between waking and sleep | `witnessing` #55 | **sleep** |
| 61 | Experience existence as wave-ing | `witnessing` #61 | **void** |
| 65 | Do not judge | `mind` #109 | **negation** |
| 82 | Feel, don't think | `void` #82 | **negation** |
| 83 | Change your focus to the gaps | `void` #83 | **negation** |
| 84 | Detach yourself from your body | `movement` #100 | **void** |
| 85 | Thinking no thing | `movement` #101 | **void** |
| 88 | Know the knower and the known | `witnessing` #62 | **mind** |
| 90 | Touch your eyes lightly | `sensory` #69 | **heart** |
| 94 | Feel yourself saturated | `sleep` #107 | **tantra** |
| 98 | Feel the peace in your heart | `negation` #96 | **heart** |
| 99 | Expand in all directions | `negation` #97 | **movement** |
| 101 | Believe that you are all-powerful | `negation` #92 | **mind** |
| 102 | Imagine spirit within and without | `death` #80 | **imagination** |
| 112 | Enter the space within | `movement` #102 | **void** |

---
## C. REWRITE  (paraphrased / corrupted sutra wording → verbatim Osho text)

| File | Badge | Canonical # | What it says now (excerpt) | Replace with (verbatim Osho) |
|---|---:|---:|---|---|
| `centering` | 19 | 19 | _Sit only on the buttocks, leaving legs and arms unsupported. Suddenly, the centering.…_ | _"Without support for feet or hands, sit only on the buttocks. Suddenly, the centering."_ |
| `sensory` | 69 | 90 | _Touch eyeballs as feathers, subtlety within. The heart opens.…_ | _"Touching eyeballs as a feather, lightness between them opens into heart and there permeates the cosmos."_ |
| `death` | 82 | 25 | _Just as you have the intuition that something will happen, the very moment you feel it wil…_ | _"Just as you have the impulse to do something, stop."_ |
| `sleep` | 107 | 94 | _Think of your body as being made of cosmic essences and leave it to be consumed.…_ | _"Feel your substance, bones, flesh, blood, saturated with the cosmic essence."_ |

---
## D. RENUMBER  (every retained entry → Osho's canonical 1-112 number)

After steps A–C, every retained entry must have its "Technique X of 112" badge set to the canonical number from Osho's *List of Meditations* appendix. Today the repo's badges are inconsistent — e.g. canonical #19 currently appears as centering #19 *and* sleep #104 *and* void #87. After dedup the lone keeper's badge becomes simply **#19**.

---
## E. ADD  (35 Osho sutras entirely missing from the repo)

For each row below, write a fresh entry in the indicated category file: verbatim sutra, faithful "In Plain English" paraphrase tied to Osho's commentary in the cited chapter, and a "How to Practice" section drawn from that same chapter (the EPUB is in the repo and is the source of truth).

| Canonical # | Short title | Verbatim sutra | Target category | Source chapter |
|---:|---|---|---|---|
| 10 | Become the caress | _"While being caressed, sweet princess, enter the caress as everlasting life."_ | **tantra** | 7. Techniques to Put You at Ease |
| 11 | Close your senses, become stone-like | _"Stop the doors of the senses when feeling the creeping of an ant. Then."_ | **sensory** | 7. Techniques to Put You at Ease |
| 12 | Let yourself become weightless | _"When on a bed or a seat, let yourself become weightless, beyond mind."_ | **sensory** | 7. Techniques to Put You at Ease |
| 14 | Put your awareness on your spine | _"Place your whole attention in the nerve, delicate as the lotus thread, in the center of your spinal column. In such be transformed."_ | **centering** | 9. Techniques for Centering |
| 18 | Look lovingly at an object | _"Look lovingly at some object. Do not go to another object. Here in the middle of the object – the blessing."_ | **centering** | 13. Inner Centering |
| 22 | Look at your past, disidentified | _"Let attention be at a place where you are seeing some past happening, and even your form, having lost its present characteristics, is transformed."_ | **witnessing** | 15. Seeing the Past as a Dream |
| 24 | Watch your moods | _"When a mood against someone or for someone arises, do not place it on the person in question, but remain centered."_ | **witnessing** | 15. Seeing the Past as a Dream |
| 30 | Close the eyes and stop their movement | _"Eyes closed, see your inner being in detail. Thus see your true nature."_ | **sensory** | 21. Three Looking Techniques |
| 34 | A secret method | _"Listen while the ultimate mystical teaching is imparted. Eyes still, without blinking, at once become absolutely free."_ | **light** | 23. Several More Looking Methods |
| 35 | Look into a deep well | _"At the edge of a deep well look steadily into its depths until – the wondrousness."_ | **light** | 23. Several More Looking Methods |
| 36 | Withdraw yourself completely | _"Look upon some object, then slowly withdraw your sight from it, then slowly withdraw your thought from it. Then."_ | **light** | 23. Several More Looking Methods |
| 43 | Focus your mind on the tongue | _"With mouth slightly open, keep mind in the middle of the tongue. Or, as breath comes silently in, feel the sound “hh.”"_ | **sound** | 29. Methods for the Dropping of Mind |
| 44 | A method for those with a sensitive ear | _"Center on the sound “aum” without any “a” or “m.”"_ | **sound** | 29. Methods for the Dropping of Mind |
| 46 | Closing ears and contracting rectum | _"Stopping ears by pressing and the rectum by contracting, enter the sound."_ | **sound** | 31. From Sound to Inner Silence |
| 63 | Be aware who is sensing | _"When vividly aware through some particular sense, keep in the awareness."_ | **sensory** | 39. From the Wave to the Cosmic Ocean |
| 66 | Be aware of that which never changes in you | _"Be the unsame same to friend as to stranger, in honor and dishonor."_ | **witnessing** | 43. Finding the Changeless through the Changing |
| 67 | Remember that everything changes | _"Here is the sphere of change, change, change. Through change consume change."_ | **witnessing** | 43. Finding the Changeless through the Changing |
| 68 | Be hope-less | _"As a hen mothers her chicks, mother particular knowings, particular doings, in reality."_ | **negation** | 45. Remaining with the Real |
| 69 | Go beyond bondage and freedom | _"Since, in truth, bondage and freedom are relative, these words are only for those terrified with the universe. This universe is a reflection of minds. As you see many suns in water from one sun, so see bondage and liberation."_ | **negation** | 45. Remaining with the Real |
| 80 | Imagine the whole world burning | _"Meditate on the make-believe world as burning to ashes and become being above human."_ | **death** | 53. From Death to Deathlessness |
| 81 | Everything converges in your being | _"As subjectively, letters flow into words and words into sentences, and as, objectively, circles flow into worlds and worlds into principles, find at last these converging in your being."_ | **imagination** | 53. From Death to Deathlessness |
| 86 | Imagine the unimaginable | _"Suppose you contemplate something beyond perception, beyond grasping, beyond not being. – you."_ | **imagination** | 59. Watch from the Hill |
| 87 | Feel "I am" | _"I am existing. This is mine. This is this. Oh beloved, even in such know illimitably."_ | **negation** | 59. Watch from the Hill |
| 89 | Include everything in your being | _"Beloved, at this moment let, mind, knowing, breath, form, be included."_ | **mind** | 61. Techniques to Become One with the Whole |
| 91 | Experience your etheric body | _"Kind Devi, enter etheric presence pervading far above and below your form."_ | **imagination** | 63. Start Creating Yourself |
| 92 | Be aware of the moments of no-thought | _"Put mind-stuff in such inexpressible fineness above, below and in your heart."_ | **imagination** | 65. Destroy the Limits |
| 93 | Consider the body limitless | _"Consider any area of your present form as limitlessly spacious."_ | **imagination** | 65. Destroy the Limits |
| 95 | Concentrate on the breasts, or on the root of the penis | _"Feel the fine qualities of creativity permeating your breasts’ and assuming delicate configurations."_ | **tantra** | 67. Go Beyond Mind and Matter |
| 97 | Fill endless space with your bliss body | _"Consider the plenum to be your own body of bliss."_ | **imagination** | 69. You Are Unknown to Yourself |
| 103 | Do not fight with desire | _"With your entire consciousness in the very start of desire, of knowing, know."_ | **mind** | 75. Seek the Rhythm of Opposites |
| 104 | The limits of perception | _"O Shakti, each particular perception is limited, disappearing in omnipotence."_ | **mind** | 75. Seek the Rhythm of Opposites |
| 105 | Realize the oneness of existence | _"In truth forms are inseparate. Inseparate are omnipresent being and your own form. Realize each as made of this consciousness."_ | **mind** | 75. Seek the Rhythm of Opposites |
| 108 | Become your own inner guide | _"This consciousness is the spirit of guidance of each one. Be this one."_ | **movement** | 77. Become Each Being |
| 109 | Feel your body as empty | _"Suppose your passive form to be an empty room with walls of skin – empty."_ | **void** | 79. The Philosophy of Emptiness |
| 110 | Be playful in activity | _"Gracious one, play. The universe is an empty shell wherein your mind frolics infinitely."_ | **void** | 79. The Philosophy of Emptiness |

---
## F. FINAL CATEGORY STRUCTURE  (target end-state)

**112** unique techniques across **15** category files. Per-file counts will sum exactly to 112 (the current index footer claims 112 but actually sums to 104).

| Category file | Final count | Canonical # included |
|---|---:|---|
| `vigyan-bhairav-breath-techniques.html` | 8 | 1, 2, 3, 4, 5, 6, 7, 8 |
| `vigyan-bhairav-centering-techniques.html` | 9 | 13, 14, 15, 16, 17, 18, 19, 20, 21 |
| `vigyan-bhairav-sound-techniques.html` | 11 | 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47 |
| `vigyan-bhairav-tantra-techniques.html` | 6 | 10, 48, 49, 50, 94, 95 |
| `vigyan-bhairav-witnessing-techniques.html` | 12 | 22, 24, 25, 26, 53, 54, 57, 58, 59, 60, 66, 67 |
| `vigyan-bhairav-sensory-techniques.html` | 8 | 11, 12, 30, 31, 32, 52, 63, 64 |
| `vigyan-bhairav-negation-techniques.html` | 7 | 56, 65, 68, 69, 82, 83, 87 |
| `vigyan-bhairav-light-techniques.html` | 13 | 33, 34, 35, 36, 70, 71, 72, 73, 74, 75, 76, 77, 78 |
| `vigyan-bhairav-death-techniques.html` | 2 | 79, 80 |
| `vigyan-bhairav-void-techniques.html` | 9 | 23, 27, 28, 61, 84, 85, 109, 110, 112 |
| `vigyan-bhairav-imagination-techniques.html` | 8 | 81, 86, 91, 92, 93, 96, 97, 102 |
| `vigyan-bhairav-heart-techniques.html` | 4 | 29, 51, 90, 98 |
| `vigyan-bhairav-mind-techniques.html` | 9 | 62, 88, 89, 100, 101, 103, 104, 105, 111 |
| `vigyan-bhairav-movement-techniques.html` | 4 | 99, 106, 107, 108 |
| `vigyan-bhairav-sleep-techniques.html` | 2 | 9, 55 |

---
## G. SUGGESTED EXECUTION ORDER

1. **Section A.1** — Delete the 6 fabricated entries (their commentary is also fabricated; nothing is salvageable).
2. **Section C** — Replace the wording of the 4 paraphrased entries with the verbatim Osho text. Keep their existing "How to Practice" only if it's actually consistent with the verbatim sutra; otherwise rewrite from the cited chapter.
3. **Section A.2** — Delete the duplicate copies. Keepers are now verbatim from step 2.
4. **Section B** — Move surviving keepers into their target category files (drag the `<article class="technique">` block from one file to another, update tags + nav links + jumplink anchor).
5. **Section D** — Update every retained entry's "Technique X of 112" badge to the canonical number.
6. **Section E** — Add the 35 missing sutras using the verbatim text in the table; new commentary tied to Osho's chapter for each.
7. Update `important-first-access-this.html` (the index): correct the 15 per-category counts so they actually sum to 112, and fix any "15 categories · 112 techniques" claim that today is arithmetically wrong.
8. Re-run the existing `AUDIT_REPORT.md`-style fidelity audit on the 35 new entries before publishing, since they will be the largest tranche of new commentary.
