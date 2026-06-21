---
title: CI vs Continuous Delivery vs Continuous Deployment
tags: [ci-cd, testing]
topic: concepts
status: notes
level: beginner
related:
  - concepts/continuous-delivery.md
  - concepts/devops-capability-model.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/release-confidence.md
source: "Jez Humble & David Farley — Continuous Delivery (2010)"
updated: 2026-06-21
---

# CI vs Continuous Delivery vs Continuous Deployment

The three terms share the "CD" abbreviation and are routinely conflated, but they
name three different things at three different stages of the pipeline. The clean
way to hold them apart: each one extends the previous by **automating one more
step** between a developer's keystroke and a running production change.

```
CI                 → keep the codebase integrated and green
Continuous Delivery → keep every green build releasable on demand
Continuous Deployment → release every green build automatically
```

## The three, precisely

### Continuous Integration (CI)
Developers merge small changes into a shared trunk frequently — at least daily —
and **every merge triggers an automated build and test run**. The aim is to catch
integration problems within minutes rather than letting them accumulate on
long-lived branches. CI is about the *codebase staying in a working, integrated
state*. It says nothing about deployment.

### Continuous Delivery (CD)
Builds on CI: **every change that passes the pipeline is a candidate for release**.
The software is always in a deployable state, and pushing it to production is a
push-button operation — but the *decision* to do so remains a human one. Release
becomes a business choice, not a technical event. See
[Continuous Delivery](continuous-delivery.md) for the deep dive.

### Continuous Deployment
The strict superset of Continuous Delivery: **every change that passes the pipeline
is deployed to production automatically**, with no human approval gate. There is no
"release button" because there is no human in the loop — passing tests *is* the
decision to ship.

## The distinction in one table

| | What's automated | Last manual step | Production cadence |
|---|---|---|---|
| **Continuous Integration** | Build + test on every merge | Everything from release onward | None (CI doesn't deploy) |
| **Continuous Delivery** | Build, test, and the release mechanism | The decision to release | On demand, push-button |
| **Continuous Deployment** | The whole path, including release | Nothing — it's fully automated | Every passing change, automatically |

The pivot point between the last two is a single thing: **whether a human approves
the final release**. Continuous Delivery keeps that gate; Continuous Deployment
removes it.

## Two common confusions

**"CD" is ambiguous.** It almost always means Continuous *Delivery*. Continuous
*Deployment* is usually spelled out to avoid the clash.

**Deploy ≠ release.** Even under Continuous Deployment, automatically *deploying*
code to production does not mean *releasing* a feature to users. Feature flags
decouple the two: code ships dark on every merge, and the feature is switched on as
a separate decision. This is what lets teams deploy continuously without exposing
half-finished work — see [Trunk-Based Development](../engineering/practices/trunk-based-development.md).

## Why a team might stop at Continuous Delivery

Continuous Deployment is not strictly "better" — it is a policy choice. Many teams
deliberately keep the manual release gate:

- **Regulated or high-risk domains** may require an audited human sign-off before
  a production change — see
  [Release Process for Regulated and High-Risk Services](../engineering/practices/regulated-service-release-process.md).
- **Business timing** — marketing launches, contractual windows, or coordinated
  multi-system changes need a human to choose the moment.
- **Confidence ramp** — teams often adopt Continuous Delivery first and only remove
  the gate once test coverage and observability make automatic release low-drama.
  That earned trust is [release confidence](../engineering/practices/release-confidence.md).

## How they nest

Each is a prerequisite for the next:

```
Continuous Integration ⊂ Continuous Delivery ⊂ Continuous Deployment
```

You cannot practise Continuous Delivery without CI (you need green, integrated
builds to release), and you cannot practise Continuous Deployment without
Continuous Delivery (you can only auto-release if every build is already
releasable). All three sit inside the broader
[DevOps capability model](devops-capability-model.md), where CI, trunk-based
development, and continuous delivery appear as named capabilities driving delivery
performance.
