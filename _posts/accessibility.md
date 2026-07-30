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
description: "The accessibility commitments for draftlib.com and the draft command line."
format-detection: telephone=no
hreflang: en
icon: "https://draftlib.com/img/draft.svg"
id: "https://draftlib.com/accessibility/"
image_alt: "draft logo"
image_height: 120
image_width: 120
image: "https://draftlib.com/img/draft.svg"
keywords: "accessibility, wcag, a11y, keyboard, contrast"
language: en-GB
layout: page
locale: en_GB
logo_alt: "draft logo"
logo_height: 36
logo_width: 36
logo: "https://draftlib.com/img/draft.svg"
menu: active
name: draft
permalink: "https://draftlib.com/accessibility/"
rating: general
referrer: no-referrer
revisit-after: "7 days"
robots: "index, follow"
short_name: draft
subtitle: "The accessibility commitments for draftlib.com and the draft command line."
tags: "draft, grounded generation, research, markdown, go"
theme_color: "#0b0e14"
title: "Accessibility — draft"
url: "https://draftlib.com/accessibility/"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"
---

# Accessibility

## This site

draftlib.com is built to meet WCAG 2.2 AA. In practice that means: a skip link
to the main content, a visible focus ring on every interactive element, colour
contrast checked in both themes, no motion that cannot be stopped, and a layout
that reflows to 320 CSS pixels without horizontal scrolling.

The theme follows your operating system preference unless you override it, and
the choice persists. Fonts are self-hosted, so no third-party request is needed
to render a page.

## The command line

`draft` runs headlessly with `--print` or `--json` when a full-screen interface
is unhelpful — including with a screen reader, in a pipeline, or over a slow
connection. Colour is dropped automatically when output is not a terminal, and
`DRAFT_SHOW_LOGO=0` suppresses the banner.

The dashboard is fully keyboard-driven: arrow keys or `j`/`k` scroll, `q` or
`Esc` quits, and the queue can be extended without a mouse.

## Feedback

If something here does not work for you, please
[open an issue](https://github.com/sebastienrousseau/draft/issues). Accessibility
defects are treated as ordinary bugs, not enhancements.
