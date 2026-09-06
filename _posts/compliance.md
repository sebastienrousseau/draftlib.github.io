---
name: "draft"
short_name: "draft"
title: "Provenance & compliance — draft"
description: "draft ships C2PA content credentials and per-sentence attribution with every article, so AI-assisted work carries machine-readable provenance by default — the direction regulators are moving."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
breadcrumb: true
permalink: "https://draftlib.com/compliance/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Compliance"
headline: "Provenance and compliance"
lead: "Every article draft writes carries machine-readable provenance by default — the direction disclosure rules for AI-assisted content are moving."
---

## What draft gives you

Most tools bolt provenance on afterwards, if at all. draft writes it with every
article, as part of the run that produced the text:

- **A C2PA manifest.** Every article set ships a manifest built on the
  [C2PA](https://c2pa.org) Content Credentials standard — the interoperable,
  cross-industry format for machine-readable content provenance.
- **Per-sentence attribution.** A separate file maps each sentence in the
  article to the claim, and the verbatim source quote, that backs it.
- **A verification command.** `draft --verify <final.md>` recomputes the
  manifest digests and reports whether the article is still exactly what the
  ledger was verified against. Anyone with the files can run it.

Nothing here is a paid add-on or a separate step. It is what a run outputs.

## Why this matters now

The regulatory direction of travel for AI-assisted content is clear and
converging: **disclosure and machine-readable provenance.** The EU AI Act
introduces transparency obligations for AI-generated and AI-manipulated
content, and several US states have passed or proposed AI-disclosure laws. The
common thread across them is that AI involvement should be **detectable and
declared**, and C2PA Content Credentials are the standard the industry has
lined up behind to do exactly that.

A tool that produces AI-assisted text with **no** provenance leaves that entire
burden on you. draft produces it with the provenance layer already attached and
checkable.

## How draft maps to the requirements

| The direction rules are moving | What draft ships |
| --- | --- |
| AI involvement must be disclosed | A C2PA manifest declaring it, per article |
| Provenance should be machine-readable | C2PA Content Credentials, not prose |
| Claims should be traceable to sources | Per-sentence attribution to verbatim quotes |
| Provenance should be verifiable, not asserted | `draft --verify` recomputes and checks the digests |

## Honest scope

draft provides the **provenance layer**: it makes AI-assisted articles carry
checkable, standards-based credentials by default. It does **not**, by itself,
make you compliant with any specific law — compliance depends on your full
publishing workflow, your role, and your jurisdiction, and this page is not
legal advice. Confirm your own obligations. What draft removes is the hardest
part to retrofit: producing the provenance in the first place, bound to the
text, at the moment the text is written.

See [how grounding works](/grounding/) for the verification gate, and
[security](/security/) for the local-first, keyless posture.
