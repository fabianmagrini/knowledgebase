---
type: case-study
title: Oracle AI Agent Memory
description: "how Oracle builds a governed, unified memory core for AI agents on a single database: the extract→enrich→store→retrieve pipeline, hybrid (vector + keyword + RRF) recall, conversation/session/user/org lifetime layers with TTL, a typed memory graph, and provenance/audit as the enterprise differentiator (\"memory with receipts\")"
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/cress-context-engineering.md
  - engineering/ai-native/harness-engineering.md
source: "https://blogs.oracle.com/developers/whats-new-in-oracle-ai-agent-memory-custom-extraction-hybrid-search-and-more-control"
updated: 2026-07-19
---

# Oracle AI Agent Memory

A case study of **Oracle AI Agent Memory** — Oracle's memory subsystem for AI
agents, built on Oracle AI Database and marketed as a *governed, unified memory
core for enterprise agents*. Where [Long-Running Agents](../engineering/ai-native/long-running-agents.md)
argues that persistent agency needs "memory governed like microservices" but
leaves the subsystem abstract, this note examines one concrete implementation of
that memory layer.

The **26.6 release** ("Memory With Receipts") is the anchor: it adds custom
extraction, hybrid search, in-database embeddings, and full lifecycle control. All
capability and design claims here are Oracle's own, self-reported. *Access
caveat:* the primary announcement is behind an anti-bot block (HTTP 403), so the
mechanics below are reconstructed from Oracle's surrounding posts and a community
deep-dive of the underlying technique — treat specific internals (edge tables,
embedding dimensions, the layer table) as illustrative of the approach rather than
a guaranteed description of the shipped product surface.

## The distinctive stance: one database, not a memory stack

Oracle's central pitch is **consolidation**. Rather than assembling agent memory
from a vector database + a state store + a retrieval service + its own backup
pipeline, everything lives in a single Oracle AI Database instance: vector search,
structured state, JSON document retrieval, transactional consistency, keyword
search, hybrid indexes, retention controls, deletion workflows, and
database-native audit. Oracle's framing — "no second vector database, third
service to monitor, or fourth backup pipeline" — is a vendor claim, but it names a
real architectural fork: **agent memory as a bolted-together stack vs. a governed
single store**.

## The entity model

The 26.6 release exposes full CRUD over five first-class entities:

| Entity | Role |
|---|---|
| **Thread** | A conversation / interaction container |
| **Message** | An individual turn within a thread |
| **Memory** | A durable extracted fact, preference, or record |
| **User profile** | Accumulated per-user state and preferences |
| **Agent profile** | Per-agent configuration and accumulated state |

Underneath, a **memory** is a database row: a unique id, user/agent **scope**
identifiers, the content (CLOB), JSON metadata, a vector embedding (community
sources describe 384-dimensional float32), lifecycle timestamps
(created / updated / accessed), and an access-frequency counter. A separate
**edge table** records typed relationships between memories — `related`,
`same_as`, `supersedes`, `contradicts` — making the store a **memory graph**, not
a flat bucket.

## Memory by lifetime

Oracle separates **short-term** memory (keeping the active conversation compact
via summaries and "context cards") from **long-term** memory (durable facts,
preferences, and records reusable across sessions). The underlying technique
layers memory by expected lifetime:

| Layer | Scope | Lifetime |
|---|---|---|
| Conversation | run id | Short-lived, near-immediate expiry |
| Session | user id + run id | Working context |
| User | user id | Durable preferences |
| Org | app / org id | Team conventions, longest-lived |

**TTL** support underpins this: default retention periods, per-record overrides,
and expiration-aware retrieval so stale records fall out of results.

## Memory formation: the extraction pipeline

Memory is treated as a **pipeline, not a write**. Raw messages are not stored
verbatim as "memory"; they pass through enrichment — normalisation,
deduplication, embedding generation, and classification — before becoming durable
memories.

- **Custom extraction** (new in 26.6) lets developers supply domain-aware
  instructions that control *what* is worth extracting and *how* it is stored,
  making memory formation domain-specific rather than one-size-fits-all.
- **In-database embeddings** via `OracleDBEmbedder` generate vectors inside the
  database, removing an external network hop and reducing extraction latency —
  Oracle cites this as part of a broader latency improvement.

## Retrieval: hybrid recall fused by rank

Retrieval is deliberately **not** vector-only. Oracle's `DBMS_HYBRID_VECTOR.SEARCH`
runs vector similarity and Oracle Text keyword search **in parallel** and fuses
them with **Reciprocal Rank Fusion (RRF)** — RRF ranks each result by its
*position* in each list rather than trying to normalise two incompatible scoring
systems.

The rationale is that agent memory is full of tokens where lexical exactness
matters and embeddings blur: identifiers, commands, error strings, flags, paths,
package names, ticket numbers. The broader technique layers even more signals into
the final ranking:

- **Vector similarity** — paraphrases and semantic variants.
- **Oracle Text (lexical)** — exact identifiers, commands, error strings.
- **Entity overlap** — durable anchors (package names, paths, tickets).
- **Graph expansion** — related memories reached by edge traversal.
- **Recency / importance** — timestamp and explicit priority.

Component scores are **preserved** in the final result for explainability, rather
than being collapsed into one opaque number.

## Governance: "memory with receipts"

The release name is the thesis: governance is the enterprise differentiator, not a
footnote. The system layers **retention rules, provenance tracking, redaction
strategies, and approval workflows** over the same store, plus database-native
audit and explicit deletion workflows. Provenance ("receipts") is assembled from
access timestamps and counts, the score components behind a retrieval, and
relationship metadata — so a memory's presence and its retrieval can be explained
and audited. Full CRUD over threads, messages, memories, and profiles closes the
loop: what gets stored, retrieved, updated, and injected back into agent context
is all controllable.

## Generalisable patterns

Beyond the Oracle specifics, the design encodes several patterns for any agent
memory subsystem:

1. **Memory is a pipeline** — extract → enrich (normalise / dedup / embed /
   classify) → store → retrieve → inject. *Custom extraction* is domain-aware
   formation at the front of that pipeline.
2. **Hybrid retrieval beats vector-only** — fuse semantic (vector) and exact
   (keyword) recall by **rank** (RRF), because agent memory carries identifiers and
   error strings that embeddings smear together.
3. **Scope memory by lifetime** — conversation / session / user / org layers with
   TTL bound context and cost, and counter the **memory drift** that
   [Long-Running Agents](../engineering/ai-native/long-running-agents.md) warns
   about.
4. **Memory as a typed graph** — `supersedes` / `contradicts` edges let the store
   resolve stale and conflicting facts instead of silently accumulating
   contradictions.
5. **Governance is the moat** — provenance, audit, retention, and redaction
   ("receipts") are what move a memory store from a demo to something an
   enterprise will run.

## Relationship to other notes

- [Long-Running Agents](../engineering/ai-native/long-running-agents.md) — argues
  persistent agents need curated, governed long-term memory to avoid drift; this is
  a concrete memory subsystem built to that brief.
- [CRESS Principles for Context Engineering](../engineering/ai-native/cress-context-engineering.md)
  — memory retrieval is *how* Current, Small, and Specific context gets selected
  and injected; hybrid recall + TTL is the selection mechanism behind those
  properties.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — memory
  is one of the harness's core components; this shows a productised version of it,
  externalised into a database rather than the agent process.
