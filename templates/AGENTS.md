# AGENTS.md

## Project purpose

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

## Validation commands

List exact commands.

Examples:

```bash
./gradlew :app:assembleDebug
./gradlew :app:testDebugUnitTest
```

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
