# draftlib.com

The website for [`draft`](https://github.com/sebastienrousseau/draft) — a
command-line tool that turns research papers into publication-ready Markdown,
with every claim verified verbatim against its source.

Built with [Shokunin SSG](https://shokunin.one). GitHub Pages serves the
`docs/` directory on the default branch.

## Build

```sh
./build.sh          # build and publish to docs/
./build.sh --audit  # build, publish, then run the ssg audit gates
```

Requires `ssg` on `PATH` (`cargo install ssg`) and Python 3 for the postbuild
repair pass.

## Layout

```text
_posts/      page content (Markdown + frontmatter), one file per URL
_layouts/    index.html (home, with hero) and page.html (everything else)
static/      assets mirrored to the site root: fonts, brand mark, CSS
scripts/     postbuild_fix.py — repairs ssg output (see its docstring)
docs/        the built site; GitHub Pages serves this. Do not edit by hand.
```

## Two things worth knowing before editing

**Fenced code blocks belong on `page`-layout pages.** ssg whitespace-collapses
the `{{content}}` blob on index pages, so a multi-line fenced block written in
`_posts/index.md` loses its newlines and renders as one long line. Home-page
code samples are therefore hard-coded in `_layouts/index.html`, inside an
`<article class="content-body">` so they pick up the same prose styling.

**`docs/` is generated.** Every edit goes in `_posts/`, `_layouts/` or
`static/`, then `./build.sh`.

## Licence

Dual-licensed Apache-2.0 or MIT, matching the `draft` project. © 2026
Sebastien Rousseau.
