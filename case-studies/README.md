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
- [OpenAI's Agent-First Harness](openai-agent-first-harness.md) — five months shipping an internal product with zero manually-written code (~1M lines, ~1,500 PRs, self-reported): agent legibility as the organising principle, the repository as system of record, a ~100-line AGENTS.md table of contents, mechanically-enforced layered architecture, and linters whose error messages carry the fix
- [Intercom's AI PR Approval](intercom-ai-pr-approval.md) — AI auto-approving ~19% of PRs with no human reviewer: sub-agents per review dimension, execution-path tracing, accountability moving from reviewer to author, the refusal to approve large changes as the actual safety mechanism, and why the headline 10x revert-rate gap compares the wrong variables
- [Rootly Dropped Its Small-PR Rule](rootly-pr-size-risk-labels.md) — retiring a two-year small-PR rule once agents authored 80%+ of the code: risk labels in place of diff-size limits, an AI reviewer that assigns a risk classification rather than style feedback, feature flags moving the safety gate from merge-time to progressive rollout, and a PR template demanding a revert plan
- [Zalando's Client-Side Load Balancing](zalando-client-side-load-balancing.md) — moving ~1M req/s off a shared edge load balancer into the calling process: watch-based discovery, consistent hashing with hash parity, occupancy (Little's Law) as the load signal, N-ring fade-in, bounded-load walk, and the cache-locality-vs-zone-cost trade-offs
- [Oracle AI Agent Memory](oracle-ai-agent-memory.md) — a governed, unified memory core for AI agents on a single database: the extract→enrich→store→retrieve pipeline, hybrid (vector + keyword + RRF) recall, conversation/session/user/org lifetime layers with TTL, a typed memory graph, and provenance/audit as the enterprise differentiator ("memory with receipts")
- [Netflix's Service Topology at Scale](netflix-service-topology.md) — a real-time service dependency graph from millions of flow records/sec: three physical layers, a three-stage aggregation pipeline whose load-bearing step resolves network intermediaries into true application edges, consistent-hashing load distribution against 100x hot nodes, immutable-snapshot time travel, and the cascading-bottleneck lessons
- [Slack AI's Path to Multi-Cloud](slack-ai-multi-cloud.md) — four phases from SageMaker to AWS+GCP: the capacity economics of provisioned vs on-demand throughput and the spillover pattern between them, an intelligent routing layer with circuit breakers and a backup model per feature, the API normalisation layer that is the real price of provider agnosticism, and the operational costs (cost attribution, on-call knowledge gaps) they admit to
- [Slack's Agentic E2E Testing Experiment](slack-agentic-e2e-testing.md) — a measured experiment on where AI agents fit in the E2E testing stack: goal-based vs journey-based testing, three execution models (Playwright MCP / CLI / generated tests) compared across 200+ runs, and the cost/reliability/token trade-offs that put agents at the apex of the pyramid rather than replacing deterministic tests
