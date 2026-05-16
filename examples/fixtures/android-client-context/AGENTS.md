# AGENTS.md

## Project purpose

This fixture demonstrates an Android MVP context pack for AI coding agents.

## Before making changes

Read:

- `docs/README.md`
- `docs/AI_CONTEXT.md`

For Android-specific work, also read:

- `docs/BUILD_MATRIX.md`
- `docs/MODULE_MAP.md`
- `docs/TESTING_MATRIX.md`
- `docs/MANIFEST_AND_PERMISSIONS.md`

## Source of truth

- `settings.gradle.kts` defines included Gradle modules.
- `app/build.gradle.kts` defines app build types, flavors, and dependencies.
- `app/src/main/AndroidManifest.xml` defines exported components and permissions.
- `app/src/test/` and `app/src/androidTest/` define test source sets.

## Validation commands

Quick:

```bash
./gradlew :app:testDemoDebugUnitTest
python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android
```

Full:

```bash
./gradlew :app:assembleDemoDebug
```

Device-required:

```bash
./gradlew :app:connectedDemoDebugAndroidTest
```

## Task routing

- Build or Gradle changes: read `docs/BUILD_MATRIX.md`.
- Module boundary changes: read `docs/MODULE_MAP.md`.
- Test changes: read `docs/TESTING_MATRIX.md`.
- Manifest, permissions, or exported components: read `docs/MANIFEST_AND_PERMISSIONS.md`.

## Do not

- Do not invent Gradle tasks.
- Do not change module dependencies without updating `docs/MODULE_MAP.md`.
- Do not add permissions without updating `docs/MANIFEST_AND_PERMISSIONS.md`.
