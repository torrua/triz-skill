#!/usr/bin/env python3
"""
Cross-platform deployment synchronization and release packager for triz-universal.

Supports:
- Checking or applying byte-identical skill deployment to any target directory
- Platform presets: Antigravity (~/.gemini/config/skills), Claude Code (~/.claude/skills),
  Cursor (~/.cursor/skills), Codex CLI (~/.codex/skills)
- Building a clean zip package for Claude.ai upload and GitHub Releases
"""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT_DIR / "triz-universal"
VERSION_FILE = ROOT_DIR / "VERSION"

PLATFORM_DESTINATIONS = {
    "antigravity": Path.home() / ".gemini" / "config" / "skills" / "triz-universal",
    "claude-code": Path.home() / ".claude" / "skills" / "triz-universal",
    "cursor": Path.home() / ".cursor" / "skills" / "triz-universal",
    "codex": Path.home() / ".codex" / "skills" / "triz-universal",
}


def compute_file_hashes(directory: Path) -> dict[str, str]:
    """Return a mapping of POSIX relative paths to SHA-256 hex digests."""
    if not directory.is_dir():
        return {}
    hashes: dict[str, str] = {}
    for path in sorted(directory.rglob("*")):
        if path.is_file() and not path.name.startswith(".") and "__pycache__" not in path.parts:
            rel = path.relative_to(directory).as_posix()
            hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def package_zip(output_path: Path | None = None) -> Path:
    """Create a clean release zip containing the triz-universal/ skill folder."""
    version = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else "3.0.0"
    dist_dir = ROOT_DIR / "dist"
    dist_dir.mkdir(parents=True, exist_ok=True)
    target_zip = output_path or (dist_dir / f"triz-universal-v{version}.zip")
    target_zip.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(target_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(SOURCE_DIR.rglob("*")):
            if file_path.is_file() and not file_path.name.startswith("."):
                arcname = Path("triz-universal") / file_path.relative_to(SOURCE_DIR)
                zf.write(file_path, arcname.as_posix())

    # Also keep a version-agnostic alias in dist/ when using default output
    if output_path is None:
        latest_alias = dist_dir / "triz-universal.zip"
        if latest_alias != target_zip:
            shutil.copy2(target_zip, latest_alias)

    return target_zip


def sync_deployment(mode: str, destination: Path) -> int:
    """Synchronize or verify byte-for-byte parity between source and destination."""
    if not SOURCE_DIR.is_dir():
        print(f"Error: Source skill directory does not exist: {SOURCE_DIR}", file=sys.stderr)
        return 1

    dest_resolved = destination.expanduser().resolve()
    if dest_resolved.name != "triz-universal":
        print(
            f"Error: Destination must end with 'triz-universal', got: {dest_resolved}",
            file=sys.stderr,
        )
        return 1

    normalized_mode = mode.lower()
    if normalized_mode == "apply":
        if dest_resolved.exists():
            shutil.rmtree(dest_resolved)
        dest_resolved.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SOURCE_DIR, dest_resolved)

    src_hashes = compute_file_hashes(SOURCE_DIR)
    dst_hashes = compute_file_hashes(dest_resolved)

    if src_hashes != dst_hashes:
        diff_keys = sorted(set(src_hashes.keys()) ^ set(dst_hashes.keys()))
        modified = sorted(
            k for k in src_hashes.keys() & dst_hashes.keys() if src_hashes[k] != dst_hashes[k]
        )
        print(
            f"Deployed skill differs from source at {dest_resolved}. "
            f"Missing/extra={diff_keys}, modified={modified}. "
            f"Run with --mode apply to synchronize.",
            file=sys.stderr,
        )
        return 1

    print(f"Deployment is synchronized ({len(src_hashes)} files verified): {dest_resolved}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Cross-platform installer, parity checker, and zip packager for triz-universal."
    )
    parser.add_argument(
        "--mode",
        choices=["check", "apply", "Check", "Apply"],
        default="check",
        help="Check SHA-256 parity or Apply (copy) the skill to the destination.",
    )
    parser.add_argument(
        "--destination",
        default=os.environ.get("TRIZ_DEPLOY_DIR", ""),
        help="Explicit destination path ending in 'triz-universal' (or set TRIZ_DEPLOY_DIR).",
    )
    parser.add_argument(
        "--platform",
        choices=sorted(PLATFORM_DESTINATIONS.keys()),
        help="Target platform preset (antigravity, claude-code, cursor, codex).",
    )
    parser.add_argument(
        "--package-zip",
        nargs="?",
        const="",
        default=None,
        help="Build a clean release zip archive for Claude.ai / GitHub Releases.",
    )

    args = parser.parse_args(argv)

    if args.package_zip is not None:
        out_path = Path(args.package_zip) if args.package_zip else None
        created = package_zip(out_path)
        print(f"Created release archive: {created}")
        if not args.destination and not args.platform:
            return 0

    dest_str = args.destination
    if not dest_str and args.platform:
        dest_path = PLATFORM_DESTINATIONS[args.platform]
    elif dest_str:
        dest_path = Path(dest_str)
    else:
        parser.error("Provide --destination, set TRIZ_DEPLOY_DIR, or specify --platform (or --package-zip).")
        return 2

    return sync_deployment(args.mode, dest_path)


if __name__ == "__main__":
    raise SystemExit(main())
