---
name: "draft"
short_name: "draft"
title: "Examples — draft"
description: "End-to-end examples: a research paper in, a grounded article out, with attribution and a C2PA manifest you can verify."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
breadcrumb: true
permalink: "https://draftlib.com/examples/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Examples"
headline: "Examples"
lead: "See a paper become a grounded article — command, output, and the provenance you can check."
---

## One paper, start to finish

```sh
draft "2603.23420.pdf"
```

draft reads the paper, builds a verified claim ledger, writes the article from
it, and saves a dated set:

```text
2026-07-29/
├── source/2026-07-29-attention-routing-body.md
├── yaml/2026-07-29-attention-routing-frontmatter.yaml
├── final/2026-07-29-attention-routing-final.md
└── provenance/
    ├── 2026-07-29-attention-routing-attribution.json
    └── 2026-07-29-attention-routing-c2pa.json
```

The attribution file maps each sentence in the article to the claim, and the
verbatim source quote, that backs it. Nothing in the body exists without a line
in that file.

## Verify it

```sh
draft --verify 2026-07-29/final/2026-07-29-attention-routing-final.md
```

The manifest digests are recomputed and checked. Edit a sentence the ledger did
not support and verification fails — that is the guarantee.

## A batch, merged into one draft

```sh
draft --merge a.pdf b.pdf c.pdf
```

## Offline, on a plane

```sh
draft --engine ollama "my-paper.pdf"
```

No network, no API key. The same gate runs; only the writer changes.

More runnable examples live in the
[repository](https://github.com/sebastienrousseau/draft/tree/main/examples).
