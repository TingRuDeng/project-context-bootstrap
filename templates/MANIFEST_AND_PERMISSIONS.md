---
ai_summary:
  purpose: "Android manifest and permissions authority document."
  read_when:
    - "When changing manifests, exported components, permissions, or intent filters."
  source_of_truth:
    - "app/src/main/AndroidManifest.xml"
  verify_with:
    - "./gradlew :app:processDemoDebugMainManifest"
  stale_when:
    - "Manifest files, permissions, exported components, or intent filters change."
---

# Manifest And Permissions

## Purpose

Explain manifest paths, exported components, permissions, intent filters, manifest merge risks, and verification steps.

## Source of truth

List Android manifest files and Gradle build files that influence manifest merge output.

## Key facts

| Area | Value |
| --- | --- |
| Main manifest | `app/src/main/AndroidManifest.xml` |
| Main activity | `.MainActivity` |
| Main activity exported | `true` |
| Permissions | `android.permission.INTERNET` |

## How to verify

```bash
./gradlew :app:processDemoDebugMainManifest
```

## Stale when

- Manifest entries change.
- Permissions change.
- Intent filters or exported status change.
