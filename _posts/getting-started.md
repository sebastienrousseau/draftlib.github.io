---
name: "Draft Lib"
short_name: "draftlib"
title: "Getting Started with Draft Lib: Installation & Quickstart"
description: "How to install Draft Lib via Cargo and begin compiling structured documents."
keywords: "install draftlib, cargo draftlib, rust document quickstart"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://draftlib.com/getting-started/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Draft Lib — Fast Document Processing & Drafting Engine in Rust"
---

# Getting Started with Draft Lib

## 1. Installation

Add `draftlib` to your `Cargo.toml`:

```toml
[dependencies]
draftlib = "0.0.1"
```

---

## 2. Basic Example

```rust
use draftlib::{Document, Result};

fn main() -> Result<()> {
    let markdown_input = r#"
---
title: "Master Services Agreement"
version: "1.0.0"
---

# 1. Scope of Services
The service provider agrees to perform the services detailed in Schedule A.
    "#;

    let doc = Document::from_markdown(markdown_input)?;
    println!("Parsed Title: {}", doc.metadata.get("title").unwrap());
    Ok(())
}
```
