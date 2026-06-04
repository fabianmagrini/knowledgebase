# AGENTS.md

Guidance for AI agents working in this repository.

## What this repository is

A personal engineering knowledge base composed entirely of Markdown files. There is no build system, test suite, or runtime. The primary tasks here are creating, editing, linking, and organising notes.

## Conventions

All conventions are documented in [conventions.md](conventions.md). Read it before creating or editing notes. Key points:

- Every `.md` file must include YAML frontmatter with `title`, `tags`, `status`, and `updated`
- File names are lowercase and hyphenated: `event-driven-architecture.md`
- Tags are lowercase and hyphenated; use the established vocabulary in `conventions.md` before inventing new tags
- Status values: `draft` → `notes` → `complete`

## Structure

```
engineering/        # architecture, practices, security
languages/          # per-language notes
tools/              # cloud, containers, editors
concepts/           # algorithms, data structures, CS fundamentals
reading/            # notes from books, papers, articles
```

Each folder has a `README.md` as its index. When adding a new note to a folder, update that folder's `README.md` to link to it.

## Creating notes

Use this frontmatter starter:

```yaml
---
title: 
tags: []
topic: folder/subfolder
status: draft
updated: YYYY-MM-DD
related:
  - path/to/related.md
source: ""
---
```

Set `source` for notes derived from external material (books, papers, URLs). Omit it for original notes.

## Searching

```bash
# Find notes by tag
grep -rl "distributed-systems" .

# Find all drafts
grep -rl "status: draft" .

# Find reading notes
grep -rl "tags:.*reading" .

# Find stale notes
grep -rl "updated: 2024" .
```

## Cross-linking

When creating a note, check for related existing notes and add `related:` entries in both directions. This keeps the knowledge graph navigable.
