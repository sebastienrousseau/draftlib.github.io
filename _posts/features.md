---
name: "draft"
short_name: "draft"
title: "Features — draft"
description: "Grounded by construction, keyless, offline-capable and provable. Every capability draft ships, and how it proves each one."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "features"
breadcrumb: true
permalink: "https://draftlib.com/features/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Features"
headline: "Features"
lead: "Grounded, keyless, provable. What draft does, and how it proves it."
---

### Grounded by construction

A small local model will invent a plausible number. A cloud API will charge for it and want a network. draft takes neither risk: before a word is written, your sources are mined for claims, and a claim survives only if its quote appears verbatim in the source and every number in it appears in that quote.

### What it does

- **Any agent you already have.** Ten CLIs supported — Claude, Codex, Copilot, Cursor, Grok and more — driven headlessly through their own logged-in sessions. No API key.
- **Works offline.** When a session call fails because you are on a plane, the chain advances to a local Ollama model and stays there.
- **Verbatim grounding.** Quote-checked claims, numeric cross-checks and metric-conversion detection. Unverifiable claims are dropped before writing.
- **Two readers.** `pdftotext` by default (a 62-page paper in ~110&nbsp;ms); `--reader docling` when tables and structure matter.
- **House style, enforced.** Banned words and phrases, British English, sentence-rhythm and structure rules — checked, not merely requested. Configurable with `--style`.
- **Provenance you can check.** Per-sentence attribution plus a C2PA manifest beside every set; `draft --verify` recomputes the digests.
- **Publish-ready sets.** Body, frontmatter and combined document, written side by side and regenerable without losing a curated field.
- **Never re-pay for extraction.** A failed run leaves its verified ledger on disk; `--resume` re-verifies it and skips straight to writing.

### Grounded, keyless, provable

Point it at one paper or twenty. Each becomes its own draft, and every draft can prove itself against its sources.
