# Agent operations

## Roles
- Readiness scanner: confirm whether a change is standards-led or runtime-specific in a consuming repo.
- Worker agent: implement one IPS change with explicit governance traceability.
- Worker monitor: check for cross-repo conflicts in onboarding standards and validator behavior.
- Integration validator: validate the repo remains a standards hub and does not claim a runtime service.

## Before work
- Confirm the change is in IPS standard or tooling scope rather than in a service-owned runtime.
- Inspect the affected standard, template, validator, or onboarding doc before editing.
- Preserve the repo’s honest standards-hub boundary.

## Parallel work
- Large IPS updates should be coordinated with the ecosystem repos they affect.
- No parallel workstream should claim runtime ownership that belongs to a service repo.

## Validation debt
- Known runtime-service issues belong to the owning service repo, not this standards hub.
- Documentation-only updates do not create runtime ownership.

## Handoff
- Document any standard or template change that affects multiple project onboarding profiles downstream.

## Project-specific operations
- Standards changes must remain generic, reviewable, and compatible with multiple repo archetypes.
- Adoption and validation updates must remain truthful about the repo’s non-runtime scope.
