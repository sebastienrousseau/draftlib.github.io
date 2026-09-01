---
name: "Draft Lib"
short_name: "draftlib"
title: "Draft Lib: Fast Document Processing & Drafting Engine in Rust"
description: "A modular, type-safe Rust library for compiling, formatting, and generating structured legal and technical drafts with zero allocations."
keywords: "draftlib, rust document engine, markdown ast compiler, type-safe drafting"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "index"
permalink: "https://draftlib.com/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Draft Lib — Fast Document Processing & Drafting Engine in Rust"
---

<section class="hero-editorial">
<div class="eyebrow-badge">
<span class="eyebrow-pulse"></span>
<span>Document Engineering · Open Source · Rust · Updated September 2026</span>
</div>
<h1>High-velocity document compilation & drafting.<br>Type-safe. Zero-allocation. Modular.</h1>
<p class="hero-lead">An open-source, high-performance Rust library for generating, validating, and formatting technical specifications, regulatory filings, and legal contracts. Compiles Markdown and structured schemas into deterministic ASTs with sub-millisecond latency.</p>
<div class="hero-actions">
<a href="/getting-started/index.html" class="btn-primary-quantum">Get Started (Crate & CLI) →</a>
<a href="/features/index.html" class="btn-secondary-quantum">Explore Capabilities</a>
</div>
</section>

<!-- SECTION 2: KEY STATS TICKER -->
<section class="clock-ticker-section my-5" aria-label="Performance Benchmarks">
<div class="row g-3">
<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">&lt; 0.4 ms</div>
<div class="stat-label">AST Parse Latency</div>
<div class="stat-source">Zero-copy token streaming · <a href="/benchmarks/index.html">Benchmark Specs ↗</a></div>
</div>
</div>

<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">100% Type-Safe</div>
<div class="stat-label">Compile-Time Validation</div>
<div class="stat-source">Strict schema enforcement · <a href="/features/index.html">Type Safety ↗</a></div>
</div>
</div>

<div class="col-md-4 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">100% Sovereign</div>
<div class="stat-label">Zero Telemetry</div>
<div class="stat-source">Air-gapped execution · <a href="/security/index.html">Security Architecture ↗</a></div>
</div>
</div>

<div class="col-md-6 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">Multi-Target</div>
<div class="stat-label">HTML, PDF & Plaintext</div>
<div class="stat-source">Pluggable backend renderers · <a href="/documentation/index.html">Renderer API ↗</a></div>
</div>
</div>

<div class="col-md-6 col-lg-2-4">
<div class="stat-card">
<div class="stat-figure">Dual Apache/MIT</div>
<div class="stat-label">Open Source License</div>
<div class="stat-source">Enterprise friendly · <a href="https://github.com/sebastienrousseau/draftlib.github.io" target="_blank" rel="noopener noreferrer">GitHub Repo ↗</a></div>
</div>
</div>
</div>
</section>

<!-- SECTION 3: CORE CAPABILITIES BENTO GRID -->
<section class="my-5" aria-label="Core Capabilities">
<div class="text-center mb-4">
<h2 class="h3 fw-bold">Built for Mission-Critical Document Pipelines</h2>
<p class="text-muted">Transform unstructured drafting workflows into reproducible, version-controlled software assets.</p>
</div>

<div class="bento-grid">
<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">AST Compiler</div>
<h3 class="bento-title">Streaming Markdown Parser</h3>
<p class="bento-desc">Zero-copy tokenizer that transforms complex Markdown text, tables, and frontmatter metadata into an immutable, type-checked abstract syntax tree.</p>
</div>
<a href="/features/index.html" class="author-link">View AST Compiler Specs →</a>
</div>

<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Schema Validation</div>
<h3 class="bento-title">Deterministic Template Engine</h3>
<p class="bento-desc">Enforce required sections, clause references, signature blocks, and regulatory disclosure tables at compile-time with custom Rust traits.</p>
</div>
<a href="/documentation/index.html" class="author-link">Explore Template Engine →</a>
</div>

<div class="bento-card bento-col-4">
<div>
<div class="bento-tag">Render Backends</div>
<h3 class="bento-title">Multi-Format Exporters</h3>
<p class="bento-desc">Export ASTs directly to semantic HTML5, PDF via headless print drivers, or structured JSON feeds for downstream indexing.</p>
</div>
<a href="/examples/index.html" class="author-link">View Output Examples →</a>
</div>
</div>
</section>

<!-- SECTION 4: TERMINAL QUICKSTART -->
<section class="my-5" aria-label="Developer Quickstart">
<div class="card-surface p-4 p-md-5">
<div class="row align-items-center g-4">
<div class="col-lg-6">
<div class="eyebrow-badge">Developer Quickstart</div>
<h2 class="h3 fw-bold text-headline mb-3">Add Draft Lib to Your Cargo.toml</h2>
<p class="text-muted mb-4">Integrate high-speed document compilation into your Rust microservices and CLI tools with a single dependency.</p>
<div class="d-flex gap-3 flex-wrap">
<a href="/getting-started/index.html" class="btn-primary-quantum">Get Started Guide →</a>
<a href="/documentation/index.html" class="btn-secondary-quantum">API Reference</a>
</div>
</div>
<div class="col-lg-6">
<div class="hero-visual-terminal">
<div class="terminal-header">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — draftlib</span>
</div>
<pre><code><span class="text-muted">// 1. Add dependency</span>
[dependencies]
draftlib = "0.0.1"

<span class="text-muted">// 2. Parse and render document</span>
use draftlib::{Document, HtmlRenderer};

let doc = Document::from_markdown("# Clause 1\nTerms...")?;
let html = HtmlRenderer::new().render(&doc)?;
println!("Compiled in 0.38ms!");</code></pre>
</div>
</div>
</div>
</div>
</section>

<!-- SECTION 5: QUESTIONS? ANSWERS. -->
<section class="my-5" aria-label="Frequently Asked Questions">
<div class="apple-faq-section">
<div class="apple-faq-header">
<h2 class="apple-faq-title">Questions? Answers.</h2>
<button type="button" class="apple-faq-expand-btn" id="faqExpandAllBtn" aria-expanded="false">
<span class="apple-faq-btn-text">Expand all</span>
<svg class="apple-faq-expand-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
</button>
</div>

<div class="apple-faq-list">
<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">How does Draft Lib compare to Pandoc or Pulldown-Cmark?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>While Pulldown-Cmark focuses purely on CommonMark parsing, Draft Lib provides high-level schema validation, legal clause numbering, template variables, cross-reference resolution, and multi-format compilation designed for enterprise documents.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Can Draft Lib be embedded in WebAssembly (WASM)?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>Yes. Draft Lib is built with zero non-standard system dependencies and compiles cleanly to `wasm32-unknown-unknown` for in-browser client-side drafting and validation.</p>
</div>
</details>
</div>
</div>
</section>

<!-- SECTION 6: NEXT STEPS -->
<section class="card-surface p-4 p-md-5 my-5 text-center" aria-label="Conversion Next Steps">
<h2 class="h2 fw-bold text-headline mb-3">Accelerate Your Document Workflows</h2>
<p class="text-muted fs-5 mb-4 max-w-2xl mx-auto">Get started in minutes with the Rust crate or explore comprehensive architectural guides:</p>
<div class="d-flex justify-content-center gap-3 flex-wrap">
<a href="/getting-started/index.html" class="btn-primary-quantum">Get Started (Install) →</a>
<a href="https://github.com/sebastienrousseau/draftlib.github.io" target="_blank" rel="noopener noreferrer" class="btn-secondary-quantum">View on GitHub (Stars & Code) ↗</a>
<a href="/documentation/index.html" class="btn-secondary-quantum">API Reference</a>
</div>
</section>
