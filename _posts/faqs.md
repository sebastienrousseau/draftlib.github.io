---
name: "draft"
short_name: "draft"
title: "FAQ — draft"
description: "Common questions about draft: how grounding works, which agent CLIs it uses, offline mode, provenance and licensing."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "faqs"
breadcrumb: true
faqpage: true
permalink: "https://draftlib.com/faqs/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "FAQ"
headline: "Frequently asked questions"
lead: "What draft is, how it grounds every sentence, and how your data is handled."
---

## What does "grounded by construction" mean?

Before a word is written, draft mines your sources for claims. A claim survives
only if its quote appears verbatim in the source and every number in it appears
in that quote. The writer is given that verified ledger and nothing else, so a
sentence with no backing claim cannot be written. See
[how grounding works](/grounding/).

## How is this different from RAG, or from asking an LLM to summarise a paper?

Retrieval hands a model source text and hopes it stays faithful. draft verifies
each claim *before* writing and drops anything unverifiable, then attributes
every sentence to the claim that backs it. The check is structural, not a prompt.

## Which agent CLIs does it use, and does it need an API key?

No API key by default. In `auto` mode draft drives whichever supported agent CLI
you are already logged into — Claude, Copilot, Codex, Cursor, Grok, Gemini and
more — through that tool's own session. Offline, it uses a local Ollama model.

If you have no agent CLI at all, `--engine api:anthropic` (or `api:openai`) is
an opt-in escape hatch that calls a hosted API directly with your own key from
the environment. It is never chosen automatically — the keyless path stays the
default — and exists only so a machine without an agent CLI still has an online
option.

## Can I set defaults so I don't repeat flags?

Yes. Put them in a project `draft.toml` or a user `~/.config/draft/config.toml`
(engine, reader, models, output directory, style, signing key). Precedence is
flags &gt; environment &gt; project file &gt; user file &gt; built-in default, so
a config file never changes what a command already does. `DRAFT_CONFIG` names an
explicit file; `DRAFT_NO_CONFIG` disables the layer.

## Does my paper leave my machine?

It depends on the engine. With a local Ollama model, nothing leaves your
machine. With a cloud agent CLI, the source excerpts draft needs to extract and
write are sent through that tool, exactly as if you had pasted them into it —
so choose the engine that matches your privacy needs. draft itself has no
servers and sends no telemetry.

## What runs fully offline?

`--engine ollama` keeps the entire pipeline local. Reading, claim
verification, house-style checks and provenance are all deterministic Go and
never touch the network.

## What is the C2PA manifest, and what does `--verify` check?

Every article ships a per-sentence attribution file and a C2PA manifest.
`draft --verify` recomputes the digests and reports whether the article still
matches the ledger it was written from. Editing an unsupported sentence makes
it fail. Configure a signing certificate (`DRAFT_C2PA_CERT` / `DRAFT_C2PA_KEY`,
with `c2patool` installed) and draft also writes a **signed** `.c2pa` credential
bound to the article, whose signature and trust chain `--verify` checks too.
`draft --verify --json` prints a portable `draft.verification-record/v1` receipt
that any other tool can re-check.

## Can draft check that a claim is used *correctly*, not just quoted?

The verbatim gate deliberately checks wording, not meaning. `--second-gate`
closes that gap on request: a local model judges whether each verified quote
actually *supports* its claim and drops the ones it does not. It is opt-in,
strictly additive, and fail-open, so it can only tighten the ledger — see
[how grounding works](/grounding/#the-optional-semantic-second-gate).

## What inputs are supported?

PDF, Markdown, plain text, DOCX and **LaTeX (`.tex`)** are all read directly.
`.docx` is built in on macOS via `textutil`, and works on any platform with
`--reader docling`; `.tex` needs no external tool and keeps a formula as exact
text. PDFs are read by `pdftotext` by default, or by `--reader docling` when
tables and structure matter — which also **mines table cells into claims**. The
one remaining input limit is a scanned PDF with no text layer; OCR is on the
[roadmap](/roadmap/).

## Does it work with non-English papers?

The verification gate is largely language-agnostic: UTF-8 handling,
normalisation and verbatim quote matching do not assume English. The
English-biased parts are the house-style rules and sentence-boundary repair,
which you can adjust with `--style`. Full locale-configurable style is on the
[roadmap](/roadmap/).

## Can I use the output commercially?

Yes. draft is free and open source under the MIT or Apache-2.0 licence. No
account, no telemetry.
