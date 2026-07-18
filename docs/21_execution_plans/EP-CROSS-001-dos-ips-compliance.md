# EP-CROSS-001: Implement IPS Compliance Inside DOS

```yaml
id: EP-CROSS-001
status: validated
source_task: cross-repository-alignment
owner: AI agent
created: 2026-06-08
last_updated: 2026-06-13
completeness_level: validated
target_repository: /Users/Sergej.Stasok/Documents/Gitlab/dos
upstream:
  - ../00_constitution/CONSTITUTION.md
  - ../01_vision/VISION.md
  - ../17_governance/AI_AGENT_RULES.md
  - ../17_governance/CHANGE_CONTROL.md
  - ../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md
downstream:
  - EP-CROSS-002-dos-patterns-to-ips.md
  - EP-CROSS-003-cross-reference-shared-principles.md
```

## Purpose

Implement the Intent Preservation System governance model inside the DOS repository so the original TDOS vision becomes protected, traceable, auditable and enforceable before development or deployment work proceeds.

DOS already has strong product invariants, contract validation, synthetic-data rules and phase gates. The missing layer is IPS-style immutable intent governance: protected vision and constitution, formal amendment control, required traceability from vision to implementation, and automated gates that detect drift before coding and deployment.

## Upstream Traceability

- IPS Constitution: `00_constitution/CONSTITUTION.md`
- IPS Vision: `01_vision/VISION.md`
- IPS AI rules: `17_governance/AI_AGENT_RULES.md`
- IPS change control: `17_governance/CHANGE_CONTROL.md`
- IPS documentation completeness standard: `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- DOS canonical idea: `/Users/Sergej.Stasok/Documents/Gitlab/dos/docs/idea/README.md`
- DOS business idea: `/Users/Sergej.Stasok/Documents/Gitlab/dos/docs/idea/BUSINESS_IDEA.md`
- DOS agent rules: `/Users/Sergej.Stasok/Documents/Gitlab/dos/AGENTS.md`
- DOS phase gates: `/Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase9_pre_coding_gate.py`, `/Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase10_integration_readiness_gate.py`

## Goal Impact

This work preserves the original TDOS intent by making the big picture explicit and immutable:

- TDOS remains governed decision infrastructure, not generic workflow automation.
- Decision artefacts remain canonical truth.
- Excel remains a projection only.
- Raw production data remains machine-only.
- Humans use controlled views and supervisory tooling.
- Replay, lineage, idempotency, trust separation, policy separation and auditability remain day-one properties.
- Telecom-grade interoperability remains part of the long-term vision.

## Scope

Create or update DOS documentation and gates so all future DOS development must pass an intent-preservation check before coding, integration readiness or deployment readiness.

The implementation agent should work in the DOS repository:

```text
/Users/Sergej.Stasok/Documents/Gitlab/dos
```

## Parallel Execution Strategy

This plan can be split into parallel goal workstreams after the initial source-reading step. Documentation baseline, validator implementation, gate integration, and test/report work can run in separate sessions if each agent owns distinct files and the validator interface is agreed first.

Integration owner: one final agent merges the documentation, script, test, and gate outputs, then runs the full DOS validation set.

## Goal Blockers And Dependencies

| Goal | Can start now? | Blockers | Dependencies | Integration point |
| --- | --- | --- | --- | --- |
| G1: DOS intent baseline docs | Yes | None after source docs are read | IPS constitution, IPS vision, DOS idea docs | Protected docs and governance docs |
| G2: Intent validator | Yes | Validator contract must stay local and deterministic | Required document list from G1 may add checks, but initial skeleton can start now | `scripts/validate_intent_preservation.py` |
| G3: Validator tests | Yes | Test expectations depend on G2 function names; use CLI-level tests to reduce coupling | G2 CLI behavior | `tests/test_validate_intent_preservation.py` |
| G4: Gate integration | Blocked | Wait until G2 exposes stable CLI exit behavior | G2 | Phase9 and phase10 gate scripts |
| G5: Final validation and report | Blocked | Wait until G1-G4 finish | G1-G4 | `reports/validation/` evidence or final report |

## Parallel Dispatch List

### Goal G1: DOS Intent Baseline Docs

- Owner role: documentation/governance agent
- Objective: create DOS constitution, vision, amendment path, goal-impact map, traceability standard, and AI-agent rules without changing TDOS meaning.
- Allowed files: `00_constitution/`, `01_vision/`, `17_governance/`, `22_goal_impact/`, `23_documentation_contracts/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/ai-development/README.md`
- Forbidden files: `docs/idea/README.md`, `docs/idea/BUSINESS_IDEA.md` except read-only inspection
- Required inputs: IPS governance docs and DOS idea docs listed in Files to Inspect
- Blockers: none
- Validation evidence: document completeness review and any available local markdown/audit checks
- Handoff output: list of created governance documents and protected intent rules for G2/G4

### Goal G2: DOS Intent Validator

- Owner role: validation-script agent
- Objective: implement deterministic local intent-preservation validation for required docs, protected markers, amendment path, traceability fields, prompt bypasses, and DOS invariants.
- Allowed files: `scripts/validate_intent_preservation.py`
- Forbidden files: protected intent docs after G1 creates them
- Required inputs: required file list from this plan; G1 outputs if available
- Blockers: none
- Validation evidence: direct validator command output
- Handoff output: stable CLI contract for G3 and G4

### Goal G3: Validator Tests

- Owner role: test agent
- Objective: add focused tests for the validator using temporary fixtures and CLI-level expectations.
- Allowed files: `tests/test_validate_intent_preservation.py`
- Forbidden files: production docs and gate scripts
- Required inputs: G2 CLI behavior; can start with expected command-level contract
- Blockers: none if tests use CLI behavior, otherwise wait for G2 function names
- Validation evidence: `python -m pytest -q tests/test_validate_intent_preservation.py`
- Handoff output: test coverage summary and failing assumptions, if any

### Goal G4: Gate Integration

- Owner role: gate-integration agent
- Objective: call the intent validator first from phase9 and phase10 gates without weakening existing DOS checks.
- Allowed files: `scripts/phase9_pre_coding_gate.py`, `scripts/phase10_integration_readiness_gate.py`
- Forbidden files: validator internals except through the CLI contract
- Required inputs: G2 stable CLI exit codes
- Blockers: blocked until G2 CLI is available
- Validation evidence: phase9 and phase10 command output or documented slow-command skip
- Handoff output: gate integration notes for final validation

### Goal G5: Final Integration And Validation

- Owner role: integration agent
- Objective: merge outputs, resolve conflicts, run validator, phase gates, and targeted tests, then report remaining gaps.
- Allowed files: validation reports under `reports/validation/` if needed
- Forbidden files: unrelated source files
- Required inputs: G1-G4 handoff outputs
- Blockers: blocked until G1-G4 finish
- Validation evidence: full command list from Test Plan
- Handoff output: final validation report and deviations list

## Non-Goals

- Do not rewrite TDOS product strategy.
- Do not weaken existing DOS invariants.
- Do not introduce live Microsoft Graph, SharePoint, OCR, OPA, Excel, queue, database or cloud object-store calls.
- Do not add real supplier, customer, tenant, mailbox, token, attachment or production identifiers.
- Do not change production runtime behavior unless the gate integration requires a small local validation change.
- Do not directly modify protected intent files after creating them unless the same change includes an approved amendment model.

## Files to Inspect

In IPS:

```text
00_constitution/CONSTITUTION.md
01_vision/VISION.md
17_governance/AI_AGENT_RULES.md
17_governance/CHANGE_CONTROL.md
18_templates/EXECUTION_PLAN_TEMPLATE.md
18_templates/TASK_TEMPLATE.md
18_templates/GOAL_IMPACT_TEMPLATE.md
23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md
```

In DOS:

```text
README.md
AGENTS.md
CLAUDE.md
copilot-instructions.md
docs/idea/README.md
docs/idea/BUSINESS_IDEA.md
docs/ai-development/README.md
docs/contracts/README.md
docs/contracts/contract-validation-policy.md
docs/implementation/phase9-ai-coding-prompts.md
docs/implementation/phase9-coding-readiness-checklist.md
scripts/phase9_pre_coding_gate.py
scripts/phase10_integration_readiness_gate.py
```

## Files to Create In DOS

Recommended:

```text
00_constitution/CONSTITUTION.md
01_vision/VISION.md
01_vision/VISION_EVOLUTION.md
17_governance/CHANGE_CONTROL.md
17_governance/AI_AGENT_RULES.md
17_governance/amendments/README.md
17_governance/amendments/AMENDMENT_TEMPLATE.md
22_goal_impact/README.md
22_goal_impact/TDOS_GOAL_IMPACT_MAP.md
23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md
23_documentation_contracts/INTENT_TRACEABILITY_STANDARD.md
scripts/validate_intent_preservation.py
tests/test_validate_intent_preservation.py
```

Optional, if the agent has enough time:

```text
04_systems/README.md
05_subsystems/README.md
10_features/README.md
11_tasks/README.md
12_validation/README.md
21_execution_plans/README.md
```

## Files to Modify In DOS

```text
README.md
AGENTS.md
CLAUDE.md
docs/ai-development/README.md
scripts/phase9_pre_coding_gate.py
scripts/phase10_integration_readiness_gate.py
```

Modify only if needed:

```text
.gitlab-ci.yml
.github/workflows/*.yml
.gitlab/CODEOWNERS
```

## Files That Must Not Be Modified

Until amendment control exists:

```text
docs/idea/README.md
docs/idea/BUSINESS_IDEA.md
```

After creating the protected DOS files, do not make further semantic edits to:

```text
00_constitution/CONSTITUTION.md
01_vision/VISION.md
```

unless the change is explicitly part of initial creation in this task or is routed through the amendment model.

## Implementation Steps

1. Read the IPS constitution, vision, AI-agent rules, change-control file and documentation completeness standard.
2. Read the DOS idea, agent rules, AI-development workflow and existing gate scripts.
3. Draft `00_constitution/CONSTITUTION.md` in DOS using IPS principles adapted to TDOS.
4. Draft `01_vision/VISION.md` in DOS from the existing TDOS idea docs without changing product meaning.
5. Draft `01_vision/VISION_EVOLUTION.md` to record future evolution proposals only.
6. Draft DOS change-control and AI-agent rules.
7. Add amendment folder and amendment template.
8. Add goal impact map with stable TDOS vision goals.
9. Add intent traceability standard requiring this chain:

```text
Vision Goal -> Goal Impact -> System -> Subsystem -> Feature -> Task -> Execution Plan -> Coding Prompt -> Code -> Validation Report
```

10. Update DOS AI development plan template so every plan includes upstream vision goal, goal impact, affected files, forbidden files, data-protection classification, replay/idempotency impact, validation report path and rollback plan.
11. Implement `scripts/validate_intent_preservation.py`.
12. The validator must check at minimum:
    - required immutable documents exist;
    - protected documents contain AI write restrictions;
    - amendment template exists;
    - goal impact map exists;
    - AI workflow template requires upstream traceability;
    - phase9 prompts do not bypass traceability;
    - protected intent files are not directly changed without an amendment marker when git history is available;
    - DOS non-negotiables are still present in agent rules.
13. Add tests for the validator.
14. Integrate the new validator as the first step in `phase9_pre_coding_gate.py`.
15. Integrate the new validator as the first command in `phase10_integration_readiness_gate.py`.
16. Update README to describe the new protected intent layer and the required validation command.

## Test Plan

Run from DOS:

```bash
python scripts/validate_intent_preservation.py --root .
python scripts/phase9_pre_coding_gate.py --root .
python scripts/phase10_integration_readiness_gate.py --root .
python -m pytest -q tests/test_validate_intent_preservation.py
```

If the full phase10 gate is too slow for the task session, run the targeted validator tests plus phase9 gate and report the skipped command clearly.

## Validation Plan

The task is valid only when:

- DOS has a protected constitution and vision.
- DOS has a formal amendment path.
- DOS AI-agent rules include IPS non-negotiables.
- DOS plans/prompts require traceability to original vision goals.
- Existing DOS product invariants remain intact.
- Pre-coding and integration gates run intent validation before other checks.
- Validation evidence is written under `reports/validation/` or reported in the final response.

## Rollback Plan

If the implementation causes gate failures:

1. Revert only the files changed in this task.
2. Leave unrelated DOS changes untouched.
3. If the failure is in the validator, disable only the gate integration temporarily and keep the new docs for review.
4. Report the exact failed check and remediation.

## Agent Handoff Prompt

```text
You are Agent 1. Implement IPS compliance inside the DOS repository at /Users/Sergej.Stasok/Documents/Gitlab/dos.

Use the Intent Preservation System repository at /Users/Sergej.Stasok/Documents/Gitlab/intent-preservation-system as the governance source. Read these IPS files first: 00_constitution/CONSTITUTION.md, 01_vision/VISION.md, 17_governance/AI_AGENT_RULES.md, 17_governance/CHANGE_CONTROL.md, and 23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md.

Your objective is to add an immutable TDOS constitution and vision, formal amendment control, full traceability requirements from vision to task to validation, and a local gate that enforces those rules before DOS coding or deployment readiness gates run.

Do not rewrite the TDOS product idea. Preserve the existing DOS invariants: decision artefact is source of truth, Excel is projection only, raw production data is machine-only, evidence is immutable, replay is deterministic, trust and policy stay separate, and synthetic or masked examples are required.

Create the protected DOS documents, amendment template, goal impact map, traceability standard, AI-agent rule updates, and scripts/validate_intent_preservation.py. Integrate the validator as the first step in phase9_pre_coding_gate.py and phase10_integration_readiness_gate.py. Add tests for the validator.

Run: python scripts/validate_intent_preservation.py --root ., python scripts/phase9_pre_coding_gate.py --root ., python scripts/phase10_integration_readiness_gate.py --root ., and targeted pytest for the validator. Report files changed, tests run, validation evidence, deviations, and any remaining gaps.
```

## Completion Checklist

- [x] DOS immutable constitution created.
- [x] DOS immutable vision created.
- [x] DOS amendment process created.
- [x] DOS goal impact mapping created.
- [x] DOS traceability standard created.
- [x] DOS AI-agent rules updated.
- [x] DOS AI-development template updated.
- [x] Intent preservation validator implemented.
- [x] Validator tests added.
- [x] Phase9 gate calls intent validator first.
- [x] Phase10 gate calls intent validator first.
- [x] Validation commands pass or failures are documented.
