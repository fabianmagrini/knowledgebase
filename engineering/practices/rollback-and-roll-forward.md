---
type: note
title: Rollback and Roll Forward
description: "The two ways to recover from a bad production change, and when each is the right call."
tags: [ci-cd, observability, testing]
topic: engineering/practices
status: notes
level: intermediate
related:
  - concepts/continuous-delivery.md
  - concepts/progressive-delivery.md
  - engineering/practices/gitops.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/practices/release-confidence.md
  - concepts/devops-capability-model.md
  - sre/incident-swarming.md
  - engineering/practices/database-migration-strategies.md
source: "Jez Humble & David Farley — Continuous Delivery (2010); Google — Site Reliability Engineering"
updated: 2026-06-21
---

# Rollback and Roll Forward

When a change reaches production and turns out to be bad, there are two ways to
recover:

- **Rollback** — return the system to the previous known-good version, undoing the
  change.
- **Roll forward** (or *fix forward*) — leave the change in place and ship a *new*
  version that corrects the problem.

Both restore service; they trade off differently on speed, certainty, and what is
even *possible* given the nature of the change. The decision is usually made under
pressure during an [incident](../../sre/incident-swarming.md), so the real work is
done beforehand — in making rollback safe and the choice obvious.

## The core trade-off

| | Rollback | Roll forward |
|---|---|---|
| **Speed to recover** | Fast — restore a tested, known-good state | Slower — write, test, and ship a new fix |
| **Certainty** | High — that version already worked | Lower — the fix is unproven, written under stress |
| **Cognitive load mid-incident** | Low — a mechanical, rehearsed action | High — diagnosing and coding while degraded |
| **When it fails** | Irreversible changes (data, schema, external side-effects) | Rarely impossible, but risky if the fix is wrong |

The default during an incident should be **rollback**: it returns to a state you
*know* worked, with the least thinking required when thinking is hardest. Roll
forward is the choice when rollback is impossible or more dangerous than the bug.

## When you must roll forward

Rollback assumes the change is *reversible*. It often isn't:

- **Destructive database migrations** — a dropped column or transformed data can't
  be un-dropped by redeploying old code.
- **Stateful side-effects** — emails sent, payments taken, messages published to
  other systems.
- **Forward-only data** — once new-format data has been written, the old code may
  no longer be able to read it.

In these cases the previous artifact won't run correctly against the changed world,
so the only path is forward: ship a fix that tolerates or repairs the new state.

## What makes rollback safe: backward compatibility

Rollback is only as safe as the **compatibility between adjacent versions**. The
discipline that buys it is **expand/contract** (a.k.a. *parallel change*),
especially for schema and API changes:

```text
Expand    — add the new column/field/endpoint; write to both old and new
Migrate   — backfill; move readers to the new shape; both versions coexist
Contract  — remove the old column/field/endpoint, only once nothing reads it
```

By never coupling a single deploy to a breaking, irreversible schema change, each
deploy stays individually reversible. This is the same decoupling principle behind
[feature flags](feature-flags-and-branch-by-abstraction.md): keep code deployment
separate from the risky state change, so you can undo one without the other.

## Mechanisms

Recovery isn't a single action — pick the cheapest one that works:

| Mechanism | Recovers by | Notes |
|---|---|---|
| **Feature-flag kill switch** | Flipping the new path off | Fastest — *neither* a deploy nor a rollback; instant and reversible |
| **Redeploy previous artifact** | Promoting the last known-good build | The classic rollback; relies on build-once, immutable artifacts |
| **Blue-green switch** | Routing traffic back to the old environment | Near-instant if the old stack is still warm |
| **Canary abort** | Halting and reversing a [progressive rollout](../../concepts/progressive-delivery.md) | Often automated against guardrail metrics |
| **`git revert`** | Reverting the commit in the GitOps repo | Reconciliation converges the cluster back — see [GitOps](gitops.md) |
| **Roll forward** | Shipping a new corrective version | The fallback when none of the above can undo the change |

A feature flag turning the bad path off is usually the best of all worlds: faster
than a rollback deploy and instantly reversible if the flag itself was the wrong
call.

## Why it matters

Recovery strategy is the lever behind the [DORA](../../concepts/devops-capability-model.md)
**time to restore service** metric. High performers don't avoid failure — they make
*recovery* fast and boring. The ability to undo a change in seconds, with
confidence, is exactly what [release confidence](release-confidence.md) and
[managed disruption](../../leadership/managed-disruption.md) are built on: when
recovery is cheap and rehearsed, teams can ship faster because being wrong costs
little.

## Practical guidance

- **Make rollback the rehearsed default.** Test it like any other path; an
  un-practised rollback fails when you need it.
- **Keep deploys individually reversible** via expand/contract, so "roll back" is
  always on the table.
- **Decide the policy before the incident**, not during it — e.g. "roll back first,
  diagnose after" unless a migration makes it impossible.
- **Prefer the kill switch** when the change sits behind a flag; it's faster and
  finer-grained than redeploying.

## Relationship to other notes

- [Progressive Delivery](../../concepts/progressive-delivery.md) — a canary abort is
  rollback applied to a partial rollout, often automated on telemetry.
- [GitOps](gitops.md) — makes rollback a `git revert` against a declared desired
  state, with reconciliation doing the work.
- [Feature Flags and Branch by Abstraction](feature-flags-and-branch-by-abstraction.md)
  — the kill switch is the fastest recovery mechanism and needs no deploy.
- [Release Confidence as a System Property](release-confidence.md) — cheap,
  trustworthy recovery is what turns shipping from a high-stakes event into routine.
