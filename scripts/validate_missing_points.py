#!/usr/bin/env python3
"""Validate that task report markdown files contain a complete Missing Points Conclusion block."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ("Missing", "Root cause", "Risk", "Action", "Owner", "Deadline")
HEADING_PATTERN = re.compile(r"^###\s+Missing Points Conclusion\s*$", re.IGNORECASE | re.MULTILINE)
FIELD_PATTERN_TEMPLATE = r"^[-*]\s+{field}\s*:"


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")

    if not HEADING_PATTERN.search(content):
        return [f"{path}: missing heading '### Missing Points Conclusion'"]

    for field in REQUIRED_FIELDS:
        pattern = re.compile(FIELD_PATTERN_TEMPLATE.format(field=re.escape(field)), re.IGNORECASE | re.MULTILINE)
        if not pattern.search(content):
            errors.append(f"{path}: missing field '{field}:' in Missing Points Conclusion")

    return errors


def find_markdown_files(root: Path) -> list[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def run(root: Path, strict: bool) -> int:
    files = find_markdown_files(root)
    if not files:
        print(f"No markdown files found in {root}")
        return 1 if strict else 0

    errors: list[str] = []
    for file_path in files:
        errors.extend(validate_file(file_path))

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Validation passed for {len(files)} markdown file(s) in {root}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default="task_reports", help="Directory containing task report markdown files")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if the target directory has no markdown files",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.path)

    if not root.exists():
        print(f"Path does not exist: {root}")
        return 1

    if not root.is_dir():
        print(f"Path is not a directory: {root}")
        return 1

    return run(root, strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
