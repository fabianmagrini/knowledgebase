#!/usr/bin/env python3
"""Validate knowledge-base notes against the repo conventions.

Checks (see conventions.md and AGENTS.md):
  ERRORS (fail the build)
    - frontmatter present and well-formed
    - required fields: title, tags, status, updated
    - status is one of draft | notes | complete
    - updated is a YYYY-MM-DD date
    - tags are lowercase, hyphenated, non-empty
    - file names are lowercase and hyphenated
    - related: links resolve to existing files
  WARNINGS (reported; fail only with --strict)
    - related: links are not reciprocated (bidirectional convention)
    - a note is not linked from its folder README index
    - a tag is used by only one note (likely sprawl, not a shared facet)

Usage:
    python3 scripts/lint-notes.py            # report; exit 1 on errors
    python3 scripts/lint-notes.py --strict   # warnings also cause exit 1
    python3 scripts/lint-notes.py --quiet     # only show problems, no summary

Zero dependencies; runs on Python 3.8+.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories never scanned.
EXCLUDE_DIRS = {".git", ".claude", ".obsidian", "node_modules", "scripts", "drafts"}
# Agent/instruction files that are not notes and carry no frontmatter.
EXCLUDE_FILES = {"CLAUDE.md", "AGENTS.md"}

REQUIRED_FIELDS = ("title", "tags", "status", "updated")
VALID_STATUS = {"draft", "notes", "complete"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TAG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FILENAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")


class Note:
    def __init__(self, path: Path):
        self.path = path
        self.rel = path.relative_to(REPO_ROOT).as_posix()
        self.is_index = path.name == "README.md"
        self.fields: dict[str, object] = {}
        self.has_frontmatter = False
        self.parse_error: str | None = None
        self._parse()

    def _parse(self) -> None:
        text = self.path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return
        end = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end = i
                break
        if end is None:
            self.parse_error = "frontmatter opened with '---' but never closed"
            return
        self.has_frontmatter = True
        self._parse_fields(lines[1:end])

    def _parse_fields(self, fm: list[str]) -> None:
        key = None
        i = 0
        while i < len(fm):
            line = fm[i]
            m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
            if m:
                key, value = m.group(1), m.group(2).strip()
                if value == "":
                    # Possibly a block list on following indented lines.
                    block, consumed = self._read_block(fm, i + 1)
                    self.fields[key] = block if block else ""
                    i += 1 + consumed
                    continue
                self.fields[key] = self._scalar(value)
            i += 1

    @staticmethod
    def _read_block(fm: list[str], start: int) -> tuple[list[str], int]:
        items: list[str] = []
        i = start
        while i < len(fm):
            lm = re.match(r"^\s+-\s*(.+?)\s*$", fm[i])
            if not lm:
                break
            items.append(lm.group(1).strip().strip('"').strip("'"))
            i += 1
        return items, i - start

    @staticmethod
    def _scalar(value: str):
        # Inline list: [a, b, c]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                return []
            return [v.strip().strip('"').strip("'") for v in inner.split(",")]
        return value.strip().strip('"').strip("'")

    @property
    def tags(self) -> list[str]:
        t = self.fields.get("tags")
        if isinstance(t, list):
            return t
        if isinstance(t, str) and t:
            return [t]
        return []

    @property
    def related(self) -> list[str]:
        r = self.fields.get("related")
        return r if isinstance(r, list) else []


def discover_notes() -> list[Note]:
    notes = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for name in filenames:
            if not name.endswith(".md") or name in EXCLUDE_FILES:
                continue
            notes.append(Note(Path(dirpath) / name))
    return notes


def resolve_link(src: Note, link: str, by_rel: dict[str, Note]) -> Note | None:
    """Resolve a related: path relative to the note's dir, then repo root."""
    if link.startswith(("http://", "https://")):
        return None
    src_dir = src.path.parent
    candidates = [
        os.path.normpath(src_dir / link),
        os.path.normpath(REPO_ROOT / link),
    ]
    for cand in candidates:
        try:
            rel = Path(cand).resolve().relative_to(REPO_ROOT).as_posix()
        except ValueError:
            continue
        if rel in by_rel:
            return by_rel[rel]
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint knowledge-base notes.")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    ap.add_argument("--quiet", action="store_true", help="suppress the summary line")
    ap.add_argument(
        "--errors-only", action="store_true", help="report errors only, hide warnings"
    )
    args = ap.parse_args()

    notes = discover_notes()
    by_rel = {n.rel: n for n in notes}

    errors: list[str] = []
    warnings: list[str] = []

    # Map each note to a normalized resolution of its related targets (for reciprocity).
    related_targets: dict[str, set[str]] = defaultdict(set)
    tag_usage: dict[str, list[str]] = defaultdict(list)

    for note in sorted(notes, key=lambda n: n.rel):
        # --- file naming ---
        if not note.is_index and not FILENAME_RE.match(note.path.name):
            errors.append(f"{note.rel}: file name is not lowercase-hyphenated")

        # --- frontmatter structure ---
        if note.parse_error:
            errors.append(f"{note.rel}: {note.parse_error}")
            continue
        if not note.has_frontmatter:
            errors.append(f"{note.rel}: missing YAML frontmatter")
            continue

        # --- required fields ---
        for field in REQUIRED_FIELDS:
            if field not in note.fields or note.fields[field] in ("", [], None):
                errors.append(f"{note.rel}: missing required field '{field}'")

        # --- status ---
        status = note.fields.get("status")
        if isinstance(status, str) and status not in VALID_STATUS:
            errors.append(
                f"{note.rel}: invalid status '{status}' "
                f"(expected one of {', '.join(sorted(VALID_STATUS))})"
            )

        # --- updated date ---
        updated = note.fields.get("updated")
        if isinstance(updated, str) and updated and not DATE_RE.match(updated):
            errors.append(f"{note.rel}: 'updated' is not YYYY-MM-DD ('{updated}')")

        # --- tags ---
        for tag in note.tags:
            if not TAG_RE.match(tag):
                errors.append(f"{note.rel}: tag '{tag}' is not lowercase-hyphenated")
            elif not note.is_index:
                tag_usage[tag].append(note.rel)

        # --- related links resolve ---
        for link in note.related:
            target = resolve_link(note, link, by_rel)
            if target is None:
                errors.append(f"{note.rel}: related link does not resolve -> '{link}'")
            elif target.is_index:
                warnings.append(
                    f"{note.rel}: related link points at an index README -> '{link}'"
                )
            else:
                related_targets[note.rel].add(target.rel)

    # --- bidirectional related links (warning) ---
    for src_rel, targets in related_targets.items():
        for tgt_rel in sorted(targets):
            if src_rel not in related_targets.get(tgt_rel, set()):
                warnings.append(
                    f"{src_rel}: related -> {tgt_rel} is not reciprocated (no back-link)"
                )

    # --- folder README index coverage (warning) ---
    for note in sorted(notes, key=lambda n: n.rel):
        if note.is_index:
            continue
        readme = note.path.parent / "README.md"
        if readme.exists():
            if note.path.name not in readme.read_text(encoding="utf-8"):
                warnings.append(
                    f"{note.rel}: not linked from its folder index "
                    f"{readme.relative_to(REPO_ROOT).as_posix()}"
                )

    # --- single-use tags (warning) ---
    for tag, users in sorted(tag_usage.items()):
        if len(users) == 1:
            warnings.append(
                f"single-use tag '{tag}' (only {users[0]}) — not a shared facet"
            )

    # --- report ---
    if not args.errors_only:
        for w in warnings:
            print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if not args.quiet:
        print(
            f"\n{len(notes)} notes checked: "
            f"{len(errors)} error(s), {len(warnings)} warning(s)."
        )

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
