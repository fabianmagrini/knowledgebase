---
title: The New SDLC with Vibe Coding (Kaggle / Osmani et al.)
tags: [ai-engineering, agentic-workflows, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-sdlc-terminology.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/ai-factory.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/ai-native/scaling-ai-adoption.md
source: "https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding"
updated: 2026-07-03
---

# The New SDLC with Vibe Coding (Kaggle / Osmani et al.)

A ~50-page whitepaper by Addy Osmani, Shubham Saboo, and Dr. Sokratis Kartakis,
released with Kaggle's 5-day AI Agents course. Despite the title, it is really
about the shift from *coding* → *vibe coding* → *agentic engineering*, and argues
the real differentiator is **not whether you use AI, but how outputs get
verified.**

## Core thesis

AI compresses the software lifecycle *unevenly*. Implementation collapses from
weeks to hours, but requirements, architecture, and verification stay
judgment-intensive — so **specification quality and verification become the
bottleneck**, not typing. The job shifts from *writing code to judging it*.

## Vibe coding vs. agentic engineering (a spectrum)

The two sit at opposite ends of a **verification-rigor spectrum**, not a
tool choice:

- **Vibe coding** — casual natural-language prompts, accept the output, paste the
  error back when it breaks. Fast, fun, great for prototypes; high-risk in
  production. Cheap upfront but expensive long-term (token burn, maintenance tax,
  security cleanup). *"Vibe coding is not vibe in production."*
- **Agentic engineering** — formal specs, automated evals, CI/CD gates. Higher
  initial investment, flatter cost curve, and reportedly **3–10× lower per-feature
  cost** past the crossover point.

This maps directly onto the vocabulary in
[AI in the SDLC — Terminology](../engineering/ai-native/ai-sdlc-terminology.md).

## Agent = model + harness

An agent is roughly **10% model, 90% harness** — instructions/rule files, tools
and MCP servers, sandboxes and sub-agent orchestration, deterministic hooks, and
observability. Cited proof: a team reached the Terminal Bench 2.0 top 5 by
changing *only the harness* with an identical model. **Most agent failures are
configuration failures, not model failures** — which is encouraging, because the
harness can be fixed immediately. This is the paper's version of
[Harness Engineering](../engineering/ai-native/harness-engineering.md).

## How each SDLC phase changes

| Phase | Shift |
|---|---|
| Requirements | A conversation that produces spec *and* prototype at once; agents draft stories and surface edge cases |
| Architecture | Stays stubbornly human — the developer makes structural decisions the agent implements |
| Implementation | 25–39% productivity gain (or ~19% *slower* once review time is counted); writing → reviewing |
| Testing/QA | Flips from downstream to *primary*: tests and evals become the specification mechanism |
| Maintenance | Code once "too risky" becomes readable/refactorable by agents; migrations finally happen |

## Frameworks worth keeping

- **Context engineering** — six context types (instructions, knowledge, memory,
  examples, tools, guardrails), split into **static** (always loaded, reliable,
  costly) vs **dynamic** (loaded on demand, low marginal cost). The static/dynamic
  boundary should be **versioned like code and reviewed in PRs**.
- **Agent skills with progressive disclosure** — metadata at startup, full
  instructions on match, heavy reference only when needed — so dozens of skills
  don't all cost tokens at once.
- **Two operating modes** — **Conductor** (real-time, IDE-integrated, keystroke by
  keystroke — for exploration) vs **Orchestrator** (async goal-setting with agent
  review — for well-specified work).

## Verification: the real subject

- **Tests** cover deterministic input→output parts.
- **Output evals** verify the final result is correct.
- **Trajectory evals** verify the *reasoning path and tool use* — arguably more
  critical, since a right answer reached by skipping checks is dangerous.

Guardrails live in rule files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) and in core
static context; progressive disclosure prevents **context collapse**. This is the
eval-first stance of
[Eval-Driven Development](../engineering/ai-native/eval-driven-ai-development.md).

## The 80% problem

Agents reach ~80% of a feature quickly; the last 20% (edge cases, system seams)
still needs domain context the model lacks — which is where human judgment
concentrates.

## Terminology & numbers

- **Terms:** harness engineering, factory model, orchestration tax, prompting tax,
  context collapse, the 80% problem, trajectory evaluation.
- **Adoption (early 2026):** 85% of pro developers use AI coding agents regularly;
  51% daily; ~41% of new code is AI-generated.
- **Economics:** implementation compression gives 25–39% gains (surveys); a METR
  study found experienced devs 19% slower once verification is counted; model
  routing (cheap models for routine work, expensive for hard reasoning) is a
  direct TCO lever.

## Why it matters here

The "factory model" and per-agent harness echo [The AI Factory](../engineering/ai-native/ai-factory.md);
the spec-as-bottleneck point reinforces
[Spec-Driven Development](../engineering/ai-native/spec-driven-development.md); and
getting an organisation to the agentic-engineering end of the spectrum is exactly
the readiness work in
[Scaling AI Adoption in the SDLC](../engineering/ai-native/scaling-ai-adoption.md).
