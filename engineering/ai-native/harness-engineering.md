---
type: note
title: Harness Engineering
description: "A harness is the orchestration system built around an LLM to manage its non-determinism and limitations."
tags: [ai-engineering, architecture, reading, agentic-workflows]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/ai-native/prompt-engineering-for-programmers.md
  - engineering/ai-native/cress-context-engineering.md
  - tools/claude-code-steering-mechanisms.md
  - reading/agentic-ai-architecture-emag.md
  - reading/agentic-sdlc-survey.md
  - reading/building-effective-agents.md
  - reading/llm-maintained-wiki.md
  - case-studies/cloudflare-ai-code-review.md
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/ai-factory.md
  - reading/new-sdlc-vibe-coding.md
  - case-studies/microsoft-ai-core-competency.md
source: "https://diego-pacheco.blogspot.com/2026/05/harness-engineering.html"
updated: 2026-06-20
---

# Harness Engineering

A **harness** is the orchestration system built *around* an LLM to manage its non-determinism
and limitations. The model is effectively rented; the orchestration layer is owned and
engineered. The distinction the article draws is one of altitude: a short 2–10 line prompt is
not a harness — a harness requires rules, structure, design, and architecture. It adds
determinism through code and tool integration while accepting that the model itself stays
probabilistic.

This note describes the *engineering of the harness program itself* — the kind of system Claude
Code and Codex are. Other notes here use "harness" at a higher altitude (the
governance/validation platform that gates agent output); see
[Relationship to other notes](#relationship-to-other-notes) below.

## Anatomy of a harness

Five core components:

| Component | Role |
|---|---|
| **LLM integration** | Remote APIs or local models (Ollama/LocalAI). Always external, never embedded. |
| **Core loop** | The orchestration engine: read instructions → call the LLM → integrate tool calls → parse outputs → format the data exchange. |
| **Tools** | Bash execution, file operations, script execution. Needed because the model emits text, not compiled actions. |
| **Memory** | Short-term as plaintext/Markdown files; long-term via RAG and vector databases. |
| **State storage** | File-system JSON or a virtual abstraction over it. |

**Optional: sandbox.** An isolation layer for security when executing model-directed actions.

## Design patterns

The article catalogs a large set of patterns (it cites ~46); three representative ones:

- **Progressive disclosure** — don't front-load all context. Reference external files (e.g.
  `linter-js.md`) that load on demand, conserving the context window.
- **Advisor pattern** — separate decision from execution: delegate sub-tasks to smaller models,
  then aggregate their results through a larger coordinating model.
- **Escape hatch** — because models tend toward agreeable, people-pleasing output, provide a
  human override path. Example: a code-review agent offering "accept" or "route to manual
  review."

A related building block is the **skill**: a reusable, Markdown-defined harness component.

## Trade-offs

| Factor | Tension |
|---|---|
| **Complexity** | More sophisticated harnesses reduce low-quality output but raise maintenance burden. |
| **Cost** | Higher inference volume improves reliability but increases token consumption. |
| **Control** | Closed-source harnesses vs. open, inspectable implementations. |
| **Generalization** | Specialized harnesses excel at specific tasks but transfer poorly to others. |

## Failure modes to watch

- Harnesses growing into large, opaque monoliths that are hard to debug.
- Token consumption drifting upward through wasteful usage patterns.
- Treating prompt engineering as a substitute for architecture.
- Expecting deterministic output from an inherently probabilistic core, or expecting the system
  to run without human oversight.
- **Slop** — low-quality or incorrect generated output that accumulates without safeguards.

## Practical positioning

The article frames realistic gains at roughly **10–30%** when harnesses are built with
engineering discipline rather than treated as a turnkey productivity solution. Getting there is
presented as ordinary engineering rigor applied to a probabilistic component: testing and CI/CD,
strong observability, and human code review rather than blind acceptance of generated output.

> Reference implementations: Claude Code and Codex are described as production harnesses —
> "operational systems for agents." TypeScript + Ink is the common implementation stack today;
> the author favours Rust/Java/Scala for serious harness work.

### Seen in practice

The Claude Code environment this note was written in is itself a harness exhibiting these
patterns: **skills** as Markdown-defined components, **progressive disclosure** via on-demand
file/skill loading, tool integration for file and shell operations, and **escape-hatch**-style
permission prompts before consequential actions.

## Relationship to other notes

This note is deliberately concrete and component-level. It complements the higher-altitude uses
of "harness" elsewhere:

- [The Agentic SDLC](agentic-sdlc.md) — "the harness is the product" there means the
  evaluation/repair/policy *platform* that makes agent output safe. This note zooms in on how
  the harness program is actually built.
- [The AI-Native Engineering Stack](ai-native-engineering-stack.md) — the harness sits in the
  orchestration/skills layers of that stack.
- [Eval-Driven Development](eval-driven-ai-development.md) — the evaluation loops that keep a
  harness honest.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — escape hatches, tools,
  and human review are mechanisms that keep probabilistic output within a system's safe
  absorption capacity.

It also serves as a grounded, expectations-setting counterpart to the more bullish
strategy and maturity notes: harnesses deliver value, but as engineered systems with real
complexity, cost, and oversight requirements.
