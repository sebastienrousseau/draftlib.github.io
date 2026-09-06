---
name: "draft"
short_name: "draft"
title: "Privacy — draft"
description: "The draft website uses no tracking cookies and no analytics. The CLI runs on your machine."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
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
depends on the engine you choose:

- **Offline (`--engine ollama`):** nothing leaves your machine.
- **A cloud agent CLI:** the source excerpts draft needs to extract and write
  pass through that tool under your own session, the same as using it directly.

draft stores no credentials and has no servers.
