# Integration contract

## Purpose
This contract documents that `intent-preservation-system` is a standards and governance hub, not an application runtime. It defines the ecosystem boundary for the IPS templates, validators, and onboarding guidance used across the platform.

## Capability decisions
- auth: not-applicable — no auth runtime is owned by this repo.
- postgres: not-applicable — no database runtime is owned by this repo.
- redis: not-applicable — no Redis runtime is owned by this repo.
- logging: not-applicable — logging is emitted by the service repos and platform layers, not by this standards repo.
- notifications: not-applicable — notifications remain the responsibility of runtime service repos.
- ai: not-applicable — AI runtime ownership stays outside this repo.
- payments: not-applicable — payment handling is not within the standards repo scope.
- catalog: not-applicable — catalog ownership remains with the service repos that own the product domain.
- orders: not-applicable — order-processing runtime ownership is outside the repo.
- warehouse: not-applicable — warehouse ownership is outside this repo.
- invoices: not-applicable — invoice ownership remains outside the repo.
- object-storage: not-applicable — object storage remains outside the standards repo.
- event-bus: not-applicable — event-bus contracts belong to runtime services and not to this repo.
- docs-rag: not-applicable — this repo provides the governance standard, not the retrieval service.
- monitoring: not-applicable — monitoring remains with the runtime repos and platform components.
- backups: not-applicable — backup ownership remains with the service or platform layers.

## Data ownership
The repo stores governance, validation, and onboarding artifacts, not service runtime data, customer records, product truth, or payment payloads.

## Authentication and authorization
No service-specific auth boundary exists in this repo. Authentication and access controls remain with the runtime service repos and platform security layers that depend on the IPS standard.

## Synchronous dependencies
- `shared` and the service repos that consume the IPS standard and adoption templates
- Ecosystem governance and deployment conventions across the wider Alfares platform

## Asynchronous dependencies
- Consumer repos apply the standard in their own onboarding and governance flow
- No event-stream ownership is claimed by the IPS standards repo itself

## Degraded operation
If the IPS standard or validator is unavailable, consuming repos must keep their own governance evidence and wait for the standard to be restored rather than inventing a runtime service claim for this repo.

## Validation
- `python3 intent-preservation-system/scripts/validate_adoption_profile.py --root intent-preservation-system --phase planning`
- Adoption quality review stays focused on truthful boundary ownership and standards consistency across the ecosystem
