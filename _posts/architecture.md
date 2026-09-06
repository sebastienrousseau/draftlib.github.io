---
name: "Draft Lib"
short_name: "draftlib"
title: "Internal Architecture: Lexer, AST Pipeline & Exporters"
description: "Architectural overview of Draft Lib's token streaming, AST reconciliation, and memory model."
keywords: "draftlib architecture, rust AST parser design"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://draftlib.com/architecture/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Draft Lib — Fast Document Processing & Drafting Engine in Rust"
eyebrow: "draft"
headline: "Internal Architecture: Lexer, AST Pipeline & Exporters"
lead: "Architectural overview of Draft Lib's token streaming, AST reconciliation, and memory model."
---

## Internal Architecture & Design

```
+--------------------+     +---------------------+     +--------------------+
| Markdown Stream    | --> | AST Synthesizer     | --> | Target Renderer    |
| (Zero-Copy Lexer)  |     | (Schema Validation) |     | (HTML / PDF / JSON)|
+--------------------+     +---------------------+     +--------------------+
```

1. **Zero-Copy Lexer:** Scans bytes linearly using string slicing without heap allocation.
2. **Schema Validator:** Inspects AST tree structure against declarative contract schemas.
3. **Target Exporter:** Emits formatted artifacts directly into buffered writers.
