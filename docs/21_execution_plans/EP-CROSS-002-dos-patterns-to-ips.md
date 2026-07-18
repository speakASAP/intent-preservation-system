# EP-CROSS-002: Transfer DOS Operational Patterns Into IPS

```yaml
id: EP-CROSS-002
status: validated
source_task: cross-repository-alignment
owner: AI agent
created: 2026-06-08
last_updated: 2026-06-13
completeness_level: validated
target_repository: /Users/Sergej.Stasok/Documents/Gitlab/intent-preservation-system
upstream:
  - EP-CROSS-001-dos-ips-compliance.md
  - ../00_constitution/CONSTITUTION.md
  - ../01_vision/VISION.md
  - ../17_governance/AI_AGENT_RULES.md
  - ../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md
external_sources:
  - /Users/Sergej.Stasok/Documents/Gitlab/dos/AGENTS.md
  - /Users/Sergej.Stasok/Documents/Gitlab/dos/docs/contracts/contract-validation-policy.md
  - /Users/Sergej.Stasok/Documents/Gitlab/dos/docs/ai-development/README.md
  - /Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase9_pre_coding_gate.py
  - /Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase10_integration_readiness_gate.py
downstream:
  - EP-CROSS-003-cross-reference-shared-principles.md
```

## Purpose

Transfer the strongest DOS operational patterns into the Intent Preservation System so IPS becomes more practical for real software delivery. DOS is strong in local gates, invariant checks, synthetic-data discipline, contract validation, replay/determinism and phase readiness. IPS should generalize those patterns without becoming TDOS-specific.

## Upstream Traceability

- IPS Vision outcome: validate every task against original goals and audit existing projects for weak planning.
- IPS Constitution principle: validation at every level.
- IPS Constitution principle: documentation before implementation.
- IPS Constitution principle: auditability.
- DOS source pattern: phase9 and phase10 gates.
- DOS source pattern: no production data in prompts, tests, examples, logs or reports.
- DOS source pattern: contract-first validation before runtime work.
- DOS source pattern: replay and deterministic validation.

## Goal Impact

This task strengthens IPS by adding operational mechanisms that make intent preservation enforceable in active development:

- pre-coding gates;
- deployment-readiness gates;
- project invariant declarations;
- sensitive-data policy;
- contract validation policy template;
- replay/determinism fields in plans and validation reports;
- AI-cycle review artifact templates.

## Scope

Modify IPS templates, governance docs and scripts so IPS can express and audit DOS-style delivery controls generically for any project.

## Parallel Execution Strategy

This plan can run as four parallel goals once the DOS source patterns are inspected: governance/policy docs, templates, gate scripts, and audit/readme integration. The final validation goal must run after those outputs are merged.

Integration owner: one IPS integration agent reconciles shared files such as `README.md`, `17_governance/AI_AGENT_RULES.md`, `18_templates/EXECUTION_PLAN_TEMPLATE.md`, and `scripts/strict_doc_audit.py`.

## Goal Blockers And Dependencies

| Goal | Can start now? | Blockers | Dependencies | Integration point |
| --- | --- | --- | --- | --- |
| G1: Governance and policy docs | Yes | None | DOS source docs are read-only inputs | Governance docs |
| G2: Template updates | Yes | None | Existing IPS templates | `18_templates/` |
| G3: Gate scripts | Yes | None | Existing IPS audit model | `scripts/pre_coding_gate.py`, `scripts/deployment_readiness_gate.py` |
| G4: Audit and README integration | Blocked | Wait for G1-G3 names/paths to stabilize | G1-G3 | `README.md`, `strict_doc_audit.py`, guide docs |
| G5: Final validation | Blocked | Wait for G1-G4 | G1-G4 | Gate and audit evidence |

## Parallel Dispatch List

### Goal G1: Governance And Policy Docs

- Owner role: governance documentation agent
- Objective: generalize DOS operational patterns into IPS project invariants, sensitive-data policy, and operational gate standard.
- Allowed files: `17_governance/PROJECT_INVARIANTS.md`, `23_documentation_contracts/SENSITIVE_DATA_POLICY.md`, `23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`, `17_governance/AI_AGENT_RULES.md`
- Forbidden files: `00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`
- Required inputs: DOS AGENTS, contract policy, and phase gate docs listed in this plan
- Blockers: none
- Validation evidence: documentation completeness/audit findings for changed docs
- Handoff output: policy file paths and required fields for G2/G3

### Goal G2: IPS Template Updates

- Owner role: template agent
- Objective: update task, execution-plan, validation-report, readiness, contract, project-invariant, and AI-cycle templates.
- Allowed files: `18_templates/`, `21_execution_plans/EXECUTION_PLAN_GUIDE.md`, `14_prompts/PROMPT_GUIDELINES.md`
- Forbidden files: immutable constitution and vision
- Required inputs: existing IPS templates and G1 policy names if available
- Blockers: none
- Validation evidence: strict document audit or manual section check
- Handoff output: list of required metadata/sections for G3/G4

### Goal G3: Generic Gate Scripts

- Owner role: tooling agent
- Objective: implement generic pre-coding and deployment-readiness gates with local deterministic checks and sensitive-data policy scanning.
- Allowed files: `scripts/pre_coding_gate.py`, `scripts/deployment_readiness_gate.py`, targeted tests if added
- Forbidden files: governance docs except read-only inspection
- Required inputs: required sections from this plan and existing `scripts/strict_doc_audit.py`
- Blockers: none
- Validation evidence: gate command outputs
- Handoff output: CLI behavior and report fields for G4/G5

### Goal G4: Audit And README Integration

- Owner role: integration documentation agent
- Objective: wire new operational layer into README, strict audit checks if needed, and guide references after file names stabilize.
- Allowed files: `README.md`, `scripts/strict_doc_audit.py`, `15_audits/AUDIT_CHECKLIST.md`, `14_prompts/PROMPT_GUIDELINES.md`, `21_execution_plans/EXECUTION_PLAN_GUIDE.md`
- Forbidden files: immutable constitution and vision
- Required inputs: G1-G3 output paths and CLI names
- Blockers: blocked until G1-G3 interfaces are stable
- Validation evidence: strict audit and gate outputs
- Handoff output: integrated docs/tooling summary

### Goal G5: Final IPS Validation

- Owner role: validation agent
- Objective: run strict audit, pre-coding gate, deployment-readiness gate, and report unresolved gaps.
- Allowed files: validation reports if needed
- Forbidden files: implementation files except for narrow validation-report updates
- Required inputs: G1-G4 merged output
- Blockers: blocked until G1-G4 finish
- Validation evidence: commands in Test Plan
- Handoff output: final validation evidence and deviations

## Non-Goals

- Do not import TDOS product-specific concepts as universal IPS rules.
- Do not make replay mandatory for every project; make replay/determinism a declared project property.
- Do not weaken the immutable vision and constitution model.
- Do not add external network dependencies.
- Do not modify DOS in this task.

## Files to Inspect

In IPS:

```text
README.md
00_constitution/CONSTITUTION.md
17_governance/AI_AGENT_RULES.md
18_templates/TASK_TEMPLATE.md
18_templates/EXECUTION_PLAN_TEMPLATE.md
18_templates/VALIDATION_REPORT_TEMPLATE.md
21_execution_plans/EXECUTION_PLAN_GUIDE.md
23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md
scripts/strict_doc_audit.py
```

In DOS:

```text
/Users/Sergej.Stasok/Documents/Gitlab/dos/AGENTS.md
/Users/Sergej.Stasok/Documents/Gitlab/dos/docs/ai-development/README.md
/Users/Sergej.Stasok/Documents/Gitlab/dos/docs/contracts/contract-validation-policy.md
/Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase9_pre_coding_gate.py
/Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase10_integration_readiness_gate.py
```

## Files to Create In IPS

Recommended:

```text
17_governance/PROJECT_INVARIANTS.md
18_templates/PROJECT_INVARIANTS_TEMPLATE.md
18_templates/READINESS_GATE_TEMPLATE.md
18_templates/CONTRACT_VALIDATION_POLICY_TEMPLATE.md
18_templates/AI_CYCLE_PLAN_REVIEW_TEMPLATE.md
18_templates/AI_CYCLE_DATA_PROTECTION_REVIEW_TEMPLATE.md
18_templates/AI_CYCLE_CONTRACT_REVIEW_TEMPLATE.md
18_templates/AI_CYCLE_EXECUTOR_REPORT_TEMPLATE.md
18_templates/AI_CYCLE_SUMMARY_TEMPLATE.md
23_documentation_contracts/SENSITIVE_DATA_POLICY.md
23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md
scripts/pre_coding_gate.py
scripts/deployment_readiness_gate.py
```

Optional:

```text
12_validation/READINESS_GATE_REPORT_TEMPLATE.md
12_validation/REPLAY_DETERMINISM_REPORT_TEMPLATE.md
```

## Files to Modify In IPS

```text
README.md
17_governance/AI_AGENT_RULES.md
18_templates/TASK_TEMPLATE.md
18_templates/EXECUTION_PLAN_TEMPLATE.md
18_templates/VALIDATION_REPORT_TEMPLATE.md
21_execution_plans/EXECUTION_PLAN_GUIDE.md
23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md
scripts/strict_doc_audit.py
```

Modify only if useful:

```text
15_audits/AUDIT_CHECKLIST.md
14_prompts/PROMPT_GUIDELINES.md
```

## Files That Must Not Be Modified

```text
00_constitution/CONSTITUTION.md
01_vision/VISION.md
```

This task transfers operational patterns. It must not change IPS original intent.

## Implementation Steps

1. Read DOS gate scripts and summarize the reusable gate model:
   - required files;
   - forbidden patterns;
   - invariant checks;
   - command execution;
   - report output.
2. Create `17_governance/PROJECT_INVARIANTS.md` explaining how a project declares non-negotiable product invariants.
3. Create `18_templates/PROJECT_INVARIANTS_TEMPLATE.md`.
4. Create `23_documentation_contracts/SENSITIVE_DATA_POLICY.md` based on DOS synthetic-data discipline, generalized to any project.
5. Update `17_governance/AI_AGENT_RULES.md` so agents must not place secrets, raw production data, confidential identifiers or real customer data into prompts, tests, examples, logs or reports.
6. Create `23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md` to define pre-coding, integration-readiness and deployment-readiness gates.
7. Create `18_templates/READINESS_GATE_TEMPLATE.md`.
8. Create `18_templates/CONTRACT_VALIDATION_POLICY_TEMPLATE.md` to generalize DOS schema/example validation.
9. Update `18_templates/TASK_TEMPLATE.md` to include:
   - project invariant impact;
   - sensitive-data classification;
   - contract/schema impact;
   - replay/determinism impact;
   - required gates.
10. Update `18_templates/EXECUTION_PLAN_TEMPLATE.md` to include:
    - invariant checks;
    - sensitive-data handling;
    - contract validation plan;
    - replay/determinism plan;
    - gate commands.
11. Update `18_templates/VALIDATION_REPORT_TEMPLATE.md` to include:
    - gate evidence;
    - invariant evidence;
    - sensitive-data scan evidence;
    - replay/determinism evidence when applicable.
12. Create AI-cycle artifact templates from the DOS model:
    - plan review;
    - data-protection review;
    - contract review;
    - executor report;
    - cycle summary.
13. Update `21_execution_plans/EXECUTION_PLAN_GUIDE.md` to explain when to use those AI-cycle artifacts.
14. Implement `scripts/pre_coding_gate.py` as a generic IPS gate that checks:
    - required immutable documents exist;
    - task and execution plan exist;
    - task has upstream traceability;
    - execution plan has validation plan;
    - project invariants file exists or is explicitly marked not applicable;
    - no sensitive-data policy violations in text files.
15. Implement `scripts/deployment_readiness_gate.py` as a generic IPS gate that checks:
    - pre-coding gate passes;
    - strict doc audit passes or is invoked;
    - validation report exists for deployment target;
    - unresolved `[MISSING: ...]` markers are reported;
    - protected vision/constitution are not modified.
16. Extend `scripts/strict_doc_audit.py` only if needed and only with narrowly scoped checks.
17. Update README with the new operational gate layer.

## Test Plan

Run from IPS:

```bash
python3 scripts/strict_doc_audit.py --format markdown
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root .
```

If new gate scripts support report output, verify generated reports manually.

## Validation Plan

The task is valid when:

- IPS has a generic project-invariants mechanism.
- IPS has a sensitive-data policy.
- IPS has readiness gate templates.
- IPS templates include contract, replay, invariant and data-protection fields.
- IPS has runnable pre-coding and deployment-readiness gates.
- Existing IPS immutable files are not modified.
- The new material is generic and not TDOS-specific.

## Rollback Plan

If the changes make IPS audit too strict or noisy:

1. Keep templates and governance documents.
2. Temporarily mark new gate checks as advisory.
3. Report which checks need tuning.
4. Do not remove immutable governance files or existing audit behavior.

## Agent Handoff Prompt

```text
You are Agent 2. Transfer the best operational patterns from DOS into the Intent Preservation System repository at /Users/Sergej.Stasok/Documents/Gitlab/intent-preservation-system.

Read these DOS files first: /Users/Sergej.Stasok/Documents/Gitlab/dos/AGENTS.md, /Users/Sergej.Stasok/Documents/Gitlab/dos/docs/ai-development/README.md, /Users/Sergej.Stasok/Documents/Gitlab/dos/docs/contracts/contract-validation-policy.md, /Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase9_pre_coding_gate.py, and /Users/Sergej.Stasok/Documents/Gitlab/dos/scripts/phase10_integration_readiness_gate.py.

Your objective is to generalize DOS strengths into IPS: operational gates, project invariant checks, synthetic and sensitive-data discipline, contract-first validation, replay/determinism impact, and AI-cycle review artifacts.

Do not modify 00_constitution/CONSTITUTION.md or 01_vision/VISION.md. Do not import TDOS-specific product rules as universal IPS rules. Make the patterns generic and template-driven.

Create or update IPS governance docs, templates and scripts so future projects can declare invariants, run pre-coding gates, run deployment-readiness gates, validate contract/schema work, declare replay impact, and keep sensitive production data out of prompts, tests, examples, logs and reports.

Run: python3 scripts/strict_doc_audit.py --format markdown, python3 scripts/pre_coding_gate.py --root ., and python3 scripts/deployment_readiness_gate.py --root . if the scripts are implemented. Report files changed, tests run, validation evidence, deviations, and remaining gaps.
```

## Completion Checklist

- [x] DOS reusable patterns inspected.
- [x] IPS project invariants mechanism added.
- [x] Sensitive-data policy added.
- [x] Operational gate standard added.
- [x] Readiness gate template added.
- [x] Contract validation policy template added.
- [x] Task template updated.
- [x] Execution plan template updated.
- [x] Validation report template updated.
- [x] AI-cycle artifact templates added.
- [x] Pre-coding gate implemented.
- [x] Deployment-readiness gate implemented.
- [x] README updated.
- [x] Validation commands pass or failures are documented.
