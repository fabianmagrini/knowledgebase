---
type: note
title: Database Migration Strategies
description: "Database changes are the hardest part of continuous delivery because the database is stateful, shared, and not trivially reversible."
tags: [ci-cd, system-design, testing, api-design]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/rollback-and-roll-forward.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - concepts/continuous-delivery.md
  - engineering/practices/trunk-based-development.md
  - concepts/resilient-software-design.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/gitops.md
  - tools/postgresql-ha-kubernetes.md
source: ""
updated: 2026-06-21
---

# Database Migration Strategies

Database changes are the hardest part of continuous delivery because the database
is **stateful, shared, and not trivially reversible**. Application code can be
redeployed or rolled back in seconds; a schema you have altered and a column you
have dropped cannot. Migrations are the single biggest reason a deploy stops being
individually reversible — see [Rollback and Roll Forward](rollback-and-roll-forward.md).

The whole discipline reduces to one principle: **decouple the schema change from
the code change, and keep adjacent versions compatible**, so that old and new
application code can both run correctly against the database at every moment of a
deploy. Get that right and migrations become zero-downtime and reversible; get it
wrong and every schema change is a coordinated outage.

## Why a "big-bang" migration fails

The naïve approach — take the app down, run `ALTER TABLE`, deploy new code, bring
it back — assumes you can stop the world. In a continuously delivered system you
can't: during any rollout, **old and new code run simultaneously** (rolling deploy,
canary, or just the seconds between instances updating). A migration that only the
new code understands breaks the old code that is still serving traffic. The fix is
to never make a single change that both versions can't tolerate.

## Expand / contract (parallel change)

The canonical pattern. A breaking change is split into a sequence of **individually
backward-compatible deploys**, so that at no single step does running code see a
schema it can't handle. Renaming `full_name` to `display_name`:

```text
1. EXPAND   Add display_name (nullable). Deploy. Old code ignores it.
2. DUAL-WRITE  Deploy code that writes BOTH full_name and display_name.
3. BACKFILL    Copy full_name → display_name for existing rows (batched, out of band).
4. MIGRATE READS  Deploy code that reads display_name, still writing both.
5. STOP OLD WRITES  Deploy code that uses display_name only.
6. CONTRACT   Drop full_name — only once nothing reads or writes it.
```

Each numbered step is a separate, individually reversible release. The expensive,
irreversible action (the `DROP` in step 6) happens last, long after everything has
moved off the old column, when undoing it is no longer needed. This is the database
expression of the same decoupling behind
[feature flags and branch by abstraction](feature-flags-and-branch-by-abstraction.md).

### The ordering rule

A simple rule of thumb captures most of expand/contract:

- **Additive (expand) changes ship _before_ the code that needs them.**
- **Destructive (contract) changes ship _after_ the code that stopped using them.**
- **Never drop or rename in the same release that stops using the thing.**

## Online / non-blocking schema changes

Even additive changes can take a database down if they hold a lock. On a large
table, a careless `ALTER` can block reads or writes for the duration of a full
table rewrite.

- Know your engine's locking behaviour: which DDL is instant (metadata-only) vs
  which rewrites the whole table. Postgres `ADD COLUMN` with a non-volatile default
  is cheap on modern versions; adding certain constraints validates the whole table.
- Add constraints in two steps — create `NOT VALID`, then `VALIDATE` separately — to
  avoid a long blocking scan.
- For heavy changes on big tables, use **online schema-change tools**:
  `pt-online-schema-change` and `gh-ost` (MySQL) build a shadow table and swap;
  Postgres often handles it natively or via logical replication.

## Backfilling data safely

Populating the new column for existing rows is a **data migration**, distinct from
the **schema migration**, and is usually the riskiest part on a large table:

- **Batch and throttle** — update in chunks (e.g. 1–10k rows) with pauses, never one
  giant transaction that locks the table or blows out the WAL/undo log.
- **Idempotent and resumable** — a backfill must survive being interrupted and
  re-run; track progress so it can continue, not restart.
- **Run out of band** — as a background job or one-off task, not inside the deploy's
  migration step, so a slow backfill doesn't block or time out the release.

## Migration mechanics and tooling

- **Versioned, in source control.** Migrations are ordered, immutable files
  committed alongside the code — the same source-of-truth discipline as
  [GitOps](gitops.md). Tools: Flyway, Liquibase, Alembic, Rails/ActiveRecord,
  Prisma, Django.
- **Forward-only vs up/down.** Down-migrations are tempting but often can't truly
  reverse data loss; many teams go **forward-only** and treat recovery as a new
  forward migration. (See the rollback-vs-roll-forward trade-off.)
- **Migrations run once, in order, idempotently.** The runner records which have
  applied; never edit an already-applied migration — add a new one.
- **Separate migration from deploy.** Decide deliberately whether schema changes run
  before, during, or after the code deploy; expand/contract dictates the answer per
  change.

## Rollback considerations

Because destructive changes are what make a release irreversible, the goal is to
keep every release reversible *until you no longer need to reverse it*:

- Prefer **additive now, destructive later** so the risky window is short and the
  drop happens when rollback is moot.
- If a migration genuinely can't be reversed, you have committed to
  **rolling forward** — make sure a forward fix is feasible and tested before you
  run it.
- Treat the contract step as its own low-risk release, never bundled with feature
  work.

## Larger migrations: changing the store itself

Migrating to a *different* database or a re-modelled schema is expand/contract at
the system level, usually via **dual writes and shadow reads**: write to both old
and new stores, backfill history, read-compare to validate parity, then cut reads
over and finally retire the old store. The
[branch-by-abstraction](feature-flags-and-branch-by-abstraction.md) interface over
the data layer is what lets callers stay stable through the swap, and a
[feature flag](feature-flags-and-branch-by-abstraction.md) gates the read cutover.

## Anti-patterns

- **Destructive change coupled to a code deploy** — drop/rename in the same release
  that stops using it; rollback now means data loss.
- **Downtime maintenance window** as the default rather than the exception.
- **Unbatched backfill** that locks a large table for minutes.
- **Editing an applied migration** instead of adding a new one.
- **A migration with no tested recovery path** — neither reversible nor a proven
  forward fix.

## Relationship to other notes

- [Rollback and Roll Forward](rollback-and-roll-forward.md) — migrations are *the*
  reason a deploy may not be reversible; expand/contract is what keeps them so.
- [Feature Flags and Branch by Abstraction](feature-flags-and-branch-by-abstraction.md)
  — the same decouple-and-migrate-incrementally pattern, applied to state.
- [Resilient Software Design](../../concepts/resilient-software-design.md) — backward
  compatibility and reversibility are designing for failure at the data layer.
- [Highly Available PostgreSQL on Kubernetes](../../tools/postgresql-ha-kubernetes.md)
  — a concrete case study in the operational side of running the database safely.
