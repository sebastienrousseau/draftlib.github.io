---
name: "draft"
short_name: "draft"
title: "Architecture — draft"
description: "How draft turns a paper into a grounded article: read and section, extract and verify, write, then attribute and sign."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "architecture"
breadcrumb: true
permalink: "https://draftlib.com/architecture/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Architecture"
headline: "How draft is built"
lead: "Four phases, one claim gate. Read and section, extract and verify, write, then attribute and sign."
---

## The pipeline

```text
PDF ──▶ Read & section ──▶ Extract & verify ──▶ Write ──▶ Attribute & sign
        (pdftotext /        (the claim gate)     (engine)   (provenance +
         docling)                                            C2PA manifest)
```

1. **Read and section.** `pdftotext` extracts the text (a 62-page paper in
   about 110 ms); `--reader docling` is available when tables and structure
   matter. The text is split into sections.
2. **Extract and verify.** Each section is mined for claims. A claim is a short
   factual statement plus the source span that supports it, and it survives
   only if its quote appears verbatim in the source and every number in it
   appears in that quote. This gate is the choke point of the whole design.
3. **Write.** The verified ledger — and nothing else — is handed to the engine.
   Online, that is whichever agent CLI you are logged into; offline, a local
   Ollama model. House-style rules are enforced on the result, not merely
   requested.
4. **Attribute and sign.** Every sentence is mapped back to the claim that
   backs it, and the set is written with a per-sentence attribution file and a
   C2PA manifest a reader can check.

## The engine seam

Everything model-facing sits behind one small interface, so the same pipeline
drives a one-shot CLI, a long-lived Agent Client Protocol agent, or a local
model, and the whole test suite runs without a network:

```go
type Engine interface {
	Name() string
	Generate(ctx context.Context, req Request) (Result, error)
}
```

The capabilities are importable Go packages — `claims`, `engine`, `pipeline`,
`provenance`, `validate` and more. See the [library](/library/) page and
[pkg.go.dev](https://pkg.go.dev/github.com/sebastienrousseau/draft).
