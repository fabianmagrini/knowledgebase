---
title: Naming Conventions
tags: [refactoring, code-review, api-design, documentation]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/software-design-principles.md
  - engineering/practices/code-review-policy.md
  - concepts/clean-code-and-solid.md
updated: 2026-06-29
---

# Naming Conventions

Naming is one of the genuinely hard problems in software. A well-considered
naming convention improves readability, reduces onboarding time, and removes a
whole class of bugs that stem from misunderstanding. This note is a practical
guideline spanning general principles through to code, databases, APIs, and
infrastructure.

## The golden rules

These apply regardless of language or system:

- **Intention-revealing.** A name should tell you why it exists, what it does,
  and how it is used. If a name needs a comment to be understood, the name is not
  good enough — prefer `elapsedTimeInDays` over `d`.
- **Pronounceable and searchable.** Avoid abstract acronyms. You should be able
  to say the name out loud in a meeting without spelling it out, and grep for it
  without a thousand false positives.
- **Avoid disinformation.** Don't use words that imply something untrue. Don't
  call a list `accountGroup` if it's an array — call it `accounts` or
  `accountList`.
- **Consistency over correctness.** If the team already has a standard, follow
  it. A consistently applied "imperfect" convention beats three different "good"
  conventions in the same codebase.

## Standard casing styles

| Style | Example | Typical use |
|---|---|---|
| `camelCase` | `firstName` | Variables and functions in Java, JS/TS, C++ |
| `PascalCase` | `UserAccount` | Classes, interfaces, types; methods in C# |
| `snake_case` | `first_name` | Python, Rust, Ruby identifiers; DB columns |
| `kebab-case` | `first-name` | URLs, CSS classes, git repos, file names |
| `UPPER_SNAKE_CASE` | `MAX_RETRIES` | Constants and environment variables |

## Code-level conventions

- **Variables (nouns).** Represent state or data — use nouns or noun phrases:
  `user`, `activeUsers`, `connectionString`. Avoid `usr`, `data`, `process`.
- **Booleans (questions).** Sound like a true/false question — prefix with `is`,
  `has`, `can`, or `should`: `isActive`, `hasPermission`, `canEdit`. Avoid
  `active`, `permission`, `editStatus`.
- **Functions and methods (verbs).** Perform actions — use verbs or verb phrases:
  `getUser()`, `calculateTotal()`, `validateInput()`. Keep verb prefixes
  consistent: if `get` fetches data, don't also use `fetch` or `retrieve` for the
  same concept elsewhere.
- **Classes and types (nouns).** `PascalCase` nouns: `Customer`,
  `InvoiceManager`, `AuthenticationService`. Avoid verb-y names like
  `ManageInvoices` or `Authenticate`.

## Database conventions

Databases are hard to refactor, so naming matters more.

- **Tables.** `snake_case`. Decide as a team between plural (`users`, `orders`)
  and singular (`user`, `order`). Plural is the prevailing web-framework default.
- **Columns.** `snake_case`, descriptive.
- **Primary keys.** Just `id` — `user_id` in the `users` table is redundant.
- **Foreign keys.** Singular target table plus the key: `user_id`, `company_id`.
- **Junction tables (many-to-many).** Combine the two table names, typically in
  alphabetical order: `article_tags` (or `article_tag`).

## API design (REST)

REST conventions use `kebab-case` paths and rely on HTTP methods rather than
action words in the URL.

- **Nouns, not verbs.** `POST /users` (good) over `POST /createUser` (bad).
- **Plurals for collections.** `/users/123` (good) over `/user/123` (bad).
- **Hierarchy in the path.** `GET /users/123/orders` to get the orders for user
  123.

## DevOps, git, and file systems

**Git branches** — group by intention with a prefix, slash, optional issue
number, and a `kebab-case` description:

- `feat/123-add-sso-login` — new features
- `fix/456-button-alignment` — bug fixes
- `chore/update-dependencies` — maintenance
- `docs/readme-update` — documentation

**Repositories and file names** — most file systems and URLs are case-sensitive,
so strictly use lowercase `kebab-case` for repos, directories, and files
(`user-auth-service`, `utils.js`) to avoid cross-platform breakage. Exceptions:
conventional files (`README.md`, `Dockerfile`) and language-mandated names (Java
files must match the `PascalCase` class name).

## PR review checklist

When reviewing or designing, ask:

1. Is it obvious what this variable/function/system does just from the name?
2. Does it follow the casing convention for this language/framework?
3. Is it free of arbitrary abbreviations? (`config` is fine; `cfg` is not.)
4. Is it consistent with how similar concepts are named elsewhere?
