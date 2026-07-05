---
title: Agentic AI in the SDLC — A Research Survey
tags: [ai-engineering, agentic-workflows, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/agentic-code-review.md
  - engineering/practices/apex-framework.md
  - engineering/practices/ai-augmented-engineering-team.md
  - engineering/practices/agentic-sdlc-maturity-model.md
  - engineering/practices/ai-native-engineering-overview.md
  - reading/building-effective-agents.md
  - reading/multi-agent-coding-coordination.md
  - reading/agentic-ai-architecture-emag.md
source: "https://arxiv.org/abs/2604.26275"
updated: 2026-06-26
---

# Agentic AI in the SDLC — A Research Survey

Notes on Happy Bhati's 2026 survey *Agentic AI in the Software Development
Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software
Engineering* (arXiv 2604.26275). It is useful here as the **empirical anchor**
under an otherwise framework- and practitioner-opinion-driven cluster: where
[The Agentic SDLC](../engineering/practices/agentic-sdlc.md) and the
[APEX framework](../engineering/practices/apex-framework.md) *assert* that AI
shifts leverage upstream and that local speed ≠ system throughput, this survey
supplies the benchmarks and controlled-study numbers behind those claims.

The paper's organising distinction is between AI tools that merely *accelerate*
existing processes and **agentic systems performing autonomous engineering work**
— what it calls the **Agentic SDLC (A-SDLC)**.

## Six-layer reference architecture

The survey proposes a six-layer stack for agentic software-engineering systems.
It maps closely onto the component anatomy in
[Harness Engineering](../engineering/practices/harness-engineering.md).

| Layer | Concern | Notes |
|---|---|---|
| **L0** Foundation model | Base LLM reasoning / code generation | Frontier anchors (Claude Opus, GPT-5.x, Gemini 3.x); open-weights for self-hosting |
| **L1** Reasoning, memory, self-reflection | Chain-of-thought / ReAct planning, short- and long-term memory, self-critique | Self-reflection accounts for much of the gap between zero-shot accuracy and agentic resolution |
| **L2** Agent–Computer Interface (ACI) | Translates LLM tokens into concrete computer operations | Princeton's claim: *ACI design quality is empirically as important as model size* |
| **L3** Tools and environment | Filesystem/editor, shell, browsing, test runners, compilers, VCS/CI-CD | The agent's "hands" |
| **L4** Orchestration | Single-agent loops (SWE-agent, Claude Code) vs multi-agent role decomposition (MetaGPT, ChatDev) | One cognitive locus vs role-specialised agents |
| **L5** Governance and safety | Permission boundaries, sandboxing, audit logs, sensitive-operation policy | The paper's sharpest claim: *the least mature layer, rapidly becoming the bottleneck on enterprise deployment* |

## Traditional SDLC vs A-SDLC

| Phase | Traditional | Agentic |
|---|---|---|
| Requirements | Analyst writes specs; stakeholder review | Intent specification; agent drafts the spec |
| Design | Architect produces diagrams/ADRs | Agents propose & critique; human selects |
| Implementation | Engineers write code file-by-file | Coding agents execute the plan; human reviews |
| Testing | QA writes/runs tests | Testing agents generate suites in a sandbox |
| Deploy | Manual or pipeline promotion | CI agent gates; human approves production |
| Maintenance | On-call, tickets, hotfixes | Monitor agents triage; repair agents patch |

Three structural shifts:

- The **work unit shrinks** from two-week sprints to agent-completable tasks
  (minutes to hours).
- The **developer role shifts** from producing code to *orchestrating, reviewing,
  and directing* — the survey's "delegation interface".
- **Behavioural metrics** (agent acceptance rate, escalation quality) displace
  process metrics — the same move
  [APEX](../engineering/practices/apex-framework.md) makes by measuring at the PR.

## Empirical evidence

**Capability — SWE-bench Verified (Oct 2023 → Apr 2026):**

| Date | System | Score |
|---|---|---|
| Oct 2023 | RAG baseline | 1.96% |
| Nov 2024 | SWE-agent | 12.5% |
| 2024 | Claude 3.5 Sonnet | ~49% |
| Apr 2026 | Claude Opus 4.7 | 78.4% |

The trajectory is "approximately logistic", with **non-agentic systems plateauing
near 20%** — the survey's evidence that *scaffolding dominates raw model
capability* (reinforcing the L2/L4 claims above).

**Productivity — controlled and field studies:**

- Peng et al.: 55.8% completion-time reduction on a JavaScript HTTP-server task.
- Microsoft field study: +12.92%–21.83% pull requests per week.
- Accenture field study: +7.51%–8.69%.
- Brandebusemeyer et al.: moderate Copilot use helped; *excessive use eroded the
  benefit*.

**The caveat the cluster needs:** these are *benchmark and task-level* gains.
SWE-bench is dominated by Python bug-fixing with ground-truth tests that
real-world tasks lack, and task-level speed-ups do not equal team-level
throughput. This is the measured basis for "Feeling Fast, Delivering Slow" in
[The Agentic SDLC](../engineering/practices/agentic-sdlc.md) and for APEX's
insistence on measuring in the critical path rather than by tool adoption.

## Five open problems

The survey closes on five unresolved problems — each already has a home in this
knowledge base:

| Open problem | Summary | Where it lands |
|---|---|---|
| Evaluation beyond SWE-bench | SWE-bench is Python/bug-fix biased and assumes ground-truth tests; SWE-bench Pro/Multimodal, Terminal-Bench, SWE-Compass extend it | [Eval-Driven Development](../engineering/practices/eval-driven-ai-development.md) |
| Governance, safety, audit | "Proliferation of deployed agents alongside a deficit in governance"; human–agent responsibility mapping as a non-optional design step | [The Agentic SDLC](../engineering/practices/agentic-sdlc.md), [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) |
| The technical-debt hypothesis | Agents bias toward *more code and local fixes* over global redesign; long-term repository-health studies are missing | [Loop-Driven Development](../engineering/practices/loop-driven-development.md) (comprehension debt) |
| Skill redistribution | A two-track market: experienced engineers compound gains, newcomers underperform; teaching decomposition/judgement matters | [The AI-Augmented Engineering Team](../engineering/practices/ai-augmented-engineering-team.md) |
| The economics of attention | If agents emit plausible patches fast, *human review is the rate-limiting resource* | [Agentic Code Review](../engineering/practices/agentic-code-review.md) |

## Distinctive vocabulary

- **Agent–Computer Interface (ACI)** — the structured command layer translating
  model output into concrete operations; design quality rivals model size.
- **Delegation interface** — engineers define goals and review results rather than
  guiding steps.
- **Capability–autonomy plane** — positioning systems on two axes (capability %,
  autonomy level); a sharper version of the
  [maturity model](../engineering/practices/agentic-sdlc-maturity-model.md)'s stages.
- **Human–agent responsibility mapping** — explicit authority allocation and
  approval-gate design as a governance primitive.

## Relationship to other notes

This is the research-grounded counterpart to the cluster's opinion and framework
notes. It supplies evidence for [The Agentic SDLC](../engineering/practices/agentic-sdlc.md),
a published architecture that parallels [Harness Engineering](../engineering/practices/harness-engineering.md),
and a problem list whose five items map onto
[eval-driven development](../engineering/practices/eval-driven-ai-development.md),
[agentic code review](../engineering/practices/agentic-code-review.md),
[the AI-augmented team](../engineering/practices/ai-augmented-engineering-team.md),
and the [AI-native overview](../engineering/practices/ai-native-engineering-overview.md)
map it sits under.
