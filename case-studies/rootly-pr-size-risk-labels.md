---
type: case-study
title: Rootly Dropped Its Small-PR Rule
description: "Rootly retired a two-year small-PR rule once agents authored most of its code, replacing diff-size limits with risk labels, an AI reviewer that classifies rather than nitpicks, feature flags as the safety gate, and a PR template demanding a revert plan."
tags: [ai-engineering, code-review, agentic-workflows, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-code-review.md
  - engineering/practices/code-review-policy.md
  - case-studies/cloudflare-ai-code-review.md
  - case-studies/doordash-ai-code-review.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/practices/rollback-and-roll-forward.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/intercom-ai-pr-approval.md
  - case-studies/rewind-ai-pr-approval.md
  - concepts/control-plane-data-plane.md
source: "https://rootly.com/blog/why-we-got-rid-of-our-small-pr-rule"
updated: 2026-07-26
---

# Rootly Dropped Its Small-PR Rule

Rootly enforced a small-PR rule — diffs under a few hundred lines — for two years, on the
standard reasoning that "smaller diffs are easier to review, easier to revert, easier to
reason about". They report retiring it once AI agents were authoring **over 80%** of their
code, and replacing the size constraint with risk classification.

This is a single company's experience report on a vendor blog, with no external data. The
80%+ authorship figure is self-reported and is load-bearing for the entire argument — a team
where agents write a fifth of the code has not met the condition that broke the rule.

## Why they say the rule stopped working

Their claim is that the rule's usefulness depended on a constraint that no longer binds. A
human writing a feature produces it incrementally, so small PRs match how the work arrives.
An agent produces the whole feature — migration, model, service, tests, UI — as one atomic
unit, and splitting it afterwards is work performed purely to satisfy the rule:

- Reviewers must understand the entire feature to review any slice of it, so stacking buys
  no reduction in what has to be held in the head
- Cross-PR dependencies made review *harder* rather than easier
- The splitting itself was "busywork with no upside"

The supporting argument is the sharpest line in the piece: **"AI bugs are context bugs. The
code works, but it's applied to the wrong thing."** If the characteristic agent failure is
misapplication rather than local defect, then line count measures the wrong property — risk
lives in blast radius and shared boundaries, which are uncorrelated with diff size.

## What replaced it

| Mechanism | What it does |
|---|---|
| **`risk:low` / `risk:medium` / `risk:high` labels** | Scrutiny keyed to production impact instead of line count |
| **An internal AI reviewer** | Flags dangerous patterns — migrations, security changes, core workflows — and *assigns a risk classification*, rather than giving style feedback |
| **Feature flags as the safety gate** | Moves the decisive control from merge-time to progressive rollout, so a kill-switch exists before broad exposure |
| **A structured PR template** | Requires a revert plan, rollback procedure, and deployment checklist — in place of a size limit |

The through-line: they did not lower the bar, they **moved the gate**. Merge stops being the
moment of maximum scrutiny, and rollout becomes it. That only works if the flag and rollback
machinery is genuinely reliable — see
[Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
and [Rollback and Roll Forward](../engineering/practices/rollback-and-roll-forward.md).

## The disagreement worth noting

Rootly's risk-tiering is not itself novel — it is close to what
[Agentic Code Review](../engineering/ai-native/agentic-code-review.md) and
[Code Review Policy](../engineering/practices/code-review-policy.md) already prescribe, and both
of those already tier on blast radius rather than authorship. The interesting part is that
Rootly reaches the **opposite conclusion on one specific point**:

| Position | Claim |
|---|---|
| Addy Osmani (tiering point 4 in [Agentic Code Review](../engineering/ai-native/agentic-code-review.md)) | Keep PRs small; instruct agents to produce digestible commits, because large diffs get rejected or rubber-stamped |
| Rootly | Size is the wrong axis; forcing an agent-authored feature into small PRs is busywork that degrades review |

Both accept that review is the binding constraint and both tier by risk. They diverge on
whether diff size remains a useful proxy once agents write the code. Osmani's worry — that
large diffs get rubber-stamped — is a claim about *reviewer behaviour*, which Rootly does not
directly rebut; they argue instead that the split doesn't reduce what must be understood.
The positions are reconcilable if you read Rootly as saying size should not be a *gate*,
while Osmani is saying it remains a *risk signal*.

## Relationship to other notes

- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — the principles this
  case study both instantiates (tier by blast radius) and partly disputes (keep PRs small).
- [Code Review Policy](../engineering/practices/code-review-policy.md) — a policy that currently
  sets 200–400 line review thresholds and lists overly large PRs as an anti-pattern; Rootly is
  the counterargument to that specific threshold, not to the risk tiers, which already agree.
- [Cloudflare's AI Code Review System](cloudflare-ai-code-review.md) and
  [DoorDash's AI Code Reviewer](doordash-ai-code-review.md) — both build the AI reviewer as a
  detection system; Rootly's reviewer is unusual in that its output is a *risk classification*
  used to route the human's attention.
