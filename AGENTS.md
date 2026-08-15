# AGENTS.md

Guidance for AI agents working in this repository.

## What this repository is

A personal engineering knowledge base composed entirely of Markdown files. There is no build system, test suite, or runtime. The primary tasks here are creating, editing, linking, and organising notes.

## Conventions

All conventions are documented in [conventions.md](conventions.md). Read it before creating or editing notes. Key points:

- Every `.md` file must include YAML frontmatter with `type`, `title`, `tags`, `status`, and `updated` (and a recommended one-line `description`)
- `type` is the [OKF](standards/open-knowledge-format.md) concept type: `note` | `index` (folder READMEs) | `overview` (thematic maps) | `case-study` | `reading` | `reference`
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
type: note
title: 
description: ""
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

`source` records **where the material canonically lives, not how you happened to read it**. If a URL was given, that URL is the `source` — even if the content was actually read from a saved PDF, a local file, a mirror, a cached copy, or a reader view. Never put a machine-local path (`~/Downloads/…`, `/Users/…`) in `source`; those are meaningless to anyone else and break as soon as the file moves. A local path belongs there only when there is genuinely no URL behind the material.

Where a piece is published in more than one canonical place, prefer the more durable one and record the other alongside it — a personal domain generally outlasts a newsletter platform.

## Considering a source: note, fold, or cite

Not every worthwhile article earns a note. Before writing one, check whether the URL is already a `source:` anywhere (`grep -rn "<url-or-domain>" --include='*.md' .`) — repeats and cross-posts are common — then pick one of four outcomes:

| Outcome | When |
|---|---|
| **New note** | It carries an argument, framework, or evidence the repo does not hold, at an altitude no existing note occupies |
| **Fold into an existing note** | The core claim is already held and the source adds a section's worth — a mechanism, a caveat, a second data point. Prefer this to a near-duplicate note; a cluster with three overlapping notes on one idea is a link dump, not a map |
| **Cite in `reading/README.md`** | On-topic and worth being findable, but the argument is covered in more depth elsewhere here. Record what it *does* add and state why there is no note, so the decision reads as deliberate rather than as an oversight |
| **Skip** | Thin, off-topic, or resting on a contested claim that a neutral summary would launder into the repo's voice |

Two habits that make the judgement easier:

- **Say what is genuinely new, out loud, before writing.** If the honest answer is one idea, that is a fold or a citation.
- **Note the provenance, always.** Vendor marketing, an author restating their own back catalogue, self-reported metrics, a sponsored post, or a single practitioner's experience are all publishable — they just need saying in the note rather than being smoothed into neutral prose.

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

Hub notes are the exception: folder `README.md` indexes and `type: overview` maps link *down* to a whole cluster, and the spokes are not expected to link back. `scripts/lint-notes.py` exempts them from the reciprocity check for this reason.

## Reviewing the structure

Adding notes one at a time optimises each note locally. Structural problems only appear in aggregate — a folder quietly reaching 35 notes, a lint rule generating 90% noise, a topic stuck at two notes while an adjacent one has thirty. Nothing in the per-note workflow surfaces these, so review the shape of the repository periodically: after a run of additions, or when a cluster visibly shifts.

**Measure, don't guess.** Read the actual files before asserting a problem — a finding inferred from a `grep` excerpt is how you end up "fixing" something that was already fine.

```bash
# Notes per folder — look for imbalance, not absolute size
for d in engineering/* leadership product languages-and-frameworks tools sre standards concepts case-studies reading drafts; do
  [ -d "$d" ] && printf "%-32s %s\n" "$d" "$(ls "$d"/*.md 2>/dev/null | grep -vc README)"
done

# Where lint warnings actually come from — a few files dominating means the rule is wrong, not the notes
python3 scripts/lint-notes.py 2>&1 | grep -E '^WARN  [^ ]+\.md:' | sed -E 's/^WARN  ([^:]+):.*/\1/' | sort | uniq -c | sort -rn

# Status spread — if almost everything sits at one value, the lifecycle isn't discriminating
grep -rh "^status:" --include='*.md' . | sort | uniq -c | sort -rn
```

What to look for, and the bias to apply:

- **Folder balance** — a large folder is fine if its `README.md` is sectioned and its overview map is current. Prefer sectioning an index over splitting a folder: moving notes rewrites hundreds of relative links for little navigational gain.
- **Content gaps** — a topic repeatedly referenced from other notes but with no home of its own.
- **Linter signal-to-noise** — if most warnings come from a handful of files, question the rule before editing the notes.
- **Conventions still serving** — a status value nothing reaches, a folder nothing is filed in, a tag that never became a cluster.

Rank findings by fix-cost against value, and prefer changes that don't touch note content.
