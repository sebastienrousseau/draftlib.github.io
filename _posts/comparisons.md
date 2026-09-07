---
name: "draft"
short_name: "draft"
title: "Comparisons — draft"
description: "How draft compares to RAG pipelines, to asking an LLM to summarise a paper, and to research-summary tools. An honest, criteria-based look."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "comparisons"
breadcrumb: true
permalink: "https://draftlib.com/comparisons/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Comparisons"
headline: "How draft compares"
lead: "Where draft sits next to retrieval pipelines, a plain LLM summary, and research-summary tools."
---

## draft vs. a RAG pipeline

Retrieval-augmented generation hands a model some retrieved source text at
generation time and hopes the output stays faithful to it. The fidelity is a
matter of prompt and luck, and it is checked after the fact, if at all.

draft inverts the order. It verifies each claim **before** writing: a claim
survives only if its quote appears verbatim in the source and every number in
it appears in that quote. The writer receives that verified ledger and nothing
else, and every sentence it produces is attributed back to a claim.

| | RAG pipeline | draft |
| --- | --- | --- |
| When is fidelity checked? | After generation, if at all | Before writing, as a gate |
| What can the writer say? | Anything, grounded or not | Only what a verified claim supports |
| Numbers | Model-generated | Cross-checked against the quote |
| Output provenance | None by default | Per-sentence attribution + C2PA manifest |

## draft vs. asking an LLM to summarise a paper

A general chat model will produce a fluent summary, and it will occasionally
invent a statistic, a citation or a result that reads perfectly and is simply
false. There is no gate and no record of which sentence came from where.

draft cannot write a sentence that no verified claim supports, and it ships an
attribution file mapping every sentence to the source span that backs it. When
a source is thin, the draft is visibly short rather than confidently padded.

## draft vs. research-summary tools

Tools such as NotebookLM, Elicit and SciSpace are strong at exploration:
question-answering across a library, semantic search, and interactive reading.
draft is not an exploration tool. It does one thing: turn a paper into a
publication-ready article whose every sentence is grounded and checkable, with
no account and no API key, and offline if you want.

If you want to *interrogate* a corpus, reach for those. If you want to
*publish* a grounded article from a paper and be able to prove it, that is
draft.

## Capability matrix

A criteria-based summary, as of September 2026. The rows are the dimensions that
actually differ; the columns are categories, with example products, rather than
a claim about any one product's current feature set. These tools evolve quickly,
so check a product's own documentation before relying on a cell.

| Capability | draft | Retrieval / RAG pipeline | General chat assistant | Research-summary platform (NotebookLM, Elicit, SciSpace, …) |
| --- | --- | --- | --- | --- |
| Fidelity check | Verbatim quote + numeric gate, before writing | Optional, after generation | None | Varies; usually citation links, not a verbatim gate |
| Per-sentence provenance | Yes, as a file | Rarely | No | Citations/links, not sentence-level attribution files |
| Signed content credentials (C2PA) | Yes, by default | No | No | Not typically |
| Independent verification | `draft --verify` recomputes digests | No | No | No |
| Runs fully offline | Yes (local model) | Depends on stack | No | No (hosted) |
| No account / no API key | Yes | Depends | Account required | Account required |
| Primary output | A publication-ready article | Answers/passages | Chat answer | Summaries, extractions, Q&A |
| Best at | Turning one paper into a grounded, provable article | Answering over a private corpus | Fast, flexible drafting | Exploring and reviewing a literature |

The distinction that matters: the research-summary platforms are literature
*review* and exploration tools, and they are good at it. draft is a paper-to-
*publication* pipeline. If your job is to survey a field or interrogate a
library, one of those fits better. If your job is to publish a grounded article
from a specific paper and be able to prove each sentence, that is draft.

## The honest limits

draft is not magic, and the [roadmap](/roadmap/) lists what it does not yet do:
table and figure values, LaTeX-heavy math, and scanned PDFs are current gaps.
See [how grounding works](/grounding/) for the gate in detail.
