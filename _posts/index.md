---
author: "contact@draftlib.com (Sebastien Rousseau)"
banner_alt: "A terminal drafting a grounded article from a research paper, each claim checked verbatim against its source."
banner_height: 630
banner_width: 1200
banner: "https://draftlib.com/img/og-card.png"
cdn: "https://draftlib.com"
changefreq: weekly
charset: utf-8
cname: draftlib.com
copyright: "© 2026 Sebastien Rousseau. Dual Apache-2.0 / MIT."
date: "2026-07-30T08:00:00+00:00"
description: "draft turns research papers into publication-ready Markdown. A claim survives only if its quote appears verbatim in the source and every number in it appears in that quote. Go, no API key, works offline."
download: "https://github.com/sebastienrousseau/draft/releases"
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "draft, grounded generation, research papers, Markdown, Go CLI, Ollama, claim verification, hallucination, local LLM, static analysis"
language: en-GB
layout: index
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "Every sentence grounded in a fact it can prove."
tags: "grounded generation, research, markdown, go, cli, ollama, local-first"
theme_color: "#0b0e14"
title: "draft — grounded article drafting from research papers"
url: "https://draftlib.com/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
---

## Grounded by construction

A small local model will invent a plausible number. A cloud API will charge you
for the privilege and want a network. `draft` takes neither risk.

Before a word is written, your sources are mined for claims. A claim survives
only if its quote appears **verbatim** in the source, and every number in it
appears inside that quote. That verified ledger is the only factual substrate
the writer is given. It arranges facts. It does not source them.

Read [how grounding works](/grounding/) for the whole gate, check by check.

## No API key. No model download. No network required.

Online, `draft` writes through whichever AI coding-agent CLI you already have —
Claude, Codex, Copilot, Cursor, Grok and more — using that tool's own logged-in
session. No token is read, stored or logged. Offline, it falls back to a local
Ollama model and stays there.

There is no up-front network probe, because a flaky connectivity check must
never be what downgrades an online machine to the local model. If a call fails,
the chain advances and stays there for the rest of the run.

## Three files that stay in step

Finished work lands in `~/Drop/Drafts/YYYY-MM-DD/` as an article body, its
frontmatter, and the combined document. Edit the body and regenerate the other
two in place: the filename is the article's identity, your curated fields always
win, and reprocessing unchanged input rewrites every file byte for byte
identically. See the [command reference](/documentation/).

## Fast where it counts

Measured on Apple silicon, a 62-page book chapter is read and sectioned in
about **110 ms** by a 10 MB binary — roughly 580 pages per second. Everything
after that is model latency, which is exactly the point: the deterministic path
is never what makes a run slow.

## What it will not do

Honesty here saves you an evening.

- It is not a general-purpose summariser. A thin source yields a thin ledger
  and a short draft. That is the design, not a defect.
- It does not OCR. A PDF with no text layer is reported as such.
- It does not extract tables, figures or LaTeX maths.
- There is no direct API mode: you need an agent CLI or Ollama.

## Open source

Dual-licensed Apache-2.0 or MIT. Signed releases with a CycloneDX SBOM per
archive, an OpenSSF Scorecard, and a test suite gated at 95% statement coverage
with fuzzed parsers on every untrusted input.
