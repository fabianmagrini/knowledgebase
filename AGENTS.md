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
engineering/            # architecture, practices, security
  architecture/         # system design, distributed systems, patterns
  practices/            # testing, CI/CD, release engineering, code review
  ai-native/            # the agentic SDLC, AI adoption, agent operation, context engineering
  security/             # security principles, threat modeling, vulnerabilities
leadership/             # leadership, communication, decision governance, culture
product/                # product management and discovery
languages-and-frameworks/  # per-language and framework notes
tools/                  # tooling, platforms, infrastructure (flat)
sre/                    # site reliability, incident response, operations
standards/              # specifications, protocols, formats
concepts/               # algorithms, data structures, CS fundamentals
case-studies/           # deep-dives into how real production systems are built
reading/                # notes from books, papers, articles
```

Each folder has a `README.md` as its index. When adding a new note to a folder, update that folder's `README.md` to link to it.

`drafts/` also exists for rough, unplaced captures, but prefer filing a note in its topical folder with `status: draft` over parking it here.

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
