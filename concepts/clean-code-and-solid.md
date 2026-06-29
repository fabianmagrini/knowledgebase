---
title: Clean Code and SOLID
tags: [system-design, refactoring, code-review]
topic: concepts
status: draft
level: intermediate
related:
  - engineering/practices/software-design-principles.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/practices/quality-first-ai-coding.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/practices/naming-conventions.md
updated: 2026-06-19
---

# Clean Code and SOLID

SOLID and Clean Code are routinely treated as synonyms. They are not: **SOLID is a
subset of the broader Clean Code philosophy.** Both are strongly associated with
Robert C. Martin. This note is the reference for the concepts; for *which*
principles to prioritise and why in an AI-native workflow, see
[Software Design Principles](../engineering/practices/software-design-principles.md).

## The hierarchy

```text
Software Craftsmanship
    └── Clean Code
            ├── Naming
            ├── Functions
            ├── Testing
            ├── Refactoring
            ├── Readability
            ├── Code Smells
            ├── Architecture
            └── SOLID Principles
```

SOLID is a set of **object-oriented design principles** for building maintainable
systems. Clean Code is the much broader philosophy of writing software that is easy
to understand, modify, and operate. SOLID lives *inside* Clean Code.

## The five SOLID principles

- **S — Single Responsibility.** A class or module has one reason to change.
- **O — Open/Closed.** Open for extension, closed for modification — add new
  behaviour (e.g. a new `PaymentProcessor` implementation) without editing existing
  code.
- **L — Liskov Substitution.** Subtypes must be usable wherever their base type is
  expected; any `Repository` implementation must work correctly in code written
  against the interface.
- **I — Interface Segregation.** Clients should not depend on methods they do not
  use — prefer focused interfaces (`ReadRepository`, `WriteRepository`) over one
  fat one.
- **D — Dependency Inversion.** Depend on abstractions, not concretions: inject an
  `AccountRepository`, not a `MongoAccountRepository`.

## Clean Code is much more than SOLID

SOLID is the design-principles slice; Clean Code also covers the day-to-day craft:

- **Meaningful naming** — `accountOpenedDate`, not `d`.
- **Small, focused functions** — `validateCustomer()`, `saveCustomer()`,
  `sendWelcomeEmail()` rather than one `processCustomer()` that validates,
  persists, emails, audits, and logs.
- **Readability** — code is read far more often than written; most Clean Code
  practices optimise for the future reader.
- **Testing** — automated tests, fast feedback, testable designs, dependency
  injection.
- **Refactoring** — treated as a continuous activity, not a one-off cleanup.

## Modern perspective: prefer simplicity until abstraction is justified

By 2026 the emphasis has shifted. Still highly relevant: SRP, dependency inversion,
cohesion, loose coupling, clear naming, testability. But several ideas are now
recognised as **frequently over-applied** — codebases padded with parallel
abstractions for trivial work:

```text
IAccountService    AccountService
IAccountRepository AccountRepository
IAccountMapper     AccountMapper
```

…for simple CRUD. An interface with exactly one implementation, added "for SOLID",
is usually just indirection. The prevailing guidance:

> Prefer simplicity until abstraction is justified.

Introduce the seam when there is a second implementation, a genuine boundary, or a
real need to substitute — not pre-emptively. This is the same instinct as
[emergent, reversibility-aware design](../engineering/architecture/agile-design-decisions.md):
add structure when it pays for itself.

## Clean Code vs Clean Architecture

Another common confusion — they operate at different altitudes:

| | Focuses on |
|---|---|
| **Clean Code** | classes, functions, naming, maintainability |
| **Clean Architecture** | system boundaries, dependency direction, domain isolation, framework independence |

Clean Architecture uses SOLID heavily (especially Dependency Inversion) but its
concern is the *shape of the system*, not the *shape of a function*. The
boundary-level view connects to
[Microfrontend Architecture Principles](../engineering/architecture/micro-frontend-principles.md)
and the broader point that, at scale, **boundaries and ownership matter more for
maintainability than strict SOLID** — SOLID supports the architecture rather than
driving it (developed in
[Software Design Principles](../engineering/practices/software-design-principles.md)).
