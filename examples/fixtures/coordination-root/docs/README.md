---
ai_summary:
  purpose: "Coordination-root fixture documentation index."
  read_when:
    - "When checking how nested repository context docs should be routed."
  source_of_truth:
    - "AGENTS.md"
    - "docs/AI_CONTEXT.md"
  verify_with:
    - "python3 scripts/validate_docs.py examples/fixtures/coordination-root --profile generic"
  stale_when:
    - "Fixture authority docs or nested repository routing changes."
---

# Coordination Root Docs

## Purpose

Route maintainers and AI coding agents to the right authority docs for a coordination directory.

## Source of truth

- `AGENTS.md`
- `docs/AI_CONTEXT.md`

## Key facts

- `AGENTS.md` defines the coordination-root execution rules.
- `docs/AI_CONTEXT.md` summarizes nested repository boundaries.

## How to verify

```bash
python3 scripts/validate_docs.py examples/fixtures/coordination-root --profile generic
```

## Stale when

- Fixture authority docs or nested repository routing changes.
