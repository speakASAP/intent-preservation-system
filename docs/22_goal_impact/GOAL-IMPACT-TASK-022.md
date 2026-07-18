# GOAL-IMPACT-TASK-022: Provider Status Manager Interface

```yaml
id: GOAL-IMPACT-TASK-022
artifact_type: task
artifact_id: TASK-022
artifact_path: ../11_tasks/TASK-022-surface-provider-status-in-manager-interface.md
primary_goal: Make provider safety and promotion status manager-visible.
secondary_goals:
  - Reduce manager dependence on CLI output.
  - Preserve optional retrieval boundaries.
  - Show dry-run and zero-network provider evidence.
impact_level: medium
impact_description: This task extends the manager interface with provider gate and promotion status derived from validated provider artifacts.
success_metric: A manager can open the interface and see whether the dry-run provider is safe, offline and promotable.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../10_features/FEAT-004-manager-visibility.md
  - ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
  - ../11_tasks/TASK-021-add-provider-promotion-thresholds.md
downstream_links:
  - ../21_execution_plans/EP-TASK-022.md
  - ../12_validation/VAL-TASK-022-provider-status-manager-interface.md
validation_method: Run provider gates, repository validation and deployment-readiness gate.
status: validated
```

## Explanation

TASK-022 turns provider safety and promotion evidence into manager-readable
dashboard status. It helps managers distinguish an offline dry-run provider
candidate from a real external provider.

## Evidence

- Manager interface: `../../manager_interface/index.html`
- Provider safety config: `../../config/embedding_provider_gates.json`
- Provider promotion rules: `../../config/provider_promotion_rules.json`
- Dry-run candidate fixture: `../../tests/fixtures/retrieval_candidate_dry_run.json`

## Validation

The impact is validated when the interface displays provider gate and promotion
status and the provider safety, promotion and repository gates pass.
