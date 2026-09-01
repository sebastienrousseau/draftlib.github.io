import os, glob, re, json, html, shutil

def post_build():
    output_dir = "public"
    docs_dir = "docs"
    base_url = "https://draftlib.com"

    os.makedirs(docs_dir, exist_ok=True)
    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(docs_dir, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    all_pages = set()
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            if f.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, f), output_dir)
                if rel_path == "index.html":
                    all_pages.add(f"{base_url}/")
                else:
                    all_pages.add(f"{base_url}/{rel_path}")

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in sorted(all_pages):
        sitemap_xml += f'  <url>\n    <loc>{p}</loc>\n    <lastmod>2026-09-01</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    sitemap_xml += '</urlset>\n'

    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sitemap_xml)

    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "CNAME"), "w", encoding="utf-8") as f:
            f.write("draftlib.com\n")

    llms_txt = f"""# Draft Lib
> Fast document processing and drafting engine in Rust with zero allocations and type-safe AST compilation.

## Core Documentation & Resources
- Homepage: {base_url}/
- Getting Started: {base_url}/getting-started/index.html
- Features: {base_url}/features/index.html
- Documentation: {base_url}/documentation/index.html
- Examples: {base_url}/examples/index.html
- Benchmarks: {base_url}/benchmarks/index.html
- Architecture: {base_url}/architecture/index.html
- Security: {base_url}/security/index.html
- About Sebastien Rousseau: {base_url}/about/index.html
"""
    for d in [output_dir, docs_dir]:
        with open(os.path.join(d, "llms.txt"), "w", encoding="utf-8") as f:
            f.write(llms_txt)

    for base_path in [output_dir, docs_dir]:
        for html_file in glob.glob(f"{base_path}/**/*.html", recursive=True):
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace("http://127.0.0.1:8000", base_url)
            content = content.replace("http://localhost:8000", base_url)

            content = re.sub(r'<pre><code><span class="text plain">(.*?)</span></code></pre>', lambda m: m.group(1) if ('<div' in m.group(1) or '<section' in m.group(1) or '<details' in m.group(1) or '<table' in m.group(1)) else m.group(0), content, flags=re.DOTALL)
            content = re.sub(r'<pre><code class="language-html">(.*?)</code></pre>', lambda m: m.group(1) if ('<div' in m.group(1) or '<section' in m.group(1) or '<details' in m.group(1) or '<table' in m.group(1)) else m.group(0), content, flags=re.DOTALL)
            content = re.sub(r'<pre><code>(.*?)</code></pre>', lambda m: m.group(1) if ('<div' in m.group(1) or '<section' in m.group(1) or '<details' in m.group(1) or '<table' in m.group(1)) else m.group(0), content, flags=re.DOTALL)

            def fix_html_tags(match):
                tag = match.group(0)
                for ent, val in [("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'"), ("&#x27;", "'")]:
                    tag = tag.replace(ent, val)
                return tag

            content = re.sub(r'&lt;/?(section|div|details|summary|table|thead|tbody|tr|th|td|form|label|input|textarea|button|svg|circle|line|path|polyline|kbd|span class|h2|h3|h4|p class|a class|img class).*?&gt;', fix_html_tags, content, flags=re.DOTALL)

            with open(html_file, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"Post-build optimization complete ({len(all_pages)} URLs).")

if __name__ == "__main__":
    post_build()
