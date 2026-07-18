# EP-TASK-003: Create Context Package Schema

## Metadata

```yaml
id: EP-TASK-003
status: draft
source_task: ../11_tasks/TASK-003-create-context-package-schema.md
owner: context-engine-agent
created: 2026-06-08
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: parallel_goals
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
feature: ../10_features/FEAT-002-context-package-generation.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-003.md
```

## Goal Impact

This plan supports bounded context generation by enforcing a stable context
package artifact contract.

## Project Invariants

This plan preserves the Vision -> Goal Impact -> System -> Feature -> Task ->
Execution Plan -> Coding Prompt -> Code -> Validation chain by requiring
context packages to carry explicit target task, traceability, constraints and
validation sections before agents use them.

Source policy: `../17_governance/PROJECT_INVARIANTS.md`

## Sensitive-Data Handling

Use repository documentation and synthetic fixture content only. Do not include
credentials, production logs, private integration payloads or customer data in
context-package examples, tests or validation evidence.

Source policy: `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Contract Validation Plan

| Contract or schema | Impact | Validator/command | Evidence path | Owner |
|---|---|---|---|---|
| Context package required-section contract | validates | `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues` | terminal output or TASK-003 validation report | context-engine-agent |

## Replay/Determinism Plan

| Behavior | Required? | Validation method | Evidence path |
|---|---|---|---|
| Replay | yes | Run focused context-package fixture tests twice with unchanged inputs. | terminal output or TASK-003 validation report |
| Idempotency | yes | Confirm strict audit does not mutate context-package artifacts. | git status before/after validation |
| Deterministic output | yes | Verify missing-section and broken-reference findings are stable for the same fixtures. | fixture test output |

## Scope

Define and audit the required sections of context package documents.

## Non-Goals

- Do not implement vector retrieval.
- Do not generate prompts directly.
- Do not change task or feature scope.

## Parallelization Plan

TASK-003 can be decomposed into two ready-now workstreams because the context
package documentation contract and the audit implementation can be prepared in
separate files. A final integration workstream owns conflict resolution and
validation.

### Ready-Now Parallel Goals

- `WS-003-A`: Define or clarify the context-package section contract in
  context package guidance and templates.
- `WS-003-B`: Implement audit classification, section checks and fixture tests
  for context packages.

### Dependency-Gated Goals

- `WS-003-FINAL`: Integrate documentation and audit behavior, run gates and
  record validation evidence after `WS-003-A` and `WS-003-B` complete.

### Blockers

None open. If `WS-003-A` changes required section names, `WS-003-B` must align
test expectations before final validation.

### Shared Files And Merge Order

`scripts/strict_doc_audit.py` is owned only by `WS-003-B`.
`13_context_packages/README.md` and `18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
are owned only by `WS-003-A`. Merge order:

1. `WS-003-A` documentation/template contract.
2. `WS-003-B` audit implementation and tests aligned to that contract.
3. `WS-003-FINAL` repository validation and handoff.

## Files to Inspect

- `13_context_packages/README.md`
- `18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
- `06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`

## Files to Create

- Fixture tests for context package section validation.

## Files to Modify

- `scripts/strict_doc_audit.py`
- `13_context_packages/README.md` if naming conventions need clarification.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

Parallel wave 1:

1. `WS-003-A`: Confirm the required context-package sections in guidance and templates.
2. `WS-003-B`: Classify `CP-*.md` files as context packages in the strict audit.
3. `WS-003-B`: Require target task, traceability, included documents, constraints, prompt and validation sections.
4. `WS-003-B`: Validate references inside included document lists.
5. `WS-003-B`: Add tests for missing or empty sections.

Final integration:

6. `WS-003-FINAL`: Align implementation and documentation, run tests and strict audit, then record evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-003-A | Define the context-package section contract in documentation and templates. | yes | documentation-contract agent | `13_context_packages/README.md`; `18_templates/CONTEXT_PACKAGE_TEMPLATE.md`; TASK-003 validation artifact if needed | Clear required-section contract for context packages | none |
| WS-003-B | Implement context-package audit classification, section checks and fixture tests. | yes, after reading current template names | audit implementation agent | `scripts/strict_doc_audit.py`; focused TASK-003 tests under `tests/` | Deterministic audit findings for missing/empty context-package sections and broken included-doc references | align with WS-003-A before final validation |
| WS-003-FINAL | Integrate documentation and audit behavior, run validation and record evidence. | no; dependency-gated | validation owner/integration agent | validation commands; TASK-003 validation report or terminal evidence | strict audit evidence, gate result and residual-risk summary | WS-003-A and WS-003-B complete |

Ready-now workstreams `WS-003-A` and `WS-003-B` should be opened as separate
Codex threads if implementation resumes from this plan. The original thread
keeps `WS-003-FINAL` integration ownership.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-003-A | none | documentation-contract agent | not applicable | resolved |
| WS-003-B | section names must match the documentation contract | audit implementation agent | read the current template and align with `WS-003-A` output before final validation | open until integration |
| WS-003-FINAL | WS-003-A and WS-003-B | validation owner | run tests and strict audit after both workstreams land | dependency-gated |

## Parallel Dispatch List

### Goal WS-003-A: Context Package Contract Documentation

- Owner role: documentation-contract agent
- Objective: Make the required context-package sections explicit in guidance and templates without changing task or feature scope.
- Allowed files: `13_context_packages/README.md`; `18_templates/CONTEXT_PACKAGE_TEMPLATE.md`; TASK-003 validation artifact only if recording evidence.
- Forbidden files: `00_constitution/CONSTITUTION.md`; `01_vision/VISION.md`; `scripts/strict_doc_audit.py`; unrelated task, prompt and graph files.
- Required inputs: `../11_tasks/TASK-003-create-context-package-schema.md`; `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`; current context-package examples.
- Blockers: none.
- Validation evidence: documentation diff summary and template section checklist.
- Handoff output: final section names, required/optional classification and any compatibility notes.

### Goal WS-003-B: Context Package Audit Implementation

- Owner role: audit implementation agent
- Objective: Implement deterministic strict-audit checks for context package classification, required sections and included-document references.
- Allowed files: `scripts/strict_doc_audit.py`; focused TASK-003 tests under `tests/`.
- Forbidden files: `00_constitution/CONSTITUTION.md`; `01_vision/VISION.md`; context-package guidance/template files owned by `WS-003-A`; unrelated generated artifacts.
- Required inputs: `../13_context_packages/README.md`; `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`; `WS-003-A` handoff if available.
- Blockers: final validation waits for `WS-003-A` contract names.
- Validation evidence: focused tests and `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues`.
- Handoff output: code/test diff summary, validation commands run, findings format examples and deviations.

### Goal WS-003-FINAL: Integration And Validation

- Owner role: validation owner/integration agent
- Objective: Merge the documentation contract and audit implementation, resolve naming conflicts, and prove the repository passes the required gates.
- Allowed files: validation report or executor evidence for TASK-003; implementation files only if integration exposes a TASK-003 defect.
- Forbidden files: `00_constitution/CONSTITUTION.md`; `01_vision/VISION.md`; unrelated implementation files.
- Required inputs: completed `WS-003-A` and `WS-003-B` handoffs.
- Blockers: both ready-now workstreams complete.
- Validation evidence: focused tests, strict doc audit and pre-coding gate if operational changes are present.
- Handoff output: final validation summary and residual risks.

## Parallel Agent Handoff Prompts

### Workstream WS-003-A

Clarify the TASK-003 context-package contract. Read
`11_tasks/TASK-003-create-context-package-schema.md`,
`06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`,
`13_context_packages/README.md` and
`18_templates/CONTEXT_PACKAGE_TEMPLATE.md`. Modify only
`13_context_packages/README.md`, `18_templates/CONTEXT_PACKAGE_TEMPLATE.md` and
a TASK-003 validation artifact if evidence must be recorded. Do not edit audit
code or protected Vision/Constitution files. Return the final required section
names, optional sections and compatibility notes for the audit implementation
agent.

### Workstream WS-003-B

Implement TASK-003 strict-audit checks for context packages. Read
`13_context_packages/README.md`, `18_templates/CONTEXT_PACKAGE_TEMPLATE.md` and
the `WS-003-A` handoff if available. Modify only `scripts/strict_doc_audit.py`
and focused TASK-003 tests under `tests/`. Do not edit context-package
documentation/template files owned by `WS-003-A` or protected baseline files.
Add deterministic classification for `CP-*.md`, missing/empty section findings
and broken included-document reference checks. Validate with focused tests and
`python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues`.

### Workstream WS-003-FINAL

Integrate TASK-003 after `WS-003-A` and `WS-003-B` complete. Resolve only
contract-name mismatches between documentation and audit tests, run the focused
tests and strict documentation audit, confirm protected Vision and Constitution
files are unchanged, and record the final evidence.

## Test Plan

- Test a complete context package.
- Test missing target task.
- Test missing validation instructions.
- Test broken included-document references.

## Validation Plan

Run fixture tests and strict audit.

## Gate Commands

Source policy: `../23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`

```bash
python3 scripts/pre_coding_gate.py --root .
python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues
```

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Pre-coding | yes | `python3 scripts/pre_coding_gate.py --root .` | terminal output or TASK-003 validation report | yes |
| Contract/schema | yes | `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues` | terminal output or TASK-003 validation report | yes |
| Replay/determinism | yes | focused TASK-003 fixture tests run twice with unchanged inputs | terminal output or TASK-003 validation report | yes |
| Integration-readiness | yes | strict doc audit against repository | terminal output or TASK-003 validation report | yes |
| Deployment-readiness | no | not required for local schema/audit behavior unless deployment gate changes | not applicable | no |

## Documentation Updates

Update context package guidance if the required sections change.

## Rollback Plan

Revert audit code, tests and context-package documentation updates for this task.

## Agent Handoff Prompt

Use the workstream-specific prompts under `Parallel Agent Handoff Prompts`.
Final integration remains with `WS-003-FINAL`.

## Completion Checklist

- [x] Context package classification implemented.
- [x] Required sections enforced.
- [x] Reference checks covered by tests.
- [x] Parallelizable workstreams identified.
- [x] Blockers and serial dependencies documented.
- [x] Agent handoff prompts created for independent workstreams.
- [x] Integration order documented.
- [x] Validation report created.
