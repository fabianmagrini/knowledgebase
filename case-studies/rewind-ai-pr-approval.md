---
type: case-study
title: Rewind's AI PR Approval Under Compliance
description: "A second production instance of unattended AI approval at 40% of PRs and ~$0.73 each: deterministic gates underneath the model, and controls mappings and risk assessments as first-class artefacts."
tags: [ai-engineering, code-review, governance, security, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/intercom-ai-pr-approval.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/dark-factories-examined.md
source: "https://rewind.com/blog/ai-approve-pull-requests-safely/"
updated: 2026-08-08
---

# Rewind's AI PR Approval Under Compliance

Dave North (Rewind, June 2026) reports a second production system where AI approves pull
requests without a human reviewer. It opens by naming its own prior art:

> Two companies published the playbook before us.

— crediting Intercom and Rootly. That is worth recording on its own: unattended AI approval
now has a **documented lineage** rather than being one company's experiment, which is a
stronger signal than any single account.

Rewind runs a multi-tenant backup SaaS with audit obligations, and the compliance framing is
what distinguishes this from [Intercom's account](intercom-ai-pr-approval.md).

## Two instances of the same practice

| | [Intercom](intercom-ai-pr-approval.md) | Rewind |
|---|---|---|
| PRs auto-approved | **19%** | **40%** |
| Cost per PR | not reported | **~$0.73** |
| Reported outcome | zero reverts across 100+ pilot PRs | zero incidents in early weeks |
| Distinguishing angle | accountability moves from reviewer to author | compliance artefacts and deterministic gates |

**The 2× gap in how much is handed over is the interesting number.** Both report no incidents,
so the difference is not obviously explained by one being more careful. Candidate readings,
none of them settled by the sources:

- Different codebases and risk profiles — a backup SaaS and a support product do not have the
  same blast radius per change
- Different refusal thresholds in the reviewer, which is the real dial (see below)
- Different appetite, helped by sequence: Rewind had Intercom's published playbook to
  calibrate against, and second movers can start further along

Read together they establish a **range** rather than a number. Anyone adopting this should
expect to tune the threshold rather than inherit one.

## Deterministic gates underneath the model

The design point most worth taking: AI approval sits **on top of** mechanical checks, not in
place of them. Tests, linting and the rest still gate the merge; the model decides only
whether the change is simple and aligned enough to skip human review.

That keeps the [CI/CD control plane](../engineering/ai-native/ci-cd-ai-engineering.md) doing
the load-bearing verification, and confines the probabilistic component to a judgement about
*scope and risk* rather than about *correctness*. It is a much narrower thing to trust a model
with, and it is why the practice can be defensible without the reviewer being excellent.

## Compliance as a first-class artefact

The genuinely new contribution. Removing a human approver in an audited environment is not
just an engineering decision — the control has to be shown to still exist in a different form:

- **Controls mappings** — demonstrating which audit control the automated approval satisfies,
  and how
- **Risk assessments** for the automation itself
- **Internal feedback loops and calibration** documented as an ongoing process, not a one-off
  validation

This is the missing AI-era chapter of
[Release Process for Regulated and High-Risk Services](../engineering/practices/regulated-service-release-process.md).
That note treats human approval as a control to be evidenced; Rewind's account is what it
looks like to evidence an *automated* approver instead. The obligation does not disappear —
it converts from "a named person signed off" into "here is the control, its risk assessment,
and its calibration record."

The named systems — **Diff Vader** (the reviewer) and **the Death Star** (the backend) — are
colour rather than substance, but they signal a built platform rather than a bot on a webhook.

## Reading the numbers

Both this and Intercom's account are **self-reported, early, and by the teams that built the
systems**. "Zero incidents in early weeks" is a genuinely short window against which to judge
a control that was previously staffed by humans, and the same selection effect applies as at
Intercom: the auto-approved population is chosen for simplicity, so its low incident rate is
partly a statement about the changes rather than about the reviewer.

The cost figure is more solidly useful. **~$0.73 per PR** is the first published unit economic
for this practice in these notes, and it makes the trade explicit: the question is not whether
AI review is cheap, but whether $0.73 and a residual risk beat the queueing cost of a human
reviewer who may be rubber-stamping anyway.

## Relationship to other notes

- [Intercom's AI PR Approval](intercom-ai-pr-approval.md) — the same practice, the prior art
  this one cites, and the source of the accountability-moves-to-the-author framing that Rewind
  inherits without restating.
- [Release Process for Regulated and High-Risk Services](../engineering/practices/regulated-service-release-process.md)
  — where the compliance obligations come from; this shows one way to satisfy them without a
  human approver.
- [CI/CD as the Control Plane](../engineering/ai-native/ci-cd-ai-engineering.md) — the
  deterministic layer that makes the probabilistic layer's job narrow enough to trust.
- [Code Review Policy](../engineering/practices/code-review-policy.md) — the human-approval
  requirement both case studies test; note that a refusal threshold is itself a risk tier.
