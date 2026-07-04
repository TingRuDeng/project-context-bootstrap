---
ai_summary:
  purpose: "Coordination-root fixture agent entrypoint."
  read_when:
    - "When validating context packs for roots that coordinate nested repositories."
  source_of_truth:
    - "backend/README.md"
    - "frontend/README.md"
    - "docs/AI_CONTEXT.md"
  verify_with:
    - "python3 scripts/validate_docs.py examples/fixtures/coordination-root --profile generic"
    - "git -C backend diff --check"
    - "git -C frontend diff --check"
  stale_when:
    - "Nested repository names, validation commands, or coordination-root docs change."
---

# AGENTS.md

## Purpose

Define the portable entrypoint for a coordination directory that contains nested implementation repositories.

## Source of truth

- `backend/README.md`
- `frontend/README.md`
- `docs/AI_CONTEXT.md`

## Key facts

- This fixture models a coordination directory.
- `backend/` and `frontend/` are treated as separate git units in generated docs.
- Root-level git output is not strong evidence for nested repository changes.

## How to verify

Quick:

```bash
python3 scripts/validate_docs.py examples/fixtures/coordination-root --profile generic
git -C backend diff --check
git -C frontend diff --check
```

## Stale when

- Nested repository names, validation commands, or coordination-root docs change.
