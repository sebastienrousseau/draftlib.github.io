---
name: "draft"
short_name: "draft"
title: "Benchmarks — draft"
description: "Measured numbers: a 62-page paper read in about 110 ms, a 10 MB binary, and the drop-rate reduction the claim gate delivers, with the methodology to reproduce them."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
breadcrumb: true
permalink: "https://draftlib.com/benchmarks/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Benchmarks"
headline: "Benchmarks"
lead: "The numbers draft quotes, and the methodology behind them."
---

### Extraction is not the bottleneck

Measured on Apple silicon, five runs each, on a 62-page book chapter.

| Stage | Time |
| --- | --- |
| Text extraction (`pdftotext`) | **107&nbsp;ms** (≈580 pages/s) |
| Sectioning | **2.1&nbsp;ms** (163,530 chars → 53 sections) |
| Claim parsing and verbatim verification | 23&nbsp;µs per claim block |
| House-rule validation of a finished draft | 662&nbsp;µs |
| **The whole deterministic path** | **~110&nbsp;ms** |

A **10&nbsp;MB** binary. **29&nbsp;ms** to start. **12&nbsp;MB** peak RSS. No Python, no PyTorch, no model weights, no GPU, no network.

Everything after that is model latency. On a 12-section paper against a local model, claim extraction runs to roughly ten minutes; the Go code accounts for well under a second of it. That ratio is the whole design.

### Recall

Measured over 3,217 extraction blocks from real papers, rendering-tolerant matching and source-based quote repair cut the verification drop rate from **29.6% to 8.5%**, with no loosening of the verbatim gate.

The recall figure is a ratchet, not a one-off measurement: a deterministic
corpus lives in the repository at `claims/testdata/corpus/`, and a test fails CI
if verified-claim recall across it ever falls. So the number cannot silently
regress between releases.

### Environment and method

- **Hardware:** Apple silicon (arm64).
- **Toolchain:** Go 1.24.2, Poppler (`pdftotext`) 26.07.
- **Deterministic-path timings** are warm runs of the reader, sectioner, claim
  gate and house-style checks — the work that happens without a model. Model
  latency is reported separately because it dominates and depends on your
  engine, not on draft.
- **Microbenchmarks** run at `-count=8` and are compared with `benchstat`, so a
  change has to clear measurement noise before it counts; CI fails a pull
  request whose benchmarks regress by more than 25%.

The binary, start-time and RSS figures are the conservative numbers draft
publishes; measured builds come out smaller and faster.

### Reproduce it yourself

From a clone of [the repository](https://github.com/sebastienrousseau/draft):

```sh
# Deterministic microbenchmarks (allocations included), comparable with benchstat
go test -run='^$' -bench=. -benchmem -benchtime=250ms -count=8 ./...

# The recall corpus — the 29.6% -> 8.5% drop-rate ratchet
go test ./claims

# The whole non-model path on your own paper, warm
draft --dry-run your-paper.pdf

# Binary size, stripped, as shipped
go build -ldflags='-s -w' -o draft ./cmd/draft && ls -lh draft
```

The benchmark regression gate that runs on every pull request is
`.github/workflows/benchmark.yml`.
