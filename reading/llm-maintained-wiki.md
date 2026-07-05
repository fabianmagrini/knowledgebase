---
title: The LLM-Maintained Wiki (Karpathy)
tags: [ai-engineering, documentation, agentic-workflows, reading]
topic: reading
status: notes
level: intermediate
related:
  - standards/open-knowledge-format.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/modern-engineering-values.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/ai-native-engineering-overview.md
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
updated: 2026-06-27
---

# The LLM-Maintained Wiki (Karpathy)

Notes on Andrej Karpathy's *LLM Wiki* pattern. The proposal: rather than a
retrieval system (RAG) that rediscovers answers from raw documents on every query,
have an LLM **compile knowledge once and then keep it current** — a persistent,
compounding wiki that sits between you and your sources and whose synthesis
improves with each new source.

## The core argument

- **Bookkeeping is the hard part.** Humans abandon wikis because the upkeep —
  updating cross-references, flagging contradictions, keeping pages consistent —
  grows faster than the value. This is "the load-bearing insight".
- **LLMs don't get bored**, so that maintenance cost falls towards zero, which is
  exactly what made human-maintained knowledge bases collapse.
- **Division of labour:** humans *curate sources and ask questions*; the LLM does
  *everything else* — synthesis, entity pages, cross-links, consistency. The system
  shifts from a search index to an evolving synthesis engine.

## Three-layer architecture

| Layer | What it is |
|---|---|
| **Raw sources** | Immutable, curated inputs — articles, papers, images |
| **The wiki** | LLM-generated markdown: summaries, entity pages, cross-references, an index and a log |
| **The schema** | Configuration (e.g. a `CLAUDE.md`) specifying the wiki's conventions and workflows |

## Three operations

- **Ingest** — process *one source at a time*; the LLM reads it and updates ~10–15
  wiki pages plus the index and log.
- **Query** — search wiki pages and synthesise an answer *with citations*; file
  good answers back into the wiki as new pages.
- **Lint** — health-check for contradictions, stale claims, orphan pages, broken
  links, and data gaps.

Two mental models Karpathy offers: *"the wiki is the IDE; the LLM is the
programmer"*, and the wiki as a **persistent, compounding artifact** — richer and
more reliable than chat history, cheaper to maintain than human-edited docs.

## Lineage and tooling

The pattern revives Vannevar Bush's 1945 **Memex** — associative trails between
documents mattering as much as the documents — which foundered on the maintenance
problem LLMs now dissolve. Karpathy's example stack: **Obsidian** (+ Web Clipper)
to browse and clip, **qmd** for hybrid BM25/vector local search over MCP,
**Dataview** for queries over frontmatter, **Marp** for slides, and **Git** for
versioning the markdown. These are one concrete instantiation, not the pattern
itself.

## This knowledge base as an instance

This repository is a (human-curated, LLM-assisted) example of the pattern, which
makes the mapping a useful lens:

| Karpathy's layer/operation | Here |
|---|---|
| Schema | `conventions.md` + `AGENTS.md` |
| Wiki | the notes and folder `README.md` indexes |
| Ingest | the `consider-article` workflow (one source → new/edited notes + cross-links) |
| Lint | `scripts/lint-notes.py` and the relative-link integrity check |

The differences are honest ones: here a human still approves every page and writes
the synthesis, where Karpathy pushes for the LLM to own maintenance end-to-end.

## Relationship to other notes

- [Open Knowledge Format (OKF)](../standards/open-knowledge-format.md) — a portable
  *format* for agent-consumable knowledge; this note is the *maintenance pattern*
  that would produce and curate such knowledge.
- [The Agentic SDLC](../engineering/ai-native/agentic-sdlc.md) — its Context
  Development Lifecycle (curate, version, prune context) is the same discipline
  applied to an agent's working context rather than a personal wiki.
- [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md)
  — "context in the repo" as a value; the LLM wiki is that idea taken to a
  standalone knowledge artifact.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the
  wiki-vs-RAG contrast is a memory-architecture choice: a compiled, maintained
  store rather than retrieval over raw documents.
