---
name: "draft"
short_name: "draft"
title: "Documentation — draft"
description: "Install draft, run your first paper-to-post in a minute, understand the four-phase run, and read the full command-line reference — with real terminal output at every step."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
toc: true
og_card: "documentation"
breadcrumb: true
permalink: "https://draftlib.com/documentation/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Docs"
headline: "Documentation"
lead: "Install draft, run your first paper in a minute, and read the full command-line reference — with real terminal output at every step."
---

draft is a command-line tool that turns a research PDF into a publication-ready
Markdown article where every sentence is grounded in a quote-verified claim from
the source. This page takes you from a clean machine to a checked, published
article, then documents every flag, output and failure mode.

New to the idea? Read [how grounding works](/grounding/) first — it explains the
gate that makes the output trustworthy. Ready to run it? Start below.

## Overview

A run moves a paper through four phases. Only two of them call a model; the rest
are deterministic Go.

1. **Read and section.** The PDF is read to text and split into sections.
2. **Extract and verify.** Each section is mined for claims, and a claim
   survives only if its quote appears verbatim in the source and every number
   in it appears in that quote.
3. **Write.** The verified ledger — and nothing else — is arranged into an
   article in your house style.
4. **Attribute and sign.** Every sentence is mapped back to the claim behind it,
   and a C2PA manifest is written beside the article.

<div class="callout callout-note">
<span class="callout-label">Before you start</span>
draft never asks for an API key. Online, it drives an AI coding-agent CLI you
are already logged into; offline, it uses a local model. Your PDF is read on
your machine. See <a href="/compliance/">provenance &amp; compliance</a> for
exactly what leaves it.
</div>

## Install

Pick one. Homebrew is the shortest path on macOS; `go install` works anywhere
with a Go toolchain.

**Homebrew (macOS)**

```sh
brew install --cask sebastienrousseau/tap/draft
```

**Go toolchain (any platform)**

```sh
go install github.com/sebastienrousseau/draft/cmd/draft@latest
```

**From source**

```sh
git clone https://github.com/sebastienrousseau/draft
cd draft && make build
```

### Dependencies by platform

draft reads PDFs with `pdftotext` (Poppler) and, offline, writes with a local
[Ollama](https://ollama.com) model. `.docx` is read by `textutil` on macOS
(built in) or by `--reader docling` anywhere.

| Platform | Poppler (`pdftotext`) | Ollama (offline writing) |
| --- | --- | --- |
| **macOS** | `brew install poppler` | `brew install ollama` |
| **Debian / Ubuntu** | `sudo apt-get install poppler-utils` | `curl -fsSL https://ollama.com/install.sh \| sh` |
| **Fedora** | `sudo dnf install poppler-utils` | `curl -fsSL https://ollama.com/install.sh \| sh` |
| **Windows** | `scoop install poppler` (or `choco install poppler`) | download from [ollama.com/download](https://ollama.com/download) |

You need Poppler only for PDF input, and Ollama only for offline runs.

## Quickstart

From a clean machine to a checked article in four steps.

### 1. Check the machine

`draft --doctor` reports what draft can find: readers, backends, and the paths
it will read from and write to. You need one online backend **or** a running
Ollama server.

<div class="figure">
<div class="terminal">
  <div class="terminal-bar" aria-hidden="true"><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-title">draft --doctor</span></div>
  <div class="terminal-screen" tabindex="0" role="group" aria-label="draft --doctor output">
<p class="tui-head">SOURCE TOOLING</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>pdftotext            /opt/homebrew/bin/pdftotext</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>docling              --reader docling: tables and structure, slower</p>
<p class="tui-head">BACKENDS</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>claude               session provider</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>copilot              session provider</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>ollama               responding at http://127.0.0.1:11434</p>
<p class="tui-head">PATHS</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>drafts (--out)       ~/Drop/Drafts</p>
<p class="tui-out">Ready. Run draft --dry-run &lt;source&gt; to check a specific paper.</p>
  </div>
</div>
<p class="term-caption">Real <code>draft --doctor</code> output. A green tick is a backend draft can use; run <code>--dry-run</code> to check one specific paper without calling a model.</p>
</div>

### 2. Run a paper

Point draft at a PDF. In `auto` mode it picks the first backend you are logged
into and shows a live view of the four phases as they run.

```sh
draft "2603.23420.pdf"
```

<div class="figure">
<div class="terminal">
  <div class="terminal-bar" aria-hidden="true"><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-title">draft — live run</span></div>
  <div class="terminal-screen" tabindex="0" role="group" aria-label="the draft terminal UI during a run">
<p class="tui-headline"><span class="tui-wordmark">draft</span>  ⧇ Drafting Grounded Articles — claude · sonnet · 900–1200 words</p>
<hr class="tui-rule">
<div class="tui-cols">
<div class="tui-col">
<p class="tui-section">Queue</p>
<p class="tui-phase tui-run"><span class="tui-count">[1/1]</span> <span class="tui-marker">⠙</span>2603.23420.pdf</p>
<p class="tui-section">Pipeline</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Resolve source</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Read and section</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Extract claims</p>
<p class="tui-phase tui-run"><span class="tui-marker">⠙</span>Write article</p>
<p class="tui-phase tui-pending"><span class="tui-marker">·</span>Validate and save</p>
<p class="tui-section">Log</p>
<p class="tui-log">· read 5 section(s)</p>
<p class="tui-log">· 6 claim(s) verified, 9 dropped</p>
<p class="tui-log">· writing…</p>
</div>
<div class="tui-col">
<p class="tui-section">Live Draft</p>
<p class="tui-status"><span class="tui-marker tui-spin">⠙</span> writing, 342 words visible</p>
<p><span aria-hidden="true"><span class="tui-progressbar">████████████████</span><span class="tui-progressempty">░░░░░░░░░░░░</span></span> <span class="tui-pct">57%</span></p>
<p class="tui-preview">## Router-S: conditional compute at a fixed budget<br><br>Router-S reaches a validation loss of 3.41 against a dense baseline on an identical token budget — but the same evaluation reports that seed variance exceeds the gap being measured, which is the more important number to sit with.<br><br>Sparse routing is designed to cut the compute spent on tokens that are trivially predictable<span class="tui-pcursor">▋</span></p>
</div>
</div>
<p class="tui-shortcuts">[q] quit · [j/k] up/down · [pgup/pgdn] page</p>
  </div>
</div>
<p class="term-caption">The draft terminal UI mid-run. On the left, the queue and the five-phase pipeline with a live log; on the right, the <strong>Live Draft</strong> panel — a status line, a progress bar, and the grounded article previewing as it is written, sentence by sentence. Prefer no UI? Add <code>--print</code> (paths to stdout) or <code>--json</code> (one JSON object per job).</p>
</div>

When it finishes, the summary line reports the result:

<div class="figure">
<div class="terminal">
  <div class="terminal-bar" aria-hidden="true"><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-title">draft — complete</span></div>
  <div class="terminal-screen" tabindex="0" role="group" aria-label="a completed run">
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Resolve source</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Read and section</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Extract claims <span class="tui-note">· 6 verified, 9 dropped</span></p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Write article</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>Validate and save</p>
<p class="tui-out">✓ 1,066 words via claude in 3m 54s · 16,230 tokens · $0.52</p>
  </div>
</div>
<p class="term-caption">A finished run. Nine of fifteen candidate claims were dropped by the gate — that is grounded-by-construction working, not a bug. A thin source yields a short draft rather than a padded one.</p>
</div>

### 3. Inspect the article set

Each run writes one article as a dated set: three files that stay in sync, plus
two a reader can check.

```text
~/Drop/Drafts/2026-07-29/
├── source/2026-07-29-<slug>-body.md          # the article — edit this
├── yaml/2026-07-29-<slug>-frontmatter.yaml   # adjacent frontmatter
├── final/2026-07-29-<slug>-final.md          # combined, ready to publish
└── provenance/
    ├── 2026-07-29-<slug>-attribution.json    # which claim backs each sentence
    └── 2026-07-29-<slug>-c2pa.json           # C2PA manifest
```

Edit the body, then regenerate the other two in place with
`draft --frontmatter <body.md>`. Your curated fields are preserved; only missing
ones are rebuilt. See [the article set](#the-article-set) for the rules.

### 4. Verify it

`draft --verify` recomputes the digests and confirms the article still matches
the ledger it was written from.

<div class="figure">
<div class="terminal">
  <div class="terminal-bar" aria-hidden="true"><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-dot"></span><span class="terminal-title">draft --verify …-final.md</span></div>
  <div class="terminal-screen" tabindex="0" role="group" aria-label="draft --verify output">
<p class="tui-head">PROVENANCE</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>made by            draft 0.0.35</p>
<p class="tui-phase tui-pending"><span class="tui-marker">·</span>written with       claude sonnet</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>article            unchanged since it was written (64261b97…)</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>claim ledger       matches the verified claims</p>
<p class="tui-head">GROUNDING</p>
<p class="tui-phase tui-pending"><span class="tui-marker">·</span>claims             6 verified</p>
<p class="tui-phase tui-pending"><span class="tui-marker">·</span>attribution        13 of 36 sentences rest on a claim</p>
<p class="tui-head">SOURCES</p>
<p class="tui-phase tui-done"><span class="tui-marker">✓</span>two-column.pdf     unchanged since it was read</p>
<p class="tui-out">Verified. The article matches the provenance written beside it.</p>
  </div>
</div>
<p class="term-caption">Edit a sentence the ledger did not support and re-run this: verification fails. Download a real, verifiable set on the <a href="/compliance/">provenance &amp; compliance</a> page and run <code>--verify</code> on it yourself.</p>
</div>

## The run, phase by phase

The live view above maps one-to-one onto the pipeline. Each phase reports as it
completes:

| Phase | What happens | Model call? |
| --- | --- | --- |
| **Resolve source** | Locate the file; bare names resolve against `~/Drop/Drafts/Sources`. | No |
| **Read and section** | `pdftotext` (or `--reader docling`) extracts text; it is split into sections. | No |
| **Extract claims** | One call per section mines claims; each is checked against the source and dropped unless its quote is verbatim. | Yes |
| **Write article** | One call arranges the verified ledger into an article in your house style. | Yes |
| **Validate and save** | House-style checks run; the set is written with attribution and a C2PA manifest. | No |

<div class="callout callout-tip">
<span class="callout-label">Tip</span>
The deterministic path — read, section, gate, validate — runs in about a tenth
of a second on a 62-page paper. Everything else is model latency, which depends
on your engine, not on draft. See the <a href="/benchmarks/">benchmarks</a>.
</div>

## Choosing an engine

In `auto` mode draft walks a preference list and uses the first backend you are
logged into. Force one with `--engine <name>`, or split the two model phases
with `--extract-engine` and `--write-engine`.

**Verified, used by auto mode:** `claude`, `copilot`, `codex`, `grok`, `agy`,
`cursor-agent`.

**Experimental** (invocation correct, output unverified; auto uses them only
with `--experimental`): `amp`, `crush`, `goose`, `qwen`, `gemini-acp`,
`codex-acp`.

**Offline:** `--engine ollama` runs the whole pipeline against a local model. If
an online call fails because you are offline, draft fails over to Ollama and
stays there for the rest of the run.

<div class="callout callout-note">
<span class="callout-label">No API key</span>
A session backend uses that tool's own logged-in session — the same credentials
you already use with the CLI directly. draft stores no keys and adds no network
calls of its own.
</div>

**Escape hatch (opt-in):** on a machine with no agent CLI, `--engine
api:anthropic` or `--engine api:openai` calls a hosted API directly, reading
your own key from `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`. It is never chosen by
`auto` mode — the keyless agent-session path stays the default — and it fails
over to Ollama like any other backend.

## Readers

| Reader | Use it for | Speed |
| --- | --- | --- |
| `pdftotext` (default) | Most PDFs. A 62-page paper in about 110&nbsp;ms. | Fast |
| `--reader docling` | Papers where tables and structure matter; reads PDF and DOCX on every platform. Mines table cells into claims. | Slower |

PDF, Markdown, plain text and DOCX are all accepted, and so is **LaTeX
(`.tex`)** — read directly with no external tool, keeping a formula as exact
text where `pdftotext` would scramble it.

## Command reference

```text
draft [flags] <source> [more-sources...]
```

Bare filenames resolve against `~/Drop/Drafts/Sources`. Each source becomes its
own draft, processed as a queue.

### Engine and model

| Flag | Description |
| --- | --- |
| `--engine <mode>` | `auto` (default), `ollama`, a provider name, or `api:<provider>` |
| `--extract-engine <m>` | Backend for claim extraction (default: `--engine`) |
| `--write-engine <m>` | Backend for writing (default: `--engine`) |
| `--model <name>` | Session-provider model override (e.g. `opus`) |
| `--experimental` | Let auto mode use experimental providers |
| `--num-ctx <n>` | Ollama context window (default `8192`) |
| `--num-predict <n>` | Ollama max output tokens (default `6000`) |

### Reading and grounding

| Flag | Description |
| --- | --- |
| `--reader <name>` | `pdftotext` (default) or `docling` |
| `--style <file>` | JSON house-style file: word band, banned vocabulary, language variant |
| `--strict-numbers` | Fail on a number found in no verified claim |
| `--second-gate` | Opt-in semantic pass: drop verified claims a local model finds unsupported by their quote |
| `--no-cache` | Re-extract instead of reusing cached claims |
| `--clear-cache` | Delete every cached claim extraction and exit |

### Output and workflow

| Flag | Description |
| --- | --- |
| `--out <dir>` | Directory to write drafts into (default `~/Drop/Drafts`) |
| `--sources-dir <dir>` | Directory bare filenames resolve against |
| `--merge` | Combine all sources into one draft |
| `--force-new` | Draft even if today's folder already has one |
| `--resume` | Reuse a verified claim ledger from an earlier attempt |
| `--review <draft.md>` | Enhance an existing draft with surgical edits |
| `--frontmatter <file>` | Regenerate frontmatter and the final article |
| `--verify <file>` | Check an article against its provenance, and exit |
| `--keep-artifacts` | Keep prompt/ledger files beside a successful draft |

### Modes and info

| Flag | Description |
| --- | --- |
| `--print` | Run without the UI; print draft paths to stdout |
| `--json` | Machine-readable output: one JSON object per job, or a verification record with `--verify` |
| `--dry-run` | Report what a run would do, without calling a model |
| `--doctor` | Check that this machine can run draft, and exit |
| `--completion <sh>` | Print a completion script: `bash`, `zsh`, or `fish` |
| `--version` | Print version and exit |
| `-h, --help` | Show help |

### Examples

```sh
draft "2603.23420.pdf"                  # one paper
draft a.pdf b.pdf c.pdf                 # three drafts, queued
draft --merge notes.md paper.pdf        # combine into a single draft
draft --engine ollama paper.pdf         # force the local model
draft --review draft.md paper.pdf       # enhance an existing draft
draft --frontmatter source/x-body.md    # regenerate the yaml + final set
```

## The article set

**One article. Three files. Always in sync.** Plus two a reader can check. Edit
the body, then run `draft --frontmatter <body.md>` to regenerate the frontmatter
and combined document. Three rules make that safe to run at any time:

1. **The filename is the article's identity.** Its date and slug drive every URL
   in the frontmatter. Retitle the article and the permalink holds.
2. **Your edits always win.** Curated fields are preserved verbatim; only missing
   ones are generated. Delete a field to have it rebuilt.
3. **Unchanged input is a no-op.** Reprocessing a set that has not changed
   rewrites every file byte for byte identically.

The provenance pair is written once, by the run that produced the article, and
is not regenerated — it describes the article the ledger was verified against.

## Provenance and verification

Every set ships a per-sentence attribution file and a C2PA manifest.
`draft --verify <final.md>` recomputes the digests and reports whether the
article, the ledger and the sources are all unchanged. It is the reader's check,
not just yours — anyone with the files can run it.

**Signed credentials (opt-in).** Configure a signing certificate chain and key
(`DRAFT_C2PA_CERT` / `DRAFT_C2PA_KEY`, with `c2patool` installed) and draft also
writes a signed, detached `.c2pa` credential bound to the article; `draft
--verify` then validates its signature and trust chain as well as the digests.
Without a certificate the manifest stays an unsigned definition, exactly as
before.

**A portable record.** `draft --verify --json` prints a self-contained
`draft.verification-record/v1` — the article digest and whether it matches, the
grounding summary, the signature state, and the overall verdict — that a script
or another tool can consume and re-check without the CLI.

See [provenance &amp; compliance](/compliance/) for what the manifest contains,
how it maps to AI-disclosure rules, and a real set you can download and verify.

## House style

`--style <file>` points draft at a JSON house-style file: a word band, a banned
vocabulary, and a language variant. Style is **enforced** on the finished draft,
not merely requested — a draft that breaks a rule is corrected, not shipped.

## Configuration and environment

Most flags have an environment-variable equivalent, useful for CI or a shared
default:

```text
DRAFT_ENGINE, DRAFT_EXTRACT_ENGINE, DRAFT_WRITE_ENGINE, DRAFT_EDIT_ENGINE,
DRAFT_MODEL_SESSION, DRAFT_MODEL, DRAFT_WRITE_MODEL, DRAFT_EXTRACT_MODEL,
DRAFT_EDIT_MODEL, DRAFT_NUM_CTX, DRAFT_NUM_PREDICT, DRAFT_STRICT_NUMBERS,
DRAFT_SECOND_GATE, DRAFT_READER, DRAFT_DRAFTS_DIR, DRAFT_SOURCES_DIR,
DRAFT_CACHE_DIR, DRAFT_NO_CACHE, DRAFT_C2PA_CERT, DRAFT_C2PA_KEY,
DRAFT_C2PA_ALG, OLLAMA_HOST
```

Set `DRAFT_SHOW_LOGO=0` to suppress the nib mark in `--help`. Publisher identity
for the C2PA manifest is configured with the `DRAFT_SITE_*` variables.

### Config files

For defaults you would otherwise repeat, draft reads a project `draft.toml` in
the working directory and a user `~/.config/draft/config.toml` (honouring
`XDG_CONFIG_HOME`). They set the same settings as the flags — `engine`,
`extract-engine`, `write-engine`, `edit-engine`, `reader`, `model`, the Ollama
models, `out`, `sources-dir`, `style`, and the `c2pa-cert` / `c2pa-key` /
`c2pa-alg` signing keys.

Precedence is **flags &gt; environment &gt; project file &gt; user file &gt;
built-in default**, so adding a config file never changes what an existing
command already does. `DRAFT_CONFIG` names an explicit file; `DRAFT_NO_CONFIG`
disables the layer. The parser is a dependency-free flat `key = value` reader —
no new module.

```toml
# draft.toml
engine = "claude"
reader = "docling"
out    = "~/Drafts"
```

## Troubleshooting

<div class="callout callout-warning">
<span class="callout-label">No text in the PDF</span>
A scanned PDF has no text layer, so extraction returns nothing and the run
fails. Use a source with selectable text, or convert it with OCR first. Native
OCR is on the <a href="/roadmap/">roadmap</a>.
</div>

**No backend found.** Run `draft --doctor`. Log into one supported agent CLI, or
install Ollama and start it for offline runs. You need exactly one.

**A thin ledger.** A source with few checkable claims yields a short draft by
design. draft never pads; a short draft means the paper offered little the gate
could verify.

**Offline model not pulled.** `--engine ollama` needs the model downloaded
beforehand and the Ollama server running. `draft --doctor` reports whether it is
reachable.

**A run failed partway.** The verified ledger is left on disk. Re-run with
`--resume` to skip straight to writing rather than re-paying for extraction.

## Next steps

- [How grounding works](/grounding/) — the nine-check gate, in detail.
- [Examples](/examples/) — a sentence, its source span, and the attribution that binds them.
- [Provenance &amp; compliance](/compliance/) — a real set you can download and verify.
- [Go packages](/library/) — every capability as an importable Go package.
- [Roadmap](/roadmap/) — what draft does not yet do.
