# EP-CROSS-003: Cross-Reference Shared IPS And DOS Principles

```yaml
id: EP-CROSS-003
status: validated
source_task: cross-repository-alignment
owner: AI agent
created: 2026-06-08
last_updated: 2026-06-13
completeness_level: validated
target_repositories:
  - /Users/Sergej.Stasok/Documents/Gitlab/intent-preservation-system
  - /Users/Sergej.Stasok/Documents/Gitlab/dos
upstream:
  - EP-CROSS-001-dos-ips-compliance.md
  - EP-CROSS-002-dos-patterns-to-ips.md
  - ../00_constitution/CONSTITUTION.md
  - ../01_vision/VISION.md
```

## Purpose

Create durable cross-references between IPS and DOS so both systems benefit from each other without merging their identities.

IPS should remain the general framework for preserving original intent across AI-assisted projects. DOS should remain a concrete TDOS application and decision operating system. The shared principle layer should make the relationship explicit:

- IPS provides immutable intent governance.
- DOS provides a practical example of contract-first, gate-driven, synthetic-data-safe implementation.
- DOS uses IPS to prevent TDOS vision drift.
- IPS uses DOS patterns to improve operational enforcement.

## Upstream Traceability

- Agent 1 output: DOS IPS compliance implementation.
- Agent 2 output: DOS operational patterns transferred into IPS.
- IPS Constitution principle: intent preservation.
- IPS Constitution principle: decision memory.
- IPS Constitution principle: auditability.
- DOS product invariant: governed decision infrastructure, not generic automation.

## Goal Impact

This work reduces future drift between the two repositories and makes cross-project learning explicit. It also prevents accidental overreach:

- IPS does not become TDOS-specific.
- DOS does not become detached from IPS governance.
- Shared principles are documented once in each repository.
- Each repository can audit whether it still honors the relationship.

## Scope

Add cross-reference documents and lightweight validation checks in both repositories after Agent 1 and Agent 2 have completed their work.

This plan may require writes to both repositories:

```text
/Users/Sergej.Stasok/Documents/Gitlab/intent-preservation-system
/Users/Sergej.Stasok/Documents/Gitlab/dos
```

If the executing agent only has write access to one repository, it must complete that repository's side and report the other side as blocked by permissions.

## Parallel Execution Strategy

This plan is explicitly parallel across repositories. One agent can complete the IPS-side cross-reference work while another completes the DOS-side work. A third integration/validation agent should start after both sides publish their shared-principles document paths and gate behavior.

Integration owner: Agent 3 or a separate validation agent reconciles README references, confirms both repositories point to the correct counterpart, and runs the local gates in both repositories.

## Goal Blockers And Dependencies

| Goal | Can start now? | Blockers | Dependencies | Integration point |
| --- | --- | --- | --- | --- |
| G1: IPS-side shared principles | Yes | IPS repository write access | Agent 2 deliverables should exist, but missing items can be reported as gaps | IPS README, IPS gate checks |
| G2: DOS-side shared principles | Yes | DOS repository write access | Agent 1 deliverables should exist, but missing items can be reported as gaps | DOS README, DOS intent validator |
| G3: Cross-repo validation reports | Blocked | Wait for G1 and G2 document paths | G1-G2 | IPS and DOS validation reports |
| G4: Final gate run and conflict review | Blocked | Wait for G1-G3 | G1-G3 | Final evidence and remaining gaps |

## Parallel Dispatch List

### Goal G1: IPS-Side Cross-References

- Owner role: IPS documentation/gate agent
- Objective: create IPS shared-principles and DOS reference-project documents, add IPS goal impact record, and wire lightweight IPS gate checks.
- Allowed files: `17_governance/SHARED_PRINCIPLES_WITH_DOS.md`, `19_examples/DOS_AS_IPS_REFERENCE_PROJECT.md`, `22_goal_impact/GOAL-IMPACT-CROSS-REPO-DOS-PATTERNS.md`, `README.md`, `scripts/pre_coding_gate.py`, `scripts/deployment_readiness_gate.py`
- Forbidden files: `00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`
- Required inputs: Agent 2 IPS deliverables and DOS source docs as read-only references
- Blockers: none if IPS is writable; otherwise blocked by repository permissions
- Validation evidence: IPS pre-coding/deployment gate output or documented existing failures
- Handoff output: IPS document paths and gate-check behavior for G3

### Goal G2: DOS-Side Cross-References

- Owner role: DOS documentation/gate agent
- Objective: create DOS shared-principles and IPS-compliance handoff docs, update DOS README/agent docs, and wire lightweight DOS validator checks.
- Allowed files: `17_governance/SHARED_PRINCIPLES_WITH_IPS.md`, `12_validation/VAL-IPS-COMPLIANCE.md`, `docs/ai-development/ips-compliance-handoff.md`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `scripts/validate_intent_preservation.py`
- Forbidden files: `00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`
- Required inputs: Agent 1 DOS deliverables and IPS governance docs as read-only references
- Blockers: none if DOS is writable; otherwise blocked by repository permissions
- Validation evidence: DOS intent validator and phase gate output or documented existing failures
- Handoff output: DOS document paths and validator behavior for G3

### Goal G3: Cross-Repository Validation Reports

- Owner role: validation documentation agent
- Objective: add or update validation reports proving the two-way alignment without making either repository authoritative over the other.
- Allowed files: IPS `12_validation/VAL-CROSS-REPO-DOS-ALIGNMENT.md`, DOS `12_validation/VAL-IPS-COMPLIANCE.md`
- Forbidden files: immutable constitution and vision files in both repositories
- Required inputs: G1 and G2 document paths and gate behavior
- Blockers: blocked until G1 and G2 handoff paths exist
- Validation evidence: report sections linking to both repositories' local evidence
- Handoff output: validation report paths and unresolved gap list

### Goal G4: Final Gate Run And Conflict Review

- Owner role: integration agent
- Objective: run relevant IPS and DOS gates, verify links, resolve README/reference conflicts, and produce final deviations/permission-blocker report.
- Allowed files: validation reports and narrow README/gate reference fixes
- Forbidden files: unrelated implementation files and immutable intent files
- Required inputs: G1-G3 merged output
- Blockers: blocked until G1-G3 finish
- Validation evidence: all commands in Test Plan
- Handoff output: final validation evidence and remaining gaps

## Non-Goals

- Do not duplicate whole documents between repositories.
- Do not make DOS the source of truth for IPS.
- Do not make IPS responsible for TDOS product decisions.
- Do not alter immutable vision or constitution files except by approved amendment.
- Do not create circular governance where neither repository can change without the other.

## Files to Inspect

In IPS:

```text
README.md
00_constitution/CONSTITUTION.md
01_vision/VISION.md
17_governance/AI_AGENT_RULES.md
17_governance/PROJECT_INVARIANTS.md
23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md
scripts/pre_coding_gate.py
scripts/deployment_readiness_gate.py
```

In DOS:

```text
README.md
00_constitution/CONSTITUTION.md
01_vision/VISION.md
17_governance/AI_AGENT_RULES.md
22_goal_impact/TDOS_GOAL_IMPACT_MAP.md
23_documentation_contracts/INTENT_TRACEABILITY_STANDARD.md
scripts/validate_intent_preservation.py
scripts/phase9_pre_coding_gate.py
scripts/phase10_integration_readiness_gate.py
```

## Files to Create In IPS

Recommended:

```text
19_examples/DOS_AS_IPS_REFERENCE_PROJECT.md
17_governance/SHARED_PRINCIPLES_WITH_DOS.md
22_goal_impact/GOAL-IMPACT-CROSS-REPO-DOS-PATTERNS.md
12_validation/VAL-CROSS-REPO-DOS-ALIGNMENT.md
```

Optional:

```text
15_audits/AUDIT_REPORT_DOS_ALIGNMENT_TEMPLATE.md
```

## Files to Create In DOS

Recommended:

```text
17_governance/SHARED_PRINCIPLES_WITH_IPS.md
12_validation/VAL-IPS-COMPLIANCE.md
docs/ai-development/ips-compliance-handoff.md
```

Optional:

```text
docs/implementation/ips-traceability-retrofit-map.md
```

## Files to Modify In IPS

```text
README.md
17_governance/AI_AGENT_RULES.md
scripts/pre_coding_gate.py
scripts/deployment_readiness_gate.py
```

Only if created by Agent 2:

```text
17_governance/PROJECT_INVARIANTS.md
23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md
```

## Files to Modify In DOS

```text
README.md
AGENTS.md
CLAUDE.md
scripts/validate_intent_preservation.py
```

Only if created by Agent 1:

```text
17_governance/AI_AGENT_RULES.md
23_documentation_contracts/INTENT_TRACEABILITY_STANDARD.md
```

## Files That Must Not Be Modified

In IPS:

```text
00_constitution/CONSTITUTION.md
01_vision/VISION.md
```

In DOS, after Agent 1 creates the protected baseline:

```text
00_constitution/CONSTITUTION.md
01_vision/VISION.md
```

## Implementation Steps

1. Verify Agent 1 deliverables exist in DOS:
   - DOS constitution;
   - DOS vision;
   - DOS amendment control;
   - DOS intent validator;
   - DOS gate integration.
2. Verify Agent 2 deliverables exist in IPS:
   - project invariants mechanism;
   - sensitive-data policy;
   - operational gate standard;
   - pre-coding and deployment gates.
3. Create IPS shared-principles document explaining:
   - IPS is the general intent-preservation framework;
   - DOS is a reference implementation target and operational-pattern source;
   - shared ideas include immutable intent, traceability, gates, data safety, contract validation, replay and project invariants;
   - DOS-specific rules must not become universal IPS rules without abstraction.
4. Create DOS shared-principles document explaining:
   - DOS uses IPS to protect original TDOS vision;
   - DOS contributes operational gate patterns back to IPS;
   - DOS must not change original TDOS intent outside amendment control;
   - DOS must keep product invariants aligned with its protected vision.
5. Add IPS reference example `19_examples/DOS_AS_IPS_REFERENCE_PROJECT.md` showing how a real application maps to IPS layers:

```text
TDOS Vision -> TDOS Goal Impact -> TDOS Systems -> TDOS Features -> TDOS Tasks -> TDOS Plans -> TDOS Gates -> TDOS Validation
```

6. Add IPS goal impact record for transferring DOS patterns.
7. Add validation report in IPS confirming the two-way alignment.
8. Add DOS validation report confirming IPS compliance status.
9. Update IPS README with a short "Reference project pattern" entry linking to the DOS example.
10. Update DOS README with a short "Intent preservation governance" entry linking to IPS principles.
11. Update validators so each repository can check the cross-reference document exists:
    - IPS pre-coding or deployment gate checks `17_governance/SHARED_PRINCIPLES_WITH_DOS.md` if cross-repo mode is enabled or if the file exists.
    - DOS intent validator checks `17_governance/SHARED_PRINCIPLES_WITH_IPS.md`.
12. Keep the validator checks lightweight. They should require presence and minimum sections, not external network or cross-repo reads.

## Test Plan

Run from IPS:

```bash
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root .
python3 scripts/strict_doc_audit.py --format markdown
```

Run from DOS:

```bash
python scripts/validate_intent_preservation.py --root .
python scripts/phase9_pre_coding_gate.py --root .
python scripts/phase10_integration_readiness_gate.py --root .
```

If one repository is not writable or unavailable, run the available repository's validation and report the exact blocker.

## Validation Plan

The task is valid when:

- IPS has a shared-principles document referencing DOS without making DOS authoritative over IPS.
- DOS has a shared-principles document referencing IPS without losing TDOS product independence.
- IPS documents DOS as a reference project pattern.
- DOS documents IPS as its intent governance model.
- Validators or gates include lightweight checks for the shared-principles documents.
- Both repositories can pass their local gates or have clearly documented remaining failures.

## Rollback Plan

If cross-reference checks are too strict:

1. Keep the cross-reference documents.
2. Change validator enforcement to advisory.
3. Report the exact missing or ambiguous sections.
4. Do not remove the new shared-principles documents unless they contain incorrect governance claims.

## Agent Handoff Prompt

```text
You are Agent 3. Make the Intent Preservation System and DOS cross-reference their shared principles after Agent 1 has implemented IPS compliance in DOS and Agent 2 has transferred DOS operational patterns into IPS.

Work with these repositories:
- /Users/Sergej.Stasok/Documents/Gitlab/intent-preservation-system
- /Users/Sergej.Stasok/Documents/Gitlab/dos

First verify Agent 1 deliverables in DOS: constitution, vision, amendment control, goal impact mapping, intent traceability standard, validate_intent_preservation.py, and gate integration. Then verify Agent 2 deliverables in IPS: project invariants, sensitive-data policy, operational gate standard, pre-coding gate, and deployment-readiness gate.

Your objective is to create durable cross-references. IPS should describe DOS as a reference project and operational-pattern source. DOS should describe IPS as its intent-preservation governance model. Do not merge the identities of the systems. IPS stays general. DOS stays TDOS-specific.

Create shared-principles documents in both repositories, update README files, add validation records, and add lightweight gate checks so each repository can confirm its shared-principles document exists. Do not modify immutable constitution or vision files in either repository except through the amendment process.

Run the relevant local gates in both repositories. Report files changed, tests run, validation evidence, deviations, permission blockers, and remaining gaps.
```

## Completion Checklist

- [x] Agent 1 DOS deliverables verified.
- [x] Agent 2 IPS deliverables verified.
- [x] IPS shared-principles document created.
- [x] DOS shared-principles document created.
- [x] IPS DOS reference-project example created.
- [x] IPS goal-impact record for DOS pattern transfer created.
- [x] IPS alignment validation report created.
- [x] DOS IPS-compliance validation report created.
- [x] IPS README updated.
- [x] DOS README updated.
- [x] Lightweight shared-principles gate checks added.
- [x] IPS validation commands run.
- [x] DOS validation commands run.
- [x] Remaining gaps documented.
