---
name: "draft"
short_name: "draft"
title: "Contributing — draft"
description: "How to contribute to draft, the open-source Go CLI."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "contributing"
breadcrumb: true
permalink: "https://draftlib.com/contributing/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Contributing"
headline: "Contributing"
lead: "draft is open source under MIT or Apache-2.0. Issues and pull requests are welcome."
---

draft is developed in the open at
[github.com/sebastienrousseau/draft](https://github.com/sebastienrousseau/draft).

## Getting set up

```sh
git clone https://github.com/sebastienrousseau/draft
cd draft && make build && make test
```

## Before you open a pull request

The project holds a strict gate. Run it locally:

- `gofmt` and `go vet` clean
- `golangci-lint run` with zero issues
- `go test -race ./...` green, with the coverage floor met
- REUSE-compliant licence headers on new files

Small, focused pull requests with a test that fails before your change and
passes after are the easiest to review. Open an issue first for anything large.
