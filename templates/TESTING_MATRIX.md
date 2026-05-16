---
ai_summary:
  purpose: "Android test matrix authority document."
  read_when:
    - "When changing tests, test directories, or verification commands."
  source_of_truth:
    - "app/src/test/"
    - "app/src/androidTest/"
    - "app/build.gradle.kts"
  verify_with:
    - "./gradlew :app:testDemoDebugUnitTest"
  stale_when:
    - "Test tasks, test directories, or test frameworks change."
---

# Testing Matrix

## Purpose

Explain local unit tests, instrumented tests, UI tests, screenshot tests if present, and when to run each command.

## Source of truth

List test source directories, Gradle test tasks, and build files that define test behavior.

## Key facts

| Test type | Path | Command | Use when |
| --- | --- | --- | --- |
| Local unit tests | `app/src/test/` | `./gradlew :app:testDemoDebugUnitTest` | Pure JVM logic |
| Instrumented tests | `app/src/androidTest/` | `./gradlew :app:connectedDemoDebugAndroidTest` | Android framework behavior |

## How to verify

```bash
./gradlew :app:testDemoDebugUnitTest
./gradlew :app:connectedDemoDebugAndroidTest
```

## Stale when

- Test directories move.
- Gradle test tasks change.
- Test framework dependencies change.
