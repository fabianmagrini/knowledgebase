---
title: The Micro-Frontend Shell as Platform Runtime
tags: [architecture, system-design, microservices]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/micro-frontend-canvas.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/design-systems-ai-control-plane.md
updated: 2026-06-22
---

# The Micro-Frontend Shell as Platform Runtime

In a single-page-app shell that hosts Module Federation micro-frontends, the
shell is best built as a **platform runtime, not a layout wrapper**. Its job is
to own the *enterprise runtime* — the cross-cutting services every product area
needs — so that each remote can focus on its own domain rather than reinventing
auth, navigation, telemetry, and HTTP.

This is the concrete operationalisation of several
[micro-frontend principles](micro-frontend-principles.md): the platform should
provide *guardrails, not dependencies* (autonomy), MFEs should *consume shared
platform services rather than reimplement them* (shared-nothing-by-default), and
navigation/identity/design are *shell-owned* to keep the experience seamless.

## Core shell services

The shell typically provides these as platform services. Each is something a
remote should consume, not re-implement.

| # | Service | Owns | Notes |
|---|---|---|---|
| 1 | **Routing** | Top-level routing; which MFE mounts for each route | Route registry, lazy remote loading, guards, fallbacks, 404/unauthorized, deep links |
| 2 | **Session / authentication** | The user session | Login/logout orchestration, token refresh, timeout, SSO, secure token handoff to remotes |
| 3 | **Authorization / entitlements** | What the user may see and do | Role/permission lookup, route + menu + action-level checks |
| 4 | **Navigation / menu** | Global navigation | Primary/side nav, breadcrumbs, active state, permission-filtered menus, cross-MFE nav APIs |
| 5 | **Layout** | The application frame | Header, sidebar, footer, content container, skeletons, error boundaries, full-screen mode |
| 6 | **Remote module registry** | Where MFEs live | Remote manifest loading, env-specific URLs, version metadata, health/fallback, canary rollout |
| 7 | **Feature flags** | Flag evaluation | Enable/disable MFEs, experiments, phased rollout, kill switches, cohort targeting |
| 8 | **Configuration** | Runtime config | API base URLs, env metadata, CDN paths, tenant/brand config, telemetry keys |
| 9 | **Event bus / messaging** | Loose shell↔MFE communication | Cross-MFE events, commands, session/navigation events — *use sparingly* |
| 10 | **Notifications** | Toasts, alerts, banners | Outage/maintenance banners, contextual notifications |
| 11 | **Error handling** | Consistent error UX | Global boundary, remote-load-failure handling, forbidden/unauthorized, retry, correlation IDs |
| 12 | **Observability / telemetry** | Standardised instrumentation | Page/route views, remote load times, Core Web Vitals, errors, tracing headers |
| 13 | **API client / platform HTTP** | Shared HTTP abstraction | Auth headers, correlation IDs, retry/timeout, error mapping, interceptors |
| 14 | **Design system integration** | Shared UI foundations | Theme provider, tokens, CSS baseline, dark/light, density, brand switching |
| 15 | **State / context** | A *small* set of global state | Current user, selected account/customer, tenant/brand, locale, workspace, session status |
| 16 | **Localization** | Language and formatting | Locale selection, date/currency formatting, translation loading, timezone handling |
| 17 | **Accessibility / focus** | Cross-MFE a11y conventions | Focus restore on navigation, skip links, page-title and route announcements, modal stacking |
| 18 | **MFE lifecycle** | How remotes mount/unmount/fail | Mount/unmount contract, cleanup hooks, readiness signals, version checks, degraded mode |

A few of these warrant emphasis:

- **Authorization** is a capability check, not a UI concern. Expose it as a simple
  predicate the shell and remotes share:

  ```ts
  can("accounts.transfer")
  can("cards.freeze")
  can("admin.viewAudit")
  ```

- **Remote registry** decouples deployment from the build. The shell loads a
  manifest at runtime rather than baking remote URLs into the bundle:

  ```json
  {
    "accounts": {
      "remoteEntry": "https://cdn/app/accounts/remoteEntry.js",
      "scope": "accounts",
      "module": "./Routes"
    }
  }
  ```

- **Event bus** is powerful and easily abused. Prefer explicit contracts over a
  global free-for-all; reserve the bus for genuinely cross-cutting signals such as
  `session:expired` or `customer:selected`.

- **Error handling** matters more here than in a monolith because remotes load
  *independently* — a single remote failing to load must not take down the frame.

## The platform contract

Expose a small, typed contract to remotes rather than letting each one wire up its
own cross-cutting concerns:

```ts
type ShellPlatform = {
  auth: AuthService
  navigation: NavigationService
  permissions: PermissionService
  config: ConfigService
  notifications: NotificationService
  telemetry: TelemetryService
  http: HttpService
  eventBus: EventBus
  logger: LoggerService
}
```

Remotes receive it either through the mount contract:

```ts
mount(container, {
  platform,
  routeParams,
  initialContext
})
```

or through a shared provider:

```tsx
<ShellPlatformProvider value={platform}>
  <RemoteApp />
</ShellPlatformProvider>
```

## What not to put in the shell

The failure mode is a shell that grows into a giant shared application — a
distributed monolith with a single chokepoint. Keep product concerns out:

- individual product workflows and domain business rules
- MFE-specific forms and page-level UI state
- feature-specific API orchestration and validation
- complex shared stores used by everyone

Mirroring service 15: good shell-owned state is *global context* (current user,
tenant, locale, selected account); bad shell-owned state is *page/form state* and
*domain state owned by one product area*. The shell owns the **enterprise
runtime**, not every product concern.

## Recommended minimum set

A strong platform foundation without turning the shell into a monolith starts with
twelve services:

1. Routing
2. Auth / session
3. Authorization
4. Navigation / menu
5. Layout
6. Remote registry
7. Runtime config
8. Notifications
9. Error handling
10. Observability
11. HTTP client
12. Feature flags

The remaining services (localization, a11y, design-system providers, lifecycle,
event bus, shared state) are added as the platform matures.

## Relationship to other notes

- [Microfrontend Architecture Principles](micro-frontend-principles.md) — the
  principles this shell embodies: platform-over-governance, shared-nothing-by-
  default, shell-owned navigation, and team autonomy. This note is the *runtime*
  that delivers them.
- [The Micro-Frontend Canvas](micro-frontend-canvas.md) — designs one remote's
  boundary; this note designs the host that composes the remotes.
- [Composable Architecture](composable-architecture.md) — the wider
  packaged-business-capability paradigm the shell and remotes sit within.
- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) —
  the shared design system the shell applies as a global provider (service 14).
