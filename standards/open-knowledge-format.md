---
title: Open Knowledge Format (OKF)
tags: [ai-engineering, documentation, reading]
topic: standards
status: notes
level: intermediate
related:
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/modern-engineering-values.md
  - engineering/practices/loop-driven-development.md
  - engineering/practices/ai-native-engineering-stack.md
  - reading/llm-maintained-wiki.md
source: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/"
updated: 2026-06-14
---

# Open Knowledge Format (OKF)

OKF is an open, vendor-neutral specification (introduced by Google Cloud) for representing and
sharing the internal knowledge — metadata, context, documentation — that AI agents and foundation
models need. The central argument is that knowledge should be a portable, interoperable **format**
rather than something locked inside a platform: "a bundle of OKF documents is just markdown, just
files, just YAML frontmatter."

## The problem it addresses

Organisational knowledge is scattered across incompatible surfaces — metadata catalogs with
proprietary APIs, wikis, shared drives, code comments, notebooks, and "the heads of senior
engineers." When an agent needs to answer "how do I compute weekly active users from our event
stream?", it must reassemble the answer from mutually incompatible sources. So every agent builder
re-solves context assembly, every catalog vendor reinvents the same data models, and knowledge
stays locked behind whichever tool created it. The missing piece is not another service but a
format that anyone can produce without SDKs, consume without integrations, keep in version control
alongside code, and that is readable by humans *and* parseable by agents from the same file.

## How it works

An **OKF bundle** is a directory of markdown files, each representing a **concept** (a table,
dataset, metric, playbook, runbook, API). The file path is the concept's identity, and markdown
cross-links between files form an implicit knowledge graph.

```
sales/
├── index.md
├── tables/
│   ├── orders.md
│   └── customers.md
└── metrics/
    └── weekly_active_users.md
```

Each document is **YAML frontmatter + a markdown body**:

```yaml
---
type: BigQuery Table          # the only required field
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?...
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---

# Schema
| Column | Type | Description |
|--------|------|-------------|
| order_id | STRING | Globally unique order identifier. |
```

Optional `index.md` files give progressive disclosure of a directory; optional `log.md` files
record change history.

## Three design principles

1. **Minimally opinionated.** The only requirement is a `type` field on every concept. Producers
   decide what types exist, what other fields to add, and how to structure the body. The spec
   defines the *interoperability surface*, not the content model.
2. **Producer/consumer independence.** The format is the contract; tooling is swappable. A
   human-authored bundle can be consumed by an agent; a metadata pipeline's export can be browsed
   in a visualiser; one model can synthesise a bundle that another model queries.
3. **Format, not platform.** Vendor-, cloud-, database- and model-agnostic; no proprietary
   accounts or SDKs. The value comes from adoption, not ownership.

## Reference implementations

Google shipped, as living examples: a **producer** enrichment agent that walks BigQuery datasets
and drafts an OKF concept per table (with a second LLM pass adding citations, schemas, and join
paths); a **consumer** static-HTML visualiser that renders any bundle as an interactive graph with
no backend; and sample bundles (GA4 e-commerce, Stack Overflow, Bitcoin public datasets). Google
Cloud's Knowledge Catalog now ingests OKF and serves it to agents.

> Andrej Karpathy's point, cited in support: LLMs "don't get bored, don't forget to update a
> cross-reference, and can touch 15 files in one pass" — they are good at exactly the bookkeeping
> that makes humans abandon wikis.

## Relation to adjacent ideas

OKF formalises the **"LLM-wiki" pattern** that already appears in bespoke forms — Obsidian vaults,
`AGENTS.md` / `CLAUDE.md` conventions, metadata-as-code repositories, `index.md` / `log.md`
artifacts — none of which were designed to interoperate. It overlaps with **metadata catalogs**
(replacing vendor-locked APIs with a portable format), **semantic layers** (join paths, metric
definitions), **knowledge graphs** (the cross-links are RDF-like), and **infrastructure-as-code**
(git-friendly, versioned).

### Seen in practice

This knowledge base is itself an instance of the same pattern: a version-controlled directory of
markdown files with YAML frontmatter (`title`, `tags`, `topic`, `status`, `related`), cross-linked
into an implicit graph, with `AGENTS.md` / `CLAUDE.md` conventions — exactly the bespoke "LLM-wiki"
shape OKF aims to standardise.

### Caveat

OKF is **v0.1** and explicitly a starting point, introduced by a single vendor (Google). It is an
open specification, but its value depends entirely on how many independent producers and consumers
adopt it; treat it as a promising convention to watch rather than a settled standard.

## Relationship to other notes

- [The Agentic SDLC](../engineering/practices/agentic-sdlc.md) — its *Context Development
  Lifecycle* ("managing context is as important as managing source code") is the practice OKF
  gives a concrete, portable format for.
- [Modern Engineering Values](../engineering/practices/modern-engineering-values.md) — the
  *context in the repo* value; OKF is a standardised way to externalise that context.
- [Loop-Driven Development](../engineering/practices/loop-driven-development.md) — *context
  engineering* and skills as `SKILL.md`; OKF concepts are a parallel knowledge surface for agents.
- [The AI-Native Engineering Stack](../engineering/practices/ai-native-engineering-stack.md) — OKF
  sits at the knowledge/context layer agents read from.
