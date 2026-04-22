#!/usr/bin/env python3
"""Validate that markdown task reports contain a Missing Points Conclusion block."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

REQUIRED_FIELDS = [
    "- Missing:",
    "- Root cause:",
    "- Risk:",
    "- Action:",
    "- Owner:",
    "- Deadline:",
]

HEADER_PATTERN = re.compile(r"^###\s+Missing Points Conclusion\s*$", re.MULTILINE)


def check_file(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not HEADER_PATTERN.search(text):
        errors.append("Missing header: ### Missing Points Conclusion")
        return errors

    for field in REQUIRED_FIELDS:
        if field not in text:
            errors.append(f"Missing field: {field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ensure task markdown files contain a Missing Points Conclusion block."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Markdown files or directories to scan (default: reports/tasks)",
    )
    args = parser.parse_args()

    raw_paths = args.paths or ["reports/tasks"]
    md_files: list[pathlib.Path] = []

    for raw in raw_paths:
        p = pathlib.Path(raw)
        if not p.exists():
            print(f"[WARN] Path not found, skipped: {p}")
            continue
        if p.is_dir():
            md_files.extend(sorted(p.rglob("*.md")))
        elif p.suffix.lower() == ".md":
            md_files.append(p)

    if not md_files:
        print("[INFO] No markdown task reports found. Nothing to validate.")
        return 0

    has_error = False
    for file in md_files:
        errors = check_file(file)
        if errors:
            has_error = True
            print(f"[FAIL] {file}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"[PASS] {file}")

    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
