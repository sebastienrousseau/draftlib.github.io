// SPDX-FileCopyrightText: 2026 Sebastien Rousseau
// SPDX-License-Identifier: MIT OR Apache-2.0
//
// Measured performance/SEO/best-practices/accessibility gate. Runs Lighthouse
// (desktop) over key pages in headless Chrome and fails the build if a score
// drops below its floor. The deterministic categories are held at 100; the
// performance floor is a little lower to absorb CI-runner noise, since it is a
// timing measurement, not a static check.
//
// Usage: node scripts/lighthouse-check.mjs [baseUrl]
// Browser: CHROME_PATH (or the runner's google-chrome) via chrome-launcher.

import { createRequire } from "module";
const require = createRequire(import.meta.url);
const lighthouse = (await import("lighthouse")).default;
const desktopConfig = (await import("lighthouse/core/config/desktop-config.js"))
  .default;
const chromeLauncher = await import("chrome-launcher");

const base = (process.argv[2] || "http://localhost:8099").replace(/\/$/, "");

// Page -> per-category floors (0..1). Deterministic categories are pinned to 1.
const PAGES = ["/", "/documentation/", "/grounding/", "/compliance/"];
const FLOORS = {
  performance: 0.9,
  accessibility: 1.0,
  "best-practices": 1.0,
  seo: 1.0,
};

const chrome = await chromeLauncher.launch({
  chromePath: process.env.CHROME_PATH || undefined,
  chromeFlags: ["--headless=new", "--no-sandbox", "--disable-dev-shm-usage"],
});

let failed = false;
const rows = [];
try {
  for (const p of PAGES) {
    const url = base + p;
    const { lhr } = await lighthouse(
      url,
      { port: chrome.port, output: "json", logLevel: "error" },
      desktopConfig,
    );
    const scores = Object.fromEntries(
      Object.entries(lhr.categories).map(([k, v]) => [k, v.score]),
    );
    rows.push([p, scores]);
    for (const [cat, floor] of Object.entries(FLOORS)) {
      const s = scores[cat];
      if (s == null || s < floor) {
        failed = true;
        console.error(
          `  FAIL ${p} ${cat}=${Math.round((s ?? 0) * 100)} (floor ${Math.round(floor * 100)})`,
        );
      }
    }
  }
} finally {
  await chrome.kill();
}

console.log("Lighthouse (desktop):");
for (const [p, s] of rows) {
  console.log(
    `  ${p.padEnd(18)} perf ${Math.round(s.performance * 100)}  a11y ${Math.round(
      s.accessibility * 100,
    )}  bp ${Math.round(s["best-practices"] * 100)}  seo ${Math.round(s.seo * 100)}`,
  );
}
if (failed) {
  console.error("Lighthouse gate FAILED.");
  process.exit(1);
}
console.log("Lighthouse gate passed.");
