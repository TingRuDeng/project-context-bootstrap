---
ai_summary:
  purpose: "Android fixture test matrix."
  read_when:
    - "When changing tests, test directories, or Gradle test commands."
  source_of_truth:
    - "app/src/test/"
    - "app/src/androidTest/"
    - "app/build.gradle.kts"
  verify_with:
    - "./gradlew :app:testDemoDebugUnitTest"
    - "./gradlew :app:connectedDemoDebugAndroidTest"
  stale_when:
    - "Test source sets, test task names, or test framework dependencies change."
---

# Testing Matrix

## Purpose

Document Android fixture test types, test directories, Gradle test tasks, and when each test command is required.

## Source of truth

- `app/src/test/`
- `app/src/androidTest/`
- `app/build.gradle.kts`

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

- Test source sets move.
- Gradle test task names change.
- Android test framework dependencies change.
