---
title: Knowledge Base Conventions
tags: [meta]
status: complete
updated: 2026-06-15
---

# Conventions

## Frontmatter Schema

Every note should include YAML frontmatter at the top:

```yaml
---
title: Note Title
tags: [tag1, tag2]
topic: folder/subfolder
status: draft        # draft | notes | complete
level: intermediate  # beginner | intermediate | advanced
related:
  - path/to/related.md
source: ""           # URL, book title, ISBN — omit if original notes
updated: YYYY-MM-DD
---
```

### Required fields

| Field | Description |
|---|---|
| `title` | Human-readable title |
| `tags` | Array of lowercase, hyphenated tags |
| `status` | Completeness of the note |
| `updated` | Date last meaningfully edited |

### Optional fields

| Field | Description |
|---|---|
| `topic` | Canonical location path — useful if file moves |
| `level` | Assumed reader knowledge level |
| `related` | Explicit cross-links to other notes |
| `source` | Attribution for reading notes |

## Tag Conventions

- Lowercase and hyphenated: `system-design`, not `System Design`
- Tags name a **facet shared across notes**, not the note's topic — a tag used by
  only one note restates the title and adds no navigational value
- Reuse the vocabulary below before coining a new tag; `scripts/lint-notes.py`
  warns on single-use tags
- New tags are welcome when a real cluster emerges (roughly two or more notes)

### Common tags

This is the active vocabulary in use, grouped by facet. Counts shift as notes are
added; the point is the shape, not the exact numbers.

**Architecture & systems**
`architecture`, `system-design`, `microservices`, `api-design`, `observability`, `performance`

**Delivery & practices**
`ci-cd`, `testing`, `code-review`, `refactoring`, `git`, `documentation`, `security`

**AI engineering**
`ai-engineering` (umbrella — pair it with a sub-facet), `agentic-workflows`

**Process & governance**
`governance`, `decision-making`

**People & culture**
`leadership`, `communication`, `culture`

**Languages** (seed tags — extend as language notes appear)
`typescript`

**Meta**
`meta`, `reading`

## File Naming

- Lowercase and hyphenated: `event-driven-architecture.md`
- Descriptive but concise: prefer `cap-theorem.md` over `notes-on-cap.md`
- Each folder has a `README.md` as its index

## Status Lifecycle

```
draft → notes → complete
```

- **draft** — placeholder or rough capture, may be incomplete
- **notes** — useful content but not polished
- **complete** — well-structured, reviewed, cross-linked

## Filtering

```bash
# Find all draft notes
grep -rl "status: draft" .

# Find notes by tag
grep -rl "distributed-systems" .

# Find all reading notes
grep -rl "tags:.*reading" .

# Find stale notes (not updated in a while)
grep -rl "updated: 2024" .
```
