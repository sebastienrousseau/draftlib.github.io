---
name: "draft"
short_name: "draft"
title: "Go packages — draft"
description: "draft is a command-line tool first, but every capability is an importable Go package."
author: "contact@draftlib.com (Sebastien Rousseau)"
date: "2026-07-30T08:00:00+00:00"
language: en-GB
layout: "page"
permalink: "https://draftlib.com/library/"
logo: "https://draftlib.com/img/draft.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Library"
headline: "Go packages"
lead: "draft is a command-line tool first, but every capability is an importable Go package."
---

## Go packages

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
| `provenance` | Per-sentence claim attribution and the C2PA manifest a reader can check |
| `rules` | Shared editorial constants |
| `validate` | House-rule and faithfulness checks |

Each has its own README with a runnable quick start and an API table. Full
reference on [pkg.go.dev](https://pkg.go.dev/github.com/sebastienrousseau/draft).

### The seam that matters

`Engine` is two methods. The whole test suite and every example run against
in-process implementations of it, which is why none of them need a network:

```go
type Engine interface {
	Name() string
	Generate(ctx context.Context, req Request) (Result, error)
}
```

Return `Result{Truncated: true}` and the pipeline continues generation rather
than saving a mid-sentence article; `Result` also carries a `Usage` the
pipeline sums into the per-job token and dollar cost. A backend can drive a
one-shot CLI, a long-lived Agent Client Protocol agent, or the local model,
all behind the same two methods.

> **API stability.** While the module is `0.0.x`, the exported Go API may
> change between releases without a deprecation cycle. Pin an exact version if
> you depend on it. The CLI's flags and output layout are the stable surface;
> the Go packages are not yet.
