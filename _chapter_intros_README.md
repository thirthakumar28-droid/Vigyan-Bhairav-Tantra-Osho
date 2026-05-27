# `_chapter_intros.json` — Handoff Notes

## What this file is

Comprehensive multi-paragraph framings of the 39 sutra-introducing chapters in
Osho's *The Book of Secrets* (commentaries on the 112 sutras of *Vigyan Bhairav
Tantra*).

Each entry captures the frame of mind Osho asks the reader to bring before
practising the techniques in that chapter, including the major anecdotes,
illustrations, distinctions and arguments he uses to set up the techniques.
Each chapter exposes 3–4 paragraphs of paraphrased framing plus 2–3 short
attributed direct quotes (each under 30 words).

## Schema

```json
{
  "source_book": "...",
  "description": "...",
  "chapter_count": 39,
  "chapters": [
    {
      "chapter": 3,
      "title": "Breath - A Bridge to the Universe",
      "paragraphs": [
        "Before the four breath techniques are even named, Osho asks ...",
        "The obstacle, Osho insists, is the very mechanism we are trying ...",
        "This is why Shiva refuses to philosophise ...",
        "The four breath sutras, then, are simply turnings of attention ..."
      ],
      "quotes": [
        "You cannot seek truth. You can find it, but you cannot seek it. The very seeking is the hindrance.",
        "The truth is in the present, and mind is always in the future or in the past, so there is no meeting between mind and truth.",
        "Your being here and now is the truth, and your being here and now is the freedom, and your being here and now is the nirvana."
      ]
    },
    ...
  ]
}
```

## Chapter coverage (39)

3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79

(The book's even-numbered chapters are Q&A sessions and are not summarised
here. Chapter 1, an opening overture without specific techniques, is also
excluded.)

## Authoring rules followed

- Paragraphs are written in **paraphrased form** in the file author's own
  English prose, but track Osho's framing argument faithfully chapter by
  chapter, using the discourse text that opens each chapter (extracted from
  the EPUB into `.epub_work/extracted/chNN_framing.txt`).
- Each `quotes[]` entry is a short verbatim fragment attributed to Osho
  (each under 30 words).
- Per-chapter targets:
  - 3–5 paragraphs (actual: 3 or 4 in every chapter)
  - 2–4 short quotes (actual: 3 in nearly every chapter)
  - Each paragraph at least 60 words.
- Total body words across all chapters: ~14,500 (avg ~370 per chapter).
- The build script enforces all of this with `assert` checks.

## Renderer (in `_build_merged.py`)

`render_chapter_intro` reads each entry's `paragraphs` and `quotes` lists and
emits one `<p class="chapter-intro-body">` per paragraph plus one
`<blockquote class="chapter-intro-quote">` per quote, all wrapped in an
`<aside class="chapter-intro">`. The renderer also retains backward
compatibility with the legacy single-`summary` / single-`quote` schema, so old
JSON files will still render correctly.

## Rebuilding this JSON

If the source EPUB or the desired phrasing changes, edit the `CHAPTERS` list
in `_build_chapter_intros.py` and run:

```bash
python3 _build_chapter_intros.py
```

The script performs sanity checks (39 chapters in the correct numerical order,
paragraph count and word-count bounds, quote length under 35 words) before
writing the JSON.

## Re-extracting the source framings (optional)

The framing source for each chapter is extracted from the bundled EPUB by
unzipping it into `.epub_work/` and running the extractor:

```bash
unzip -q "The Book of Secrets (Osho) (z-library.sk, 1lib.sk, z-lib.sk).epub" -d .epub_work
python3 .epub_work/extract_framings.py
```

This populates `.epub_work/extracted/chNN_framing.txt` with the discourse
text after the chapter's "The Sutras:" listing and before the first specific
technique commentary, for each odd-numbered chapter from 3 to 79.
