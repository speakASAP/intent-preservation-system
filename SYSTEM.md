# System Index — Intent Preservation System

Status: factual index
Last verified: 2026-08-30T21:27:06Z
Source documents: `README.md`, `docs/06_architecture/ARCHITECTURE_OVERVIEW.md`, `docs/24_onboarding/PROJECT_ADOPTION_STANDARD.md`

## Purpose
Define and maintain the IPS documentation architecture, governance contracts, and validation tooling used across adopting repositories.

## Major components
- `docs/`: canonical layered IPS documentation (00–24).
- `scripts/`: audit, gate, adoption, and context tooling.
- `graph/`: schema and example knowledge graph assets.
- `config/`: validator and gate configuration.
- `tests/`: regression tests for tooling and contracts.
- `manager_interface/`: static manager visibility assets.

## Interfaces
- CLI entry points in `scripts/*.py`.
- Markdown and JSON governance artifacts under `docs/` and root indexes.
- Shared contract validation tooling consumed from `shared/scripts/*`.

## Runtime/deployment posture
- Repository kind: governance hub.
- Deployment mode: none (documentation/tooling repository only).

## Canonical detail
- `docs/06_architecture/ARCHITECTURE_OVERVIEW.md`
- `docs/README.md`
