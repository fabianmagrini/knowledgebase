---
title: Cloudflare's AI Code Review System
tags: [ai-engineering, code-review, agentic-workflows, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-code-review.md
  - reading/building-effective-agents.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - case-studies/doordash-ai-code-review.md
  - reading/multi-agent-coding-coordination.md
  - engineering/ai-native/ai-native-engineering-overview.md
source: "https://blog.cloudflare.com/ai-code-review/"
updated: 2026-06-27
---

# Cloudflare's AI Code Review System

A Cloudflare engineering case study of a production AI code-review system — 131,246
reviews across 48,095 merge requests in a single month. It is the concrete,
operational counterpart to the principles in
[Agentic Code Review](../engineering/ai-native/agentic-code-review.md): where that
note argues *why* review is the bottleneck and how to tier it, this shows one team
*building* it at scale. The metrics are Cloudflare's own and self-reported.

## Architecture

A CI-native orchestration that replaces a single monolithic reviewer with
**specialised sub-agents coordinated by a judge** — the orchestrator–workers and
evaluator patterns from [Building Effective Agents](../reading/building-effective-agents.md)
applied to review.

- **Up to seven concurrent reviewers** — security, performance, code quality,
  documentation, release, compliance, and an `AGENTS.md` reviewer — each launched
  in its own session with a specialised prompt via the OpenCode SDK.
- **A judge/coordinator agent** dedupes findings and decides approval. It runs the
  hardest reasoning, so it gets the top-tier models.
- **Structured findings** returned as XML with severity (critical / warning /
  suggestion).
- **Plugin system** — domain logic isolated behind interfaces; GitLab coupling
  lives in one config file; providers and models are swappable without core
  changes.
- **Control plane** — a Cloudflare Worker + KV serves runtime config; disabling a
  provider filters it from model selection within ~5 seconds, no redeploy. This is
  a literal instance of the [CI/CD control plane](../engineering/ai-native/ci-cd-ai-engineering.md)
  idea.

## The load-bearing insight: "What NOT to Flag"

The article's central engineering claim is that the value lives in **negative
prompting**. Generic LLM review produces a firehose of warnings; tight,
domain-scoped *"What NOT to Flag"* sections are what make it usable. The security
reviewer explicitly ignores "theoretical risks" and "defense-in-depth
suggestions". Scoping, not raw model power, is what controls false positives.

## Risk and model tiering

Cost and agent count scale with diff size — the production form of
[risk-based tiering](../engineering/ai-native/agentic-code-review.md):

| Tier | Agents | Model tier | ~Cost |
|---|---|---|---|
| Trivial (≤10 lines) | 2 | Sonnet | ~$0.20 |
| Full | 7 | Opus | ~$1.68 |

Models are matched to job difficulty: top-tier (Opus 4.7 / GPT-5.4) for the
coordinator only; standard (Sonnet 4.6 / GPT-5.3 Codex) for the heavy lifting;
lightweight (Kimi K2.5) for text-heavy reviewers (docs, release). Using *different
model families* across agents is the same defence against correlated blind spots
that the principles note recommends.

## Trust and false positives

- **Judge re-reasoning** — when uncertain, the coordinator re-reads the source and
  uses tools to verify before deciding.
- **Biased toward approval** — a single warning in a clean MR yields
  *approved-with-comments*, not a block; only multiple warnings or critical items
  block merge.
- **Incremental re-reviews** — the system remembers prior findings and the
  developer's replies ("won't fix", "acknowledged", or a code disagreement) inform
  later passes.
- **"Break glass"** — commenting it forces approval (provider outages, urgent
  hotfixes); used on 0.6% of MRs and tracked in telemetry. This is the
  [escape hatch](../engineering/ai-native/harness-engineering.md) made operational.

## Economics and resilience

- **Token discipline** — a shared context file on disk (sub-reviewers read rather
  than duplicate MR metadata), per-file diffs read on demand, and an **85.7%
  prompt-cache hit rate**. Median review **$0.98** and **3m 39s**; ~120 billion
  tokens over 30 days.
- **Resilience** — per-tier circuit breakers, failback chains (Opus 4.7 → 4.6),
  coordinator-level model hot-swap on retryable errors, per-agent timeouts, and
  3-second status polling to catch silent crashes.
- **Hardening** — boundary-tag stripping on user input to prevent prompt injection;
  diff filtering that drops lock files, minified assets, and generated code (except
  migrations) before agents see it.

## Acknowledged limitations

The team is explicit that the system **does not**:

- understand system-design philosophy (no architectural awareness);
- verify cross-system impact (an API-contract change may break undiscovered
  consumers);
- catch subtle concurrency/race bugs that need timing, not static inspection;
- stay cheap on huge diffs (a 500-file refactor triggers a full seven-agent run).

These are exactly the "human-shaped gaps" the principles note assigns to the
human-on-the-loop.

## Relationship to other notes

- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — the
  principles (tiering, different model families, judge synthesis, escape hatch,
  human-on-the-loop) this system implements in production.
- [Building Effective Agents](../reading/building-effective-agents.md) — the
  orchestrator–workers + evaluator patterns the seven-reviewers-plus-judge design
  instantiates.
- [CI/CD as the Control Plane](../engineering/ai-native/ci-cd-ai-engineering.md) —
  the deterministic, CI-native gating the system plugs into.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the
  orchestration harness anatomy: sessions, tools, resilience, token management.
- [Multi-Agent Coding Without Worktree Chaos](../reading/multi-agent-coding-coordination.md)
  — a coordinated agent *swarm* for writing; this is the same shape for *reviewing*.
