# Audit Checklist

## Purpose

This checklist verifies whether the project documentation is complete enough for safe AI-assisted implementation.

## Core source-of-truth checks

- [ ] Constitution exists.
- [ ] Vision exists.
- [ ] Vision is marked immutable.
- [ ] Vision evolution log exists.
- [ ] Business case exists.

## Decomposition checks

- [ ] Systems are documented.
- [ ] Subsystems are documented.
- [ ] Features are documented.
- [ ] Tasks are documented.
- [ ] Tasks link to upstream features or milestones.

## Goal impact checks

- [ ] Goal impact mapping guide exists.
- [ ] Every feature has goal impact.
- [ ] Every task has goal impact.
- [ ] Every execution plan has goal impact.
- [ ] No implementation artifact has `impact_level: none` without justification.

## Execution plan checks

- [ ] Execution plan guide exists.
- [ ] Coding tasks have execution plans.
- [ ] Execution plans define scope and non-goals.
- [ ] Execution plans list files to inspect, create, modify, and protect.
- [ ] Execution plans include test and validation plans.
- [ ] Execution plans include rollback plans.

## Semantic compression checks

- [ ] Semantic compression guide exists.
- [ ] Important long documents have summaries.
- [ ] Important long documents have ultra-summaries where useful.
- [ ] Summaries link back to source documents.
- [ ] Summaries preserve constraints and traceability.

## Knowledge graph checks

- [ ] Graph schema exists.
- [ ] Graph example exists.
- [ ] Tasks connect to goals.
- [ ] Execution plans connect to tasks.
- [ ] Coding prompts connect to execution plans.
- [ ] Validation reports connect to validated artifacts.

## Documentation completeness checks

- [ ] Documentation completeness standard exists.
- [ ] Agent gap filling rules exist.
- [ ] Major documents include metadata.
- [ ] Required sections exist.
- [ ] Required sections are not empty.
- [ ] Missing information is marked with `[MISSING: ...]`.
- [ ] Unknown information is marked with `[UNKNOWN: ...]`.

## Onboarding checks

- [ ] Onboarding generation guide exists.
- [ ] Agent onboarding template exists.
- [ ] Human onboarding can be generated from approved docs.
- [ ] Agent onboarding lists forbidden actions.

## Validation checks

- [ ] Validation pyramid exists.
- [ ] Validation report template exists.
- [ ] Every task has a validation task.
- [ ] Every completed execution plan has validation evidence.

## Audit output

The audit should produce:

- Missing files
- Missing sections
- Empty sections
- Missing traceability
- Missing goal impact
- Missing execution plans
- Suggested remediation
