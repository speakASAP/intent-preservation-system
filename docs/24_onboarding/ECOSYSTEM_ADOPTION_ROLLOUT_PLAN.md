# Ecosystem-Wide IPS Adoption Rollout Plan

```yaml
id: ECOSYSTEM-IPS-ADOPTION-ROLLOUT
status: approved-for-planning
owner: project owner
created: 2026-08-30
approval evidence: owner-confirmation: ecosystem-ips-adoption-rollout-approved
scope: every Git repository under /home/ssf/Documents/Github
```

## Objective

Bring every repository in the Alfares ecosystem into alignment with the
canonical IPS project-adoption standard used for `cv-tuning`, `runlayer`, and
`wisdom-quotes`: a complete, validator-passing `ips-adoption.json` profile plus
the required root and `docs/` document set, without inventing business intent
or overwriting real existing content.

## Method (per repository)

1. Run `scaffold_project_adoption.py` from the repo root (non-destructive —
   only creates missing files, never overwrites existing `BUSINESS.md`,
   `SYSTEM.md`, `README.md`, etc.).
2. Reformat any pre-existing root docs into the required IPS section
   structure, preserving all real, already-documented facts (goals,
   constraints, stack, integrations, SLAs). Never fabricate new business
   claims, metrics, or approvals.
3. Fill `docs/00_constitution/CONSTITUTION.md`, `docs/01_vision/VISION.md`,
   `docs/17_governance/PROJECT_INVARIANTS.md`, and
   `docs/06_architecture/INTEGRATION_CONTRACT.md` with project-specific,
   truthful capability decisions (required vs not-applicable with a reason).
4. Create the TASK-001 bootstrap task, execution plan, goal-impact and
   validation records describing this onboarding/documentation-alignment
   work itself.
5. Set `ipsAdoptionRequired: true` for the repository in
   `shared/config/ecosystem-repositories.json`.
6. Run `validate_adoption_profile.py --root . --phase planning` until it
   passes; fix any remaining required section, placeholder, or traceability
   issue.
7. Commit directly to `main` in the repository (docs-only changes; some
   repos also add `ips-adoption.json`, which is not on the deploy-skip list,
   so a queued auto-deploy may follow — this is expected and does not
   require a manual deploy).
8. Mark the repository `done` below and move to the next one.

## Status Legend

`pending` → not yet started · `in-progress` → scaffold/content underway ·
`done` → validator passes with `--phase planning`.

## Repository Rollout Order and Status

### Already aligned (prior sessions)

- [x] cv-tuning — done
- [x] runlayer — done
- [x] wisdom-quotes — done

### Priority repos

- [ ] logging-microservice — pending
- [ ] notifications-microservice — pending
- [ ] auth-microservice — pending
- [ ] database-server — pending
- [ ] vault-microservice — pending
- [ ] k8s-manifests — pending
- [ ] catalog-microservice — pending

### E-commerce backbone

- [ ] warehouse-microservice — pending
- [ ] suppliers-microservice — pending
- [ ] orders-microservice — pending
- [ ] invoices-microservice — pending
- [ ] payments-microservice — pending

### Infrastructure

- [ ] backups-microservice — pending
- [ ] docs-rag-microservice — pending
- [ ] minio-microservice — pending
- [ ] monitoring-microservice — pending
- [ ] ai-microservice — pending

### speakasap

- [ ] speakasap — pending
- [ ] speakasap-portal — pending (legacy Django, docs-only onboarding)

### Business / apps / orchestration

- [ ] agentic-email-processing-system — pending
- [ ] business-process-control-plane — pending
- [ ] leads-microservice — pending
- [ ] marketing-microservice — pending
- [ ] prompts-microservice — pending
- [ ] shop-assistant — pending
- [ ] school-committee — pending
- [ ] candidate-blueprism — pending
- [ ] cliplot — pending
- [ ] chytrakoupe — pending
- [ ] rent-a-box — pending
- [ ] goalkeeper — pending
- [ ] crypto-ai-agent — pending
- [ ] flipflop — pending
- [ ] growth — pending
- [ ] marathon — pending
- [ ] statex — pending

### Marketplace integrations

- [ ] allegro — pending
- [ ] aukro — pending
- [ ] bazos — pending
- [ ] heureka — pending

### Hubs (no runtime)

- [ ] shared — pending
- [ ] vault — pending
- [ ] intent-preservation-system — pending

### Low-priority (last)

- [ ] statex-ecosystem — pending
- [ ] domain-research — pending

## Notes

- `speakasap-portal` app server is read-only over SSH; this only touches its
  Git-tracked docs, which is unaffected by that runtime constraint.
- Deny-listed-for-deploy repos (`vault-microservice`, `vault`, `k8s-manifests`,
  `speakasap-portal`, `shared`) still get onboarded; their deploy deny-list
  status is unrelated to documentation alignment.
- Update this file's checkboxes as each repository is completed so the
  rollout is resumable across sessions.
