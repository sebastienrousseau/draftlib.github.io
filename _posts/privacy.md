---
name: "draft"
short_name: "draft"
title: "Privacy — draft"
description: "The draft website uses no tracking cookies and no analytics. The CLI runs on your machine."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "privacy"
breadcrumb: true
permalink: "https://draftlib.com/privacy/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Privacy"
headline: "Privacy"
lead: "No tracking on this site. draft runs locally; what it sends depends on the engine you choose."
---

## This website

This site sets no tracking cookies and runs no analytics. It is a static build
served as plain HTML and CSS.

## The draft CLI

draft runs on your machine and sends no telemetry. What leaves your machine
depends only on the engine you choose:

| Mode | What leaves your machine | Who sees your source text |
| --- | --- | --- |
| **Local model** (`--engine ollama`) | Nothing. Reading, the claim gate, style checks and provenance are all local. | No one. |
| **Cloud agent CLI** (default `auto`) | The source excerpts draft needs to extract claims and write the article, sent through that CLI's own session. | Whichever provider your logged-in CLI uses, under that CLI's account terms and retention. |
| **Mixed** (`--extract-engine` ≠ `--write-engine`) | Excerpts go to each stage's engine separately, so you can extract locally and write in the cloud, or the reverse. | Only the provider(s) for the cloud stage(s) you chose. |

The PDF is always read locally; only the text a cloud stage needs is sent, and
only to the CLI you are already logged into. draft stores no credentials, runs
no servers, and adds no network calls of its own — a cloud stage is exactly the
request you would make by using that CLI directly.
