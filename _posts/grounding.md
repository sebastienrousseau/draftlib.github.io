---
name: "draft"
short_name: "draft"
title: "How grounding works — draft"
description: "A claim survives only if its quote appears verbatim in the source and every number in it appears in that quote. Here is the whole gate."
author: "contact@draftlib.com (Sebastien Rousseau)"
date: "2026-07-30T08:00:00+00:00"
language: en-GB
layout: "page"
og_card: "grounding"
breadcrumb: true
permalink: "https://draftlib.com/grounding/"
logo: "https://draftlib.com/img/draft.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Grounding"
headline: "How grounding works"
lead: "A claim survives only if its quote appears verbatim in the source and every number in it appears in that quote. Here is the whole gate."
---

## How grounding works

The claim ledger is the only factual substrate the writer is given. Everything
else in `draft` exists to make that ledger trustworthy.

### What the gate does and does not check

The gate is precise about its own scope. It guarantees that every claim's quote
appears **verbatim** in the source and that every number in the claim appears in
that quote. It does **not** judge whether the claim *interprets* the quote
correctly — whether the unit, population, comparison, direction or causal
reading is faithful. Those are the writer's responsibility, and the
per-sentence attribution file is what lets a reader check them against the
source. "Grounded" here means source-linked and quote-and-number-checked, not
semantically guaranteed.

### The gate

Each source section is mined for claims. A claim is a short factual statement
plus the span of source text that supports it. `Verify` applies nine checks in
order and returns the first failure as its reason:

1. The claim and its quote are both non-empty.
2. The quote is at least 12 runes long.
3. The quote is valid UTF-8.
4. The quote holds no replacement character.
5. The quote occurs in the source.
6. The quote does not end mid-clause.
7. The claim type is one of the accepted kinds.
8. The claim strength is one of the accepted values.
9. **Every numeric token in the claim also appears in the quote.**

Anything else is dropped and counted. A thin source visibly yields a thin
ledger rather than a padded one.

### Rendering tolerance, not word tolerance

Quote matching normalises both sides before comparing, so the same words
verify however the model and the PDF extractor rendered the characters
between them: lower-cased, whitespace collapsed, smart quotes folded, a
literal `\n` a model wrote for a line break turned back into a space, a
hyphen the extractor dropped from a word restored, a ligature the PDF
rendered as one glyph split, and non-breaking or zero-width spaces removed.
That tolerance is necessary — PDF text extraction produces all of it
constantly, and byte-exact matching would drop true claims from every real
paper. Measured over 3,217 extraction blocks from real papers, it cut the
rate of dropped claims from 29.6% to 8.5%.

A quote that changes, adds, drops or reorders a *word* still fails. The
tolerance is over rendering, never over meaning.

### Repairing a cut quote

A model sometimes copies a supporting span but stops mid-clause, or copies one
too short to cite. Rather than drop it, `draft` extends the quote to its
sentence boundary using the **source's own words** — never the model's — so
the repaired quote is verbatim by construction and the same gate judges it exactly as it would any other. The extension stops at the first sentence end,
so a fabricated number living in the next sentence can never be pulled in. A
quote the source does not contain word for word is left alone and dropped.

### Why checks 3 and 4 exist

The same normalisation is lossy in one dangerous way. `strings.ToLower` maps every
invalid UTF-8 byte to the replacement character, so two *different* invalid
byte sequences normalise to the same text — and a fabricated quote could match
a source it does not occur in. A fuzzer found it. Requiring the quote to be
valid UTF-8 and free of replacement characters closes it, because normalisation
can only ever *introduce* that character, never any other.

Whitespace collapsing carries no equivalent risk: a run of spaces collapses to
one, never to none, so `a b` can never match `ab`.

### After the writing

A finished draft is checked twice more. The house rules cover structure, the
word band, banned vocabulary and emoji. The faithfulness pass cross-checks the
article against the ledger that grounded it — flagging a metric term no claim
supports, an ending that does not close a sentence, and near-duplicate
paragraphs, with ungrounded numbers and over-stated hedges reported as
warnings.

A violation triggers a targeted rewrite, not a shrug.

### Resume cannot weaken this

`--resume` reuses a ledger from an earlier attempt, but it re-verifies every
record against the freshly re-read sources first. A resumed ledger is trusted
because it still passes the same gate, not because `draft` wrote it. Edit a
source underneath and the records it no longer supports are dropped.
