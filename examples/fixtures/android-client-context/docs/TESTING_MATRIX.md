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

| Test type | Tier | Path | Command | Use when |
| --- | --- | --- | --- | --- |
| Local unit tests | quick | `app/src/test/` | `./gradlew :app:testDemoDebugUnitTest` | Pure JVM logic |
| Instrumented tests | device-required | `app/src/androidTest/` | `./gradlew :app:connectedDemoDebugAndroidTest` | Android framework behavior |

## How to verify

Quick:

```bash
./gradlew :app:testDemoDebugUnitTest
```

Device-required:

```bash
./gradlew :app:connectedDemoDebugAndroidTest
```

## Stale when

- Test source sets move.
- Gradle test task names change.
- Android test framework dependencies change.
