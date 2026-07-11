---
type: index
title: Knowledge Base
description: "Personal engineering knowledge base."
tags: [meta]
status: complete
updated: 2026-07-11
---

# Knowledge Base

Personal engineering knowledge base — a version-controlled directory of Markdown notes,
cross-linked into an implicit knowledge graph, readable by humans and parseable by agents.

## Structure

- [Engineering](engineering/) — architecture, system design, patterns, practices, AI-native engineering
- [Leadership](leadership/) — leadership, communication, decision governance, culture
- [Product](product/) — product management and discovery
- [Languages & Frameworks](languages-and-frameworks/) — programming language and framework notes
- [Tools](tools/) — CLI tools, editors, platforms, infrastructure
- [SRE](sre/) — site reliability, incident response, operations
- [Standards](standards/) — specifications, protocols, and formats
- [Concepts](concepts/) — algorithms, data structures, CS fundamentals
- [Case Studies](case-studies/) — deep-dives into how real-world production systems are built
- [Reading](reading/) — notes from books, papers, and articles

## Open Knowledge Format

This knowledge base conforms to the [Open Knowledge Format (OKF)](standards/open-knowledge-format.md) —
Google Cloud's open, vendor-neutral specification for the internal knowledge that AI agents and
foundation models consume. In OKF terms the whole repository is an **OKF bundle**: a directory of
Markdown concepts, each `type`-tagged YAML frontmatter plus a body, cross-linked into a graph.

- **Every concept carries a `type`** — OKF's one required field: `note`, `index` (folder READMEs),
  `overview` (thematic maps), `case-study`, `reading`, or `reference`.
- **Every concept carries a one-line `description`** — a summary readable by humans and parseable
  by agents.
- **The file path is the concept's identity**, and Markdown/`related:` cross-links form the graph.
- **Folder `README.md` files** act as the OKF `index` for progressive disclosure of each directory.

The frontmatter schema and the full `type` vocabulary live in
[Conventions](conventions.md); `scripts/lint-notes.py` enforces both. OKF is v0.1 and vendor-introduced,
so this is a pragmatic alignment rather than a claim of a settled standard — see the
[OKF note](standards/open-knowledge-format.md) for the caveats.

## Meta

- [Conventions](conventions.md) — knowledge base conventions, frontmatter schema, OKF types, and tags

