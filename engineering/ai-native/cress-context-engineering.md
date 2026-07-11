---
title: CRESS Principles for Context Engineering
tags: [ai-engineering, agentic-workflows, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/prompt-engineering-for-programmers.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/eval-driven-ai-development.md
  - tools/claude-code-steering-mechanisms.md
  - reading/agentic-ai-architecture-emag.md
  - case-studies/doordash-ai-code-review.md
source: "https://codemanship.wordpress.com/2026/05/04/c-r-e-s-s-principles-for-context-engineering/"
updated: 2026-07-05
---

# CRESS Principles for Context Engineering

Jason Gorman (Codemanship) offers **CRESS** as a mnemonic for the properties an LLM's *context*
should have to reliably generate code. The framing shifts attention from *how you word the
prompt* to *what qualities the information you feed the model must satisfy* — context
engineering rather than prompt wording. Gorman presents CRESS as validated by his own multi-year
closed-loop experiments, but publishes no metrics here and explicitly invites readers to test
the principles independently rather than take his word for it.

## The five principles

| Letter | Principle | Meaning |
|---|---|---|
| **C** | **Current** | Up-to-date information — not stale architecture summaries or outdated docs |
| **R** | **Refutable** | Includes a way to tell when output fails to meet intent (e.g. acceptance tests) |
| **E** | **Empirical** | Grounded in observable reality — actual code, test results, linter output — not model-generated content or assumptions |
| **S** | **Small** | Only the minimum necessary; strip redundant background, irrelevant history, and verbose noise |
| **S** | **Specific** | Narrowly scoped to a single problem with no ambiguity of intent |

The two failure directions the acronym guards against: context that is **wrong or unverifiable**
(stale, assumed, unrefutable) and context that is **noisy or diffuse** (bloated, unscoped).

## How the principles connect to existing practice

- **Refutable** is where context engineering meets
  [eval-driven development](eval-driven-ai-development.md): acceptance tests and evals are the
  concrete mechanism that lets the loop detect a miss instead of trusting agreeable output.
- **Empirical** is the discipline of feeding the model *observed* artefacts (test runs, linter
  output, the real code) rather than a summary the model itself produced — closing the gap where
  hallucinated or second-hand context creeps in.
- **Small** is the goal that [harness](harness-engineering.md) patterns like *progressive
  disclosure* exist to serve — load context on demand so the window stays lean and signal-dense.
- **Specific** overlaps with the specificity principle in
  [prompt engineering](prompt-engineering-for-programmers.md), applied to the context payload
  rather than the human's question.

## Relationship to other notes

- **[Prompt Engineering for Programmers](prompt-engineering-for-programmers.md)** — about
  *writing the prompt* as an interactive dialogue. CRESS is about the *properties of the context*
  the agent operates on; the two overlap only on "Specific".
- **[Claude Code Steering Mechanisms](../../tools/claude-code-steering-mechanisms.md)**
  — those mechanisms decide *where* context lives (CLAUDE.md, rules, skills…); CRESS decides
  *what qualities* that context needs to be worth loading.
- **[Harness Engineering](harness-engineering.md)** — progressive disclosure and tool
  integration are how a harness delivers Current, Empirical, and Small context in practice.
- **[Eval-Driven Development](eval-driven-ai-development.md)** — the Refutable principle in its
  fullest form: evaluation loops as the success/failure signal.
