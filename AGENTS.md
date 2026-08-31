# Agents

## Required reading
- `README.md`
- `SYSTEM.md`
- `BUSINESS.md`
- `TASKS.md`
- `docs/24_onboarding/PROJECT_ADOPTION_STANDARD.md`
- `scripts/validate_adoption_profile.py`
- `scripts/scaffold_project_adoption.py`

## Authority
This repository is the owner of the IPS standards, templates, schemas, and validation logic for the wider ecosystem. It provides the governance and onboarding framework, but it does not operate an application runtime.

## Intent preservation system
This repo is the source-of-truth IPS implementation used to preserve project intent, validation evidence, and operational boundary clarity across service and hub repos.

## Safety and operations
- Keep the standard truthful about repo ownership boundaries and runtime scope.
- Avoid inventing runtime capabilities or over-claiming service ownership in the ecosystem.
- Prefer clear, reviewable governance changes and traceability updates over ad hoc repo-by-repo exceptions.

## Project-specific rules
- Do not describe this repo as a runtime service or product application.
- Do not assign a service deployment or user-facing runtime boundary it does not own.
- Maintain the standards and validator framework as a shared governance platform for the wider ecosystem.

## Required final report
The final report must describe the repo’s role as the IPS standards and validation hub, list validation evidence, and clarify that service runtime ownership remains with the individual repos that run those workloads.
