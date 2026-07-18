# Onboarding Generation Guide

## Purpose

The onboarding package gives a human contributor or AI agent the minimum useful project understanding without loading the entire repository into context.

## Output files

Generated onboarding artifacts should be placed here:

```text
24_onboarding/generated/
```

Recommended files:

```text
ONBOARDING_HUMAN.md
ONBOARDING_AGENT.md
ONBOARDING_ARCHITECTURE.md
ONBOARDING_CURRENT_WORK.md
```

## Human onboarding package

Should include:

- What the project is
- What problem it solves
- Core principles
- Repository structure
- Current roadmap
- Key architecture decisions
- How to contribute documentation
- How to inspect Git diff before applying changes

## Agent onboarding package

Should include:

- Immutable documents
- Mutable documents
- Required workflow
- Forbidden actions
- Documentation completeness rules
- Context package rules
- Execution plan rules
- Validation rules

## Generation inputs

The onboarding generator should read:

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- `01_vision/VISION_EVOLUTION.md`
- `02_business_case/BUSINESS_CASE.md`
- `06_architecture/ARCHITECTURE_OVERVIEW.md`
- `07_decisions/*.md`
- `08_roadmap/ROADMAP.md`
- `23_documentation_contracts/*.md`

## Refresh triggers

Regenerate onboarding when:

- Vision evolution is approved.
- Major ADR is added.
- Roadmap changes.
- Documentation rules change.
- Execution plan process changes.
- Knowledge graph schema changes.

## Completeness checklist

- [ ] Explains project purpose.
- [ ] Lists immutable documents.
- [ ] Lists core workflow.
- [ ] Links to architecture and ADRs.
- [ ] Explains how tasks become execution plans.
- [ ] Explains validation requirements.
- [ ] Explains what agents must not do.
