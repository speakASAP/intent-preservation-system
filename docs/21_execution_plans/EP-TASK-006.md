# EP-TASK-006: Generate Context Package by Task Id

```yaml
id: EP-TASK-006
status: validated
source_task: ../11_tasks/TASK-006-generate-context-package-by-task-id.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-006.md
coding_prompt: ../14_prompts/PROMPT-TASK-006-context-package-generator.md
```

## Metadata

This execution plan implements TASK-006 and is validated by
`../12_validation/VAL-TASK-006-context-package-generator.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-002-context-package-generation.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-006.md
```

## Goal Impact

The plan advances Phase 3 by adding the first runnable context-package
generation workflow while keeping package content traceable to declared task
metadata.

## Project Invariants

- IPS-INV-001: task metadata remains the source for included upstream context.
- IPS-INV-002: protected vision and constitution files must not be modified.
- IPS-INV-003: validation commands must pass before closure.
- IPS-INV-005: tests and generated packages must avoid secrets and raw production data.

## Sensitive-Data Handling

Classification: none. The implementation reads repository Markdown files and
uses synthetic test fixtures only.

## Contract Validation Plan

The task materializes the existing context-package Markdown contract from
TASK-003. Contract validation is covered by strict documentation audit checks
for context package sections and references.

## Replay/Determinism Plan

The generator must produce stable Markdown for the same task metadata. Fixture
tests verify deterministic inclusion and overwrite safety.

## Scope

Add a dependency-free CLI that generates one Markdown context package for a
single task id from task metadata and required-context links.

## Non-Goals

- Do not implement graph traversal beyond declared task links.
- Do not implement vector or semantic retrieval.
- Do not generate coding prompts.
- Do not modify protected baseline documents.

## Files to Inspect

- `scripts/strict_doc_audit.py`
- `13_context_packages/README.md`
- `18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
- `04_systems/SYS-002-context-engine.md`
- `05_subsystems/SUB-003-context-packager.md`

## Files to Create

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `13_context_packages/CP-task-006.md`
- `12_validation/VAL-TASK-006-context-package-generator.md`

## Files to Modify

- `package.json`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Parse task metadata and required context from one task document.
2. Render an audit-valid context package with required schema sections.
3. Add overwrite protection unless `--force` is supplied.
4. Add fixture tests for generation and overwrite safety.
5. Generate the TASK-006 context package.
6. Update graph relationships and validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-006-A | Implement deterministic context-package generator and focused tests | yes, as the only implementation workstream | context-engine implementation agent | `scripts/context_package_generator.py`; `tests/test_context_package_generator.py` | CLI generator with overwrite safety and deterministic output | none |
| WS-006-D | Generate TASK-006 artifacts and graph links | no, dependency-gated | documentation/graph agent | `13_context_packages/CP-task-006.md`; `12_validation/VAL-TASK-006-context-package-generator.md`; `graph/project_graph.example.yaml`; `package.json` if command wiring changes | Generated context package, validation artifact and graph relationships | WS-006-A complete |
| WS-006-V | Run final validation and readiness gates | no, final integration | validation agent | validation report or terminal evidence for TASK-006 | Gate evidence and readiness recommendation | WS-006-A and WS-006-D complete |

WS-006-A may run in a separate Codex thread before implementation is complete.
WS-006-D and WS-006-V are serial because generated artifacts and validation
evidence depend on the final generator behavior.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-006-A | No open blocker recorded | context-engine implementation agent | Keep generation scoped to declared task metadata | resolved |
| WS-006-D | Requires final generator output | documentation/graph agent | Generate artifacts only after WS-006-A is stable | dependency-gated |
| WS-006-V | Requires implementation and artifact handoffs | validation agent | Run required gates and record evidence | dependency-gated |

## Parallel Dispatch List

### Goal WS-006-A: Context Package Generator

- Owner role: context-engine implementation agent.
- Objective: implement deterministic context-package generation for one task id.
- Allowed files: `scripts/context_package_generator.py`;
  `tests/test_context_package_generator.py`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, unrelated task artifacts and any secrets or raw
  production data.
- Required inputs: TASK-006, this plan, TASK-003 context-package schema and
  declared task metadata.
- Blockers: none open.
- Validation evidence: `python3 -m unittest tests.test_context_package_generator`.
- Handoff output: files changed, CLI behavior, tests run, blockers and
  deviations.

### Goal WS-006-D: Generated Artifacts And Graph Links

- Owner role: documentation/graph agent.
- Objective: generate TASK-006 context and validation artifacts and register
  graph/package command wiring after WS-006-A.
- Allowed files: `13_context_packages/CP-task-006.md`,
  `12_validation/VAL-TASK-006-context-package-generator.md`,
  `graph/project_graph.example.yaml`, `package.json` if command wiring changes.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-006-A handoff.
- Blockers: WS-006-A complete.
- Validation evidence: generated artifact review and strict audit output.
- Handoff output: artifact changes, graph changes, blockers and deviations.

### Goal WS-006-V: Final Validation

- Owner role: validation agent.
- Objective: run final validation for TASK-006.
- Allowed files: TASK-006 validation evidence only.
- Forbidden files: protected files and implementation files unless a validation
  defect is reported.
- Required inputs: WS-006-A and WS-006-D handoffs.
- Blockers: implementation and artifacts complete.
- Validation evidence: focused generator tests, `npm run validate`,
  pre-coding gate and deployment-readiness gate for TASK-006.
- Handoff output: validation evidence and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-006-A

You are the TASK-006 context-engine implementation agent. Implement deterministic
context-package generation from declared task metadata with overwrite safety.
Modify only `scripts/context_package_generator.py` and focused tests. Return
files changed, CLI behavior, tests run, blockers and deviations.

### Workstream WS-006-D

You are the TASK-006 documentation/graph agent. After WS-006-A, generate
TASK-006 context and validation artifacts and update graph/package wiring only
as needed. Return artifact changes, evidence, blockers and deviations.

### Workstream WS-006-V

You are the TASK-006 validation agent. After WS-006-A and WS-006-D, run focused
tests, repository validation, pre-coding gate and deployment-readiness gate for
TASK-006. Return command evidence and readiness recommendation.

## Test Plan

- Test package generation from synthetic task metadata.
- Test that generated packages include declared upstream, goal-impact,
  execution-plan, validation and required-context links.
- Test that existing output is not overwritten unless forced.

## Validation Plan

Run the focused generator tests, then run full repository validation.

## Gate Commands

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-006
```

## Documentation Updates

Add TASK-006 artifacts, generated context package, validation report and graph
nodes/edges.

## Rollback Plan

Remove the generator script, its tests, TASK-006 artifacts, generated package,
validation report and graph entries.

## Agent Handoff Prompt

Implement TASK-006 using this plan. Keep generation deterministic and scoped to
declared task metadata. Do not infer unrelated context or modify protected
baseline documents.

## Completion Checklist

- [x] Implementation complete
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
