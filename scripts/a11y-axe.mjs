// SPDX-FileCopyrightText: 2026 Sebastien Rousseau
// SPDX-License-Identifier: MIT OR Apache-2.0
//
// Rendered accessibility gate: runs axe-core over every built page in a real
// (headless) browser and fails only on axe *violations*. axe "incomplete"
// results (e.g. contrast of text over a photographic banner, which a tool
// cannot evaluate through the scrim) are reported for the record but never fail
// the build — that is the manual-review boundary, and treating it as an error
// is what makes pa11y-ci unusable here.
//
// Usage: node scripts/a11y-axe.mjs [baseUrl] [docsDir]
//   baseUrl  default http://localhost:8099
//   docsDir  default ./docs
// Browser: puppeteer-core + a system Chrome. Set CHROME_PATH (or
// PUPPETEER_EXECUTABLE_PATH); on GitHub ubuntu runners `which google-chrome`.

import fs from "fs";
import path from "path";
import { execSync } from "child_process";
import { createRequire } from "module";

const require = createRequire(import.meta.url);
const puppeteer = require("puppeteer-core");
const axeSource = fs.readFileSync(
  require.resolve("axe-core/axe.min.js"),
  "utf8",
);

const baseUrl = (process.argv[2] || "http://localhost:8099").replace(/\/$/, "");
const docsDir = path.resolve(process.argv[3] || "docs");

function chromePath() {
  const env = process.env.CHROME_PATH || process.env.PUPPETEER_EXECUTABLE_PATH;
  if (env) return env;
  const candidates = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
    "/usr/bin/chromium",
  ];
  for (const c of candidates) if (fs.existsSync(c)) return c;
  try {
    return execSync("command -v google-chrome || command -v chromium-browser")
      .toString()
      .trim();
  } catch {
    throw new Error("No Chrome found; set CHROME_PATH");
  }
}

function pages() {
  const out = execSync(`find ${JSON.stringify(docsDir)} -name index.html`)
    .toString()
    .trim()
    .split("\n")
    .filter(Boolean);
  return out.map(
    (f) =>
      baseUrl +
      "/" +
      path.relative(docsDir, f).replace(/index\.html$/, ""),
  );
}

const browser = await puppeteer.launch({
  executablePath: chromePath(),
  headless: "new",
  args: ["--no-sandbox", "--disable-dev-shm-usage"],
});
const page = await browser.newPage();
await page.setViewport({ width: 1280, height: 900 });

let violations = 0;
let incomplete = 0;
const failures = [];
const urls = pages();

for (const url of urls) {
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 30000 });
  await page.evaluate(axeSource);
  const r = await page.evaluate(async () => await window.axe.run(document));
  incomplete += r.incomplete.reduce((n, v) => n + v.nodes.length, 0);
  for (const v of r.violations) {
    for (const n of v.nodes) {
      violations++;
      failures.push(
        `  ${url.replace(baseUrl, "") || "/"}  [${v.id}]  ${n.target.join(" ")}`,
      );
    }
  }
}
await browser.close();

console.log(
  `axe-core: ${urls.length} pages, ${violations} violation(s), ${incomplete} incomplete (needs-review, not failing).`,
);
if (violations) {
  console.error("Accessibility violations:");
  for (const f of failures) console.error(f);
  process.exit(1);
}
console.log("No accessibility violations.");
