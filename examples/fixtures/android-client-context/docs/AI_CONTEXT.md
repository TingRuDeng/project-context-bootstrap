---
ai_summary:
  purpose: "Concise context map for the Android fixture."
  read_when:
    - "Before changing fixture docs or Android profile examples."
  source_of_truth:
    - "AGENTS.md"
    - "settings.gradle.kts"
    - "app/build.gradle.kts"
  verify_with:
    - "python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android"
  stale_when:
    - "Fixture modules, build variants, test tasks, or authority docs change."
---

# AI Context

## Project Snapshot

- Android fixture for validating an agent-agnostic context pack.
- Uses Gradle Kotlin DSL with `:app`, `:core:network`, and `:feature:login`.
- Demonstrates Android MVP docs for build, modules, tests, manifests, and permissions.

## Core Directories

- `app/`: Android application entrypoint.
- `core/network/`: networking primitives.
- `feature/login/`: login feature UI and flow.
- `docs/`: generated context pack authority docs.

## Documentation Map

- `docs/README.md`: generated docs index.
- `docs/BUILD_MATRIX.md`: Gradle modules, build types, flavors, variants, and build commands.
- `docs/MODULE_MAP.md`: module responsibilities and dependency boundaries.
- `docs/TESTING_MATRIX.md`: test source sets and Gradle test commands.
- `docs/MANIFEST_AND_PERMISSIONS.md`: manifest paths, exported components, intent filters, and permissions.

## Common Task Reading Paths

- Build or flavor changes: read `docs/BUILD_MATRIX.md`, then inspect `settings.gradle.kts` and `app/build.gradle.kts`.
- Module dependency changes: read `docs/MODULE_MAP.md`, then inspect each module `build.gradle.kts`.
- Test changes: read `docs/TESTING_MATRIX.md`, then inspect `app/src/test/` or `app/src/androidTest/`.
- Manifest or permission changes: read `docs/MANIFEST_AND_PERMISSIONS.md`, then inspect `app/src/main/AndroidManifest.xml`.

## High-Risk Areas

- Do not invent Gradle tasks that are not documented in authority docs.
- Do not change module dependencies without updating `docs/MODULE_MAP.md`.
- Do not add permissions without updating `docs/MANIFEST_AND_PERMISSIONS.md`.

## Validation Commands

```bash
python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android
```

## Stale when

- Gradle modules, variants, test tasks, manifest entries, or Android profile docs change.
