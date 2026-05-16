---
ai_summary:
  purpose: "Android fixture build matrix."
  read_when:
    - "When changing Gradle modules, build types, product flavors, or build variants."
  source_of_truth:
    - "settings.gradle.kts"
    - "build.gradle.kts"
    - "app/build.gradle.kts"
  verify_with:
    - "./gradlew :app:assembleDemoDebug"
    - "./gradlew :app:testDemoDebugUnitTest"
  stale_when:
    - "Gradle modules, plugins, build types, flavors, or signing rules change."
---

# Build Matrix

## Purpose

Document the Android fixture Gradle modules, build types, product flavors, build variants, and build verification commands.

## Source of truth

- `settings.gradle.kts`
- `build.gradle.kts`
- `app/build.gradle.kts`

## Key facts

| Area | Value |
| --- | --- |
| Root Gradle settings | `settings.gradle.kts` |
| Root build file | `build.gradle.kts` |
| App module | `app/` |
| App build file | `app/build.gradle.kts` |
| Build types | `debug`, `release` |
| Product flavors | `demo`, `prod` |
| Main debug build | `demoDebug` |
| Main release build | `prodRelease` |

## How to verify

```bash
./gradlew :app:assembleDemoDebug
./gradlew :app:testDemoDebugUnitTest
```

## Stale when

- `settings.gradle.kts` includes change.
- `app/build.gradle.kts` build types or product flavors change.
- Gradle task names change.
