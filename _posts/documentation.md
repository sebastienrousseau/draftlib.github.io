---
name: "draft"
short_name: "draft"
title: "Documentation — draft"
description: "Install draft, run your first paper-to-post in under a minute, and read the full command-line reference."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
breadcrumb: true
permalink: "https://draftlib.com/documentation/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Docs"
headline: "Documentation"
lead: "Install, quickstart, and the full command-line reference for draft."
---

## Install

**Homebrew (macOS, recommended)**

```sh
brew install --cask sebastienrousseau/tap/draft
```

**Go toolchain (any platform)**

```sh
go install github.com/sebastienrousseau/draft/cmd/draft@latest
```

**From source**

```sh
git clone https://github.com/sebastienrousseau/draft
cd draft && make build
```

### Dependencies by platform

draft reads PDFs with `pdftotext` (Poppler) and, offline, writes with a local
[Ollama](https://ollama.com) model. `.docx` reads through `textutil` on macOS
(built in) or `--reader docling` anywhere.

| Platform | Poppler (`pdftotext`) | Ollama (offline writing) |
| --- | --- | --- |
| **macOS** | `brew install poppler` | `brew install ollama` |
| **Debian / Ubuntu** | `sudo apt-get install poppler-utils` | `curl -fsSL https://ollama.com/install.sh \| sh` |
| **Fedora** | `sudo dnf install poppler-utils` | `curl -fsSL https://ollama.com/install.sh \| sh` |
| **Windows** | `scoop install poppler` (or `choco install poppler`) | download from [ollama.com/download](https://ollama.com/download) |

You need Poppler only for PDF input, and Ollama only for offline runs; online,
draft writes through an agent CLI you are already logged into.

## Quickstart

Check that the machine is ready, then run a paper:

```sh
draft --doctor
draft "2603.23420.pdf"
```

Online, draft drives whichever agent CLI you are already logged into. Offline,
it falls back to a local Ollama model. Each source becomes its own dated
article set.

**Supported inputs:** PDF, Markdown and plain text on every platform; `.docx`
built in on macOS (`textutil`) or anywhere with `--reader docling`.

## Command-line reference

```text
draft [flags] <source> [more-sources...]
```

| Flag                   | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| `--engine <mode>`      | `auto` (default), `ollama`, or a provider name            |
| `--model <name>`       | Session-provider model override (e.g. `opus`)             |
| `--extract-engine <m>` | Backend for claim extraction (default: `--engine`)        |
| `--write-engine <m>`   | Backend for writing the article (default: `--engine`)     |
| `--experimental`       | Let auto mode use experimental providers                  |
| `--strict-numbers`     | Fail a draft carrying a number found in no verified claim |
| `--reader <name>`      | `pdftotext` (default) or `docling` for tables and structure |
| `--style <file>`       | House-style rules to enforce                              |
| `--resume`             | Reuse a verified claim ledger from an earlier attempt     |
| `--verify <f>`         | Check an article against its provenance, and exit         |
| `--frontmatter <f>`    | Regenerate frontmatter and final document from an article |
| `--review <draft>`     | Enhance an existing draft with surgical edits             |
| `--out <dir>`          | Directory to write drafts into (default `~/Drop/Drafts`)  |
| `--merge`              | Combine all sources into one draft                        |
| `--dry-run`            | Report what a run would do, without calling a model       |
| `--doctor`             | Check that this machine can run draft, and exit           |
| `--print`              | Run without the TUI; print draft paths to stdout          |
| `--json`               | Run without the TUI; one JSON object per job on stdout    |
| `--version`            | Print version and exit                                    |
| `-h, --help`           | Show help                                                 |

The [README](https://github.com/sebastienrousseau/draft#usage) lists every
flag, including cache and Ollama-tuning options.

## Engines

draft never asks for an API key. In `auto` mode it walks a list of supported
agent CLIs and uses the first one you are logged into, driving that tool's own
session. Supported engines include Claude, Copilot, Codex, Cursor, Grok and
Gemini; offline, it uses a local Ollama model. Force one with `--engine <name>`.

## Article sets

Each run writes one article as three files that stay in sync, plus two a reader
can check:

```text
2026-07-29/
├── source/…-body.md              # the article — edit this
├── yaml/…-frontmatter.yaml       # adjacent frontmatter
├── final/…-final.md              # combined, ready to publish
└── provenance/
    ├── …-attribution.json        # which claim backs each sentence
    └── …-c2pa.json               # C2PA manifest definition
```

Edit the body, then regenerate the other two in place with
`draft --frontmatter <body.md>`. Your curated fields are preserved; only
missing ones are rebuilt.

## Provenance

Every set ships a per-sentence attribution file and a C2PA manifest.
`draft --verify <final.md>` recomputes the digests and reports whether the
article still matches the ledger it was written from.

## Troubleshooting

- **No text in the PDF.** A scanned PDF has no text layer; extraction returns
  nothing. Use a source with selectable text.
- **No engine found.** Run `draft --doctor`. Log into an agent CLI, or install
  Ollama for offline runs.
- **A thin ledger.** A source with few checkable claims yields a short draft by
  design — draft never pads.

Full library API is on
[pkg.go.dev](https://pkg.go.dev/github.com/sebastienrousseau/draft).
