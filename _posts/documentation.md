---
name: "Draft Lib"
short_name: "draftlib"
title: "API Reference & Trait Specifications"
description: "Comprehensive Rust API documentation for Document, AstNode, Renderer, and SchemaValidator."
keywords: "draftlib API, rust crate documentation"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://draftlib.com/documentation/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Draft Lib — Fast Document Processing & Drafting Engine in Rust"
---

# API Reference & Trait Specifications

## Core Types

### `struct Document`
Represents a parsed document containing frontmatter metadata and a hierarchy of AST nodes.

### `enum AstNode`
```rust
pub enum AstNode {
    Heading { level: u8, text: String },
    Paragraph(String),
    Clause { number: String, heading: String, body: Box<AstNode> },
    Table(TableNode),
    CodeBlock { language: String, content: String },
}
```

### `trait Renderer`
```rust
pub trait Renderer {
    fn render(&self, doc: &Document) -> Result<String>;
}
```
