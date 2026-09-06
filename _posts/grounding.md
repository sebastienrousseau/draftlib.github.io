---
author: "contact@draftlib.com (Sebastien Rousseau)"
banner_alt: "draft — grounded article drafting from research papers."
banner_height: 630
banner_width: 1200
banner: "https://draftlib.com/img/og-card.png"
cdn: "https://draftlib.com"
changefreq: weekly
charset: utf-8
cname: draftlib.com
copyright: "© 2026 Sebastien Rousseau. Dual Apache-2.0 / MIT."
date: "2026-07-30T08:00:00+00:00"
description: "A claim survives only if its quote appears verbatim in the source and every number in it appears in that quote. Here is the whole gate."
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/grounding/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "grounded generation, hallucination, claim verification, verbatim quote, provenance"
language: en-GB
layout: "page"
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/grounding/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "A claim survives only if its quote appears verbatim in the source and every number in it appears in that quote. Here is the whole gate."
tags: "draft, grounded generation, research, markdown, go"
theme_color: "#0b0e14"
title: "How grounding works — draft"
url: "https://draftlib.com/grounding/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
eyebrow: "draft"
headline: "How grounding works"
lead: "A claim survives only if its quote appears verbatim in the source and every number in it appears in that quote. Here is the whole gate."
---

## How grounding works

The claim ledger is the only factual substrate the writer is given. Everything
else in `draft` exists to make that ledger trustworthy.

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
