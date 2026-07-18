# EP-TASK-002: Detect Missing Traceability Fields

## Metadata

```yaml
id: EP-TASK-002
status: draft
source_task: ../11_tasks/TASK-002-detect-missing-traceability-fields.md
owner: documentation-audit-agent
created: 2026-06-08
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: validates
replay_determinism_impact: required
required_gates:
  - pre-coding
  - strict-doc-audit
```

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-001-documentation-audit.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-002.md
```

## Goal Impact

This plan supports intent preservation by making missing upstream, goal-impact
and execution-plan links visible before implementation work proceeds.

## Project Invariants

This plan preserves the protected Vision -> Goal Impact -> System -> Feature
-> Task -> Execution Plan -> Coding Prompt -> Code -> Validation chain by
making missing links visible before downstream agents receive implementation
context.

Source policy: `../17_governance/PROJECT_INVARIANTS.md`

## Sensitive-Data Handling

Use only repository documentation and synthetic fixtures. Do not add raw
production data, credentials, customer data or private integration payloads to
tests, prompts, reports or audit examples.

Source policy: `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Contract Validation Plan

| Contract or schema | Impact | Validator/command | Evidence path | Owner |
|---|---|---|---|---|
| Documentation traceability fields for task-like artifacts | validates | `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues` | terminal output or validation report for TASK-002 | documentation-audit-agent |

## Replay/Determinism Plan

| Behavior | Required? | Validation method | Evidence path |
|---|---|---|---|
| Replay | yes | Run the same fixture tests and strict audit twice with unchanged inputs. | terminal output or validation report for TASK-002 |
| Idempotency | yes | Confirm audit execution does not mutate repository artifacts. | git status before/after validation |
| Deterministic output | yes | Assert path-level findings and remediation guidance are stable for the same fixtures. | fixture test output |

## Scope

Add audit checks that detect missing traceability metadata and missing
cross-artifact links for task-like implementation artifacts.

## Non-Goals

- Do not infer goals from unrelated prose.
- Do not change protected vision or constitution files.
- Do not implement remote integrations.

## Parallelization Plan

TASK-002 is a single implementation workstream because the traceability parser,
audit findings, fixture expectations and strict-audit behavior share one public
contract. Splitting implementation across agents would create avoidable
conflicts in `scripts/strict_doc_audit.py` and the same fixture assertions.

### Ready-Now Parallel Goals

None. The only ready-now workstream is the single implementation/integration
goal `WS-002-A`.

### Dependency-Gated Goals

`WS-002-FINAL` depends on `WS-002-A` and records final validation evidence after
the audit behavior and tests are implemented.

### Blockers

None open.

### Shared Files And Merge Order

`scripts/strict_doc_audit.py` and the TASK-002 fixture tests are shared by the
implementation and validation concerns. Merge order is:

1. `WS-002-A` implementation and focused tests.
2. `WS-002-FINAL` strict audit, gate evidence and documentation handoff.

## Files to Inspect

- `scripts/strict_doc_audit.py`
- `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `22_goal_impact/GOAL_IMPACT_MAPPING.md`

## Files to Create

- Fixture tests for missing traceability cases.

## Files to Modify

- `scripts/strict_doc_audit.py`
- CI validation scripts if needed.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. `WS-002-A`: Parse required metadata from front matter and fenced YAML blocks.
2. `WS-002-A`: Detect missing upstream, goal-impact and execution-plan links.
3. `WS-002-A`: Verify linked files exist.
4. `WS-002-A`: Report actionable findings with paths and remediation templates.
5. `WS-002-FINAL`: Run focused tests and strict audit; record deterministic validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-002-A | Implement deterministic missing-traceability checks and focused tests. | yes, as the only implementation workstream | documentation-audit implementation agent | `scripts/strict_doc_audit.py`; TASK-002 fixture tests under `tests/`; TASK-002 validation artifact if evidence must be recorded | Audit findings for missing upstream, goal-impact and execution-plan links; focused tests | none |
| WS-002-FINAL | Final integration and validation for TASK-002. | no; dependency-gated | validation owner in the integration session | validation commands; TASK-002 validation report or terminal evidence | strict audit evidence, gate result and handoff summary | WS-002-A complete |

Separate Codex threads are not applicable for TASK-002 because only one
source-backed implementation workstream exists. `WS-002-FINAL` is
dependency-gated and should stay with the integration owner after `WS-002-A`
lands.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-002-A | none | documentation-audit implementation agent | not applicable | resolved |
| WS-002-FINAL | WS-002-A implementation and tests | validation owner | Run focused tests and strict audit after implementation | dependency-gated |

## Parallel Dispatch List

### Goal WS-002-A: Missing Traceability Audit Implementation

- Owner role: documentation-audit implementation agent
- Objective: Implement deterministic checks for missing upstream, goal-impact and execution-plan links in task-like artifacts.
- Allowed files: `scripts/strict_doc_audit.py`; focused TASK-002 tests under `tests/`; TASK-002 validation artifact only if recording evidence.
- Forbidden files: `00_constitution/CONSTITUTION.md`; `01_vision/VISION.md`; unrelated roadmap, feature, task, prompt and context-package artifacts.
- Required inputs: `../11_tasks/TASK-002-detect-missing-traceability-fields.md`; `../22_goal_impact/GOAL-IMPACT-TASK-002.md`; `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`; `../22_goal_impact/GOAL_IMPACT_MAPPING.md`; templates listed in the source task.
- Blockers: none.
- Validation evidence: focused fixture tests and `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues`.
- Handoff output: code/test diff summary, validation commands run, findings format examples, deviations if any.

### Goal WS-002-FINAL: Integration And Validation

- Owner role: validation owner/integration agent
- Objective: Verify the implemented TASK-002 audit behavior preserves traceability contracts and repository gates.
- Allowed files: validation report or executor evidence for TASK-002; no implementation files unless a validation defect must be fixed.
- Forbidden files: `00_constitution/CONSTITUTION.md`; `01_vision/VISION.md`; unrelated implementation files.
- Required inputs: completed `WS-002-A` handoff and repository gate policies.
- Blockers: `WS-002-A` must be complete.
- Validation evidence: focused tests, strict doc audit, pre-coding gate if operational changes are present.
- Handoff output: final validation summary and any residual risks.

## Parallel Agent Handoff Prompts

### Workstream WS-002-A

Implement TASK-002 missing-traceability detection in the Intent Preservation
System. Read `11_tasks/TASK-002-detect-missing-traceability-fields.md`,
`22_goal_impact/GOAL-IMPACT-TASK-002.md`,
`23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md` and
`22_goal_impact/GOAL_IMPACT_MAPPING.md` first. Modify only
`scripts/strict_doc_audit.py`, focused tests under `tests/` and a TASK-002
validation artifact if evidence must be recorded. Do not modify
`00_constitution/CONSTITUTION.md`, `01_vision/VISION.md` or unrelated generated
context/prompt files. Add deterministic findings for missing upstream,
goal-impact and execution-plan links, broken local references and remediation
guidance. Validate with focused tests and
`python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues`.
Return a handoff summary with changed files, validation evidence and deviations.

### Workstream WS-002-FINAL

Validate the completed TASK-002 implementation. Use the `WS-002-A` handoff,
run the focused tests and strict documentation audit, confirm no protected
Vision or Constitution files changed, and record the evidence in the TASK-002
validation artifact or final handoff summary. Do not broaden implementation
scope unless validation exposes a defect in TASK-002 behavior.

## Test Plan

- Test a complete traceability chain.
- Test a task missing goal-impact links.
- Test a task missing execution-plan links.
- Test broken local references.

## Validation Plan

Run fixture tests and the strict audit against this repository.

## Gate Commands

Source policy: `../23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`

```bash
python3 scripts/pre_coding_gate.py --root .
python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues
```

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Pre-coding | yes | `python3 scripts/pre_coding_gate.py --root .` | terminal output or TASK-002 validation report | yes |
| Contract/schema | yes | `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues` | terminal output or TASK-002 validation report | yes |
| Replay/determinism | yes | focused TASK-002 fixture tests run twice with unchanged inputs | terminal output or TASK-002 validation report | yes |
| Integration-readiness | yes | strict doc audit against repository | terminal output or TASK-002 validation report | yes |
| Deployment-readiness | no | not required for local audit behavior unless deployment gate changes | not applicable | no |

## Documentation Updates

Update audit reports and task metadata when the checks are implemented.

## Rollback Plan

Revert only audit code, tests and documentation artifacts created for this task.

## Agent Handoff Prompt

Use the workstream-specific prompts under `Parallel Agent Handoff Prompts`.
Final integration remains with `WS-002-FINAL`.

## Completion Checklist

- [x] Traceability metadata checks implemented.
- [x] Broken reference checks implemented.
- [x] Fixture tests added.
- [x] Parallelizable workstreams identified.
- [x] Blockers and serial dependencies documented.
- [x] Agent handoff prompts created for independent workstreams or documented single-agent execution.
- [x] Integration order documented.
- [x] Strict audit passes after repository fixes.
- [x] Validation report created.
