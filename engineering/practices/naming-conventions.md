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

## The macro-level exception: branded and productised names

The strict, descriptive rules above are right at the micro level — variables,
functions, columns. They invert at the macro level: internal tools, design
systems, project initiatives, teams, and repositories. When the goal shifts from
*describing* a thing to *motivating a team, driving internal adoption, or
productising* an engineering effort, you move from descriptive engineering to
product marketing, and branded names earn their keep.

- **Internal developer platforms and tools.** A name like
  `automated-testing-framework-v3` sounds like a chore to adopt; a product name
  builds identity and a shared vocabulary. Netflix's **Chaos Monkey** (the Simian
  Army), Google's **Borg** cluster manager, Twitter's **Snowflake** ID generator.
  "Are we running Chaos Monkey on this?" is stickier than "the random instance
  termination script."
- **Design systems.** Internal products that dictate look and feel get abstract,
  thematic, branded names: Google **Material**, Shopify **Polaris**, Microsoft
  **Fluent**, Atlassian **AtlasKit** — a cohesive brand, not a
  `css-component-library`.
- **Project codenames.** For a major rewrite or launch, a descriptive name can go
  stale before ship. Mythological/astronomical/thematic names (**Apollo**,
  **Titan**, **Phoenix**) rally the team and survive a pivot — `legacy-total-
  rewrite-2026` looks silly once the rewrite becomes a strangler-fig migration.
- **Agile team / squad names.** Function names (`Backend Database Maintenance
  Pod`) feel rigid; motivational or pop-culture names ("Team Avengers," "The
  Honeybadgers") build camaraderie and let a team's mandate shift without a
  rename.
- **Open-source readiness.** A company prefix or boring descriptor hurts adoption
  in the wild. Facebook shipped **React**, not `facebook-ui-rendering-engine`;
  Airbnb shipped **Airflow**, not `airbnb-data-pipeline`.

### Bridging rules — keeping it from becoming chaos

Too many branded names and new hires can't parse "Project Falcon talks to Zeus to
bypass Honeybadger." Three rules keep the exception safe:

1. **Keep it out of the micro-code.** The repo can be `zeus-engine`, but inside,
   classes stay `QueryParser` and `AuthMiddleware` — never `zeusInstance`.
2. **Brand + descriptor for repos.** Append a descriptive suffix so it's
   searchable: `apollo-graphql-gateway`, `titan-billing-service` — not bare
   `apollo` or `titan`.
3. **Maintain a lexicon.** Engineering leadership keeps a central glossary that
   translates codenames and product names to actual business functions for new
   hires.

## PR review checklist

When reviewing or designing, ask:

1. Is it obvious what this variable/function/system does just from the name?
2. Does it follow the casing convention for this language/framework?
3. Is it free of arbitrary abbreviations? (`config` is fine; `cfg` is not.)
4. Is it consistent with how similar concepts are named elsewhere?
