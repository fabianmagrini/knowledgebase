---
type: case-study
title: DoorDash's Multi-Agent Feature-Flag Cleanup
description: "Peer-reviewed agent work on a task with a natural oracle: 60,000+ flags across 623 repos, 45 of 50 usable PRs at 13.8 minutes and $4.79 each, one human checkpoint, and a precise account of where deterministic refactoring tools stop."
tags: [ai-engineering, agentic-workflows, refactoring, ci-cd, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/architecture/reversibility-decays.md
  - case-studies/doordash-ai-code-review.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/cursor-agent-swarm-economics.md
  - reading/multi-agent-coding-coordination.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - standards/agent-interop-protocols.md
source: "https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/"
updated: 2026-10-11
---

# DoorDash's Multi-Agent Feature-Flag Cleanup

DoorDash built a multi-agent LLM system to remove stale feature flags across **60,000+ flags in
roughly 623 repositories**, with **2,300 new flags created monthly** and 1,000+ already
identified as stale.

> **On retrieval.** The DoorDash blog returns **403 to automated retrieval** (tried twice). This
> note was written from [InfoQ's writeup](https://www.infoq.com/news/2026/09/doordash-feature-flag-cleanup/)
> (Leela Kumili, 18 September 2026). `source:` remains the canonical DoorDash URL per these
> notes' convention; the figures below are as InfoQ reports them.

**Two things raise this above the genre.** The work was **accepted to the ICSME 2026 industry
track**, so unlike almost every other agent case study recorded here it has been through peer
review rather than only a company blog. And the task has a **natural oracle** — see below, which
is the most transferable part.

## Why this task was tractable

Flag removal is one of the rare refactors where *correct* is mechanically checkable. Once a
flag's final value is fixed, removing it should change no behaviour at all — so the build, the
test suite and coverage are a genuine external check rather than a proxy.

That is precisely the condition
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
identifies as what makes agent output checkable: an oracle **independent of the generator**. The
verification stack here is deterministic throughout — **Gradle** builds, **JaCoCo** patch
coverage, **Detekt** static analysis — with no LLM judging its own work.

Read against the **28 of 520** migration-blindness result in
[Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md),
the contrast is instructive: migrations fail audit because "tests pass" does not establish the
old path is gone. Flag removal does not have that gap — the flag reference either exists in the
tree or it does not.

## The architecture

Built on **Google's Agent Development Kit**, with **MCP** to reach the experimentation platform
for metadata including rollout percentage.

| Phase | Model | What happens |
|---|---|---|
| **1 — Orchestration** | Claude **Sonnet** | Pull stale-flag tickets from Jira, search repositories, query experimentation metadata, produce a report |
| **— Human checkpoint —** | | An engineer reviews the report and **confirms the target value** before any code is touched |
| **2 — Cleanup** | Claude **Opus** | Locate references, decide the cleanup strategy, modify code and tests, run builds, coverage and static analysis |

Cleanup agents run in **isolated Git worktrees, up to four concurrent per repository**.

**The checkpoint is well-placed, and that is the lesson.** The human decides the one thing that
is genuinely a judgement — *what should this flag's permanent value be* — and the agent does the
mechanical consequence. That is
[calibrated autonomy](../engineering/ai-native/agentic-autonomy-levels.md) with the boundary
drawn at the right place rather than at an arbitrary autonomy level: not "review the agent's
work" but "make the decision the agent cannot."

**Role-differentiated models, inverted.** Sonnet orchestrates and Opus does the cleanup, which
is the opposite assignment from
[Cursor's swarm](cursor-agent-swarm-economics.md) — frontier planner, cheap workers. Both are
coherent once you ask where the difficulty sits. Cursor's hard part is **decomposition** of an
open-ended goal; here the plan is nearly fixed (find references, remove, verify) and the hard
part is **the code change** in unfamiliar repositories. The general rule is to put the stronger
model where the judgement is, not at a fixed layer.

**And a resolved disagreement on worktrees.**
[Multi-Agent Coding Without Worktree Chaos](../reading/multi-agent-coding-coordination.md) argues
worktrees are the wrong default, because isolation defers coordination to merge time. DoorDash
uses them happily — and the reason is the condition Wells' objection needs: his case is agents
working on *one interdependent feature*, where isolation hides collisions. Flag cleanups are
disjoint by construction, touching different flags in different files. **Worktrees are right
exactly when the work is genuinely independent**, which is rarer than it looks and is the case
here.

## Results

| Measure | Reported |
|---|---|
| Evaluation set | 50 stale flags |
| Outcome | **31 first-pass merges, 14 revisions, 5 engineer interventions** — 45 of 50 usable |
| Simple / medium / complex | **100% / 94% / 85%** |
| Time and cost | **13.8 minutes** and **$4.79** per cleanup, against a stated 1–2 hour manual estimate |
| Defects | **Zero bugs or regressions** across the 50 changes |

Two notes on reading these. The **by-complexity breakdown is the useful shape** — the degradation
from 100% to 85% as complexity rises is the honest part, and it is reported rather than averaged
away. And the 1–2 hour manual baseline is DoorDash's own *estimate*, not a measured control, so
the cost comparison is indicative; the $4.79 and 13.8 minutes are measured, the thing they are
compared against is not.

## Where deterministic tools stop

The most quotable finding, and the reason this note matters beyond flags.

Uber's **Piranha** is the existing deterministic flag-removal tool. It did not suffice at
DoorDash because their dependency-injection patterns mean the *"relationships between the flag
and application logic are semantic rather than directly represented."* And the five cases needing
human intervention involved **"deep call chains and cross-interface parameter threading."**

That is an unusually precise account of the boundary between refactoring tools and language
models. A deterministic rewriter needs the relationship to be **syntactically present**; where
the connection is mediated by a DI container, an interface or a threaded parameter, there is no
expression in the source for a rule to match on — only a meaning to infer.

It also qualifies [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md)'s
otherwise sound rule that "anything deterministic enough to lint is in the wrong loop if it waits
for a PR." True — but this names the category where the relationship *cannot* be expressed
deterministically, which is where the probabilistic tool earns its place. The two notes together
give a sharper test than either: **is the relationship present in the syntax, or only in the
meaning?**

## What this closes

[Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
prescribes flag-debt discipline — every release toggle becomes a removal ticket, set an expiry,
some teams fail the build past a sunset date — and
[Reversibility Decays](../engineering/architecture/reversibility-decays.md) calls flag debt
"reversibility debt in its most familiar form."

Neither says what to do once you already have 60,000 flags and are adding 2,300 a month. **This
is the remediation story for advice that assumes you followed it from the beginning**, which most
organisations did not. Worth holding alongside the prescription, because the prescription is
cheap to state and this is what the alternative costs.

## Relationship to other notes

- [Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
  — the discipline this cleans up after; that note's removal-ticket and expiry advice is the
  prevention, this is the cure.
- [Reversibility Decays](../engineering/architecture/reversibility-decays.md) — flag debt as the
  canonical case of exit cost rising over time; 60,000 flags is that decay at scale.
- [DoorDash's AI Code Reviewer](doordash-ai-code-review.md) — the same company's other agent
  system, and a consistent pattern: both pick a task with a checkable outcome and tune for
  precision rather than ambition.
- [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) — the human
  checkpoint placed at the judgement rather than at a review step.
- [Cursor's Agent Swarm Economics](cursor-agent-swarm-economics.md) — role-differentiated model
  selection, assigned the opposite way round, and the reasoning that reconciles both.
- [Multi-Agent Coding Without Worktree Chaos](../reading/multi-agent-coding-coordination.md) —
  the worktree disagreement, resolved by whether the work is genuinely independent.
- [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) —
  the oracle-independence condition this task happens to satisfy by construction.
- [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) — the deterministic
  preference, with the Piranha finding marking where it runs out.
- [Agent Interoperability Protocols](../standards/agent-interop-protocols.md) — MCP at the
  tools boundary and ADK as the harness, both in production here.
