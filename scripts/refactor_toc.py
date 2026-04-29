"""
Refactor PyTorch docs to extract duplicated sidebar TOC into standalone files.

Each HTML page in a Sphinx-built PyTorch docs version embeds the full sidebar
TOC (~350KB, ~2600 entries) inline. This script:

1. Extracts the TOC from each HTML file
2. Canonicalizes it (strips per-page "current" markers, normalizes URLs to be
   relative to the version root)
3. Groups files by identical canonical TOC content
4. Writes each unique TOC variant to a standalone `_toc_{n}.html` file
5. Replaces the inline TOC in each HTML with a lightweight placeholder
6. Generates `_toc_loader.js` that fetches + injects the TOC at page load

Usage:
    python3 refactor_toc.py <version_dir> [--dry-run]

Example:
    python3 refactor_toc.py 2.9
    python3 refactor_toc.py 2.9 --dry-run
"""

import argparse
import hashlib
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

NAV_START_RE = re.compile(
    r'<nav\s+class="bd-docs-nav bd-links"\s*\n?\s*aria-label="Section Navigation">'
)
NAV_END = "</nav></div>"

CURRENT_CLASS_RE = re.compile(r"\bcurrent\b")
ACTIVE_CLASS_RE = re.compile(r"\bactive\b")
OPEN_ATTR_RE = re.compile(r'\s*open="open"')
SELF_HREF_RE = re.compile(r'href="#"')

PLACEHOLDER_TEMPLATE = """\
<nav class="bd-docs-nav bd-links"
     aria-label="Section Navigation">
  <div id="toc-placeholder" data-toc-src="{toc_src}"></div>
</nav></div>"""

LOADER_JS = """\
(function() {
  'use strict';

  var placeholder = document.getElementById('toc-placeholder');
  if (!placeholder) return;

  var tocSrc = placeholder.getAttribute('data-toc-src');
  if (!tocSrc) return;

  // The TOC file contains URLs relative to the version root.
  // Compute the prefix from this page to the version root so we can
  // resolve those URLs correctly. The _toc file lives at the root,
  // so the number of "../" segments in tocSrc tells us the depth.
  var depthPrefix = tocSrc.replace(/[^/]*$/, '');  // e.g. "../" or ""

  fetch(tocSrc)
    .then(function(response) {
      if (!response.ok) throw new Error('TOC fetch failed: ' + response.status);
      return response.text();
    })
    .then(function(html) {
      var container = document.createElement('div');
      container.innerHTML = html;

      // Rewrite root-relative hrefs to be relative to this page
      if (depthPrefix) {
        var links = container.querySelectorAll('a[href]');
        for (var i = 0; i < links.length; i++) {
          var href = links[i].getAttribute('href');
          if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto:')) {
            links[i].setAttribute('href', depthPrefix + href);
          }
        }
      }

      markCurrentPage(container);
      placeholder.innerHTML = container.innerHTML;
      reinitScrollSpy();
    })
    .catch(function(err) {
      console.warn('TOC loader:', err.message);
    });

  function markCurrentPage(container) {
    var currentPath = window.location.pathname.replace(/\/+/g, '/');
    var links = container.querySelectorAll('a.reference');

    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var href = link.getAttribute('href');
      if (!href || href.startsWith('http://') || href.startsWith('https://')) continue;

      var resolved = new URL(href, window.location.href).pathname.replace(/\/+/g, '/');

      if (resolved === currentPath) {
        link.classList.add('current');
        link.setAttribute('href', '#');

        var li = link.closest('li');
        while (li) {
          li.classList.add('current');
          if (li.classList.contains('has-children')) {
            li.classList.add('active');
            var details = li.querySelector(':scope > details');
            if (details) details.setAttribute('open', 'open');
          }
          var parentUl = li.parentElement;
          li = parentUl ? parentUl.closest('li') : null;
        }

        var ul = link.closest('ul');
        if (ul) ul.classList.add('current');
        break;
      }
    }
  }

  function reinitScrollSpy() {
    if (typeof bootstrap !== 'undefined' && bootstrap.ScrollSpy) {
      var scrollElement = document.querySelector('[data-bs-spy="scroll"]');
      if (scrollElement) {
        var instance = bootstrap.ScrollSpy.getInstance(scrollElement);
        if (instance) instance.refresh();
      }
    }
  }
})();
"""

def find_toc_bounds(content):
    """Find the start and end positions of the TOC nav block in HTML content.

    Returns (start, end) positions or (None, None) if not found.
    The range includes the full `<nav ...>...</nav></div>` block.
    """
    match = NAV_START_RE.search(content)
    if not match:
        return None, None
    start = match.start()

    # Find the matching </nav></div> - need to handle nested navs
    # The TOC nav contains a <div class="bd-toc-item"> and ends with </nav></div>
    # Search for the </nav></div> that closes our nav
    # Since there are no nested <nav> elements in the TOC, find the first </nav></div> after start
    end_pos = content.find(NAV_END, start)
    if end_pos == -1:
        return None, None
    end = end_pos + len(NAV_END)
    return start, end

def canonicalize_toc(toc_html, page_relpath):
    """Canonicalize TOC HTML by stripping per-page markers and normalizing URLs.

    Args:
        toc_html: Raw TOC HTML from one page
        page_relpath: Page path relative to version root (e.g. "generated/torch.abs.html")

    Returns:
        Canonical TOC HTML with all URLs relative to the version root.
    """
    result = toc_html

    # Figure out the directory of this page relative to version root
    page_dir = os.path.dirname(page_relpath)

    # Normalize all relative URLs to be relative to version root.
    # Must happen BEFORE href="#" replacement to avoid double-prefixing.
    if page_dir:
        def rewrite_href(m):
            href = m.group(1)
            if href.startswith(("http://", "https://", "#", "mailto:")):
                return m.group(0)
            resolved = os.path.normpath(os.path.join(page_dir, href))
            resolved = resolved.replace("\\", "/")
            return f'href="{resolved}"'

        result = re.sub(r'href="([^"]*)"', rewrite_href, result)

    # Replace href="#" (self-reference for "current" page) with actual page path.
    # At this point all other hrefs are already root-relative.
    result = SELF_HREF_RE.sub(f'href="{page_relpath}"', result)

    # Strip "current" and "active" classes
    result = CURRENT_CLASS_RE.sub("", result)
    result = ACTIVE_CLASS_RE.sub("", result)

    # Strip open="open" attributes
    result = OPEN_ATTR_RE.sub("", result)

    # Normalize whitespace inside class="..." attributes, and remove empty ones
    def normalize_class(m):
        classes = m.group(1).split()
        if not classes:
            return ""
        return f'class="{" ".join(classes)}"'

    result = re.sub(r'\s*class="([^"]*)"', normalize_class, result)

    # Clean up tags with trailing space before >
    result = re.sub(r"\s+>", ">", result)

    return result

def toc_content_hash(content):
    """Return a short hash of TOC content for use in filenames."""
    return hashlib.sha256(content.encode()).hexdigest()[:8]

def process_version_dir(version_dir, dry_run=False):
    version_dir = Path(version_dir).resolve()
    if not version_dir.is_dir():
        print(f"Error: {version_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    skip_dirs = {"_sources", "_static", "_images", "_sphinx_design_static"}

    # Phase 1: Extract and canonicalize TOCs from all HTML files
    print("Phase 1: Extracting and canonicalizing TOCs...")
    page_tocs = {}  # relpath -> (toc_start, toc_end, canonical_toc)
    no_toc_pages = []

    for root, dirs, files in os.walk(version_dir):
        dirs[:] = [d for d in sorted(dirs) if d not in skip_dirs]
        for fname in sorted(files):
            if not fname.endswith(".html"):
                continue
            filepath = Path(root) / fname
            relpath = str(filepath.relative_to(version_dir))

            content = filepath.read_text(encoding="utf-8")
            start, end = find_toc_bounds(content)
            if start is None:
                no_toc_pages.append(relpath)
                continue

            toc_html = content[start:end]
            canonical = canonicalize_toc(toc_html, relpath)
            page_tocs[relpath] = (start, end, canonical)

    print(f"  Found {len(page_tocs)} pages with TOC, {len(no_toc_pages)} without")

    # Phase 2: Group pages by canonical TOC content
    print("Phase 2: Grouping by canonical TOC content...")
    toc_groups = defaultdict(list)  # canonical_toc -> [relpath, ...]
    for relpath, (start, end, canonical) in page_tocs.items():
        toc_groups[canonical].append(relpath)

    print(f"  Found {len(toc_groups)} unique TOC variant(s):")
    toc_files = {}  # canonical_toc -> toc filename
    for i, (canonical, pages) in enumerate(
        sorted(toc_groups.items(), key=lambda x: -len(x[1]))
    ):
        h = toc_content_hash(canonical)
        toc_filename = f"_toc_{h}.html" if len(toc_groups) > 1 else "_toc.html"
        toc_files[canonical] = toc_filename
        sample = pages[0]
        size_kb = len(canonical.encode()) / 1024
        print(f"    {toc_filename}: {len(pages)} pages, {size_kb:.0f}KB (e.g. {sample})")

    # Phase 3: Write standalone TOC files
    print("Phase 3: Writing standalone TOC files...")
    for canonical, toc_filename in toc_files.items():
        toc_path = version_dir / toc_filename
        # Extract just the inner content (inside the <nav> wrapper)
        # We keep the full <nav> structure in the standalone file
        # so the loader can just innerHTML it into the placeholder
        inner_start = canonical.find("<p ")
        if inner_start == -1:
            inner_start = canonical.find("<div ")
        inner_end = canonical.rfind("</div>") + len("</div>")
        inner_content = canonical[inner_start:inner_end] if inner_start != -1 else canonical

        if dry_run:
            print(f"  [DRY RUN] Would write {toc_path} ({len(inner_content)} bytes)")
        else:
            toc_path.write_text(inner_content, encoding="utf-8")
            print(f"  Wrote {toc_path} ({len(inner_content)} bytes)")

    # Phase 4: Write the TOC loader JS
    print("Phase 4: Writing _toc_loader.js...")
    loader_path = version_dir / "_toc_loader.js"
    if dry_run:
        print(f"  [DRY RUN] Would write {loader_path}")
    else:
        loader_path.write_text(LOADER_JS, encoding="utf-8")
        print(f"  Wrote {loader_path}")

    # Phase 5: Replace inline TOC in each HTML file
    print("Phase 5: Replacing inline TOCs with placeholders...")
    modified = 0
    saved_bytes = 0

    for relpath, (start, end, canonical) in page_tocs.items():
        filepath = version_dir / relpath
        content = filepath.read_text(encoding="utf-8")

        toc_filename = toc_files[canonical]

        # Compute the relative path from this page to the TOC file (in version root)
        page_dir = os.path.dirname(relpath)
        if page_dir:
            toc_src = os.path.relpath(toc_filename, page_dir)
            loader_src = os.path.relpath("_toc_loader.js", page_dir)
        else:
            toc_src = toc_filename
            loader_src = "_toc_loader.js"
        toc_src = toc_src.replace("\\", "/")
        loader_src = loader_src.replace("\\", "/")

        placeholder = PLACEHOLDER_TEMPLATE.format(toc_src=toc_src)

        # Add script tag before closing </body> if not already present
        loader_script = f'<script src="{loader_src}" defer></script>'

        old_toc = content[start:end]
        new_content = content[:start] + placeholder + content[end:]

        # Insert loader script before </body>
        if loader_script not in new_content:
            new_content = new_content.replace("</body>", f"{loader_script}\n</body>")

        bytes_saved = len(content.encode()) - len(new_content.encode())
        saved_bytes += bytes_saved

        if dry_run:
            if modified < 3:
                print(f"  [DRY RUN] {relpath}: would save {bytes_saved:,} bytes")
        else:
            filepath.write_text(new_content, encoding="utf-8")

        modified += 1

    print(f"\nDone! Modified {modified} files.")
    print(f"Total space saved: {saved_bytes / 1024 / 1024:.1f} MB")
    print(f"TOC files created: {len(toc_files)}")
    if no_toc_pages:
        print(f"Pages without TOC (skipped): {len(no_toc_pages)}")
        for p in no_toc_pages[:5]:
            print(f"  {p}")
        if len(no_toc_pages) > 5:
            print(f"  ... and {len(no_toc_pages) - 5} more")

def main():
    parser = argparse.ArgumentParser(
        description="Extract duplicated sidebar TOC from PyTorch docs into standalone files"
    )
    parser.add_argument("version_dir", help="Path to the version directory (e.g. 2.9)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without modifying files",
    )
    args = parser.parse_args()
    process_version_dir(args.version_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
