---
type: note
title: C4 Model
description: "four-level architecture diagramming with PlantUML and Structurizr DSL examples"
tags: [architecture, system-design, documentation]
topic: engineering/architecture
status: notes
updated: 2026-06-13
related:
  - engineering/ai-native/agentic-sdlc.md
  - engineering/practices/engineering-playbook.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adr.md
  - engineering/architecture/design-docs.md
source: "https://gist.github.com/fabianmagrini/caa685a8f63028f17da6feed7a848114"
---

# C4 Model

The C4 model is a simple, pragmatic way to describe software architecture using four deliberately different levels of diagrams. Designed to be readable without complex notation — teams can communicate architecture without drowning in UML formalism.

> "Readable diagrams beat formal completeness."

## The four levels

| Level | Name | Audience | Shows |
|---|---|---|---|
| 1 | System Context | Executives, stakeholders, newcomers | The system, its users, and external dependencies |
| 2 | Container | Architects, engineers | Applications, services, data stores and how they communicate |
| 3 | Component | Developers | Internal modules within a single container |
| 4 | Code | Rarely used | Classes, interfaces, methods, database tables |

## When to use each level

| Goal | Use |
|---|---|
| Explaining the system to executives or product owners | Level 1 |
| Designing deployment, runtime responsibilities, API boundaries | Level 2 |
| Planning internal module boundaries, team ownership, service decomposition | Level 3 |
| Documenting class design, important algorithms, database schema | Level 4 |

## Core notation

- **Boxes** — systems, containers, components, or classes depending on level
- **Arrows** — relationships and interactions; label with protocol, data, and frequency
- **People icons** — actors and users
- **Labels** — name, technology, short responsibility description
- Show technology only where it helps (e.g., "PostgreSQL" not generic "DB")

## Worked example: e-commerce system

### Level 1 — System Context

```
[Customer] → E-commerce System → [Payment Gateway]
                               → [Shipping Provider]
```

Boxes: the system, one user type, two external dependencies. Arrows show direction and purpose.

### Level 2 — Containers

Inside the E-commerce System:

```
[Web App (React)] → [API App (Node.js)] → [Database (PostgreSQL)]
                                        → [Worker Service]
                                        → [Payment Gateway]
                                        → [Shipping Provider]
```

### Level 3 — Components inside API App

```
Order Component → Payment Adapter → [Payment Gateway]
               → Shipping Adapter → [Shipping Provider]
Catalog Component
Auth Component
```

### Level 4 — Code inside Order Component

```
OrderService → OrderRepository
             → OrderValidator
```

## Diagrams as code

Prefer code-based tools over visual editors — diagrams stay versioned, diffable, and reproducible alongside the code they document.

### PlantUML (C4-PlantUML library)

**Level 1 — System Context**

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(customer, "Customer", "Places orders on the system")
System(ecom, "E-commerce System", "Manages products, orders, and payments")
System_Ext(payment, "Payment Gateway", "Processes payments")
System_Ext(shipping, "Shipping Provider", "Handles deliveries")

Rel(customer, ecom, "Places orders")
Rel(ecom, payment, "Processes payments via HTTPS")
Rel(ecom, shipping, "Requests deliveries via HTTPS")
@enduml
```

**Level 2 — Containers**

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(customer, "Customer", "Places orders")

System_Boundary(ecom, "E-commerce System") {
    Container(web, "Web App", "React", "Provides UI for customers")
    Container(api, "API App", "Node.js/Express", "Handles business logic and APIs")
    ContainerDb(db, "Database", "PostgreSQL", "Stores products, orders, users")
    Container(worker, "Worker Service", "Node.js worker", "Processes background jobs")
}

System_Ext(payment, "Payment Gateway", "Processes payments")
System_Ext(shipping, "Shipping Provider", "Handles deliveries")

Rel(customer, web, "Uses")
Rel(web, api, "HTTP/REST")
Rel(api, db, "Reads/Writes", "SQL")
Rel(api, worker, "Dispatches tasks")
Rel(api, payment, "Processes payments via HTTPS")
Rel(api, shipping, "Requests shipments via HTTPS")
@enduml
```

**Level 3 — Components (inside API App)**

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

Component(order, "Order Component", "Module", "Handles order creation and lifecycle")
Component(catalog, "Catalog Component", "Module", "Manages product catalog")
Component(auth, "Auth Component", "Module", "User authentication & JWT")
Component(paymentAdapter, "Payment Adapter", "Module", "Integration with Payment Gateway")
Component(shippingAdapter, "Shipping Adapter", "Module", "Integration with Shipping Provider")

Rel(order, paymentAdapter, "Uses")
Rel(order, shippingAdapter, "Uses")
@enduml
```

**Level 4 — Code (inside Order Component)**

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Code.puml

Class(orderService, "OrderService") {
  +createOrder()
  +cancelOrder()
}
Class(orderRepo, "OrderRepository") {
  +save(order)
  +findById(id)
}
Class(orderValidator, "OrderValidator") {
  +validate(orderData)
}

Rel(orderService, orderRepo, "Uses")
Rel(orderService, orderValidator, "Uses")
@enduml
```

### Structurizr DSL

**Level 1 — System Context**

```dsl
workspace {
    model {
        user = person "Customer" { description "Places orders on the system" }
        ecom = softwareSystem "E-commerce System" { description "Manages products, orders, and payments" }
        payment = softwareSystem "Payment Gateway" { external true }
        shipping = softwareSystem "Shipping Provider" { external true }

        user -> ecom "Places orders"
        ecom -> payment "Processes payments via HTTPS"
        ecom -> shipping "Requests deliveries via HTTPS"
    }
    views {
        systemContext ecom { include * ; autolayout lr }
        theme default
    }
}
```

**Level 2 — Containers**

```dsl
workspace {
    model {
        user = person "Customer"
        ecom = softwareSystem "E-commerce System" {
            container web "Web App" "React" "Provides UI"
            container api "API App" "Node.js/Express" "Business logic"
            container db "Database" "PostgreSQL" "Persistent storage"
            container worker "Worker Service" "Node.js" "Background jobs"
        }
        payment = softwareSystem "Payment Gateway" { external true }
        shipping = softwareSystem "Shipping Provider" { external true }

        user -> web "Uses"
        web -> api "HTTP/REST"
        api -> db "Reads/Writes"
        api -> worker "Dispatches tasks"
        api -> payment "Processes payments via HTTPS"
        api -> shipping "Requests shipments via HTTPS"
    }
    views {
        container ecom { include * ; autolayout lr }
        theme default
    }
}
```

## Best practices

- One diagram per level per system — do not combine levels
- Label every interaction with protocol, payload type, or frequency
- Each box has a single clear responsibility
- Version diagrams with the code (same repo, same PR)
- Review diagrams with the team — they often surface architectural mismatches and missing responsibilities
- Provide zoom context: always have a Level+1 (higher) and Level-1 (lower) diagram available

## Review checklist

Before sharing a diagram:

- [ ] Is the audience for this level clear? (stakeholders vs developers)
- [ ] Is each box's responsibility stated concisely?
- [ ] Are all external dependencies shown and labelled?
- [ ] Are interactions labelled with protocol, data, or frequency?
- [ ] Is there a diagram one level up (context) and one level down (detail) available?
