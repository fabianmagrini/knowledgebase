---
type: reading
title: Offloading Thinking to AI
description: "Yennie Jun distinguishes automating menial work from delegating thinking itself, and argues the second erodes autonomy — the counterweight to a knowledge base otherwise organised around delegating more."
tags: [ai-engineering, culture, reading]
topic: reading
status: notes
level: beginner
related:
  - reading/how-i-use-llms-2026.md
  - reading/building-software-is-learning.md
  - leadership/learning-organisation.md
  - leadership/learning-culture-ai-agents.md
  - engineering/ai-native/agentic-code-review.md
source: "https://www.artfish.ai/p/offloading-thinking-to-ai"
updated: 2026-07-26
---

# Offloading Thinking to AI

Yennie Jun, who works on measuring AI capabilities, asks whether we are delegating too much
of our *thinking* — as opposed to our labour — to AI systems.

**This is a personal essay, not a study.** Jun is explicit that the argument rests on
observation and reflection. The cited material — METR's task-completion time horizons, an
OECD report on AI in the workplace, an ILO report on digital platforms, and Ken Liu's 2012
short story *The Perfect Match* — supplies context rather than evidence for the central
claim. It is filed here for the distinction it draws, which is sharper than most treatments
of the topic, not for its empirical weight.

## The distinction

The argument turns on one line that the rest of the essay elaborates:

> Automating **menial work** is not the same as automating **thinking**.

The first is the ordinary case for tooling and is not in dispute. The second is the essay's
concern: handing over not the execution of a decision but the *forming* of it.

Jun's supporting observations:

| Observation | The claim |
|---|---|
| **The convenience trap** | Search engines forced you through intermediate steps — assembling sources, comparing them, reaching a view. Systems that return a finished answer remove those steps, making it effortless to skip the reasoning rather than choosing to. |
| **Autonomy erosion** | The worry is not delegating *tasks* but delegating *preferences* — what to eat, listen to, care about. Outsourcing preference formation means gradually losing contact with what you actually want. |
| **Learning versus efficiency** | A fast, correct answer can bypass the cognitive struggle that *is* the learning. Efficiency and understanding are not the same good, and the tool optimises the first. |

## The counter-practice

Jun's response is not abstinence but deliberate, occasional friction — doing the thinking
manually on purpose. The examples given are writing notes by hand on a plane with no
internet, and returning to analysing their own data by hand after previously handing it to a
model. The point is to keep the capability exercised rather than to reject the tool.

The essay also draws a line between queries that are genuinely trivial and worth forgetting,
and consequential thinking that is worth doing yourself. It does not offer a test for
telling them apart, which is the obvious thing one would want from it.

## Why it is filed in an engineering knowledge base

*This section is the note's own reading, not Jun's argument.* The essay is about ordinary
life — travel, food, study, family — and makes no claim about software teams. The
distinction it draws, however, transfers directly, and is the counterweight to a great deal
of what is recorded elsewhere here:

- [How I Use LLMs as a Staff Engineer (2026)](how-i-use-llms-2026.md) is organised around
  *"shift as much work onto AI"* and reads as a delegation map. Jun supplies the question
  that map does not ask — which of those handoffs cost something that matters.
- [Building Software Is Learning](building-software-is-learning.md) argues that building new
  software *is* an iterative learning process. If that is right, then delegating the
  building delegates the learning, and Jun's efficiency-versus-understanding trade-off is
  the same trade-off restated at the level of a codebase.
- **Comprehension debt** — un-understood code that becomes someone's on-call incident, per
  [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — is arguably what
  offloaded thinking looks like once it reaches production. Jun describes the individual
  version of a failure mode that note describes organisationally.

The engineering translation of the counter-practice is not obvious, and this note does not
claim to have it. "Occasionally do it by hand to keep the skill" is straightforward advice
for an individual and an unresolved question for a team under delivery pressure — which is
closer to the territory of
[The Learning Organisation and AI Adoption](../leadership/learning-organisation.md).

## Relationship to other notes

- [How I Use LLMs as a Staff Engineer (2026)](how-i-use-llms-2026.md) — where to draw the
  delegation line, argued from efficiency; this note argues the same line from what is lost.
- [A Learning Culture for AI-Augmented Teams](../leadership/learning-culture-ai-agents.md) —
  the team-level problem of keeping people learning as agents absorb the work.
- [The Learning Organisation and AI Adoption](../leadership/learning-organisation.md) — the
  organisational conditions that make deliberate, non-productive practice affordable.
