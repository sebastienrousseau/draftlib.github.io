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
description: "Runnable, network-free demos of every capability: the dashboard, grounding, the pipeline, review and article sets."
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/examples/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "draft examples, go run, demo, dashboard, pipeline"
language: en-GB
layout: page
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/examples/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "Runnable, network-free demos of every capability: the dashboard, grounding, the pipeline, review and article sets."
tags: "draft, grounded generation, research, markdown, go"
theme_color: "#0b0e14"
title: "Examples — draft"
url: "https://draftlib.com/examples/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
---

# Examples

Every capability has a runnable demo. No model, no session CLI, no API key, no
network. Clone the repository and run any of them:

```sh
git clone https://github.com/sebastienrousseau/draft
cd draft
go run ./examples/dashboard
```

| Example | What it shows |
| ------- | ------------- |
| `dashboard` | The real full-screen TUI driven by an in-process engine — queue, phases, live preview and focus timer |
| `providers` | Session providers in auto-selection order, install status, default models |
| `grounding` | Claim verification against a source, ledger rendering, grounded prompt, house-rule validation |
| `pipeline` | The five-phase pipeline end to end, merged multi-source drafting, streamed events |
| `review` | Surgical-edit enhancement: body-only prompting, frontmatter re-attachment, set resync |
| `frontmatter` | Metadata extraction, custom publisher identity, the three regeneration rules |

## Everyday recipes

| Command | What it does |
| ------- | ------------ |
| `draft paper.pdf` | Draft one paper, engine auto-selected |
| `draft a.pdf b.pdf c.pdf` | Queue three papers, one draft each |
| `draft --merge notes.md paper.pdf` | One draft from combined sources |
| `draft --dry-run paper.pdf` | See the plan and the cost first |
| `draft --resume paper.pdf` | Reuse the ledger from a failed attempt |
| `draft --engine ollama paper.pdf` | Force the local model |
| `draft --review draft.md paper.pdf` | Enhance an existing draft from its sources |
| `draft --json paper.pdf` | One JSON object per job, for scripting |

## Scripting

`--json` emits one object per job, including per-phase timings, so a run is
comparable across invocations rather than only readable:

```json
{
  "source": "/papers/router-s.pdf",
  "output": "/drafts/2026-07-30/final/2026-07-30-router-s-final.md",
  "engine": "claude",
  "words": 1180,
  "ok": true,
  "duration_ms": 214301,
  "phases_ms": { "Extract claims": 198442, "Write article": 12903 }
}
```
