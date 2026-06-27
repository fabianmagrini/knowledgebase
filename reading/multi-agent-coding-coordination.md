---
title: Multi-Agent Coding Without Worktree Chaos
tags: [ai-engineering, agentic-workflows, git, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/practices/long-running-agents.md
  - reading/building-effective-agents.md
  - engineering/practices/loop-driven-development.md
  - reading/agentic-sdlc-survey.md
  - engineering/practices/agile-in-the-age-of-ai.md
  - engineering/practices/ai-native-engineering-overview.md
source: "https://davidwells.io/blog/multi-agent-coding-without-worktree-chaos"
updated: 2026-06-27
---

# Multi-Agent Coding Without Worktree Chaos

Notes on David Wells' argument that **git worktrees are the wrong default for
running coding agents in parallel**. The common assumption is that one worktree
per agent buys safe concurrency through branch isolation; Wells argues that for
routine parallel work, **explicit coordination on a single branch** — planning,
a task graph, and file reservations — prevents collisions more effectively than
isolation does.

This is the concrete coding-workflow instantiation of the orchestrator–workers
pattern in [Building Effective Agents](building-effective-agents.md), and the
many-agent counterpart to [Long-Running Agents](../engineering/practices/long-running-agents.md),
which is about keeping *one* agent durable.

## "Worktree chaos"

Worktrees don't remove coordination problems — they **defer them to merge time**
and add secondary costs:

- duplicated setup across checkouts
- context drift between isolated branches
- repeated work when agents solve overlapping problems
- time-consuming reconciliation once everyone is "done"

The leverage, Wells argues, "comes from structured parallelism" — discipline
before execution, not the number of terminals open.

## The six-step workflow

1. **Solid planning.** Define what changes, what doesn't, the files involved,
   execution order, edge cases, and verification criteria *before* any agent
   touches code. "Measure twice, cut once" applies intensely to agents.
2. **Surface hidden questions.** Prompt agents to name ambiguities — implementation
   details, UX decisions, uncertain assumptions — so constraints sharpen up front.
3. **Directed task graph.** Convert the plan into dependency-aware tasks (the
   author uses **Beads**), which exposes what can run in parallel vs. sequentially.
4. **Coordinated agent swarm.** Spawn agents across tmux sessions; a coordinator
   agent — the **"ring leader"** — assigns unblocked tasks, detects blockers, and
   prevents duplicate work.
5. **Verification pass.** Check task completion, that file reservations are
   released, that diffs match the plan, and that risks are addressed.
6. **Summary & QA plan.** Document changes, decisions, tests run, known risks, and
   recommended human QA steps.

## Coordination mechanisms

Two mechanisms replace inferring coordination from `git status`:

- **File reservations.** An agent claims the specific files it will edit before
  editing them, preventing simultaneous modification on a shared branch.
- **Agent Mail (MCP).** Explicit messaging between agents to communicate blockers,
  API changes, helper locations, and task-scope adjustments.

## Tooling (the author's stack)

| Tool | Role |
|---|---|
| **Beads** (+ Beads Viewer) | Local-first task dependency graph and visual inspection |
| **MCP Agent Mail** | Reservation + messaging coordination layer |
| **ntm** | tmux orchestration for spawning/managing agent sessions |
| Codex, Claude Code, Gemini, Aider | The coding harnesses driven as workers |

These are the author's specific choices; the transferable idea is *plan → task
graph → reservations → coordinator loop*, not the particular tools.

## Distinctive vocabulary

- **Ring leader** — the coordinator agent running a consistent assign/detect loop.
- **Ralph loop** — single-agent iteration (see
  [Long-Running Agents](../engineering/practices/long-running-agents.md)) extended
  to a swarm.
- **Structured parallelism** — parallel motion comes from discipline, not terminal
  count.

## Trade-offs

The single-branch approach demands **upfront planning rigour** in exchange for
eliminating branch-management and merge overhead — the opposite trade from
exploratory worktree workflows. Worktrees remain useful for **isolated experiments
or risky refactors**, just not routine parallel work.

The natural ceiling is human, not technical:
[Agile in the Age of AI](../engineering/practices/agile-in-the-age-of-ai.md) reports
~three parallel agents being manageable comfortably, so a swarm's coordinator and
verification steps are what keep cognitive load bounded as agent count rises.

## Relationship to other notes

- [Building Effective Agents](building-effective-agents.md) — the abstract
  orchestrator–workers and autonomous-agent patterns; this note is one concrete
  coding instantiation with reservations and a coordinator.
- [Long-Running Agents](../engineering/practices/long-running-agents.md) — keeping
  *one* agent durable; this is coordinating *many*, and it borrows the Ralph loop.
- [Loop-Driven Development](../engineering/practices/loop-driven-development.md) —
  the per-agent generate→verify loop each worker runs inside the swarm.
- [Agentic AI in the SDLC — A Research Survey](agentic-sdlc-survey.md) — its L4
  orchestration layer (single-agent loop vs multi-agent) is the architectural
  framing of this workflow.
- [Agile in the Age of AI](../engineering/practices/agile-in-the-age-of-ai.md) —
  the human cognitive-load bound on how many agents one person can direct.
