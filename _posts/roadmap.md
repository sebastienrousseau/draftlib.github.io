---
name: "draft"
short_name: "draft"
title: "Roadmap — draft"
description: "What draft does not yet do, and the sequence for closing those gaps: table and figure extraction, LaTeX and math, OCR for scanned PDFs, and more input formats."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "roadmap"
breadcrumb: true
permalink: "https://draftlib.com/roadmap/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Roadmap"
headline: "Roadmap"
lead: "What draft does not yet do, stated plainly, and the order we mean to close the gaps."
---

draft is deliberate about its limits. A tool that sells verifiability should be
the first to say what it cannot yet verify. This page is the honest list, and
the [FAQ](/faqs/) links here from every limitation it mentions.

## Planned

### Table and figure values

Docling is already available as a reader (`--reader docling`), but tabular
values do not yet become verifiable claims. The plan is to mine table cells as
claims, with the row and column headers as the quote context, and to verify
numbers against the cell. Figure captions are text and gate-compatible; chart
values are a later step.

### LaTeX and math

Today, math around a claim can cause the surrounding text to be dropped. The
first step is to preserve inline math as opaque tokens so neighbouring claims
still verify; the second is to accept `.tex` source directly, where the math is
exact text and verbatim matching is clean.

### OCR for scanned PDFs

A scanned PDF has no text layer, so extraction returns nothing and the run
fails. The plan is to detect this and fall back to OCR, surfacing OCR-derived
claims as a distinct, flagged class rather than treating them as equal to
verbatim ones, so the trust model is preserved rather than quietly diluted.

### More input and output formats

`.docx` input already works today — built in on macOS via `textutil`, and on
any platform with `--reader docling`. The remaining input gap is HTML, which
reduces cleanly to text once the reader seam accepts it. For output beyond the
current Markdown set, an HTML export is the likely next step; a `.docx` export
is better left to a documented pandoc recipe.

### Non-English papers

The verification gate is largely language-agnostic — UTF-8, normalisation and
verbatim matching do not assume English. The English-biased parts are the
house-style rules and sentence-boundary repair. The plan is to make style rules
locale-configurable with `--style` and to document current behaviour on
non-English input.

## Not planned as the default

A direct API-key mode (`--engine api:<provider>`) is possible as an escape
hatch for users with no agent CLI, but keyless operation is the whole point, so
it will never be the default story.

---

Want something moved up the list? Open an issue on
[GitHub](https://github.com/sebastienrousseau/draft/issues).
