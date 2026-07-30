---
author: "contact@draftlib.com (Sebastien Rousseau)"
banner_alt: "draft — grounded article drafting from research papers."
banner_height: 500
banner_width: 1200
banner: "https://draftlib.com/img/draft.svg"
cdn: "https://draftlib.com"
changefreq: weekly
charset: utf-8
cname: draftlib.com
copyright: "© 2026 Sebastien Rousseau. Dual Apache-2.0 / MIT."
date: "2026-07-30T08:00:00+00:00"
description: "No tokens on disk, prompt-injection awareness, bounded external calls, and verifiable releases."
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/security/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "security, supply chain, sigstore, sbom, prompt injection, openssf scorecard"
language: en-GB
layout: page
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/security/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "No tokens on disk, prompt-injection awareness, bounded external calls, and verifiable releases."
tags: "draft, grounded generation, research, markdown, go"
theme_color: "#0b0e14"
title: "Security — draft"
url: "https://draftlib.com/security/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
---

# Security

## No tokens on disk

Session backends shell out to an already authenticated CLI. `draft` never
reads, stores or logs an API key.

## Prompts and process listings

A prompt passed as a command-line argument is visible in a process listing for
the duration of the call, along with the source excerpts it quotes. `claude`,
`codex` and `cursor-agent` are driven over stdin and are not affected; the
others were confirmed not to read stdin — their prompt flags require a value —
so they still use an argument. On a shared host, prefer one of those three, or
Ollama.

## Know your agent's trust surface

Session providers run in non-interactive modes, some of which auto-approve tool
use. `draft` asks only for text, but you are still handing a PDF to an agent
that *can* act. Treat sources as untrusted input, and prefer Ollama for
material you do not trust.

Template and source text are quoted as untrusted evidence, and the writing
prompt tells the model to ignore any instructions found inside them. Treat that
as defence in depth rather than a guarantee.

## Bounded external calls

Extraction shells out only to `pdftotext` and `textutil`, with context
timeouts, absolute paths — so a file named `-x.pdf` cannot be read as a flag —
capped output, and no shell interpolation. Every generation call is bounded by
`DRAFT_CALL_TIMEOUT`.

`OLLAMA_HOST` is validated: a value that is not a valid `http`/`https` URL is
refused rather than concatenated into a request URL, and a host that is not
loopback is reported, because a remote Ollama means your source text leaves the
machine.

## Cancellation means cancellation

Quitting the dashboard, or Ctrl+C in headless mode, cancels the run's context
and terminates any in-flight subprocess or Ollama request. A cancelled run
stops there rather than failing over to the next backend.

## Verifiable releases

Signed with keyless Sigstore cosign, published with a CycloneDX SBOM per
archive and GitHub build provenance:

```sh
cosign verify-blob --bundle checksums.txt.sigstore.json \
  --certificate-identity-regexp 'https://github.com/sebastienrousseau/draft/.*' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  checksums.txt
```

Every pull request runs build, three-OS tests, lint, an MSRV check,
`govulncheck`, CodeQL and REUSE compliance, with statement coverage gated at
95% and fuzzers on every parser that reads untrusted input.

## Reporting a vulnerability

See the [disclosure policy](https://github.com/sebastienrousseau/draft/blob/main/SECURITY.md).
