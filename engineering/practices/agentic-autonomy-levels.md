---
title: Agentic Autonomy Levels
tags: [ai-engineering, agentic-workflows, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/long-running-agents.md
  - engineering/practices/agentic-sdlc-maturity-model.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/architecture/agile-design-decisions.md
source: "https://addyo.substack.com/p/agentic-autonomy-levels"
updated: 2026-07-05
---

# Agentic Autonomy Levels

Addy Osmani argues that a single-axis "how autonomous is it" scale is too crude for agentic
engineering. Autonomy has **two dimensions** — **agency** (how independently one agent operates)
and **orchestration** (how many agents are coordinated) — which together form a six-level
progression across three operational eras. The core discipline is **calibrated autonomy**:
autonomy is a *safety* property to be matched to your ability to verify and undo, not a status to
climb for its own sake.

## The two axes

| Axis | Low | Mid | High |
|---|---|---|---|
| **Agency** | Suggest candidates and wait | Scoped work with continuous reporting and evidence | Goal-driven experimentation — tries approaches, tests, asks, reports blocks |
| **Orchestration** | Single agent, single thread | Several isolated agents, separate worktrees, different goals | An orchestrator managing queues/backlogs/schedules; intervention only on failure |

## The six levels

| Level | Name | What it means |
|---|---|---|
| **0** | Assist | Generates suggestions you always evaluate before acting (autocomplete, inline edits, chat). Verification stays local. |
| **1** | Supervised Action | Edits/runs commands for you, but asks before anything consequential. The default posture. Risk: **approval fatigue**. |
| **2** | Scoped Task Delegation | Bounded work with clear goals and success criteria; you stay available to interrupt. The industry's centre of gravity. Verification shifts to **evidence** (tests, types, lint, screenshots). |
| **3** | Goal-Driven Autonomy | "Does whatever it takes" until a **measurable stopping condition** is met (e.g. page load < 1s, remove all `any` types). |
| **4** | Parallel Delegation | Multiple agents on isolated slices. Chief risk: **false parallelism** — needs decomposition, ownership rules, independent review queues. |
| **5** | Managed-by-Exception Orchestration | A manager agent dispatches workers, monitors, verifies, and escalates — returning only decisions needing human judgement. Issue tracker in → PRs out. |

**Three eras:** (1) *you steer, agent assists* → (2) *agent owns a bounded task, you verify* →
(3) *system runs with orchestration, you step in on exceptions.*

## The execution contract

Osmani proposes every agent run be preceded by an explicit contract:

1. **Goal** — the outcome, not the activity or technique
2. **Scope** — operational domain and allowed techniques
3. **Non-goals** — explicitly excluded objectives
4. **Tools and permissions** — the boundaries on acting in the world
5. **Stopping condition** — measurable variables that mean "done"
6. **Evidence** — tests, logs, screenshots independent of the agent's own summary
7. **Escalation** — the conditions that pull a human in
8. **Budget** — token, time, attempt, and parallelism caps

The goal/scope/non-goals/stopping/evidence shape echoes the Intent Spec discipline in the
[AI-augmented engineering team](ai-augmented-engineering-team.md); writing the stopping condition
*before* execution counters the agent's tendency to self-grade as done too early.

## Calibrated autonomy: three safety questions

Before granting high autonomy, ask:

1. How quickly can we **detect** errors in what it's doing?
2. How easily can we **undo** its work?
3. What **independent proof** confirms success?

> "If the answer to all three is: not quickly, at great difficulty, and trusting the summary,
> it's not high autonomy."

So autonomy should track **reversibility and risk** — the same one-way-vs-two-way-door logic as
[Agile Design Decisions](../architecture/agile-design-decisions.md#reversibility--one-way-vs-two-way-doors).
A payment-engine refactor with strong tests, reviewer agents, and a clean rollback can support
*more* autonomy than a documentation task with no canonical source of truth.

## Anti-patterns

- **Autonomy as status**, not a safety metric.
- **Permission laundering** — granting overly broad access out of approval fatigue.
- **Summary substitution** — accepting the agent's summary in place of actual verification.
- **Fleet cosplay** — humans manually orchestrating supposedly parallel agents.

**Climb one axis at a time:** start with a single supervised agent producing defensible evidence,
then parallelise read-heavy exploration, then multiple write agents with ownership rules, then
recurring automations, and only then true orchestration. Osmani cites Anthropic usage data
(experienced Claude Code users auto-approve more; "~70% of planning decisions human, ~80% of
execution the agent") — treat as cited research, not verified fact.

## Relationship to other notes

- **[Long-Running Agents](long-running-agents.md)** — the companion Osmani piece on the
  *durability* of a long run (brain/hands/session, checkpointing); this note is the
  *how-much-autonomy* taxonomy, and its Levels 3–5 are where that durability becomes essential.
- **[Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md)** — an *organisation-level* SDLC
  ladder; this is a *per-task agent-autonomy* ladder — a useful contrast in what's being levelled.
- **[Backpressure Loops for Coding Agents](agent-backpressure-loops.md)** — the feedback that turns
  higher autonomy from reckless into safe; the control side of climbing the ladder.
- **[Agile Design Decisions](../architecture/agile-design-decisions.md)** — reversibility and
  blast radius are the axes calibrated autonomy is matched against.
