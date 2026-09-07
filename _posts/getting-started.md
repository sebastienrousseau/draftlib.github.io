---
name: "draft"
short_name: "draft"
title: "Getting started — draft"
description: "From zero to a grounded article: install draft, check your machine, and run your first paper."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "getting-started"
breadcrumb: true
permalink: "https://draftlib.com/getting-started/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Getting started"
headline: "Getting started"
lead: "Install draft, run --doctor, and turn your first paper into a grounded article."
---

## 1. Install

```sh
brew install --cask sebastienrousseau/tap/draft
```

Or with the Go toolchain:

```sh
go install github.com/sebastienrousseau/draft/cmd/draft@latest
```

## 2. Check the machine

```sh
draft --doctor
```

`--doctor` reports which agent CLIs you are logged into and whether Ollama is
reachable for offline runs. You need one online engine **or** Ollama.

```text
  ok  claude                 session provider
  ok  ollama                 responding at http://127.0.0.1:11434
  Ready. Run draft --dry-run <source> to check a specific paper.
```

## 3. Run your first paper

```sh
draft "my-paper.pdf"
```

draft reads the PDF, mines each section for claims, keeps only those whose
quote appears verbatim in the source, writes the article from that ledger, and
saves it with a per-sentence attribution file and a C2PA manifest.

## 4. Check the result

```sh
draft --verify 2026-07-29/final/2026-07-29-my-paper-final.md
```

This recomputes the digests and confirms the article still matches its ledger.

Next: the [documentation](/documentation/) for the full flag reference, or
[how grounding works](/grounding/) for the verification gate in detail.
