---
name: redirect-stubs
description: Replace duplicate documentation directories with tiny HTML redirect stubs to shrink GitHub Pages artifacts. Use when a versioned-docs site (Sphinx/MkDocs/Jekyll) ships byte-identical copies of the same content under multiple URL aliases (e.g., stable/ duplicating 2.11/), the site is over the GitHub Pages 10 GB artifact limit, or actions/upload-pages-artifact is dereferencing source-level symlinks into full copies. Generates ~200-byte meta-refresh stubs that preserve URLs while letting the bytes live once.
---

# Redirect Stubs for Versioned Docs

Replaces duplicate version directories with `<meta http-equiv="refresh">` HTML stubs so URLs keep resolving while the bytes only live once. Designed for the `actions/upload-pages-artifact` pipeline, where source-level symlinks are forcibly dereferenced via `tar --dereference --hard-dereference` and therefore can't be used for dedup.

## When to use

- A docs site has `stable/` (or `latest/`, `current/`, etc.) as a byte-for-byte copy of a versioned directory.
- Patch-version aliases (`1.10/`, `1.10.0/`, `1.10.1/`) all hold identical content.
- The Pages artifact tar is approaching or exceeds 10 GB.
- The user wants to keep the alias URLs working — if the aliases aren't externally linked, prefer `rm -rf` over stubs.

## Pre-flight checks

Before invoking the script, confirm:

1. **The directories really are identical.** Run `diff -rq <alias_dir> <canonical_dir> | head` and verify there's either no output or only trivial differences (e.g., `.buildinfo`). If they actually differ, stubbing will silently change served content.
2. **Find the alias's canonical mapping.** A canonical version is the one that will keep its real bytes (e.g., `2.11/` is canonical, `stable/` is the alias).
3. **Decide on the URL form.** Relative URLs (default) are portable; absolute URLs (`--url-prefix`) are needed if the site is mounted at a non-root path and you want stubs that work even when copy-pasted.
4. **Check what files are loaded directly by JS, not navigated to.** For Sphinx these include `searchindex.js`, `objects.inv`, and anything in `_static/` / `_images/`. The script keeps `searchindex.js` and `objects.inv` as real copies by default; review the `--keep` list against the specific docs generator.

## How to invoke

The helper script lives at `scripts/make_stubs.py` in this repo. Typical usage:

```bash
# Dry-run first — shows what would change without writing anything
python3 scripts/make_stubs.py \
    --alias /path/to/site/stable \
    --canonical /path/to/site/2.11 \
    --dry-run

# Run for real
python3 scripts/make_stubs.py \
    --alias /path/to/site/stable \
    --canonical /path/to/site/2.11
```

The script:
- Walks `<alias>` recursively.
- For every `.html` file, overwrites it with a ~250-byte stub whose `meta http-equiv="refresh"` and `<link rel="canonical">` point at the equivalent path under `<canonical>`.
- Leaves files matching `--keep` patterns untouched (default: `searchindex.js`, `objects.inv`, `.buildinfo`).
- Prints a summary: files stubbed, bytes before/after, savings.

## Workflow inside a CI / GitHub Actions pipeline

Insert one step **between** the docs assembly step and `actions/upload-pages-artifact`:

```yaml
- name: Replace duplicate version dirs with redirect stubs
  run: |
    python3 .github/scripts/make_stubs.py --alias _site/stable --canonical _site/2.11
    # Aliases that aren't externally linked can simply be removed:
    rm -rf _site/1.10 _site/1.10.0 _site/1.7.0 _site/1.9.0 _site/master

- uses: actions/upload-pages-artifact@v3
  with:
    path: _site
```

Copy `make_stubs.py` into the docs repo (e.g., `.github/scripts/`) so the workflow doesn't depend on a per-runner skill install.

## Verifying the result

After running:

1. **Sanity-check stub size**: `find <alias> -name '*.html' -size +1k` should be empty (every stub should be < 1 KB). Anything large means a non-stubbed file was missed.
2. **Spot-check a redirect**: open a stub locally in a browser; it should immediately navigate to the canonical URL.
3. **Verify search still works** in the alias: navigate to `<alias>/search.html` (which is a stub redirecting to `<canonical>/search.html`); the search box should fetch `<canonical>/searchindex.js` correctly.
4. **Measure impact**: `tar cf - <alias> | wc -c` before vs. after gives the exact tar savings.

## Common pitfalls

- **Stubbing assets** (CSS/JS/PNG/SVG): the script only touches `.html` because meta-refresh only works in HTML. Don't extend it to other extensions; instead `rm` them if you don't need them under the alias path.
- **External deep-links to alias assets**: if blog posts link directly to `stable/_images/foo.png`, deleting it 404s those references. Either keep `_images/` and `_static/` as real copies under the alias (small cost) or accept the breakage.
- **Search index in the alias**: don't stub `searchindex.js` — Sphinx's search box loads it as JSON; a stubbed HTML response will throw a JS parse error.
- **Crawler indexing**: the stub includes `<meta name="robots" content="noindex">` so search engines index the canonical instead of the redirect. Don't strip it.
- **Symlink-or-stub confusion**: do not also create a symlink at the alias path — `actions/upload-pages-artifact` will dereference it and undo your stubs. Stubs must be real files.
