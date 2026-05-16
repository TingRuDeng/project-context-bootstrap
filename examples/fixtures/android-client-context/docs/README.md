---
ai_summary:
  purpose: "Generated docs index for the Android fixture context pack."
  read_when:
    - "When entering the Android fixture repository."
  source_of_truth:
    - "AGENTS.md"
    - "docs/AI_CONTEXT.md"
  verify_with:
    - "python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android"
  stale_when:
    - "Authority docs or Android fixture structure change."
---

# Documentation Index

## Purpose

Route human maintainers and AI coding agents to the smallest useful authority docs for the Android fixture.

## Source of truth

- `AGENTS.md` defines the portable agent entrypoint.
- `docs/AI_CONTEXT.md` defines the concise context map.
- Android profile docs define Gradle, modules, tests, manifests, and permissions.

## Key facts

- Build changes start with `docs/BUILD_MATRIX.md`.
- Module boundary changes start with `docs/MODULE_MAP.md`.
- Test changes start with `docs/TESTING_MATRIX.md`.
- Manifest and permission changes start with `docs/MANIFEST_AND_PERMISSIONS.md`.

## How to verify

```bash
python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android
```

## Stale when

- The fixture file tree changes.
- Android authority docs are added, removed, or renamed.
