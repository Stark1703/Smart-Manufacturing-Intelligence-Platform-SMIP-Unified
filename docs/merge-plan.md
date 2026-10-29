# SMIP Unified Merge Plan

Repository: Stark1703/Smart-Manufacturing-Intelligence-Platform-SMIP-Unified

## Goal
Create a safe integration path for merging the branch evolution into the unified repo without damaging the mainline branch.

## Hard rules
- Do not merge directly into `main`.
- Use `integration/smip-unify` as the only integration branch until validation is complete.
- Keep a clean rollback path for each merge step.
- Treat generated outputs and runtime artifacts as non-source unless explicitly approved.

## Branch strategy
1. `main` remains the release baseline.
2. `integration/smip-unify` is created from `main`.
3. Merge `databricks-v2` into `integration/smip-unify` first.
4. Resolve the highest-risk conflict areas.
5. Merge `v2.0-dev` into the same integration branch only after the Databricks merge is stable.
6. Validate end-to-end.
7. Create a final PR from `integration/smip-unify` to `main`.

## Merge order
### Stage 1: databricks-v2
Target: `integration/smip-unify`

Reason: this branch introduces the largest architectural delta and is most likely to conflict with schema, docs, runtime data paths, and automation files.

### Stage 2: v2.0-dev
Target: `integration/smip-unify`

Reason: this should be merged only after the Databricks architecture has been reconciled and validated.

## High-risk conflict zones
These locations have the highest chance of branch drift or schema mismatch:
- `data/`
- `databricks/`
- `framework/`
- `generator/`
- `sql/`
- `requirements.txt`
- `README.md`
- `setup_project_structure.ps1`
- `docs/`

## Safety gates before each merge
Before merging a branch, check:
- the branch is being merged into `integration/smip-unify`, not `main`
- generated artifacts are not being treated as source of truth
- event schemas are consistent across all branches
- config and dependency files are compatible
- no duplicated runtime data folders are introduced

## Validation checklist after each merge
- Install dependencies from `requirements.txt`
- Confirm Python imports and package resolution
- Run a minimal smoke test for the data pipeline
- Check for duplicate event model definitions
- Confirm SQL files still align with the same ingestion model
- Verify notebook execution assets and docs still refer to the same structure
- Review generated data directories for accidental versioning

## Rollback policy
If a merge introduces breakage:
- revert the merge commit on `integration/smip-unify`
- re-check the branch comparison for the exact conflict set
- re-apply the merge in smaller units, not by large branch sweep

## Final approval gate
Only proceed to a PR against `main` when all of the following are true:
- the integration branch is stable
- the high-risk areas are reconciled
- dependencies are consistent
- run-time data paths are not duplicated
- docs reflect the unified architecture

## Current status
- `integration/smip-unify` branch exists and is the staging branch.
- No merge has been attempted into `main`.
- The next action is to merge `databricks-v2` into this integration branch in a controlled step, then validate before continuing.
