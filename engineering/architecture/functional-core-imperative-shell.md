---
type: note
title: Functional Core, Imperative Shell
description: "Bernhardt's pattern, and Rico Fritzsche's argument that it should replace Clean/Hexagonal architecture — resting on one real distinction: dependency inversion reverses source-code dependencies while leaving functional dependencies untouched, so an interface changes nothing about runtime reliance."
tags: [architecture, system-design, testing, refactoring, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/layered-architecture.md
  - concepts/clean-code-and-solid.md
  - engineering/architecture/skeleton-architecture.md
  - engineering/ai-native/agentic-verification.md
  - engineering/architecture/over-engineering.md
  - engineering/architecture/reversibility-decays.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/enforced-architecture-rules.md
  - engineering/architecture/team-topologies.md
source: "https://ricofritzsche.me/why-are-we-still-talking-about-clean-architecture/"
updated: 2026-10-26
---

# Functional Core, Imperative Shell

The pattern splits a system into two parts with different natures:

| Part | What it is |
|---|---|
| **Functional core** | *"contains the business logic. It processes values and returns results without calling external systems or causing side effects"* |
| **Imperative shell** | *"handles the necessary interactions with the outside world"* — fetch, call the core, persist |

The core is pure, so it is tested by passing values and asserting on results. The shell has
dependencies but few branches, so it is tested by integration. **The term is Gary Bernhardt's,
from his 2012 SCNA talk *Boundaries*** — worth stating because the article below does not credit
it, while criticising other people's patterns for being overrated.

This note is written from Rico Fritzsche (October 2026), who argues FCIS should **replace** Clean
Architecture and hexagonal architecture rather than complement them.

> **Provenance, which has to come first here.** The author's site links a Leanpub book,
> *Autonomous Domain Capabilities*, and a consulting practice. The piece argues against the
> dominant pattern and for the thing he wrote the book about — advocacy, not analysis, and it
> does not make the argument wrong but does set how to read it. There is **no quantitative
> evidence of any kind**, and no concession anywhere: no benefit of Clean or hexagonal
> architecture is acknowledged, and no case is offered where FCIS fits poorly.

## The distinction that earns the note

Strip the polemic and one analytical move remains, which these notes did not hold:

> Dependency inversion makes it possible to reverse source code dependencies and abstract
> concrete implementations behind interfaces… However, the **functional dependencies remain**.

> it still relies on an external operation being executed before it can apply its business
> rules… **The interface does nothing to change this.**

A repository interface inverts the *compile-time* dependency: the business logic no longer
imports the database module. The *runtime* dependency is untouched — the logic still cannot run
until someone has fetched the data. So the inversion buys substitutability of implementation and
buys nothing about the ordering constraint or the side effect.

**This repo reasons about dependency direction constantly and never separates those two
senses.** [Layered Architecture](layered-architecture.md) has dependencies flowing inward,
[Enforced Architecture Rules](enforced-architecture-rules.md) makes crossings fail a build, and
[Skeleton Architecture](skeleton-architecture.md) uses ArchUnit to assert that no AI-written
module imports the database directly. Every one of those governs *source-code* dependencies.
The functional dependency — this code cannot execute until that effect has happened — is
invisible to all of them, which is a useful thing to know about the tooling.

FCIS attacks the functional dependency instead: move the effects to the edge so the decision
logic has none.

## Mocks are a symptom — and the repo reached this from the other direction

> They're often needed because we've mixed business logic with external interactions and then
> have to simulate those dependencies for our tests. So we first introduce coupling, abstract it
> through interfaces, and then need test doubles to control the effects of that coupling during
> testing.

His worked example is a booking validation function taking a request and a context value and
returning a result, with *"a test now requires nothing more than input values and the expected
result"* — no database, no interfaces, no dependency injection, no mocks.

**[Agentic Verification](../ai-native/agentic-verification.md) arrives at the same conclusion
about mocks from verification rather than design**: *"a mock encodes the agent's own model of the
dependency"*, so if the agent misunderstood the contract the mock enshrines the misunderstanding
and the suite confirms it — *"the mock is the leak, and the mock is exactly what makes unit tests
cheap."*

Two independent routes to one place. That note's remedy is to **distrust the mock** and promote
E2E to ground truth; this one's is to **not need the mock**, by giving the logic nothing to mock.
They are complementary rather than competing, and the second is cheaper where it applies: a pure
function has no contract to misunderstand. What it does not remove is the shell, where the
contract misunderstanding simply relocates — the agentic case still needs the E2E check at the
boundary, because that is where the dependency now lives.

## Capability boundaries, not technical layers

> Instead of distributing business behavior across horizontal layers of entities, use cases,
> repositories, and adapters, the implementation of a business capability remains cohesive within
> its own boundaries… Each capability has its own functional core and its own imperative shell.
> It encapsulates its business behavior, the necessary technical interactions, and the
> responsibility for its consistency.

The property he names is **coherence** — *"the implementation of a capability remains coherent and
traceable"* — which is [change locality](change-locality.md) under another word: understanding
required for a change proportional to the change's scope rather than to the system's layering.

**Here the disagreement with [Layered Architecture](layered-architecture.md) is narrower than
either side suggests.** That note's most useful section is the **horizontal-to-vertical shift**:
slice by domain first, then layer within each slice, or the layers themselves become God-modules.
Fritzsche agrees entirely about the primary axis; he objects to the layering *inside* the slice.
Read together, the two notes bracket a live question — once a capability is the unit, is the
internal structure five layers or two parts? — rather than disagreeing about architecture
generally. The agreement is the more significant half.

## Where the argument is weaker than it reads

**The database claim is the weakest link and it is doing most of the rhetorical work:**

> In my decades of software development, how often have I seen someone come up with the idea of
> replacing the database technology in an existing application? Exactly zero times!

Personal experience, and a **weak argument form**: the value of a swappable dependency is
*option value*, which is not measured by how often the option is exercised. Nobody counts the
fire extinguishers they did not use. [Reversibility Decays](reversibility-decays.md) is the
repo's sharper treatment of exactly this — optionality is a running cost that must be maintained
rather than a property assessed once, and *"the strike price only rises"*. That note supports a
version of his conclusion better than his own argument does: the abstraction's option value
decays whether or not it is exercised, so paying for it indefinitely is the error — not the
abstraction existing.

He turns **Robert C. Martin's "The Database Is a Detail"** against its author, conceding the
rationale then asking *"what practical benefit this flexibility actually provides"*, and noting
the irony that technologies adopted to enable replacement *"often end up being extremely
difficult to replace"*. The irony lands; the ORM-as-immovable-dependency observation is fair and
widely felt.

**What he does not engage, and it is where layering actually earns its keep.** There is nothing
on **independent deployability** or **team boundaries** — the arguments that justify the ceremony
in large organisations, where a layer is also an ownership seam and a release unit. For a single
team on a single service his case is strong. For twelve teams it is not addressed, and
[DDD Strategic Design](ddd-strategic-design.md) and
[Team Topologies](team-topologies.md) are where that argument lives.

And the general objection to the whole genre applies to him as much as to his targets:
[Over-Engineering Is Solving the Wrong Problem](over-engineering.md) holds that structure should
be justified by constraints rather than adopted on principle, and
[Agile Design Decisions](agile-design-decisions.md) that structure should be added when it pays
for itself. **"Always FCIS" is the same move as "always Clean Architecture", with a different
default.** The honest reading of both is that the pattern is a tool whose cost has to be met by a
condition, and neither article names the condition.

## Relationship to other notes

- [Layered Architecture](layered-architecture.md) — the direct opposition, and a partial ally.
  Both make the domain the primary axis; they disagree about the structure inside the slice.
  That note also concedes it offers no guidance on when five layers is too much structure, which
  is the gap this argument occupies.
- [Clean Code and SOLID](../../concepts/clean-code-and-solid.md) — where Clean Architecture is
  defined in these notes ("system boundaries, dependency direction, domain isolation, framework
  independence"); this is the first note here that argues against it.
- [Agentic Verification](../ai-native/agentic-verification.md) — the same conclusion about mocks
  reached from verification. Distrust the mock versus do not need the mock.
- [Skeleton Architecture](skeleton-architecture.md) — Farry's skeleton/tissue split is FCIS for
  generated code under other names: a fixed `run()` holding the cross-cutting effects and a
  protected `_execute()` the model fills. It also isolates *"the functional core (tissue) from
  side effects (skeleton)"* for testing, which is this pattern applied to the agent problem.
- [Reversibility Decays](reversibility-decays.md) — the better argument for his conclusion than
  the one he makes: option value is a running cost, not a count of swaps performed.
- [Over-Engineering Is Solving the Wrong Problem](over-engineering.md) and
  [Agile Design Decisions](agile-design-decisions.md) — structure justified by constraints and
  added when it pays; the objection that applies to FCIS-by-default as much as to
  Clean-Architecture-by-default.
- [Change Locality and Boundary Drift](change-locality.md) — "coherence" at the capability level
  is that note's property under a different name.
- [Domain-Driven Design: Strategic Design](ddd-strategic-design.md) — where capability boundaries
  come from, and where the team-boundary argument he omits actually lives.
