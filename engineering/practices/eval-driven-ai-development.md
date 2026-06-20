---
title: Eval-Driven Development for AI Capabilities
tags: [testing, ai-engineering, ci-cd]
topic: engineering/practices
status: notes
related:
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/ai-augmented-engineering-team.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/loop-driven-development.md
  - engineering/practices/spec-driven-development.md
source: "https://gist.github.com/fabianmagrini/4399048fc0f1dd2261a1c126589f29ec"
updated: 2026-06-20
---

# Eval-Driven Development for AI Capabilities

Prompts, agent skills, tools, and other model-defined capabilities are too often shipped on
a "vibe check" — validated by a few manual prompts and declared done. They are software and
deserve a test suite. **Eval-driven development** treats an AI capability as an engineered
artifact: define what success looks like, grade against it automatically, and iterate until
the behaviour is reliable.

> You wouldn't ship a library without a test suite — so don't ship a prompt or skill without
> one either. Don't just prompt; engineer the context.

This is the AI-behaviour counterpart to the [test coverage policy](test-coverage-policy.md)
and a core practice in the [AI-native engineering stack](ai-native-engineering-stack.md).

## The loop

1. **Define success with assertions.** Move from "it looks okay" to "it passed these 5
   checks." Express the expected behaviour as explicit, structured assertions (e.g. JSON)
   rather than a subjective read.
2. **Build an eval harness.** A small script that runs the capability against a set of
   inputs, captures the model's output, and grades each against the assertions. Wire it so
   it can run locally and in CI.
3. **Hill-climbing loop.** Run the suite, read the failures, refine the instructions, repeat.
   First runs commonly land around **40–60%** pass; the goal is consistent **100%** before
   shipping. The failures tell you exactly which instruction is ambiguous.
4. **Negative tests.** Assert the capability stays *inactive* when it shouldn't apply, and
   that it omits content it must never produce. A capability that fires (or leaks) on the
   wrong input is a bug, not a quirk.

## Assertion types

| Type | Checks |
|---|---|
| **Inclusion / exact** | Output contains a required string or value |
| **Regex** | Output matches a structural pattern |
| **Negative regex** | A forbidden string/pattern is *absent* |
| **Model-as-grader** | A model judges fuzzy criteria ("is this a clear, correct summary?") that rules can't express |
| **Activation / non-activation** | The capability triggers on relevant input and stays silent on irrelevant input |

Combine cheap deterministic checks (inclusion, regex) with model-as-grader only where
judgement is genuinely needed — deterministic assertions are faster, free, and stable.

## What moves the needle

- **The trigger/routing description dominates reliability.** However a capability decides
  *when* it applies (a description, a router prompt, a tool spec), that text matters more
  than the body. Vague triggers under-fire; overly broad triggers fire too often and bloat
  context. Tune it against activation *and* non-activation tests.
- **Use imperative instructions, not suggestions.** Directives ("Always do X", "Never do
  Y") are followed far more reliably than soft recommendations ("you may want to…").
- **Version everything.** Capability definitions, assertions, and harness live in the repo
  and change through review like any other code.

## Caveats

- Tooling for authoring AI capabilities (skill formats, routing mechanics, harness APIs)
  evolves quickly — treat the specific plumbing as point-in-time and the *method* as the
  durable part.
- 100% on a fixed suite means "passes the cases you thought of." Grow the suite as new
  failure modes appear in real use, the same way you add regression tests.
