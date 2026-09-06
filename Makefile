# SPDX-License-Identifier: Apache-2.0 OR MIT
# Semantic Version: v0.0.1
.PHONY: all build audit test contrast validate compress prune clean help

all: build

help:
	@echo "Available Makefile targets:"
	@echo "  make build      - Compile static site using Rust static-site-generator"
	@echo "  make audit      - Run WCAG 2.2 AAA and regression tests"
	@echo "  make contrast   - Verify color tokens against WCAG 2.2 AAA math ratios"
	@echo "  make validate   - Validate Markdown frontmatter schema integrity"
	@echo "  make clean      - Remove build artifacts and temporary files"

build:
	@command -v ssg >/dev/null 2>&1 || { echo "ssg required: cargo install ssg --version 0.0.56 --locked"; exit 1; }
	rm -rf public
	ssg build --content _posts --template _layouts --output public
	python3 scripts/minify-css.py public/site.css _layouts/styles.css _layouts/brand.css
	@for a in main.js theme-init.js logo.svg favicon.ico apple-touch-icon.png; do cp -f _layouts/$$a public/$$a 2>/dev/null || true; done
	@h=$$(ls public/highlight.*.css 2>/dev/null | head -1); test -n "$$h" && cp -f "$$h" public/highlight.css || true
	@test -d samples && cp -r samples public/samples || true
	python3 scripts/post-build.py
	python3 scripts/check-content.py docs

audit: contrast validate
	@/usr/bin/python3 scripts/regression-test.py

contrast:
	@/usr/bin/python3 scripts/audit-contrast.py

validate:
	@/usr/bin/python3 scripts/validate-frontmatter.py

clean:
	@rm -rf public docs dist .cache coverage *.log
	@echo "Workspace cleaned."
