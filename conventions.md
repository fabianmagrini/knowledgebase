---
title: Knowledge Base Conventions
tags: [meta]
status: complete
updated: 2026-06-13
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

- Lowercase and hyphenated: `distributed-systems`, not `Distributed Systems`
- Prefer specific over generic: `event-driven` over `architecture`
- Use consistent vocabulary — see common tags below

### Common tags

**Engineering domains**
`architecture`, `distributed-systems`, `system-design`, `microservices`, `event-driven`,
`messaging`, `databases`, `api-design`, `observability`, `security`, `performance`

**Practices**
`testing`, `ci-cd`, `code-review`, `refactoring`, `debugging`, `documentation`

**Concepts**
`algorithms`, `data-structures`, `concurrency`, `networking`, `caching`, `consistency`

**Tools & platforms**
`docker`, `kubernetes`, `aws`, `gcp`, `azure`, `terraform`, `git`

**Languages**
`go`, `python`, `typescript`, `java`, `rust`, `sql`

**AI engineering**
`ai-engineering`

**People & culture**
`leadership`, `culture`, `communication`

**Meta**
`meta`, `reading`, `paper`, `book`, `talk`

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
