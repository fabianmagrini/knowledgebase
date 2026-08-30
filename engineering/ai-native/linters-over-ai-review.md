---
type: note
title: Linters Over AI Review
description: "The cost and latency case against AI code review at volume: $1,000/week versus 27 seconds, and feedback in the editor rather than at PR time — the counterweight to a cluster that otherwise assumes AI review is worth doing."
tags: [ai-engineering, code-review, testing, ci-cd, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-code-review.md
  - case-studies/cloudflare-ai-code-review.md
  - engineering/architecture/enforced-architecture-rules.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/practices/code-review-policy.md
  - case-studies/intercom-ai-pr-approval.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - case-studies/doordash-ai-code-review.md
  - case-studies/rewind-ai-pr-approval.md
  - engineering/ai-native/review-replacement.md
  - concepts/control-and-complexity.md
source: "https://swizec.com/blog/stop-burning-tokens-on-code-review"
updated: 2026-08-29
---

# Linters Over AI Review

Swizec Teller (August 2026) argues that custom linters beat AI code-review tools on cost,
speed and fit — from a team handling **2,900 PRs and 10 reviews a day**.

These notes hold five accounts of AI code review — [the principles](agentic-code-review.md),
[Cloudflare](../../case-studies/cloudflare-ai-code-review.md),
[DoorDash](../../case-studies/doordash-ai-code-review.md),
[Intercom](../../case-studies/intercom-ai-pr-approval.md),
[Rewind](../../case-studies/rewind-ai-pr-approval.md) — all concerned with doing it *well*.
None asks whether it is the right tool. This is that question.

One team's experience at one scale. No comparison of what each approach actually *caught*, and
he concedes AI review catches occasional valuable issues — the argument is about ratio, not
about it finding nothing.

## The reported costs

| Approach | Cost / speed |
|---|---|
| Cursor BugBot | **~$1,000 per week** |
| Claude review skills on GitHub Actions | **~$1,000 in a single day** |
| Custom linters | **27 seconds** maximum, pre-commit and in-editor |

Worth reading against [Cloudflare](../../case-studies/cloudflare-ai-code-review.md), which
reports a **median $0.98 per review** across 131,246 reviews in a month and treats that as a
success. Both can hold — cost per review is not cost per week, and the value of a catch
differs by codebase — but until now these notes recorded only the side where the economics
work.

The general point survives the specific figures: **AI review has a per-PR marginal cost and a
linter has close to none.** That difference compounds with volume, and volume is exactly what
agent-written code produces.

## The stronger argument is latency

Cost is the headline; placement is the better case.

AI review fires **at PR time**, and he reports 10–30 minutes to get comments. A linter fires
**in the editor**, as squiggly lines, and again at pre-commit — before a PR exists at all.

That is [Backpressure Loops for Coding Agents](agent-backpressure-loops.md)' own argument
turned against AI review. That note holds that mechanical feedback belongs in fast loops the
author — human or agent — can act on immediately, rather than in slow human-loop checks. **AI
review at PR time is a slow loop wearing automation's clothes**: it arrives after the work is
packaged, minutes later, at a point where acting on it means a new commit and another round.

Read that way, the choice is not "AI or linter" but *which loop the check belongs in*. Anything
deterministic enough for a linter is being run in the wrong place if it waits for a PR.

## What he objects to

- **Generic and poorly tuned** — not aligned to what this team actually cares about
- **Noisy**, with false positives he calls *"invented security concerns"*
- **Misses architectural concerns** the team does prioritise — so it is loud about the wrong
  things and quiet about the right ones

His term for tools in this mode: **slop cannons**.

## Building the linters from the docs

The practice worth keeping: derive rules **from the team's existing documentation**, so written
standards become executable ones. His examples — `no-raw-color`, `descriptive-test-names`,
`check_import_direction`, and a prose linter (`vale-de-blab`) for **de-blabbing** documentation.

This overlaps substantially with
[Enforced Architecture Rules](../architecture/enforced-architecture-rules.md) — `check_import_direction`
*is* Tune's layer rule, and "deterministic enforcement beats written instruction" is that
note's thesis. The addition here is the **economic argument for preferring it**, and the
observation that the documentation you already have is the specification for the rules.

It also inverts a common complaint. Standards documents are usually criticised for being
ignored; the proposal is to treat them as a **backlog of lint rules** — every guideline
nobody follows is a candidate for mechanical enforcement.

## What this does not argue

Being precise about the scope, since the title overstates it:

- **Not that AI review finds nothing.** He credits it with occasional valuable catches.
- **Not that everything is lintable.** Architectural concerns are what he says the AI *missed*
  — and they are also what a linter cannot express. Neither tool covers them, which leaves
  them with the human reviewer.
- **Not applicable at low volume.** The economics turn on 2,900 PRs; at ten PRs a week
  $1,000/week is not the comparison being made.

The defensible version: **run everything deterministic as a linter at edit time, and reserve
paid probabilistic review for what is genuinely ambiguous** — which is the tiering that
[Agentic Code Review](agentic-code-review.md) already prescribes, with the threshold moved
considerably further toward the deterministic end.

## Relationship to other notes

- [Agentic Code Review](agentic-code-review.md) — the principles for doing AI review well;
  this asks what should not go to AI review at all, and moves the tiering threshold.
- [Cloudflare's AI Code Review System](../../case-studies/cloudflare-ai-code-review.md) — the
  economics working at scale, against which these figures are the counter-case.
- [Enforced Architecture Rules](../architecture/enforced-architecture-rules.md) — the same
  deterministic-over-probabilistic thesis, argued from correctness rather than cost.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — the loop-placement
  argument this note applies against AI review itself.
