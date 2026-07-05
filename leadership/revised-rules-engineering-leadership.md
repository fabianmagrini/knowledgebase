---
title: Revised Rules of Engineering Leadership
tags: [leadership, ai-engineering, decision-making, reading]
topic: leadership
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - leadership/decision-facilitation.md
  - concepts/theory-of-constraints.md
  - leadership/engineering-leadership-overview.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - case-studies/portkey-product-engineer-company.md
source: "https://lethain.com/revised-rules-of-engineering-leadership/"
updated: 2026-06-20
---

# Revised Rules of Engineering Leadership

Will Larson revises his rules of engineering leadership for an era where AI tooling
sharply accelerates execution. His central tension: **execution got cheap, but
choosing *what* to execute stayed hard.** Success, he argues, comes not from
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

## Larson's examples (his reported figures)

Treat these as the author's reported examples, not general benchmarks: deployment
frequency raised 20–30× year-over-year via an infrastructure overhaul (two
engineers, two months); AI-tool adoption moving 25% → 100% by *removing friction*
rather than mandating; several one-engineer, one-month migrations (frontend
mono-repo, static typing, configuration unification); customer-issue triage
automated with agents handling the base case and humans the exceptions. Tools he
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
