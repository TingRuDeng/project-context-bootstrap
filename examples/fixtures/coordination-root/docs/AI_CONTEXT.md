---
ai_summary:
  purpose: "Concise context map for a coordination-root fixture."
  read_when:
    - "When validating repository-shape handling for nested repositories."
  source_of_truth:
    - "AGENTS.md"
    - "backend/README.md"
    - "frontend/README.md"
  verify_with:
    - "python3 scripts/validate_docs.py examples/fixtures/coordination-root --profile generic"
    - "git -C backend diff --check"
    - "git -C frontend diff --check"
  stale_when:
    - "Nested repository boundaries, validation commands, or fixture docs change."
---

# AI Context

## Project Snapshot

- This fixture models a coordination directory with nested backend and frontend repositories.
- The root context pack routes work; implementation facts live below `backend/` and `frontend/`.
- The profile is `generic`.

## Core Directories

- `backend/`: sample nested backend repository.
- `frontend/`: sample nested frontend repository.
- `docs/`: coordination-root authority docs.

## Documentation Map

- `AGENTS.md`: coordination-root rules and repository-shape notes.
- `docs/README.md`: documentation index.
- `docs/AI_CONTEXT.md`: concise context map.

## Common Task Reading Paths

- Backend task: read `AGENTS.md`, then `backend/README.md`.
- Frontend task: read `AGENTS.md`, then `frontend/README.md`.
- Cross-repository task: read `docs/AI_CONTEXT.md`, then check both nested repositories.

## High-Risk Areas

- Do not use root-level git output as evidence for nested repository changes.
- Use `git -C backend` and `git -C frontend` for repository-specific checks.

## Validation Commands

Quick:

```bash
python3 scripts/validate_docs.py examples/fixtures/coordination-root --profile generic
git -C backend diff --check
git -C frontend diff --check
```

## Stale when

- Nested repository boundaries, validation commands, or fixture docs change.
