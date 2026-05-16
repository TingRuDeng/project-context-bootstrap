---
ai_summary:
  purpose: "Portable agent entrypoint for this repository."
  read_when:
    - "Before making repository changes."
    - "When deciding which docs and validation commands to use."
  source_of_truth:
    - "docs/README.md"
    - "docs/AI_CONTEXT.md"
  verify_with:
    - "python3 scripts/validate_docs.py . --profile generic"
  stale_when:
    - "Project rules, source-of-truth files, or validation commands change."
---

# AGENTS.md

## Purpose

Describe what this repository does in one or two concrete paragraphs.

## Before making changes

Read these files first:

- `docs/README.md`
- `docs/AI_CONTEXT.md`

If this is an Android project, also read:

- `docs/BUILD_MATRIX.md`
- `docs/MODULE_MAP.md`
- `docs/TESTING_MATRIX.md`
- `docs/MANIFEST_AND_PERMISSIONS.md`

## Source of truth

List the files and directories that define project behavior.

Examples:

- Build configuration:
  - `settings.gradle.kts`
  - `build.gradle.kts`
  - `app/build.gradle.kts`
- Application source:
  - `app/src/main/`
- Tests:
  - `app/src/test/`
  - `app/src/androidTest/`

## Key facts

List the stable facts an AI coding agent must preserve.

Examples:

- This repository uses repository-relative paths in generated context docs.
- `docs/AI_CONTEXT.md` is a concise map, not a full architecture document.
- Legacy detail docs must be marked clearly when they are not authority docs.

## How to verify

List exact commands grouped by cost and side effect.

Examples:

Quick:

```bash
./gradlew :app:testDebugUnitTest
python3 scripts/validate_docs.py . --profile android
```

Full:

```bash
./gradlew :app:assembleDebug
./gradlew :app:lintDebug
```

Device-required:

```bash
./gradlew :app:connectedDebugAndroidTest
```

Release-side-effect:

List only if the command creates, signs, publishes, uploads, or synchronizes artifacts.

If the repository has multiple active implementations, packages, apps, or backends, list validation for each active implementation or explain why one is out of scope.

## Stale when

List concrete changes that make this entrypoint stale.

Examples:

- Project rules, source-of-truth files, or validation commands change.
- Authority docs are added, renamed, archived, or split.

## Task routing

Explain which docs to read for common tasks.

Examples:

- Build or Gradle changes: read `docs/BUILD_MATRIX.md`.
- Module boundary changes: read `docs/MODULE_MAP.md`.
- Test changes: read `docs/TESTING_MATRIX.md`.
- Manifest, permissions, or exported components: read `docs/MANIFEST_AND_PERMISSIONS.md`.

## Do not

List project-specific restrictions.

Examples:

- Do not invent Gradle tasks.
- Do not change module dependencies without updating `docs/MODULE_MAP.md`.
- Do not add permissions without updating `docs/MANIFEST_AND_PERMISSIONS.md`.
