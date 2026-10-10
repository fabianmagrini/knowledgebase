---
type: case-study
title: Cursor's Agent Swarm Economics
description: "A frontier planner over cheap workers at similar quality for a fraction of the cost, measured on a real oracle — plus a coordination failure-mode catalogue and the finding that 68,000 commits was thrash, not productivity."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - reading/multi-agent-coding-coordination.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - reading/building-effective-agents.md
  - engineering/ai-native/long-running-agents.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/ramp-inspect-agent-platform.md
  - case-studies/rootly-pr-size-risk-labels.md
  - reading/reactive-reducer-orchestration.md
  - engineering/ai-native/accountability-for-unread-code.md
  - case-studies/doordash-flag-cleanup-agents.md
  - case-studies/github-copilot-rust-migration.md
source: "https://cursor.com/blog/agent-swarm-model-economics"
updated: 2026-10-05
---

# Cursor's Agent Swarm Economics

Wilson Lin (Cursor, July 2026) reports on running coordinated swarms of coding agents, and
argues that **which model does which role matters more than how much frontier capacity you
buy**.

> **Read the provenance.** Cursor writing about Cursor's own swarm — and the cost-winning
> configuration runs **Cursor's own model (Composer 2.5) as the worker fleet** under a frontier
> planner. The headline finding is precisely the finding that sells Composer. The experimental
> setup below is unusually rigorous for this genre and the conclusion is not disinterested;
> both are true at once.

## The task, which is the best part of the setup

> "We instructed the new version of the swarm … to implement the whole of the 835-page SQLite
> manual in Rust. We withheld the source code, test suites, SQLite binary, and internet access."

Grading used **sqllogictest**, the SQLite project's own cross-engine suite — "millions of
queries with known correct answers, and the grade is the fraction the swarm's database gets
right."

That is a genuine green-or-red oracle rather than a rubric, which makes this stronger evidence
than most agent experiments recorded here —
[Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md)
concedes in its own note that its cost figures are firmer than its quality claims. The resulting
codebase is public at `github.com/cursor/minisqlite`.

## The economics

The claim: "every model mix produced similar quality while the costs varied enormously, from
**$1,339** for the Opus 4.8 hybrid to **$10,565** for GPT-5.5 alone."

Two different measurements, worth keeping distinct because the article reports both:

| Measure | GPT-5.5 for planners *and* workers | Opus 4.8 planner + Composer 2.5 workers |
|---|---|---|
| **Total run cost** | $10,565 | $1,339 |
| **Worker fleet alone** | $9,373 | $411 |

So roughly **8× on total cost and ~23× on the worker fleet**, at comparable quality. The
reasoning behind it is the line to carry:

> "Few moments in a large task genuinely require frontier intelligence, such as the original
> decomposition, the design decisions, and certain trade-offs."

**Why this is not the routing argument the repo already holds.**
[Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md) picks
the cheapest adequate model *per request*, judging each request on its own. This picks per
**role**, structurally and in advance: the planner is frontier because decomposition and design
coherence are where capability pays, and the workers are cheap because executing a
well-specified narrow task is not. The decomposition is what makes the cheap tier viable — it
manufactures work that does not need frontier intelligence.

Reported configurations also included Grok 4.5 for both roles (~80% of the suite in four hours)
and a Fable 5 + Composer 2.5 mix (~73–85% at the four-hour mark, costing more than the Opus
hybrid).

## Commit volume as an anti-metric

The most transferable result, comparing their old harness against the new one on Grok 4.5:

| | Old harness | New harness |
|---|---|---|
| Commits in 2 hours | **68,000** | ~971 |
| Merge conflicts | 70,000+, accelerating | <1,000 over 4 hours |
| Conflicts in the hottest file | 7,771 | 47 |
| Final codebase (Fable 5 mix) | 64,305 LOC | 9,908 LOC |

The 70× commit difference is attributed to **thrash, not productivity** — agents overwriting
each other and re-solving the same problems. Same task, and the quieter run produced a codebase
**six times smaller**.

This is worth holding beside the authorship figures accumulating in these notes —
[Ramp's 75% of merged PRs](ramp-inspect-agent-platform.md),
[Rootly's 80%+](rootly-pr-size-risk-labels.md),
[OpenAI's zero manually-written lines](openai-agent-first-harness.md). Those are volume counts
that say nothing about value. Here is the same ambiguity with the sign actually measured: **more
output was strictly worse**, and the metric that looked like productivity was the symptom.

## The failure-mode catalogue

What breaks at swarm scale, and the remedies offered. Several of these have no name anywhere
else in these notes:

| Failure mode | What it is | Remedy offered |
|---|---|---|
| **Split-brain design** | Uncoordinated planners independently designing the same region | Planners own design decisions; prompts enforce non-overlapping subtrees |
| **Planner contention** | Planners disagreeing about shared structure | Shared design docs with compile-checked references |
| **Megafiles** | Files growing until they become the contention point | Worker-flagged bloat triggers automatic decomposition |
| **Ossification** | Agents learning *not* to touch core systems, so defects calcify | "Licensed intentional breakage" with explanation propagation |
| **Error accumulation** | Small mistakes compounding across the tree | Stacked **review lenses** with decorrelated reviewers |
| Merge conflicts | Two workers, one region | A neutral third-party agent resolves impartially |

**Ossification** is the one most worth lifting out. An agent that has learned core code is
dangerous to modify will route around it — producing exactly the accreted workarounds a human
team produces under the same fear. The remedy is explicit permission to break things paired
with propagating *why*, which is a cultural intervention expressed as a prompt.

The organising structure is a **task tree**: root goal, recursive decomposition into executable
units, planners splitting and delegating while holding design coherence, workers executing
narrowly with full context. The stated benefit is **context efficiency rather than parallelism**
— narrow scopes avoid the context drift that degrades one long-running agent, which is the
problem [Long-Running Agents](../engineering/ai-native/long-running-agents.md) attacks from the
single-agent side.

## Infrastructure as the binding constraint

Two details that make the scale concrete:

- **Custom version control at ~1,000 commits/second**, because Git does not hold up under swarm
  write rates. Nothing else in these notes treats VCS as an agent-scale bottleneck.
- A **Field Guide** — an agent-curated, line-budgeted knowledge repository injected at startup —
  justified by **stigmergy**: coordination through the environment rather than direct messaging.
  That is the same instinct as context-in-the-repo, with an explicit line budget so the artefact
  cannot grow past its usefulness.

The framing reference is **Coase's *The Nature of the Firm***: coordination cost is what bounds
an organisation's size. Applied here, a swarm's ceiling is organisational rather than technical
— which is why the infrastructure work above buys more than adding agents does.

## The tension with the harness note

Worth stating rather than smoothing over, because both sources are experiment-backed and they
point different ways:

- [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md)
  concludes harness complexity should **shrink** as models improve, having measured a ~22× cost
  multiple for an elaborate harness over a solo agent.
- This reports elaborate coordination infrastructure plus cheap workers **beating** frontier-only
  configurations on cost at equal quality.

The likely reconciliation is task scale: Anthropic's comparison was whole small apps where a
solo agent is viable, and SQLite-from-the-manual is not a task any solo agent completes. That
suggests harness investment tracks task size rather than model generation — but it is an
inference across two experiments by interested parties, not a settled finding.

## Relationship to other notes

- [Multi-Agent Coding Without Worktree Chaos](../reading/multi-agent-coding-coordination.md) —
  the same problem hand-rolled. Wells reaches comparable conclusions with tmux, file reservations
  and a "ring leader"; this is the industrial version with custom VCS and a cost model. Both land
  on *plan → decompose → coordinate*, and that convergence from very different budgets is
  itself evidence.
- [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md)
  — the genuine tension above, plus the shared planner/worker split.
- [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md) —
  per-request routing; this is per-role selection decided structurally in advance.
- [Building Effective Agents](../reading/building-effective-agents.md) — the orchestrator–workers
  pattern this instantiates at scale, with the task tree as the recursive form.
- [Long-Running Agents](../engineering/ai-native/long-running-agents.md) — context drift tackled
  by decomposition rather than by keeping one agent durable.
- [OpenAI's Agent-First Harness](openai-agent-first-harness.md) and
  [Ramp's Inspect Agent Platform](ramp-inspect-agent-platform.md) — the other vendor-reported
  agent-scale accounts, and the authorship-volume figures this note's thrash result qualifies.
