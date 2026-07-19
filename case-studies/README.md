---
type: index
title: Case Studies
description: "Deep-dives into how real-world production systems and teams are built, and why."
tags: [meta]
status: complete
updated: 2026-06-22
---

# Case Studies

Deep-dives into how real-world production systems **and teams** are built, and
why. Each note analyses a specific company's engineering or organisational
approach, extracting the generalisable patterns behind it rather than treating it
as a one-off.

These differ from [Reading](../reading/) notes: a case study is a substantive
analysis of a specific company or system, not a one-line citation of an article.

## Notes

- [Linear's Performance Architecture](linear-performance-architecture.md) — how Linear achieves perceived speed by treating the browser as the database and the server as a sync target: local-first sync engine, optimistic updates, granular reactivity, and disciplined build/load/animation choices
- [ChatGPT's Web Performance Architecture](chatgpt-web-performance.md) — the architectural opposite of Linear, driven by serving ~1B anonymous users: streaming SSR, render-first, server-evaluated inlined flags, deferred imports until composer TTFI, prepaid bot defence, and "the network is the enemy" startup discipline
- [The Product Engineer Company (Portkey)](portkey-product-engineer-company.md) — Portkey's product-engineer operating model (24 engineers, 0 PMs, 1 designer): end-to-end ownership, the barbell structure, disciplined scope, and how AI factors into reliability-critical infrastructure work
- [Cloudflare's AI Code Review System](cloudflare-ai-code-review.md) — a production multi-agent review system (131K reviews/month): seven specialised reviewers plus a judge, "What NOT to Flag" negative prompting, risk/model tiering, and the cost/resilience engineering behind it
- [Microsoft's AI Strategy — Finding Core Competencies (Nadella)](microsoft-ai-core-competency.md) — a corporate-strategy case study from Satya Nadella's Stratechery interview: core-competency discipline, the hill-climbing machine and private evals as moat, three-bucket capital allocation, token capital, consumption pricing, and model/harness independence
- [DoorDash's AI Code Reviewer](doordash-ai-code-review.md) — a production AI review agent optimised for precision over recall: the lead-scout→deep-reviewer (notice-then-verify) architecture, company-mined domain review profiles, the three-part false-positive filter and "disprove-it pass", and acceptance rate (not findings count) as the success metric
- [Zalando's Client-Side Load Balancing](zalando-client-side-load-balancing.md) — moving ~1M req/s off a shared edge load balancer into the calling process: watch-based discovery, consistent hashing with hash parity, occupancy (Little's Law) as the load signal, N-ring fade-in, bounded-load walk, and the cache-locality-vs-zone-cost trade-offs
- [Oracle AI Agent Memory](oracle-ai-agent-memory.md) — a governed, unified memory core for AI agents on a single database: the extract→enrich→store→retrieve pipeline, hybrid (vector + keyword + RRF) recall, conversation/session/user/org lifetime layers with TTL, a typed memory graph, and provenance/audit as the enterprise differentiator ("memory with receipts")
