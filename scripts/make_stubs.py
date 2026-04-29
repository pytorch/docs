#!/usr/bin/env python3
"""
Replace HTML files in an alias directory with tiny meta-refresh redirect
stubs pointing at the matching path under a canonical directory.

Designed for versioned doc sites deployed via actions/upload-pages-artifact,
where source-level symlinks get dereferenced into full copies and inflate
the artifact tar past the 10 GB limit.

Two modes:

* Default (walk alias): the alias directory already contains a copy of the
  canonical's HTML files (e.g., `cp -r 2.11 stable` or a CI build that
  materialized the duplicate). Each .html in alias is rewritten in place to
  a stub. Files matching --keep are left as real copies.

* --mirror-canonical: the alias directory does not yet exist (or is empty).
  Walk the canonical, and for every .html file create a stub at the matching
  relative path under alias. Useful in source repos where keeping a full
  duplicate dir under git is wasteful, and for converting a symlink alias
  (e.g., `stable -> 2.11`) into a checked-in stub directory.

Usage:
    # Stub an existing duplicate dir (CI / post-build):
    make_stubs.py --alias _site/stable --canonical _site/2.11

    # Materialize stubs from canonical (in-repo / replacing a symlink):
    rm stable
    make_stubs.py --alias stable --canonical 2.11 --mirror-canonical

    # Preview without writing:
    make_stubs.py --alias stable --canonical 2.11 --mirror-canonical --dry-run
"""

import argparse
import os
import sys
import urllib.parse
from pathlib import Path

# location.replace() keeps location.hash and location.search; <meta http-equiv>
# alone drops them, so anchor deep-links like #torch.cat would lose the anchor.
# meta-refresh + <a> are the noscript / crawler fallback.
STUB_TEMPLATE = (
    '<!DOCTYPE html>\n'
    '<meta charset="utf-8">\n'
    '<title>Redirecting&hellip;</title>\n'
    '<script>location.replace("{url}" + location.hash + location.search);</script>\n'
    '<meta http-equiv="refresh" content="0; url={url}">\n'
    '<link rel="canonical" href="{url}">\n'
    '<meta name="robots" content="noindex">\n'
    '<a href="{url}">Continue to {url}</a>\n'
)

DEFAULT_KEEP = {"searchindex.js", "objects.inv", ".buildinfo"}


def quote_url_path(rel_path_posix: str) -> str:
    """URL-encode a relative path, keeping '/' as a separator."""
    return urllib.parse.quote(rel_path_posix, safe="/")


def compute_url(alias_file: Path, canonical_file: Path, rel_path: Path, url_prefix: str | None) -> str:
    """Return the URL the stub should redirect to."""
    if url_prefix is not None:
        rel = rel_path.as_posix()
        return url_prefix.rstrip("/") + "/" + quote_url_path(rel)
    rel = os.path.relpath(canonical_file, alias_file.parent).replace(os.sep, "/")
    return quote_url_path(rel)


def make_stub(alias_file: Path, canonical_file: Path, rel_path: Path, url_prefix: str | None) -> str:
    url = compute_url(alias_file, canonical_file, rel_path, url_prefix)
    return STUB_TEMPLATE.format(url=url)


def write_stub_atomically(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".stub.tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def iter_alias_html(alias: Path):
    # os.walk does not follow symlinks by default, which is what we want:
    # symlinked subtrees inside alias are skipped instead of accidentally
    # rewriting files outside the alias.
    for root, _, files in os.walk(alias):
        for name in files:
            yield Path(root) / name, name


def iter_canonical_html(canonical: Path):
    for root, _, files in os.walk(canonical):
        for name in files:
            if Path(name).suffix.lower() != ".html":
                continue
            yield Path(root) / name, name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--alias", required=True, type=Path, help="Directory to stub (e.g., _site/stable).")
    parser.add_argument("--canonical", required=True, type=Path, help="Directory holding the real bytes (e.g., _site/2.11).")
    parser.add_argument(
        "--mirror-canonical",
        action="store_true",
        help="Walk canonical (not alias) and write stubs into alias for each canonical .html. "
             "Use when alias does not yet exist or is empty.",
    )
    parser.add_argument(
        "--url-prefix",
        default=None,
        help="If set, generate absolute URLs rooted here (e.g., '/docs/2.11'). "
             "Default: relative URLs from each alias file to its canonical sibling.",
    )
    parser.add_argument(
        "--keep",
        action="append",
        default=[],
        help="Filename to keep as a real copy (repeat flag for multiple). "
             f"Defaults always include: {sorted(DEFAULT_KEEP)}.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print what would change; don't write files.")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-file output.")
    args = parser.parse_args()

    alias = args.alias.resolve() if args.alias.exists() else args.alias.absolute()
    canonical = args.canonical.resolve()

    if not canonical.is_dir():
        print(f"error: --canonical not a directory: {canonical}", file=sys.stderr)
        return 2

    if args.mirror_canonical:
        if alias.exists() and alias.is_symlink():
            print(f"error: --alias is a symlink; rm it first so a real directory can be created: {alias}", file=sys.stderr)
            return 2
        if alias.exists() and not alias.is_dir():
            print(f"error: --alias exists but is not a directory: {alias}", file=sys.stderr)
            return 2
    else:
        if not alias.is_dir():
            print(f"error: --alias not a directory (use --mirror-canonical to create from canonical): {alias}", file=sys.stderr)
            return 2

    if alias == canonical:
        print("error: --alias and --canonical resolve to the same path", file=sys.stderr)
        return 2

    keep = DEFAULT_KEEP | set(args.keep)

    stubbed = 0
    skipped_keep = 0
    missing_canonical = 0
    bytes_before = 0
    bytes_after = 0

    if args.mirror_canonical:
        for canonical_path, name in iter_canonical_html(canonical):
            if name in keep:
                skipped_keep += 1
                continue
            rel = canonical_path.relative_to(canonical)
            alias_path = alias / rel
            stub = make_stub(alias_path, canonical_path, rel, args.url_prefix)
            new_size = len(stub.encode("utf-8"))
            old_size = alias_path.stat().st_size if alias_path.is_file() else 0
            bytes_before += old_size
            bytes_after += new_size
            stubbed += 1
            if not args.dry_run:
                write_stub_atomically(alias_path, stub)
            if not args.quiet:
                print(f"  stub: {rel}  ({new_size} bytes)")
    else:
        for path, name in iter_alias_html(alias):
            if name in keep:
                skipped_keep += 1
                continue
            if path.suffix.lower() != ".html":
                continue
            rel = path.relative_to(alias)
            canonical_path = canonical / rel
            if not canonical_path.is_file():
                # Refuse to stub if canonical lacks the file — would 404.
                missing_canonical += 1
                if not args.quiet:
                    print(f"  skip (no canonical): {rel}", file=sys.stderr)
                continue
            stub = make_stub(path, canonical_path, rel, args.url_prefix)
            old_size = path.stat().st_size
            new_size = len(stub.encode("utf-8"))
            bytes_before += old_size
            bytes_after += new_size
            stubbed += 1
            if not args.dry_run:
                write_stub_atomically(path, stub)
            if not args.quiet:
                print(f"  stub: {rel}  ({old_size} -> {new_size} bytes)")

    saved = bytes_before - bytes_after
    print()
    print(f"alias:        {alias}")
    print(f"canonical:    {canonical}")
    print(f"mode:         {'mirror-canonical' if args.mirror_canonical else 'walk-alias'}")
    print(f"stubbed:      {stubbed} files")
    print(f"kept:         {skipped_keep} files (matched --keep)")
    if missing_canonical:
        print(f"unstubbed:    {missing_canonical} files (no canonical equivalent)")
    print(f"bytes before: {bytes_before:>15,}")
    print(f"bytes after:  {bytes_after:>15,}")
    print(f"saved:        {saved:>15,}  ({saved / (1024 * 1024):.1f} MiB)")
    if args.dry_run:
        print("(dry-run -- no files were modified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
