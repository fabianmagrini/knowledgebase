---
type: note
title: Caching Reference Data APIs
description: "cache patterns for slow-moving lookup data (long TTL + ETag, versioned datasets, Redis cache-aside, event invalidation, stale-while-revalidate) and a recommended enterprise topology"
tags: [api-design, performance, system-design]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/composable-architecture.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/performance-testing-strategy.md
  - concepts/resilient-software-design.md
  - tools/dynamic-configuration-sidecar.md
  - case-studies/zalando-client-side-load-balancing.md
updated: 2026-07-01
---

# Caching Reference Data APIs

Reference data is the slow-moving lookup data an application reads constantly but
rarely writes: countries, currencies, product types, branch lists, feature
codes, account categories, limits, dropdown values. For APIs serving this data
the goal is a specific quartet — **fast reads, low origin load, safe freshness,
and predictable invalidation.** The patterns below are the toolbox; most systems
combine a few.

## The patterns

### 1. Long HTTP TTL + ETag

Best for data that changes rarely. Let clients and gateways cache the response,
and use an `ETag` so they can revalidate cheaply instead of refetching.

```http
Cache-Control: public, max-age=86400
ETag: "refdata-v42"
```

Good for countries, currencies, static product categories, UI dropdowns.

### 2. Versioned reference data

Expose a version in the URL or response and publish a new version when data
changes — this sidesteps complex invalidation entirely.

```http
GET /reference-data/v42/countries
```

```json
{ "version": "42", "items": [] }
```

Good for enterprise/bank data where consumers need contract stability.

### 3. Cache-aside

The API checks the cache first and falls back to the source of truth on a miss,
populating the cache on the way back. This is the sensible default for reference
APIs.

```text
Request → API → Redis
             ↓ miss
          Database / CMS / Config Store → populate Redis
```

Use Redis for shared cache, in-memory for per-instance hot data, and a TTL as a
safety net.

### 4. Read-through

The cache layer itself knows how to load missing data, so application code just
asks the cache. Cleaner for callers but needs a solid cache abstraction — worth
it when many APIs share the same reference data.

### 5. Pre-warmed

Load all active reference data into memory on startup or deployment. Great when
the dataset is small and read frequently; watch for large datasets, startup
latency, and multi-instance consistency.

### 6. Event-driven invalidation

When reference data changes, publish an event; caches clear or refresh in
response. Good for data that changes occasionally but must propagate quickly.

```json
{ "type": "ReferenceDataChanged", "domain": "countries", "version": "43" }
```

### 7. Stale-while-revalidate

Serve cached data immediately and refresh in the background — right for
user-facing APIs where slightly stale data is acceptable.

```http
Cache-Control: max-age=300, stale-while-revalidate=3600
```

## Recommended enterprise topology

For a bank or large enterprise:

```text
Reference Data Source → Reference Data API → Redis / Distributed Cache
    → API Gateway / BFF / Consumers
```

with `ETag` and `Cache-Control` support, versioned datasets, Redis cache-aside,
event-driven invalidation, a short emergency-TTL fallback, and an audit trail for
reference-data changes. This layers onto the gateway/BFF/consumer structure in
[Composable Architecture](composable-architecture.md); the emergency TTL is a
[resilient-design](../../concepts/resilient-software-design.md) safety net for
when the source or event bus is unavailable.

## Practical default by data type

| Data type | Pattern |
|---|---|
| Very static | Long HTTP TTL + ETag |
| Small and hot | In-memory cache + version |
| Shared across services | Redis cache-aside |
| Must refresh quickly | Event invalidation |
| Large lookup data | Paginated API + partial cache |
| Consumer stability needed | Versioned reference data |

## Default recommendation

**Versioned reference data + Redis cache-aside + ETag.** That combination buys
fast reads, low database load, safe refresh, easy rollback, and consumer-friendly
contracts. A good endpoint shape:

```http
GET /reference-data/account-types
GET /reference-data/account-types?version=latest
GET /reference-data/account-types?version=2026-07-01
```

```json
{
  "name": "account-types",
  "version": "2026-07-01",
  "lastUpdated": "2026-07-01T08:30:00Z",
  "items": [
    { "code": "SAVINGS", "label": "Savings Account", "active": true }
  ]
}
```

Note the endpoint uses a plural collection noun and a `version` query parameter —
the REST conventions in [Naming Conventions](../practices/naming-conventions.md).
The version and `lastUpdated` fields are what make the cache contract legible to
consumers and testable against an [API contract](../practices/api-contract-functional-testing.md).
