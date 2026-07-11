---
title: AI-Native Engineering — Overview
tags: [meta, ai-engineering, agentic-workflows]
topic: engineering/ai-native
status: complete
related:
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/agentic-sdlc-maturity-model.md
  - engineering/ai-native/ai-sdlc-terminology.md
  - engineering/ai-native/agentic-ai-strategy-frameworks.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/ai-dlc-methodology.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - engineering/ai-native/modern-engineering-values.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/ai-native/prompt-engineering-for-programmers.md
  - standards/open-knowledge-format.md
  - leadership/learning-organisation.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/architecture/adrs-in-an-agentic-world.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/long-running-agents.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/ai-native/ai-engineering-discipline.md
  - engineering/ai-native/apex-framework.md
  - engineering/ai-native/trust-factory.md
  - reading/agentic-sdlc-survey.md
  - reading/building-effective-agents.md
  - reading/multi-agent-coding-coordination.md
  - reading/how-i-use-llms-2026.md
  - reading/llm-maintained-wiki.md
  - reading/factory-engineers.md
  - case-studies/cloudflare-ai-code-review.md
  - reading/what-is-software-engineering-ai.md
updated: 2026-06-27
---

# AI-Native Engineering — Overview

A map of the notes on building software with AI agents. They answer different questions —
*strategy, process, platform, team, control, quality* — and reinforce each other.

## Strategy & maturity — where are we going?

- [Agentic AI Strategy Frameworks](agentic-ai-strategy-frameworks.md) — how to think about
  adopting agentic AI at the organisation level.
- [Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md) — staged progression from
  assisted coding to controlled autonomy.
- [AI in the SDLC — Terminology](ai-sdlc-terminology.md) — disambiguating the competing
  umbrella terms (AI-Augmented, AI SDLC, Agentic, AI-Native).

## Process — how does work flow?

- [The Agentic SDLC](agentic-sdlc.md) — the AI-assisted software delivery lifecycle.
- [CI/CD as the Control Plane for AI-Assisted Engineering](ci-cd-ai-engineering.md) — the
  pipeline as the guardrail that makes agent-speed delivery safe.
- [CI Speed When Agents Write the Code](ci-speed-with-ai-agents.md) — why fast CI's
  context-switching rationale weakens once agents, not humans, wait on the pipeline.
- [AI-DLC and the Reimagined SDLC](ai-dlc-methodology.md) — a concrete, ceremony-level
  methodology (AI-DLC, V-Bounce, Bolts/Units/Intents) instantiating the agentic loop.
- [Spec-Driven Development](spec-driven-development.md) — the spec, not the code, as the
  primary living artifact; why "up" (raised abstraction) is not "up-front" (waterfall).
- [Agile in the Age of AI](agile-in-the-age-of-ai.md) — the counterpoint: Agile principles
  persist; sustainable pace and human cognitive load bind how many agents you can direct.
- [What Is Software Engineering? (Adapting to AI)](../../reading/what-is-software-engineering-ai.md)
  — Breck's fundamentals-endure case via Farley: AI changes tempo not principles; build speed is
  the existential investment and the cost of integration is the killer *(in reading)*.

## Platform & team — who and what enables it?

- [The AI-Native Engineering Stack](ai-native-engineering-stack.md) — the tooling/platform
  layer (the internal developer platform, golden paths).
- [The AI-Augmented Engineering Team](ai-augmented-engineering-team.md) — the operating
  model: team composition, Intent Specs, the delivery loop, transition roadmap. The capstone
  that ties the rest together.
- [Factory Engineers, Not Product Engineers](../../reading/factory-engineers.md) — the radical
  end of the operating-model spectrum: engineers build the *factory* that ships products, every
  manual change is process debt, and success is factory efficiency *(in reading)*.
- [Revised Rules of Engineering Leadership](../../leadership/revised-rules-engineering-leadership.md) —
  the leadership-altitude rules behind it: durable teams + fast, good decisions when execution
  is cheap *(in leadership)*.
- [Modern Engineering Values](modern-engineering-values.md) — a solo/small-team practitioner's
  values: ownership, taste, guardrails, context-in-the-repo, own your stack, option value.
- [The Trust Factory](trust-factory.md) — Kent Beck reframes XP as a system for *manufacturing
  trust*: code and trust are asymmetrical (trust builds slowly, evaporates instantly), AI
  accumulates code faster than trust, and "genie" development erodes the loops that build it.
- [Open Knowledge Format (OKF)](../../standards/open-knowledge-format.md) — a portable
  markdown+YAML format for the knowledge/context agents consume *(in standards)*.
- [The LLM-Maintained Wiki](../../reading/llm-maintained-wiki.md) — Karpathy's pattern of an LLM
  compiling and maintaining a persistent wiki (raw → wiki → schema; ingest/query/lint) instead of
  RAG over raw docs; the maintenance discipline behind context-in-the-repo *(in reading)*.

## Control & quality — how do we keep it correct?

- [Agentic Code Review](agentic-code-review.md) — review as the new bottleneck:
  tiered risk-based review, the human-on-the-loop shift, the AI-reviewer tool landscape, and the
  failure modes (borrowed confidence, test manipulation, AI slop).
- [Cloudflare's AI Code Review System](../../case-studies/cloudflare-ai-code-review.md) — the
  production instance of those principles: seven specialised reviewers plus a judge, "What NOT to
  Flag" negative prompting, risk/model tiering, and the cost/resilience engineering *(in case studies)*.
- [AI Demands More Engineering Discipline](ai-engineering-discipline.md) — discipline shifts from
  reviewing code to validating behaviour: observability, production-as-dev-stage, regenerability,
  and encoding knowledge outside disposable code.
- [Design Systems as the AI Control Plane](../architecture/design-systems-ai-control-plane.md)
  — codified constraints as the control plane for AI-generated UI.
- [ADRs in an Agentic World](../architecture/adrs-in-an-agentic-world.md) — when
  implementation is cheap, write the ADR *after* spiking the options; decisions
  anchored in built evidence rather than rhetoric *(in architecture)*.
- [Eval-Driven Development for AI Capabilities](eval-driven-ai-development.md) — testing the
  prompts/skills/agents themselves, not just the code they emit.
- [Harness Engineering](harness-engineering.md) — the component-level anatomy of an agent
  harness (the program agents run inside): core loop, tools, memory, patterns, trade-offs.
- [Building Effective Agents — Workflow & Agent Patterns](../../reading/building-effective-agents.md)
  — Anthropic's composition patterns (prompt chaining, routing, parallelization,
  orchestrator–workers, evaluator–optimizer, autonomous agents), simplicity-first, and when *not*
  to use agents *(in reading)*.
- [Long-Running Agents](long-running-agents.md) — the durability layer: the three walls (context
  rot, no persistent state, no self-verification), brain/hands/session, checkpoints, and memory.
- [Multi-Agent Coding Without Worktree Chaos](../../reading/multi-agent-coding-coordination.md) —
  coordinating a *swarm* of coding agents on one branch via planning, a task graph, file
  reservations, and a coordinator, rather than one worktree per agent *(in reading)*.
- [Quality-First AI Coding](quality-first-ai-coding.md) — the practitioner workflow: multi-model
  bug review and quality-over-velocity use of AI to write better code more slowly.
- [How I Use LLMs as a Staff Engineer (2026)](../../reading/how-i-use-llms-2026.md) — a
  practitioner's delegation map: what to hand to agents (bugs, tests, config), what to review
  hard (code changes), and what to keep human (PR descriptions, ADRs, comms) *(in reading)*.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — move mechanical
  correctness feedback into agent-actionable loops (sensors) so agents self-correct and humans
  stop babysitting.
- [Own the Outer Loop](own-the-outer-loop.md) — the human-accountability framing: agents run the
  inner execution loop; humans own the outer *accountability boundary* (constraints, sampling,
  audit, ownership, governance) and the Quality → Verdict → Answerability decision.
- [Go as an Agentic Language](../../languages/go-agentic-language.md) — language choice as agentic
  infrastructure: fast deterministic builds, compile-enforced types as a *gate*, and low
  distractor density tighten the loop and cut context rot *(in languages)*.
- [Loop-Driven Development](loop-driven-development.md) — the connective map: TDD scaled to agent
  loops (trigger/goal/harness/verifier/state) and the autocomplete→prompt→context→harness→loop
  leverage stack; plus the loop-engineering anatomy and the comprehension-debt / cognitive-surrender
  cautions.
- [Prompt Engineering for Programmers](prompt-engineering-for-programmers.md) — the ground-level
  craft: context, specificity, decomposition, few-shot, personas, and debugging/refactoring
  patterns. Prompt quality determines output quality.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — raising a system's
  capacity to safely absorb agent-speed change: contracts, automated verification, telemetry,
  simplification.

## Measurement — is it working?

- [The APEX Framework](apex-framework.md) — a measurement operating model (AI Leverage,
  Predictability, Flow Efficiency, Developer Experience) for judging whether AI adoption creates
  *sustainable* value, measured at the PR and in the critical path rather than by tool adoption.
- [Agentic AI in the SDLC — A Research Survey](../../reading/agentic-sdlc-survey.md) — the empirical
  anchor under the cluster: a six-layer reference architecture, the SWE-bench/productivity evidence
  (and why benchmark gains ≠ team throughput), and five open problems mapped onto these notes
  *(in reading)*.

## The through-line

When code generation is cheap, leverage moves to **intent, constraints, and judgement**.
Strategy sets direction; the SDLC and CI/CD move work; the stack and team supply capability;
design systems and evals keep output correct. See also the
[engineering leadership overview](../../leadership/engineering-leadership-overview.md) for the human/decision
side, much of which these notes depend on — and
[The Learning Organisation and AI Adoption](../../leadership/learning-organisation.md) for the
cultural prerequisite (psychological safety, slack, intelligent failure) that lets a team adopt
any of this faster than the tooling changes.
