---
name: "draft"
short_name: "draft"
title: "Accessibility — draft"
description: "How the draft website is built and tested for accessibility."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
og_card: "accessibility"
breadcrumb: true
permalink: "https://draftlib.com/accessibility/"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "research-paper"
banner_alt: "A printed research paper on a desk"
eyebrow: "Accessibility"
headline: "Accessibility"
lead: "How this site is built and tested for accessibility, and how to report an issue."
---

This site aims to meet WCAG 2.2 at Level AA. It is a static build with
semantic HTML, a visible skip link, keyboard-operable navigation, a theme
toggle, and text that reflows without loss of content.

## How it is tested

Every deploy runs three automated gates before the site can publish:

- **`html-validate`** with its recommended and WCAG rule sets, over every page.
- **A colour-contrast audit** (`audit/contrast.py`) that fails the build unless
  body text, headings, links and focus rings clear WCAG AAA ratios in both
  light and dark themes.
- **A structure guardrail** requiring exactly one `<h1>`, a canonical link, a
  Content-Security-Policy, and a visible skip link on every page, with no inline
  styles.

Automated tooling cannot catch everything, so the interactive elements —
navigation, the theme toggle and the search dialog — are also checked by
keyboard, including focus order and Escape handling.

## Found a problem?

If any part of this site is hard to use, please
[open an issue](https://github.com/sebastienrousseau/draft/issues) and we will
address it.
