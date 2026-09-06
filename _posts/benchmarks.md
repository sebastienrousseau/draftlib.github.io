---
name: "draft"
short_name: "draft"
title: "Benchmarks — draft"
description: "Measured numbers: a 62-page paper read in about 110 ms, a 10 MB binary, and the drop-rate reduction the claim gate delivers, with the methodology to reproduce them."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
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
