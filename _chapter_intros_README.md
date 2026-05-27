# `_chapter_intros.json` — Handoff Notes

## What this file is

Paraphrased summaries of the framing sections that open each of the **39 sutra-introducing chapters** in Osho's *The Book of Secrets* (commentaries on the 112 sutras of *Vigyan Bhairav Tantra*).

Each entry captures the frame of mind Osho asks the reader to bring before practising the techniques in that chapter, plus one short attributed direct quote (each under 25 words).

## Structure

```json
{
  "source_book": "...",
  "description": "...",
  "chapter_count": 39,
  "chapters": [
    {
      "chapter": 3,
      "title": "Breath - A Bridge to the Universe",
      "summary": "Before practising any breath technique, Osho asks you to drop the seeker's mistake. ... As Osho puts it: \"You cannot seek truth. You can find it, but you cannot seek it. The very seeking is the hindrance.\"",
      "quote": "You cannot seek truth. You can find it, but you cannot seek it. The very seeking is the hindrance."
    },
    ...
  ]
}
```

## Chapter coverage (39)

3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79

(The book's even-numbered chapters are Q&A sessions and are not summarised here. Chapter 1, an opening overture without specific techniques, is also excluded.)

## Authoring rules followed

- Summaries are written in **paraphrased form** (not lifted from the EPUB).
- Each summary contains exactly **one short direct quote** attributed inline ("As Osho puts it: ..."), kept under 25 words.
- Word-count target: 100–150 per summary (actual range: 113–140; mean 127).
- The same quote is also exposed as a separate `quote` field for programmatic use.

## Intended use (next session)

For the rebuild of `vigyan-bhairav-tantra-complete-book.html`:

1. Load this JSON in `_build_merged.py` (or wherever the body is assembled).
2. For each chapter section in the body, find the entry whose `chapter` number matches and inject the `summary` (and optionally a styled blockquote of `quote`) **above** the sutras for that chapter.
3. Style with a distinct CSS class (e.g. `.chapter-intro`) so it reads as Osho's framing rather than as the sutras themselves.

## Wider plan (companion changes for that next session)

**Preface section — keep:**
- Critical Disclaimer
- The 15 Categories — Master Grid
- About

**Preface section — change:**
- Replace "I can't decide — surprise me" button with an 8-question quiz that scores answers across the 15 categories and recommends one specific sutra.
- Remove "Find a technique by what's happening in your life".
- Remove "Safety & Cautions Index".
- Remove "About These Techniques · Category Overviews".

**Body — change:**
- Inject these 39 chapter intros before their respective technique blocks (this file).

## Rebuilding this JSON

If the source EPUB or the desired phrasing changes, edit the `CHAPTERS` list in `_build_chapter_intros.py` and run:

```bash
python3 _build_chapter_intros.py
```

It performs sanity checks (39 chapters, correct chapter numbers, summary word-count bounds, quote length under 25 words) before writing the JSON.
