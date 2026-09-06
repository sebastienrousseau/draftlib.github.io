---
name: "draft"
short_name: "draft"
title: "Accessibility — draft"
description: "How the draft website is built and tested for accessibility."
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
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

Automated checks run in the deploy pipeline, and the interactive elements —
navigation, the theme toggle and the search dialog — are checked by keyboard.
Automated tooling cannot catch everything, so some judgement is manual.

## Found a problem?

If any part of this site is hard to use, please
[open an issue](https://github.com/sebastienrousseau/draft/issues) and we will
address it.
