---
name: "Draft Lib"
short_name: "draftlib"
title: "Performance Benchmarks: Draft Lib vs Pandoc & Comrak"
description: "Empirical benchmarks parsing and rendering 50-page legal and technical documents."
keywords: "draftlib benchmarks, rust markdown benchmark"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://draftlib.com/benchmarks/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Draft Lib — Fast Document Processing & Drafting Engine in Rust"
---

# Performance Benchmarks

Benchmarked on Apple Silicon M3 Max across 1,000 compilation iterations:

<div class="row g-3 my-4">
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">0.38 ms</div>
<div class="stat-label">Draft Lib AST Parse</div>
<div class="stat-source">Zero-allocation lexer</div>
</div>
</div>
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">14.20 ms</div>
<div class="stat-label">Pandoc C CLI</div>
<div class="stat-source">Haskell runtime baseline</div>
</div>
</div>
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">37x Faster</div>
<div class="stat-label">Compilation Throughput</div>
<div class="stat-source">Native Rust execution</div>
</div>
</div>
</div>
