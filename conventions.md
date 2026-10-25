---
type: reference
title: Knowledge Base Conventions
description: "The knowledge base's own conventions: frontmatter schema, OKF concept types, tag vocabulary, file naming, and the status lifecycle."
tags: [meta]
status: complete
updated: 2026-07-11
---

# Conventions

## Frontmatter Schema

Every note should include YAML frontmatter at the top:

```yaml
---
type: note           # note | index | overview | case-study | reading | reference
title: Note Title
description: "One-line summary — what this concept is, for humans and agents."
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
| `type` | OKF concept type (see below) |
| `title` | Human-readable title |
| `tags` | Array of lowercase, hyphenated tags |
| `status` | Completeness of the note |
| `updated` | Date last meaningfully edited |

### Recommended fields

| Field | Description |
|---|---|
| `description` | One-line summary of the concept, readable by humans and parseable by agents |

### Optional fields

| Field | Description |
|---|---|
| `topic` | Canonical location path — useful if file moves |
| `level` | Assumed reader knowledge level |
| `related` | Explicit cross-links to other notes |
| `source` | Attribution for reading notes |

## Concept Types (OKF)

This knowledge base follows the [Open Knowledge Format](standards/open-knowledge-format.md):
every concept carries a `type`. The controlled vocabulary:

| Type | Used for |
|---|---|
| `note` | A standard content note (the default) |
| `index` | A folder `README.md` — the directory's index / progressive-disclosure entry |
| `overview` | A thematic map that orients a cluster of notes (`*-overview.md`) |
| `case-study` | A deep-dive into a specific company or production system (`case-studies/`) |
| `reading` | A summary anchored to one external source (`reading/`) |
| `reference` | A specification, standard, or the conventions themselves (`standards/`) |

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
draft → notes          (content notes)
complete               (hub documents)
```

- **draft** — a rough capture that is not yet usable: a stub, an unplaced idea, or a
  note whose claims have not been checked. Promote to `notes` as soon as it is useful
  to a reader, which is usually the same sitting.
- **notes** — **the normal and expected state for a content note**, however polished.
  A note being well-structured, verified and cross-linked does not move it off `notes`;
  that is simply what a note here looks like.
- **complete** — reserved for **hub documents**: folder `README.md` indexes,
  `type: overview` maps, and the meta files (`conventions.md`, root `README.md`). These
  have a definition of done — they describe a cluster, and they are either current or
  they are not.

> **Why `complete` is not a content state.** A structure review in October 2026 measured
> **19** files at `complete`, all of them indexes and meta documents, and **zero** of 198
> content notes. A terminal state nothing reaches is not a lifecycle stage; it is a label
> nobody can apply. Rather than invent criteria for promoting notes, the vocabulary now
> matches observed use: notes live at `notes`, hubs are `complete` or stale.
>
> The practical consequence is that `status` is a **signal about hub freshness** plus a
> *"don't trust this yet"* flag on drafts. It is not a quality grade, and
> `grep -rl "status: draft"` is the only query it needs to serve well.

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
