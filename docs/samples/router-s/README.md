# A real, verifiable draft sample

This is a complete, unedited article set that `draft` produced from the
rights-cleared test paper `two-column.pdf` ("Router-S: Conditional Compute for
Language Models"). It is published exactly as written, so you can check it
yourself.

## What's here

- `two-column.pdf` — the source paper.
- `final/2026-09-07-a-validation-loss-of-3-41-and-a-variance-that-swallows-the-result-final.md` — the generated article (frontmatter + body).
- `provenance/2026-09-07-a-validation-loss-of-3-41-and-a-variance-that-swallows-the-result-attribution.json` — every sentence mapped to the claim and
  verbatim quote that backs it. 13 of 36 sentences rest on a claim; the rest are
  connective prose.
- `provenance/2026-09-07-a-validation-loss-of-3-41-and-a-variance-that-swallows-the-result-c2pa.json` — the C2PA manifest (article and source digests,
  claim IDs, engine and reader).
- `2026-09-07-a-validation-loss-of-3-41-and-a-variance-that-swallows-the`… `-verified-claim-ledger.md` — the 6 verified claims (9 were
  dropped by the gate).

## Verify it yourself

Install draft (`brew install --cask sebastienrousseau/tap/draft`), then from
inside this folder:

```sh
draft --verify final/2026-09-07-a-validation-loss-of-3-41-and-a-variance-that-swallows-the-result-final.md
```

It recomputes the digests and confirms the article is unchanged since it was
written, the claim ledger matches, and the source PDF is unchanged since it was
read. Edit a sentence in the article and re-run it: verification fails.

Generated with a development build of draft 0.0.35, engine `claude` (model
`sonnet`), reader `pdftotext`.
