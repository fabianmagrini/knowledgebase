---
title: Feature Flags and Branch by Abstraction
tags: [ci-cd, git, testing, refactoring]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/trunk-based-development.md
  - concepts/continuous-delivery.md
  - concepts/ci-cd-continuous-deployment.md
  - engineering/practices/release-confidence.md
  - engineering/practices/regulated-service-release-process.md
  - leadership/managed-disruption.md
  - engineering/architecture/strangler-fig.md
  - concepts/progressive-delivery.md
source: "Pete Hodgson — Feature Toggles (martinfowler.com); Martin Fowler — BranchByAbstraction; Jez Humble & David Farley — Continuous Delivery (2010)"
updated: 2026-06-21
---

# Feature Flags and Branch by Abstraction

Two techniques that solve the same underlying problem: **how to integrate
incomplete or risky work into a shared trunk continuously without exposing it or
breaking the build.** They are what make
[trunk-based development](trunk-based-development.md) and
[continuous delivery](../../concepts/continuous-delivery.md) workable in practice —
the alternative is long-lived branches whose merge pain compounds with age.

The shared principle is **decoupling deploy from release**: code can ship to
production (deploy) while staying inert or hidden until a separate decision turns
it on (release).

## Feature flags

A feature flag (or toggle) is a runtime conditional that decides whether a code
path is active, without redeploying:

```text
if (flags.isEnabled("new-checkout")) {
    newCheckout();
} else {
    oldCheckout();
}
```

The code ships dark on every merge; flipping the flag — for everyone, a cohort, or
an internal group — is the release event. This is what lets a half-finished
feature live on `main` without blocking anyone.

### A taxonomy of flags

Not all flags are the same; conflating them is the root of most flag pain. Pete
Hodgson's categorisation, by **how long they live** and **how often they change**:

| Type | Purpose | Lifespan | Who flips it |
|---|---|---|---|
| **Release toggle** | Hide incomplete work in trunk | Days–weeks | Dev team |
| **Experiment toggle** | A/B test, measure variants | Weeks | Product / data |
| **Ops toggle** | Kill-switch / degrade gracefully under load | Long-lived | Operators / on-call |
| **Permission toggle** | Gate features by plan, role, or cohort | Permanent | Product / business |

The distinction matters because lifespan dictates discipline: a release toggle is
**technical debt the moment it ships** and must be removed once the feature is
fully live, whereas a permission toggle is a permanent part of the product and
belongs in configuration, not the backlog.

### Managing flag debt

Flags are not free. Each one is a branch in the code that must be built, tested,
and reasoned about. Left unmanaged they multiply combinatorially and become a
liability.

- **Make every release toggle a removal ticket** the moment it is created.
- **Set an expiry** — some teams fail the build on a flag past its sunset date.
- **Test the paths that ship.** At minimum test the on-state you intend to release
  and the current production state; testing the full combinatorial matrix is
  rarely worth it.
- **Keep the flag check at the edges**, not threaded through deep call stacks, so
  removal is a local edit.

### Why they matter beyond release

The same mechanism enables **canary and progressive rollout** (flip on for 1% →
10% → 100%, watching telemetry), **kill switches** (instantly disable a misbehaving
feature without a rollback deploy), and **graceful degradation** under load. This
is a load-bearing part of [release confidence](release-confidence.md): the ability
to turn something off fast is what makes turning it on low-drama.

## Branch by abstraction

Feature flags hide a *new path*. Branch by abstraction handles the harder case: a
**large change to existing code** — replacing a library, a data store, a framework
— that is too big for one commit but must not live on a long-lived branch.

Rather than branching in version control, you branch *in the code* behind an
abstraction, and migrate incrementally on trunk:

```text
1. Introduce an abstraction over the thing you want to change
   (e.g. a PaymentClient interface over direct Stripe calls)
2. Route existing callers through the abstraction — no behaviour change
3. Add the new implementation behind the same abstraction
4. Migrate callers / switch the implementation incrementally
   (often gated by a feature flag during cutover)
5. Delete the old implementation
6. Remove the abstraction if it no longer earns its place
```

At every step `main` compiles, tests pass, and the system is releasable. Multiple
people can work in parallel against the stable interface. The big-bang "rewrite on
a branch, merge in three months" approach is replaced by a sequence of small,
safe, reviewable changes.

### Keystone interface

A lighter-weight cousin for *new* features: build all the supporting pieces first
and commit them inert, then add the final small connecting piece — the keystone —
as the last commit that activates the feature. The work integrates continuously
but does nothing until the keystone lands. Where branch by abstraction migrates
*existing* code, the keystone assembles *new* code that is dormant until wired up.

## Choosing between them

They are complementary, not alternatives — large migrations often use both:

| Situation | Reach for |
|---|---|
| New feature, want to ship dark and release later | **Feature flag** |
| Progressive rollout / A/B test / kill switch | **Feature flag** (ops or experiment) |
| Replacing or rewriting existing infrastructure incrementally | **Branch by abstraction** |
| New feature assembled from many inert pieces | **Keystone interface** |
| Big migration you also want to roll out gradually | **Both** — abstraction for structure, flag for cutover |

## Relationship to delivery practice

These techniques are *why* you can integrate continuously without a freeze:

- They keep the trunk releasable, which is the precondition for
  [trunk-based development](trunk-based-development.md) and
  [continuous delivery](../../concepts/continuous-delivery.md).
- Decoupling deploy from release is exactly the distinction that lets a team
  practise [Continuous Deployment](../../concepts/ci-cd-continuous-deployment.md)
  safely — every merge deploys, but features release on their own schedule.
- In regulated contexts, a flag can act as a controlled, auditable release gate
  rather than a separate deployment — see
  [Release Process for Regulated and High-Risk Services](regulated-service-release-process.md).
- Rolling out change behind flags is a core tool for
  [managed disruption](../../leadership/managed-disruption.md): the blast radius of
  any one change stays small and reversible.
