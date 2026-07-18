# SYS-003 Audit Engine

## Purpose

The Audit Engine evaluates existing projects and identifies missing, weak or inconsistent documentation.

## Responsibilities

- Check required document coverage.
- Detect missing traceability.
- Detect missing validation criteria.
- Detect missing ADRs for technical decisions.
- Detect roadmap gaps.
- Detect concept drift.
- Produce recommendations.

## Audit dimensions

1. Vision completeness.
2. Business case clarity.
3. System decomposition.
4. Architecture documentation.
5. Decision records.
6. Roadmap and milestones.
7. Feature requirements.
8. Task granularity.
9. Validation coverage.
10. Context package readiness.

## Output

Audit reports should be stored in `15_audits/`.

Each report contains:

- score;
- critical gaps;
- warnings;
- recommendations;
- suggested documents to create;
- suggested task decomposition improvements.

## Validation

The audit engine is valid when it can run against this repository, report missing
documents or broken traceability with file-level detail, and fail CI when
high-severity findings remain.
