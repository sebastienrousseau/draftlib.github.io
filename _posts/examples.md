---
name: "Draft Lib"
short_name: "draftlib"
title: "Document Templates & Implementation Examples"
description: "Real-world code examples using Draft Lib for contractual and technical drafting."
keywords: "draftlib examples, rust document templates"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://draftlib.com/examples/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Draft Lib — Fast Document Processing & Drafting Engine in Rust"
eyebrow: "draft"
headline: "Document Templates & Implementation Examples"
lead: "Real-world code examples using Draft Lib for contractual and technical drafting."
---

## Document Examples & Use Cases

### 1. Automated Clause Numbering & Validation

```rust
use draftlib::{Document, ClauseValidator};

let doc = Document::from_file("contracts/nda.md")?;
let validator = ClauseValidator::standard_commercial();

match validator.validate(&doc) {
    Ok(_) => println!("Contract satisfies all compliance rules!"),
    Err(e) => eprintln!("Validation failed: {}", e),
}
```
