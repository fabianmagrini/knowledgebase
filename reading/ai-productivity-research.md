---
type: reading
title: Five Studies on AI and Software Engineering Productivity
description: "A signpost to five peer-reviewed studies measuring what AI coding assistance actually does to output, delivery, and developer experience — including the finding that +180% commits yields only +30% releases."
tags: [ai-engineering, reading, governance]
topic: reading
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/light-and-dark-factories.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/apex-framework.md
  - engineering/ai-native/harness-design-experiments.md
  - leadership/revised-rules-engineering-leadership.md
  - leadership/learning-culture-ai-agents.md
  - reading/how-i-use-llms-2026.md
  - engineering/ai-native/own-the-outer-loop.md
source: "https://newsletter.getdx.com/p/five-studies-that-are-changing-how"
updated: 2026-08-03
---

# Five Studies on AI and Software Engineering Productivity

Brian Houck (*Engineering Enablement*, July 2026) collects five studies on what AI coding
assistance measurably does. This matters for these notes because the AI-native cluster is
otherwise built almost entirely on argument and self-reported company experience — this is
**peer-reviewed measurement** (four arXiv, one NBER working paper, one ACM Queue), and it
tests claims held elsewhere here on assertion alone.

A signpost note: it summarises the roundup and points at the primary sources rather than
standing in for them.

> Houck is a co-author on study 4 and publishes the newsletter. The studies stand on their
> own; the framing that they *converge on a single narrative* is his.

## 1. Copilot and completed work

*Heilman, Kyllo & Murphy-Hill (arXiv)*

**16,223 developers over 43 weeks**, compared **within-subject** — each engineer against
themselves in high- and low-usage weeks, controlling for active coding time. That design is
the notable part: it removes the selection bias that makes most tool-adoption studies hard to
read, since enthusiastic adopters no longer form a different population from the comparison
group.

- ~**40% more completed PRs per hour** in highest-usage weeks
- Effect **strongest on larger PRs** (7+ files), not trivial changes
- A dose-response pattern that **levels off** at very high usage
- Seven robustness tests reported as consistent

## 2. Writing code is not shipping code

*Demirer, Musolff & Yang — NBER*

**100,000+ GitHub developers**, tracing gains up the delivery hierarchy from lines of code
through commits, PRs, projects, and releases.

| Assistance level | Commits |
|---|---|
| Autocomplete | **+40%** |
| Interactive agents | **+140%** |
| Autonomous agents | **+180%** |

| But | |
|---|---|
| Releases actually shipped | **+30%** |

**This is the most useful number in the roundup.** The claim that generation is cheap and
verification is the binding constraint is asserted across
[Agentic Code Review](../engineering/ai-native/agentic-code-review.md),
[Light and Dark Software Factories](../engineering/ai-native/light-and-dark-factories.md),
[Backpressure Loops](../engineering/ai-native/agent-backpressure-loops.md) and the
[Revised Rules](../leadership/revised-rules-engineering-leadership.md) — none with data behind
it. Here the attenuation is measured: a **6× gap** between commit growth and release growth.

The paper also reports an **elasticity of substitution around 0.25**, meaning AI and human
effort behave as **complements rather than substitutes** — the headcount-replacement reading
is not what the data shows.

## 3. Productivity and experience come apart

*Vella & Blincoe (arXiv)*

**95 professional engineers**, six months, two questionnaires, mixed methods.

- **84%** reported productivity improvements at *both* timepoints — stable and positive
- Yet those reporting **worse developer experience rose from 14% to 27%**
- **Flow state** was the most vulnerable dimension; cognitive load eroded modestly; feedback
  loops improved
- Change scores showed **no correlation** between developer experience and productivity

The authors call this the **productivity-experience paradox**. It contradicts the common
assumption that the two move together, and nothing else in these notes anticipates it — the
[learning-culture](../leadership/learning-culture-ai-agents.md) note treats developer
experience and capability as broadly aligned. Worth holding as an open question rather than a
settled result: it is 95 people and self-report on both axes.

## 4. Bounded delegation

*Choudhuri, Badea, Bird, Butler, DeLine & Houck (arXiv)*

**860 Microsoft developers** across roles, domains and geographies.

The central concept is **bounded delegation**: developers want AI for tedious assembly work
and decline to hand over core logic and architectural decisions — **even for tasks AI could
plausibly handle**. Capability gaps do not explain where the line falls, which makes this a
statement about judgement and accountability rather than model quality.

Also reported:
- **22 AI systems** developers want *beyond* code generation, weighted toward verification —
  incident case files, PR logic review, test generation
- A **right-shift bottleneck**: accelerating generation pushes load downstream into review and
  integration
- Four guardrails treated as non-negotiable: **explicit authority scoping, data provenance,
  uncertainty signalling, least-privilege access**

The bounded-delegation result is the empirical counterpart to the delegation lines drawn from
experience in [How I Use LLMs](how-i-use-llms-2026.md) and
[Own the Outer Loop](../engineering/ai-native/own-the-outer-loop.md).

## 5. Cognitive debt and intent debt

*Storey — ACM Queue*

A reframing of software health into three interacting debts:

| Debt | Lives in | Description |
|---|---|---|
| **Technical** | Code | Implementation compromises — the kind AI is genuinely good at reducing |
| **Cognitive** | People | Eroded shared understanding, accruing when developers accept AI output without building a mental model |
| **Intent** | Artefacts | Unclear goals, constraints and rationale — a first-order constraint on safe AI assistance |

Storey's mechanism for cognitive debt is the **"accumulation of not knowing"**, and the
argument is that the three compound rather than sitting independently, so understanding has to
be treated as a first-class deliverable alongside code.

This lands on vocabulary already held here: `agentic-code-review.md` carries **comprehension
debt** and **intent debt** from Addy Osmani's essay. Storey reaches a near-identical taxonomy
through peer-reviewed work, which is worth recording as **independent convergence** rather
than repetition — the same idea arrived at from two directions is stronger than either alone.

## What the roundup concludes

> "We're generating code faster than we're generating the systems needed to safely understand,
> verify, and deliver it."

The bottleneck has moved from typing to review, integration and understanding, and existing
metrics and team processes do not reflect the shift. That is the same conclusion much of this
knowledge base already reaches — the contribution here is that it now has measurement under
it.

## Relationship to other notes

- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — carries
  vendor-reported figures it explicitly flags as unreliable; these studies are the
  better-evidenced version of the same argument.
- [The APEX Framework](../engineering/ai-native/apex-framework.md) — measuring whether AI
  adoption creates value; study 2 is why measuring at the *commit* layer misleads.
- [Harness Design for Long-Running App Development](../engineering/ai-native/harness-design-experiments.md) —
  the other measured source here, though its numbers are self-reported rather than peer-reviewed.
