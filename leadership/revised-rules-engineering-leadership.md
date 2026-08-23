---
type: note
title: Revised Rules of Engineering Leadership
description: "Will Larson revises his rules of engineering leadership for an era where AI tooling sharply accelerates execution."
tags: [leadership, ai-engineering, decision-making, reading]
topic: leadership
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - leadership/decision-facilitation.md
  - leadership/staying-technical-as-a-manager.md
  - concepts/theory-of-constraints.md
  - leadership/engineering-leadership-overview.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - case-studies/portkey-product-engineer-company.md
  - engineering/ai-native/agentic-code-review.md
  - reading/ai-productivity-research.md
  - product/prioritisation-as-a-symptom.md
  - case-studies/anthropic-ai-native-teams.md
source: "https://lethain.com/revised-rules-of-engineering-leadership/"
updated: 2026-07-26
---

# Revised Rules of Engineering Leadership

Will Larson revises his rules of engineering leadership for an era where AI tooling
sharply accelerates execution. His central tension: **execution got cheap, but
choosing *what* to execute stayed hard.** The revision is prompted by working in a
**hypergrowth environment**, which he characterises by its compressed feedback loop:
mistakes reveal themselves monthly rather than yearly, so rules that were merely
suboptimal at a slower pace become visibly costly. Success, he argues, comes not from
individual genius but from **durable teams making quick, good decisions inside a
robust development harness** that automates the base case. This is, at the
leadership altitude, the same bottleneck shift as
[Theory of Constraints](../concepts/theory-of-constraints.md): relieve the
execution constraint and the constraint moves to decision-making.

## The five rules

1. **Migrations can be individual efforts.** AI lets one person or small team own
   ~95% of even a complex, large change in ~10% of the time. As migration cost
   falls, *quality* matters more — a small mistake breaks colleagues' mental models
   of a shared codebase — so individual judgment now carries more organisational
   weight.
2. **Working code still has real costs, even when first-pass code is cheap.**
   Production quality depends on the **development harness** — tests, CI/CD,
   validation and preview environments. Notably, "the things that were most
   valuable to speed up engineering two years ago are still the things that are
   most valuable today"; broad participation in coding still needs safe boundaries.
   The failure mode when those boundaries are missing is what he calls **slop pull
   requests** — cheap submissions that poison context and degrade outcomes rather
   than adding to them.

   > Note on terminology: Larson's "development harness" means the delivery
   > infrastructure — tests, CI/CD, validation and preview environments. It is a
   > different concept from the harness in
   > [Harness Engineering](../engineering/ai-native/harness-engineering.md), which is
   > the orchestration program an LLM runs inside. Same word, different layer.

3. **Optimise base-case processes for automation.** Most steps of most processes
   can be automated in most cases; agents should handle routine, lower-risk work
   better than humans, while humans take the exceptions and higher-stakes calls.
   Planning operates "at a higher level" than traditional sprints.
4. **Durable teams with domain context remain essential.** Persistent teams
   accumulate context, camaraderie, and ownership. The competing "genius engineers
   creating perfect solutions" vision underestimates how much **lack of domain
   context** constrains a lone contributor; durable teams stay the fundamental
   building block.
5. **Quick, good, durable decision-making is what unlocks the benefits.**
   Automation only pays off when stakeholders commit to changes through design and
   collaboration: "your team and company can only benefit from this increased pace
   ... if you can make durable decisions quickly, and those decisions are good."
   Hence CTOs must become "substantially more technical and less bureaucratic" —
   making binding decisions constantly to keep pace.

## The through-line

The first three rules say execution and routine process are cheap and increasingly
individual/automated; the last two say the scarce, leadership-owned goods are
**durable teams** and **fast, good decisions**. When technical speed rises,
organisational decision speed has to match it or it becomes the new bottleneck.

What actually slows an organisation down, once execution is no longer the
constraint, he names as three sources of friction:

| Friction | What it looks like |
|---|---|
| **Misalignment** | Stakeholders have not committed to the same change |
| **Lack of clarity** | The decision exists but nobody can say what it was |
| **Poor technical architecture** | The system itself resists the change being made |

This is the diagnosis under rule 5. Two of the three are decision defects rather
than technical ones, which is why he lands on decision-making as the leadership
obligation rather than on tooling.

## Larson's examples (his reported figures)

Treat these as the author's reported examples, not general benchmarks: deployment
frequency raised 20–30× year-over-year via an infrastructure overhaul (two
engineers, two months); AI-tool adoption moving 25% → 100% by *removing friction*
rather than mandating; several one-engineer, one-month migrations (frontend
mono-repo, static typing, configuration unification); customer-issue triage
automated with agents handling the base case and humans the exceptions, with the
agent given access to the data warehouse and ticket history; and code review split
so that agents take the first pass while humans keep the higher-value feedback (the
same division of labour argued at length in
[Agentic Code Review](../engineering/ai-native/agentic-code-review.md)). Tools he
names — Claude Code, Cursor, Linear, SierraAI — are cited as enabling examples, not
endorsements.

## Relationship to other notes

- [The AI-Augmented Engineering Team](../engineering/ai-native/ai-augmented-engineering-team.md) —
  the *operating model* these leadership rules imply (team composition, the delivery
  loop); this note is the leadership-altitude principles behind it.
- [Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) —
  the complementary point that Agile principles and sustainable pace persist; both
  argue human judgement, not raw speed, is the binding factor.
- [Facilitating Technical Decisions](decision-facilitation.md) — rule 5 in
  practice: how to make durable group-owned decisions quickly.
- [Theory of Constraints](../concepts/theory-of-constraints.md) — the bottleneck
  moving from execution to decision-making when AI relieves the coding constraint.
