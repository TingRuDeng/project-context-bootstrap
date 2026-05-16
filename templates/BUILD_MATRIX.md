---
ai_summary:
  purpose: "Android build matrix authority document."
  read_when:
    - "When changing Gradle modules, build types, flavors, or variants."
  source_of_truth:
    - "settings.gradle.kts"
    - "build.gradle.kts"
    - "app/build.gradle.kts"
  verify_with:
    - "./gradlew :app:assembleDemoDebug"
  stale_when:
    - "Gradle modules, flavors, build types, or signing rules change."
---

# Build Matrix

## Purpose

Explain Android modules, build types, product flavors, variants, signing notes, and build commands.

## Source of truth

List Gradle files that define modules, plugins, flavors, build types, and signing configuration.

## Key facts

| Area | Value |
| --- | --- |
| Root Gradle settings | `settings.gradle.kts` |
| App module | `app/` |
| App build file | `app/build.gradle.kts` |
| Build types | `debug`, `release` |
| Product flavors | `demo`, `prod` |

## How to verify

Quick:

```bash
./gradlew :app:testDemoDebugUnitTest
```

Full:

```bash
./gradlew :app:assembleDemoDebug
```

Release-side-effect:

List signing, publishing, upload, or artifact synchronization commands only when they exist.

## Stale when

- Gradle modules change.
- Build types or product flavors change.
- Signing configuration changes.
