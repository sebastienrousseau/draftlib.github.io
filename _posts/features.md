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

## Grounded by construction

A small local model will invent a plausible number. A cloud API will charge for it and want a network. draft takes neither risk: before a word is written, your sources are mined for claims, and a claim survives only if its quote appears verbatim in the source and every number in it appears in that quote.

## What it does

- **Any agent you already have.** Ten CLIs supported — Claude, Codex, Copilot, Cursor, Grok and more — driven headlessly through their own logged-in sessions. No API key. For a machine with no agent CLI, `--engine api:anthropic` (or `api:openai`) is an opt-in escape hatch that reads your own key from the environment — the keyless agent-session path stays the default and is never chosen for you.
- **Works offline.** When a session call fails because you are on a plane, the chain advances to a local Ollama model and stays there.
- **Verbatim grounding.** Quote-checked claims, numeric cross-checks and metric-conversion detection. Unverifiable claims are dropped before writing.
- **A semantic second gate, on request.** `--second-gate` adds an opt-in pass in which a local model judges whether each verified quote actually *supports* its claim, dropping the ones it does not. It is strictly additive — off by default, fail-open, and the verbatim gate stays primary — closing the one gap the verbatim gate is candid about: it checks wording, not meaning.
- **Claims from tables, not just prose.** With `--reader docling` a table is preserved as Markdown, and draft mines each numeric cell into a grounded claim — a value with its row and column headers — verified against the source like any other.
- **Every input format.** PDF, Markdown, plain text, DOCX, and **LaTeX (`.tex`)** — read directly, no external tool, with a formula kept as exact text where `pdftotext` would scramble it. `pdftotext` reads a 62-page paper in ~110&nbsp;ms; `--reader docling` adds tables and structure when they matter.
- **House style, enforced.** Banned words and phrases, British English, sentence-rhythm and structure rules — checked, not merely requested. Configurable with `--style`.
- **Provenance you can check — and sign.** Per-sentence attribution plus a C2PA manifest beside every set; `draft --verify` recomputes the digests. Configure a signing certificate (`DRAFT_C2PA_CERT` / `DRAFT_C2PA_KEY`, with `c2patool` installed) and draft emits a **signed** `.c2pa` credential bound to the article — whose signature and trust chain `--verify` then checks as well.
- **A portable verification record.** `draft --verify --json` emits a self-contained `draft.verification-record/v1` receipt — the article digest and whether it matches, the grounding summary, the signature state, and the verdict — that any other tool can re-check. Bring your own artifact, verify anywhere.
- **Configure once.** A project `draft.toml` or a user `~/.config/draft/config.toml` sets your defaults — engine, reader, models, output directory, style, signing key. Precedence is flags &gt; environment &gt; project file &gt; user file &gt; built-in default, so nothing about an existing setup changes.
- **Publish-ready sets.** Body, frontmatter and combined document, written side by side and regenerable without losing a curated field.
- **Never re-pay for extraction.** A failed run leaves its verified ledger on disk; `--resume` re-verifies it and skips straight to writing.

## Grounded, keyless, provable

Point it at one paper or twenty. Each becomes its own draft, and every draft can prove itself against its sources.
