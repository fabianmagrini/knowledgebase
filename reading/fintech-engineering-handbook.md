---
type: reading
title: Fintech Engineering Handbook
description: "Voytek Pituła's handbook collects the patterns that make software trustworthy when money is the primary object of the system."
tags: [architecture, system-design, reading]
topic: reading
status: notes
level: intermediate
related:
  - concepts/resilient-software-design.md
  - engineering/security/secure-sdlc.md
source: "https://w.pitula.me/fintech-engineering-handbook/"
updated: 2026-07-11
---

# Fintech Engineering Handbook

Voytek Pituła's handbook collects the patterns that make software **trustworthy when
money is the primary object of the system**. Its organising idea is that every
practice serves one of three principles:

| Principle | Meaning | Upheld by |
|---|---|---|
| **No invented data** | Money can't be created from nothing; no duplicates or arbitrary balance updates | Idempotency, deduplication, reconciliation |
| **No lost data** | Everything that happens to money is tracked and persisted | Full precision, at-least-once delivery, event sourcing, audit trails, immutability |
| **No trust** | Trust neither external providers, internal components, nor the world | Verify webhooks, cross-check across sources, fail loudly on broken assumptions |

## Representing money

The most fundamental decisions — get them wrong and every layer above inherits the error.

- **Precision.** Four options: floating-point (almost never — silent precision loss);
  arbitrary precision (e.g. `BigDecimal`, good for chained FX/pricing math); **minor-units
  integers** (store the smallest unit — €12.34 → `1234`; digit count is per-currency via
  ISO 4217, *not always 2*; crypto uses the same idea but per-asset, often 18 decimals,
  needing arbitrary-width integers); rational numbers (no loss, but slow and hard to
  convert). Storage and computation are separate decisions and are often combined.
- **Serialisation.** A bare JSON number is an IEEE-754 double in most parsers, so
  serialising money as a number reintroduces the float problem at the edge. Send money as
  a **string (`"12.34"`) or an integer in its smallest unit**.
- **Rounding** is inevitable, explicit, and a *business* decision (round-down to stay
  conservative, half-even for statistical fairness; who gets the fraction can have tax/legal
  implications). Round **as seldom as possible**, at boundaries. Rounding breaks sums — split
  parts may not re-add to the original, sometimes needing an explicit rounding account.
- **Currency.** Pack amount + currency in a `Money` newtype; **prohibit cross-currency
  arithmetic** (conversion must be explicit, at a controlled rate); validate against a
  controlled currency set at the boundary; codes identify *fiat* only (crypto needs
  `(network, contract address)`); pegged/wrapped assets are not the underlying.
- **FX rates** are **directional** (EUR/USD ≠ inverted USD/EUR; bid/ask spread) and
  **time-specific** (current-time vs value-date). Distinguish the **transactional rate** (what
  a real conversion happened at — derived from the two amounts, not stored) from the
  **reference rate** (mid-market/central-bank, for valuation, not a tradeable price). There is
  **no canonical rate**, so the source is part of the data.

## Recording money: the ledger

- **Double-entry bookkeeping** stores movements as entries of `(credit account, debit
  account, amount)`. Because every entry moves the same amount out of one account and into
  another, the books always balance — money is only moved, never created or destroyed.
- **Balance is never stored**; it is derived from movements. Accounts have a type (asset /
  liability / equity). External providers get their own accounts so money entering or leaving
  the system is still tracked.
- Separate **value time vs booking time vs settlement time**, and keep **audit trails** so
  state can be reconstructed years later.

## Executing money flows

- **Invariants** — assertions about money that must always hold; fail loudly when broken.
- **Funds reservation** and explicit **overdraft** handling before a flow commits.
- **Idempotency** — the same instruction applied twice must not move money twice.
- **Full resumability** — a flow interrupted anywhere can resume without double-spending or
  loss (event-sourced, at-least-once).

## The external world

- **Consuming APIs** and **verifying webhooks** (never trust an unauthenticated callback).
- **Notifying reliably** via the **Outbox pattern** and **Change Data Capture (CDC)** so an
  event is never lost between a local commit and an external notification.
- **Reconciliation** — cross-check internal records against external providers to detect drift,
  duplicates, or missing movements.

## Controls and the change trail

- **Segregation of duties** and **four-eyes** approval for sensitive actions.
- **Access control** scoped to roles.
- A **change trail** over the SDLC and **testing** discipline appropriate to money systems.

## Relationship to other notes

- [Resilient Software Design](../concepts/resilient-software-design.md) — the general theory
  this handbook applies to money: "everything fails", lost/duplicated/reordered messages, and
  the explicit choice of *at-least-once* delivery with idempotency. The fintech principles
  ("no invented / no lost / no trust") are that reliability discipline specialised to a domain
  where a dropped or duplicated message is a dropped or duplicated *payment*.
- [Secure SDLC (DevSecOps)](../engineering/security/secure-sdlc.md) — the handbook's controls
  layer (segregation of duties, four-eyes, access control, the change trail and audit trails)
  is the money-domain instance of security being a property of the whole lifecycle rather than
  a gate at the end.
