# DOS As IPS Reference Project

## Purpose

DOS is a concrete reference project for applying IPS to a real AI-assisted system. It shows how protected intent can drive a contract-first, gate-driven implementation without making the implementation domain part of the IPS core.

## Reference Mapping

```text
TDOS Vision
  -> TDOS Goal Impact
  -> TDOS Systems
  -> TDOS Features
  -> TDOS Tasks
  -> TDOS Plans
  -> TDOS Gates
  -> TDOS Validation
```

## IPS Layer Mapping

| IPS layer | DOS reference pattern |
|---|---|
| Constitution | Protected rules that prevent unmanaged changes to TDOS purpose and operating constraints. |
| Vision | Protected TDOS original intent, distinct from implementation backlog details. |
| Goal impact | TDOS goal-impact mapping explains why each delivery step preserves the protected product direction. |
| Systems and features | Runtime phases, schemas and decision infrastructure map to bounded implementation surfaces. |
| Tasks and plans | Coding work is staged through explicit implementation plans and prompts. |
| Gates | Phase gates confirm readiness before coding and integration. |
| Validation | Intent validation, contract validation and replay evidence check completed work against upstream intent. |

## Reusable Patterns

DOS contributes reusable operational patterns to IPS:

- declare project invariants before coding;
- treat schemas and contracts as protected implementation boundaries;
- keep validation examples synthetic unless a human-approved secure workflow allows otherwise;
- require readiness gates to produce evidence under `reports/validation/`;
- preserve replay and determinism expectations when AI-assisted implementation touches decision logic.

## Boundary Rules

DOS is an example, not the IPS source of truth. IPS should extract general controls from DOS but must not import TDOS-specific policy, product, customer, supplier or runtime rules as universal IPS requirements.

DOS remains responsible for TDOS product decisions through its own constitution, vision, amendment control and decision records.

## Validation Use

An IPS audit may use this example to check whether a downstream project has mapped its original intent to implementation gates and validation evidence. The audit should evaluate the mapping pattern, not whether the downstream project resembles TDOS.
