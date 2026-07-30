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
description: "Command reference for draft: flags, environment variables, engine routing, resume and dry-run."
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/documentation/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "draft documentation, CLI flags, DRAFT_ENGINE, engine routing, resume, dry-run"
language: en-GB
layout: page
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/documentation/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "Command reference for draft: flags, environment variables, engine routing, resume and dry-run."
tags: "draft, grounded generation, research, markdown, go"
theme_color: "#0b0e14"
title: "Documentation — draft"
url: "https://draftlib.com/documentation/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
---

# Documentation

`draft` is a single binary. Point it at one or more sources; each becomes its
own draft, processed as a queue.

```text
draft [flags] <source> [more-sources...]
```

Bare filenames resolve against `~/Drop/Drafts/Sources`. PDF, Markdown and text
work everywhere; DOCX is macOS only.

## Flags

| Flag | Description |
| ---- | ----------- |
| `--engine <mode>` | `auto` (default), `ollama`, or a provider name |
| `--extract-engine <m>` | Backend for claim extraction (default: `--engine`) |
| `--write-engine <m>` | Backend for writing the article (default: `--engine`) |
| `--model <name>` | Session-provider model override (e.g. `opus`) |
| `--experimental` | Let auto mode use experimental providers |
| `--num-ctx <n>` | Ollama context window (default `8192`) |
| `--num-predict <n>` | Ollama max output tokens (default `6000`) |
| `--force-new` | Draft even if today's folder already has one |
| `--merge` | Combine all sources into one draft |
| `--resume` | Reuse a verified claim ledger from an earlier attempt |
| `--dry-run` | Report what a run would do, without calling a model |
| `--review <draft>` | Enhance an existing draft with surgical edits |
| `--frontmatter <f>` | Regenerate frontmatter and final document |
| `--keep-artifacts` | Keep the claim ledger beside a successful draft |
| `--print` | Run without the TUI; print draft paths to stdout |
| `--json` | Run without the TUI; one JSON object per job |
| `--completion <sh>` | Print a completion script: `bash`, `zsh`, `fish` |
| `--version` | Print version and exit |

## Choosing a backend

In `auto` mode `draft` takes the first installed stable CLI on your `PATH` and
drives it through its own login. No token is read, stored or logged. If a call
fails — you are offline, or not logged in — the chain advances to the next
backend and stays there for the rest of the run. There is deliberately no
up-front network probe: a flaky connectivity check must never be what
downgrades an online machine to the local model.

Providers, in auto-selection order: `claude`, `copilot`, `codex`, `agy`,
`cursor-agent`, `amp`, `crush`, `goose`, `grok`, `qwen`. The last four are
experimental and skipped unless you pass `--experimental`.

## Routing stages separately

Extraction is a dozen cheap, mechanical calls per paper. Writing is one call
that decides the article's quality. They do not need the same backend:

```sh
export DRAFT_EXTRACT_ENGINE=ollama
export DRAFT_WRITE_ENGINE=claude
draft paper.pdf
```

Each stage keeps its own fallback chain, so extraction dropping to Ollama does
not drag writing down with it.

## Environment variables

Flags beat environment variables. Environment variables beat defaults.

| Variable | Default | Purpose |
| -------- | ------- | ------- |
| `DRAFT_ENGINE` | `auto` | Backend selection |
| `DRAFT_EXTRACT_ENGINE` | — | Backend for claim extraction |
| `DRAFT_WRITE_ENGINE` | — | Backend for writing |
| `DRAFT_EDIT_ENGINE` | — | Backend for `--review` edits |
| `DRAFT_MODEL_SESSION` | — | Session-provider model override |
| `DRAFT_WRITE_MODEL` | `gemma3:4b` | Ollama writing model |
| `DRAFT_EXTRACT_MODEL` | `gemma3:4b` | Ollama claim-extraction model |
| `DRAFT_NUM_CTX` | `8192` | Ollama context window |
| `DRAFT_NUM_PREDICT` | `6000` | Ollama output-token ceiling |
| `DRAFT_WRITE_RETRIES` | `2` | Rewrite attempts on rule violations |
| `DRAFT_EXTRACT_CONCURRENCY` | `4` | Parallel extraction workers |
| `DRAFT_CALL_TIMEOUT` | `1800` | Seconds bounding one call; `0` disables |
| `OLLAMA_HOST` | `http://127.0.0.1:11434` | Ollama server address |

Every numeric variable is clamped at both ends. A value outside its range is
not silently ignored: the default is used and a warning goes to stderr, because
a tunable you believe took effect but did not is worse than one that was
rejected outright.

## Article sets

One article, three files, always in step:

```text
2026-07-30/
├── source/2026-07-30-<slug>-body.md         # the article — edit this
├── yaml/2026-07-30-<slug>-frontmatter.yaml  # adjacent frontmatter
└── final/2026-07-30-<slug>-final.md         # combined, ready to publish
```

Edit the body, then regenerate the other two in place with
`draft --frontmatter <body.md>`. Three rules make that safe to run at any time:
the filename is the article's identity, your curated fields always win, and
reprocessing unchanged input rewrites every file byte for byte identically.
