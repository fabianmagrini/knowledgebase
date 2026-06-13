---
title: Start with the Why
tags: [leadership, communication]
topic: engineering/practices
status: notes
related:
  - engineering/architecture/agile-design-decisions.md
  - engineering/practices/managed-disruption.md
  - engineering/practices/decision-facilitation.md
source: "https://gist.github.com/fabianmagrini/a9419029286fb2277dc7b2bc5fc0d43d"
updated: 2026-06-13
---

# Start with the Why

Popularised by Simon Sinek, **Start with the Why** is the practice of communicating purpose
*before* approach or output. It maps directly onto an engineering principle you already use:
**outcomes over outputs**.

## The Golden Circle

Three concentric circles, communicated inside-out:

1. **Why** — the purpose. *Why does this exist? What belief drives it?*
2. **How** — the approach or differentiators. *How do we do it differently/better?*
3. **What** — the outputs: products, features, services.

Most organisations communicate **outside-in** (What → How → Why): *"We build banking
software, we focus on security, to help people manage money."*

Great ones communicate **inside-out** (Why → How → What): *"We believe people should feel
safe and confident with their money. We design secure, delightful digital experiences. We
build modern banking apps."*

## Why it matters

- **Clarity** — people make better decisions when they understand the purpose.
- **Motivation** — purpose drives engagement more than tasks.
- **Alignment** — a clear Why anchors prioritisation, trade-offs, and autonomy
  (Commander's Intent).
- **Storytelling** — makes the message memorable and resonant.

## Applied to engineering

Reframe technical statements as Why → How → What so the rationale leads:

**Architecture decision** — instead of *"We're adopting microservices for scalability,"*
say: *"To let teams deliver independently at speed (Why), we adopt loosely coupled service
boundaries and strong operational tooling (How), implemented via microservices (What)."*

**Engineering practice** — instead of *"We need more automated tests,"* say: *"We want to
ship with confidence and fewer production issues (Why), so we embrace engineering excellence
(How), like strong automated test suites (What)."*

This is the same "understand the problem first" discipline that underpins
[agile design decisions](../architecture/agile-design-decisions.md): the Why prevents
"solutioneering," and the 5 Whys / XY Problem surface the real need before a solution is
chosen.
