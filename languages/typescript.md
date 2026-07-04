---
title: TypeScript Tips
tags: [typescript, reading]
topic: languages
status: notes
level: intermediate
related:
  - engineering/practices/engineering-playbook.md
  - languages/nodejs-cli-best-practices.md
source: "https://github.com/AllThingsSmitty/typescript-tips-everyone-should-know"
updated: 2026-06-14
---

# TypeScript Tips

A compact reference of practical TypeScript techniques. Each is individually small, but together
they shift how the code feels to work in — improving safety, readability, and maintainability.
The grouping below is editorial; the source lists 15 tips.

## Prefer safer constructs

| Tip | What it does | Key syntax |
|---|---|---|
| Prefer `unknown` over `any` | Forces validation/narrowing before use, instead of opting out of type checking | `unknown` + type guards |
| Prefer `satisfies` over `as` | Checks conformance without widening the inferred type | `const x = {...} satisfies T` |
| Avoid `enum` in most cases | Literal-union `as const` arrays serialise and refactor more simply than enums | `const X = [...] as const` |
| Let type inference do the work | Avoids over-annotation and the maintenance it adds | (omit redundant annotations) |

## Derive, don't duplicate

| Tip | What it does | Key syntax |
|---|---|---|
| Derive types from values | Generates a type from real values, preventing type/value drift | `typeof value`, `as const` |
| Build new types from existing ones | Transforms rather than re-declares types | `Pick`, `Omit`, `Partial`, `Required`, `T[K]` |
| Use `as const` for config/constants | Narrows properties to literal types for precise inference | `const cfg = {...} as const` |

## Model state precisely

| Tip | What it does | Key syntax |
|---|---|---|
| Model impossible states with discriminated unions | A shared discriminator makes invalid combinations unrepresentable | `{ kind: 'a'; ... } \| { kind: 'b'; ... }` |
| Exhaustive checks with `never` | Turns an unhandled union branch into a compile error | `const _exhaustive: never = x` |
| Type predicates for reusable narrowing | Connects a runtime check to compile-time narrowing | `function isT(v): v is T` |
| Generics that infer automatically | Type parameters inferred from arguments, no manual instantiation | `function f<T>(arg: T)` |
| Template literal types | Builds string-shaped types for routes, event names, design tokens | `` `on${Capitalize<E>}` `` |

## The runtime boundary

| Tip | What it does | Key syntax / note |
|---|---|---|
| Validate external data at runtime | Type safety stops at the API boundary; validate what crosses it | runtime validators (e.g. Zod) |
| Type safety ≠ runtime safety | Type checking does not prevent runtime errors; validation is still required | — |
| Enable strict compiler options | Catches more at compile time | `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes` |

## Relationship to other notes

- [Modern Web Engineering Playbook](../engineering/practices/engineering-playbook.md) — the
  runtime-boundary tips (validate external data, type ≠ runtime safety) reinforce its themes of
  validating inputs at system boundaries.
