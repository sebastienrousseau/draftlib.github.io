---
author: "contact@draftlib.com (Sebastien Rousseau)"
banner_alt: "draft — grounded article drafting from research papers."
banner_height: 500
banner_width: 1200
banner: "https://draftlib.com/img/draft.svg"
cdn: "https://draftlib.com"
changefreq: weekly
charset: utf-8
cname: draftlib.com
copyright: "© 2026 Sebastien Rousseau. Dual Apache-2.0 / MIT."
date: "2026-07-30T08:00:00+00:00"
description: "draft is a command-line tool first, but every capability is an importable Go package."
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/library/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "go packages, library, claims, pipeline, engine, frontmatter, validate"
language: en-GB
layout: page
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/library/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "draft is a command-line tool first, but every capability is an importable Go package."
tags: "draft, grounded generation, research, markdown, go"
theme_color: "#0b0e14"
title: "Go packages — draft"
url: "https://draftlib.com/library/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
---

# Go packages

`draft` is a command-line tool first. But every capability is an importable Go
package, and only the PDF extractor, the brand assets and the TUI stay
internal.

```sh
go get github.com/sebastienrousseau/draft@latest
```

| Package | What it does |
| ------- | ------------ |
| `claims` | Claim parsing, the verbatim-quote gate, ledger rendering |
| `config` | Flag, environment and default resolution |
| `engine` | The `Engine` seam, provider registry, Ollama, fallback chain |
| `frontmatter` | Metadata, YAML generation, article-set regeneration |
| `pipeline` | Five-phase orchestration, retries, continuation, events |
| `prompt` | Grounded claim, writing and review prompts |
| `rules` | Shared editorial constants |
| `validate` | House-rule and faithfulness checks |

Each has its own README with a runnable quick start and an API table. Full
reference on [pkg.go.dev](https://pkg.go.dev/github.com/sebastienrousseau/draft).

## The seam that matters

`Engine` is two methods. The whole test suite and every example run against
in-process implementations of it, which is why none of them need a network:

```go
type Engine interface {
	Name() string
	Generate(ctx context.Context, req Request) (Result, error)
}
```

Return `Result{Truncated: true}` and the pipeline continues generation rather
than saving a mid-sentence article.

> **API stability.** While the module is `0.0.x`, the exported Go API may
> change between releases without a deprecation cycle. Pin an exact version if
> you depend on it. The CLI's flags and output layout are the stable surface;
> the Go packages are not yet.
