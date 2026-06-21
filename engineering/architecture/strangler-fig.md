---
title: Strangler Fig Pattern
tags: [architecture, refactoring, system-design]
topic: engineering/architecture
status: notes
related:
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adr.md
  - leadership/managed-disruption.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
updated: 2026-06-13
---

# Strangler Fig Pattern

The **Strangler Fig** is the canonical pattern for modernising a legacy system
*incrementally*, without a risky big-bang rewrite. The name comes from the strangler fig
vine, which grows around a host tree until it can stand on its own and the original dies away.

## How it works

1. Put a **facade / routing layer** in front of the legacy system so callers don't know
   where a request is served.
2. Build new functionality in a **modern system alongside** the old one.
3. **Reroute** capabilities one at a time from old to new, behind the facade.
4. Repeat until the legacy system is fully "strangled" and can be **decommissioned**.

```text
        ┌──────── facade / router ────────┐
calls → │  route per capability            │
        └──→ legacy (shrinking)  ──→ new (growing)
```

## Why it beats a big-bang rewrite

- **Risk is incremental.** Each migration step is small, reversible, and independently
  shippable — a stream of low-blast-radius changes rather than one irreversible cutover.
  See the reversibility framing in
  [agile design decisions](agile-design-decisions.md).
- **Value ships continuously.** The new system delivers as it grows; you don't wait for a
  multi-year rewrite to land.
- **The old system keeps running** the whole time, so there's always a working fallback.

## Practice

- The **facade** is the linchpin — it's what lets you move a capability without callers
  changing. Invest in it first.
- Migrate by **capability/seam**, not by layer; pick seams with clear boundaries.
- Record each cutover decision (and its rollback) in an [ADR](adr.md).
- Watch for the **anti-pattern**: a facade that becomes permanent because the last,
  hardest capabilities never get migrated. Set a decommission target and hold to it.

## Relationship to other notes

It is the architectural expression of [managed disruption](../../leadership/managed-disruption.md)
(controlled, incremental change), and it pairs naturally with
[composable architecture](composable-architecture.md) — the new system is often built as
composable services/capabilities behind the facade.
