---
name: "draft"
short_name: "draft"
title: "Examples — draft"
description: "End-to-end examples: a research paper in, a grounded article out, with attribution and a C2PA manifest you can verify."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "examples"
breadcrumb: true
permalink: "https://draftlib.com/examples/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Examples"
headline: "Examples"
lead: "See a paper become a grounded article — command, output, and the provenance you can check."
---

## See the gate work

Grounding is easier to trust when you can see it. Here is one sentence draft
wrote, the verbatim source span that let it survive the gate, and the
attribution entry that binds them.

**The source said** (verbatim, from the paper):

> Rendering-tolerant matching and source-based quote repair cut the
> verification drop rate from 29.6% to 8.5% across 3,217 extraction blocks.

**draft wrote:**

> Rendering-tolerant matching and source-based quote repair together lowered
> the drop rate from 29.6% to 8.5% across 3,217 extraction blocks.

**The attribution file records the link** (`…-attribution.json`):

```json
{
  "sentence": "Rendering-tolerant matching and source-based quote repair together lowered the drop rate from 29.6% to 8.5% across 3,217 extraction blocks.",
  "claim_id": "c-0417",
  "quote": "Rendering-tolerant matching and source-based quote repair cut the verification drop rate from 29.6% to 8.5% across 3,217 extraction blocks",
  "strength": "quantitative"
}
```

Every number in the sentence (`29.6`, `8.5`, `3,217`) appears in the quote, and
the quote appears verbatim in the source — the two checks that let this claim
through. Note the sentence keeps the source's *joint* attribution to both
changes: the gate checks quotes and numbers, so faithful wording is on the
writer, and this is what faithful wording looks like. A sentence without an
attribution entry cannot exist in the article, and `draft --verify` recomputes
the manifest digests against exactly this.

## One paper, start to finish

```sh
draft "2603.23420.pdf"
```

draft reads the paper, builds a verified claim ledger, writes the article from
it, and saves a dated set:

```text
2026-07-29/
├── source/2026-07-29-attention-routing-body.md
├── yaml/2026-07-29-attention-routing-frontmatter.yaml
├── final/2026-07-29-attention-routing-final.md
└── provenance/
    ├── 2026-07-29-attention-routing-attribution.json
    └── 2026-07-29-attention-routing-c2pa.json
```

The attribution file maps each sentence in the article to the claim, and the
verbatim source quote, that backs it. Nothing in the body exists without a line
in that file.

## Verify it

`draft --verify` recomputes the digests written beside the article and checks
them. Point it at any file of the set. When a signed `.c2pa` credential is
present and `c2patool` is installed, it validates the signature and trust chain
too.

```sh
draft --verify 2026-07-29/final/2026-07-29-attention-routing-final.md
```

<div class="terminal">
  <div class="terminal-bar" aria-hidden="true"><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-title">draft --verify</span></div>
  <div class="terminal-screen" tabindex="0" role="group" aria-label="draft --verify output for a signed article set">
<p class="tui-head">PROVENANCE</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>made by              draft 0.0.36</p>
<p class="tui-phase"><span class="tui-marker">·</span>written with         claude sonnet</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>article              unchanged since it was written (7254c2c8d463)</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>claim ledger         matches the verified claims</p>
<p class="tui-head">GROUNDING</p>
<p class="tui-phase"><span class="tui-marker">·</span>claims               6 verified</p>
<p class="tui-phase"><span class="tui-marker">·</span>attribution          22 of 24 sentences rest on a claim</p>
<p class="tui-head">SOURCES</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>2603.23420.pdf       unchanged since it was read</p>
<p class="tui-head">SIGNATURE</p>
<p class="tui-phase"><span class="tui-marker">·</span>signature            valid; signing certificate not in a known trust list (e.g. a development certificate)</p>
<p class="tui-out">Verified. The article matches the provenance written beside it.</p>
  </div>
</div>

Edit a sentence the ledger did not support and verification fails — that is the
guarantee. It exits non-zero when the article, the ledger, a source, or the
signature no longer matches.

### A receipt a machine can check

Add `--json` and `--verify` emits a portable `draft.verification-record/v1`
instead of the human report — the digest and whether it matches, the grounding
summary, the source and signature state, and the verdict. The schema lives in
the importable `provenance` package, so a CI gate or an independent verifier
can consume it without the CLI. *Bring your own artifact, verify anywhere.*

```json
{
  "kind": "draft.verification-record/v1",
  "verified": true,
  "generator": { "name": "draft", "version": "0.0.36" },
  "article": { "sha256": "7254c2c8d463106f…071254b6", "matches": true },
  "grounding": { "claims": 6, "sentences": 24, "attributed": 22, "ungrounded_number_sentences": 0 },
  "sources": [ { "path": "2603.23420.pdf", "found": true, "matches": true } ],
  "signature": { "present": true, "checked": true, "valid": true, "trusted": true, "state": "Valid" }
}
```

Signing is opt-in: set `DRAFT_C2PA_CERT` and `DRAFT_C2PA_KEY` to a certificate
chain and key. With no certificate, the manifest stays an unsigned definition,
and the record simply omits the signature — everything else still verifies.

## Tighten it further: the semantic second gate

The verbatim gate proves a claim's quote is in the source. It does not judge
whether the quote *supports* the claim — a different subject, or a hedge stated
as settled. `--second-gate` adds that pass on request: a local model checks each
verified claim, and unsupported ones are dropped before writing.

```sh
draft --second-gate "my-paper.pdf"
```

<div class="terminal">
  <div class="terminal-bar" aria-hidden="true"><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-title">draft --second-gate</span></div>
  <div class="terminal-screen" tabindex="0" role="group" aria-label="draft log showing the second gate dropping a claim">
<p class="tui-log">· read 5 section(s)</p>
<p class="tui-log">· 8 claim(s) verified, 5 dropped</p>
<p class="tui-log">· second gate dropped 1 claim(s) a model found unsupported by their quote</p>
<p class="tui-log">· writing…</p>
  </div>
</div>

It is strictly additive and off by default: the verbatim gate stays the primary
check, and a model error keeps the claim rather than dropping it — the pass can
only ever tighten the ledger.

## A batch, merged into one draft

```sh
draft --merge a.pdf b.pdf c.pdf
```

## Offline, on a plane

```sh
draft --engine ollama "my-paper.pdf"
```

No network, no API key. The same gate runs; only the writer changes.

A complete, verifiable set from a real run — article, attribution, C2PA
manifest and source — is on the [provenance & compliance](/compliance/)
page. More runnable examples live in the
[repository](https://github.com/sebastienrousseau/draft/tree/main/examples).
