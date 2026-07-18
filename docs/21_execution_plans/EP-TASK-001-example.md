# EP-TASK-001: Create Required Document Audit Rules

## Metadata

```yaml
id: EP-TASK-001
status: reviewed
source_task: ../11_tasks/TASK-001-create-required-document-audit-rules.md
owner: TBD
created: 2026-06-05
```

## Upstream traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-001-documentation-audit.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-001-example.md
```

## Goal impact

This execution plan supports the product goal of detecting incomplete project documentation before coding tasks are assigned to AI agents.

## Scope

Implement rules that detect whether required documentation sections exist and whether they contain meaningful content.

## Non-goals

- Do not implement a web UI.
- Do not add RAG.
- Do not add risk scoring.
- Do not modify immutable vision documents.

## Files to inspect

- `scripts/strict_doc_audit.py`
- `18_templates/*.md`
- `23_documentation_contracts/*.md`

## Files to create

- None.

## Files to modify

- `scripts/strict_doc_audit.py`
- `15_audits/AUDIT_CHECKLIST.md`

## Files that must not be modified

- `01_vision/VISION.md`
- `00_constitution/CONSTITUTION.md`

## Implementation steps

1. Define required sections for system, subsystem, feature, task, execution plan, ADR, context package, and validation report documents.
2. Add a parser that reads Markdown headings.
3. Detect missing required headings.
4. Detect empty required sections.
5. Produce machine-readable JSON output.
6. Produce human-readable Markdown output.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-001-A | Implement required-section audit rules and output formats | yes, as the only ready implementation workstream | audit implementation agent in one dedicated session | `scripts/strict_doc_audit.py`; focused tests under `tests/` if required | Strict heading/content audit behavior with JSON and Markdown output | none |
| WS-001-D | Update checklist and completeness documentation | yes, after WS-001-A defines final rule names | documentation agent | `15_audits/AUDIT_CHECKLIST.md`; `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md` | Documentation reflecting required sections and audit expectations | WS-001-A rule names and output behavior |
| WS-001-V | Validate TASK-001 and record evidence | no, dependency-gated final integration | validation agent | `12_validation/VAL-TASK-001-required-document-audit-rules.md` if present or a new TASK-001 validation report | Validation evidence and readiness recommendation | WS-001-A and WS-001-D complete |

WS-001-A should be opened as its own Codex thread when implementation is not
already complete. WS-001-D may run in a separate thread after WS-001-A publishes
the final rule and output names. WS-001-V is the final integration and
validation workstream and must run after implementation and documentation
handoffs are available.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-001-A | No open blocker recorded | audit implementation agent | Preserve immutable vision and constitution files while implementing deterministic local auditing | resolved |
| WS-001-D | Requires final audit rule names and output behavior | documentation agent | Consume WS-001-A handoff before finalizing checklist wording | dependency-gated |
| WS-001-V | Requires implementation and documentation evidence | validation agent | Run required gates and record TASK-001 validation evidence | dependency-gated |

## Parallel Dispatch List

### Goal WS-001-A: Required-Section Audit Rules

- Owner role: audit implementation agent.
- Objective: implement strict Markdown heading and non-empty-section checks for
  required IPS document types, including JSON and Markdown reports.
- Allowed files: `scripts/strict_doc_audit.py`; focused tests under `tests/` if
  required by the implementation.
- Forbidden files: `01_vision/VISION.md`, `00_constitution/CONSTITUTION.md`,
  unrelated execution plans, prompts, context packages, and artifacts containing
  secrets or raw production data.
- Required inputs: TASK-001, this execution plan,
  `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`, existing
  templates under `18_templates/`, and the current strict audit script.
- Blockers: none open.
- Validation evidence: focused tests for complete, missing-heading,
  empty-section and malformed-metadata cases; `python3 scripts/strict_doc_audit.py
  --format markdown --fail-on-issues` once fixtures and repository state are
  compatible.
- Handoff output: files changed, rule names, output examples, tests run,
  remaining blockers and deviations.

### Goal WS-001-D: Audit Documentation Alignment

- Owner role: documentation agent.
- Objective: align the audit checklist and completeness standard with the
  implemented required-section audit behavior.
- Allowed files: `15_audits/AUDIT_CHECKLIST.md`,
  `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`.
- Forbidden files: `01_vision/VISION.md`, `00_constitution/CONSTITUTION.md`,
  implementation files owned by WS-001-A unless a defect is reported as a
  deviation, and artifacts containing secrets or raw production data.
- Required inputs: WS-001-A handoff, TASK-001, this execution plan and the
  documentation completeness standard.
- Blockers: WS-001-A must publish final rule names and output behavior.
- Validation evidence: documentation diff review and strict audit gate output.
- Handoff output: documentation files changed, terminology decisions, validation
  evidence, remaining blockers and deviations.

### Goal WS-001-V: Validation Evidence And Readiness

- Owner role: validation agent.
- Objective: verify TASK-001 end to end and record validation evidence.
- Allowed files: `12_validation/VAL-TASK-001-required-document-audit-rules.md`
  if present or a new TASK-001 validation report under `12_validation/`.
- Forbidden files: `01_vision/VISION.md`, `00_constitution/CONSTITUTION.md`,
  implementation files owned by WS-001-A, documentation files owned by WS-001-D
  unless a validation defect is reported as a deviation, and artifacts
  containing secrets or raw production data.
- Required inputs: WS-001-A handoff, WS-001-D handoff, TASK-001, this execution
  plan and required gate commands.
- Blockers: WS-001-A and WS-001-D must be complete.
- Validation evidence: `python3 scripts/strict_doc_audit.py --format markdown
  --fail-on-issues`, `python3 scripts/pre_coding_gate.py --root .`, and
  `python3 scripts/deployment_readiness_gate.py --root .`.
- Handoff output: validation report update, command evidence, remaining
  blockers and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-001-A

You are the TASK-001 audit implementation agent for Intent Preservation System.
Implement strict required-document section checks in `scripts/strict_doc_audit.py`
and add focused tests under `tests/` only if required. Use TASK-001, this
execution plan, `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
and templates under `18_templates/` as source material. Do not modify
`01_vision/VISION.md`, `00_constitution/CONSTITUTION.md`, unrelated plans or
artifacts containing secrets or raw production data. Validate missing heading,
empty section, complete document and malformed metadata behavior. Return files
changed, rule names, output examples, tests run, blockers and deviations.

### Workstream WS-001-D

You are the TASK-001 documentation alignment agent for Intent Preservation
System. After WS-001-A publishes final audit rule names and output behavior,
update `15_audits/AUDIT_CHECKLIST.md` and
`23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md` so they match
the implemented strict audit behavior. Do not modify immutable vision or
constitution files, implementation files owned by WS-001-A, or artifacts
containing secrets or raw production data. Return documentation files changed,
terminology decisions, validation evidence, blockers and deviations.

### Workstream WS-001-V

You are the TASK-001 validation agent for Intent Preservation System. After
WS-001-A and WS-001-D complete, validate the required-document audit behavior and
record evidence in `12_validation/VAL-TASK-001-required-document-audit-rules.md`
if present or a new TASK-001 validation report under `12_validation/`. Run
`python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues`,
`python3 scripts/pre_coding_gate.py --root .`, and
`python3 scripts/deployment_readiness_gate.py --root .`. Return validation
evidence, readiness recommendation, blockers and deviations.

## Test plan

- Test a complete document.
- Test a document with missing headings.
- Test a document with empty headings.
- Test a document with malformed metadata.

## Validation plan

The task is valid when the audit script can identify incomplete documentation and point to specific missing sections.

## Documentation updates

Update:

- `15_audits/AUDIT_CHECKLIST.md`
- `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`

## Rollback plan

Revert only the files listed under files to create and files to modify.

## Agent handoff prompt

Use the source task, this execution plan, the documentation completeness standard, and the canonical strict audit script. Implement strict Markdown section auditing without changing project vision or constitution documents.

## Completion checklist

- [ ] Required sections are defined.
- [ ] Missing headings are detected.
- [ ] Empty sections are detected.
- [ ] JSON report is generated.
- [ ] Markdown report is generated.
- [ ] Documentation updated.
- [ ] Validation report created.
