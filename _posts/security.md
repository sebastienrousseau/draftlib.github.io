---
name: "draft"
short_name: "draft"
title: "Security — draft"
description: "draft's security posture: local-first, no API keys, signed releases and provenance you can verify."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "security"
breadcrumb: true
permalink: "https://draftlib.com/security/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Security"
headline: "Security"
lead: "Local-first by default, keyless, with releases and provenance you can check."
---

## Posture

- **Local-first.** The reader, claim gate, house-style checks and provenance
  are deterministic Go and never touch the network. Run fully offline with
  `--engine ollama`.
- **No API keys.** draft drives agent CLIs through their own logged-in
  sessions. It stores no credentials and asks for none.
- **No telemetry.** draft has no servers and phones nothing home.
- **Provenance you can verify.** Every article ships a C2PA manifest and a
  per-sentence attribution file; `draft --verify` recomputes the digests.

## Data flow

With a local model, nothing leaves your machine. With a cloud agent CLI, the
source excerpts draft needs to extract and write pass through that tool under
your own session — the same data you would send by using that CLI directly.

For how draft's provenance maps to AI-disclosure rules, see [provenance & compliance](/compliance/).

## Reporting a vulnerability

Please report security issues privately through the
[GitHub security advisories](https://github.com/sebastienrousseau/draft/security/advisories)
page rather than a public issue.
