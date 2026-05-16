---
ai_summary:
  purpose: "Android module ownership and dependency map."
  read_when:
    - "When changing module boundaries or dependencies."
  source_of_truth:
    - "settings.gradle.kts"
    - "app/build.gradle.kts"
  verify_with:
    - "./gradlew :app:assembleDemoDebug"
  stale_when:
    - "Modules, dependencies, or public entrypoints change."
---

# Module Map

## Purpose

Explain each Android module responsibility, source path, dependency boundary, and verification command.

## Source of truth

List Gradle settings, module build files, and source directories that define module behavior.

## Key facts

| Module | Source path | Responsibility | Depends on | Must not depend on |
| --- | --- | --- | --- | --- |
| `:app` | `app/` | Android application entrypoint | `:core:network`, `:feature:login` | None |
| `:core:network` | `core/network/` | Networking primitives | None | `:app`, feature modules |
| `:feature:login` | `feature/login/` | Login UI and flow | `:core:network` | `:app` |

## How to verify

Quick:

```bash
./gradlew :app:assembleDemoDebug
```

Full:

List broader module regression commands when module boundaries or dependencies change.

## Stale when

- Modules are added, removed, or renamed.
- Dependency direction changes.
- Public entrypoints move.
