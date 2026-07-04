---
ai_summary:
  purpose: "Android fixture module ownership and dependency map."
  read_when:
    - "When changing module boundaries, dependencies, or feature ownership."
  source_of_truth:
    - "settings.gradle.kts"
    - "app/build.gradle.kts"
    - "core/network/build.gradle.kts"
    - "feature/login/build.gradle.kts"
  verify_with:
    - "./gradlew :app:assembleDemoDebug"
  stale_when:
    - "Modules, dependencies, or public entrypoints change."
---

# Module Map

## Purpose

Document Android fixture module responsibilities, source paths, allowed dependencies, forbidden dependencies, and verification command.

## Source of truth

- `settings.gradle.kts`
- `app/build.gradle.kts`
- `core/network/build.gradle.kts`
- `feature/login/build.gradle.kts`

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

Use the same command in this fixture because module graph changes are covered by the demo debug build.

## Stale when

- Included modules change.
- Module dependencies change.
- Module ownership or public entrypoints change.
