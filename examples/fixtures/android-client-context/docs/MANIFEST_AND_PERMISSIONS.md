---
ai_summary:
  purpose: "Android fixture manifest and permissions authority doc."
  read_when:
    - "When changing manifest entries, exported components, permissions, or intent filters."
  source_of_truth:
    - "app/src/main/AndroidManifest.xml"
  verify_with:
    - "./gradlew :app:processDemoDebugMainManifest"
  stale_when:
    - "Manifest files, permissions, exported components, or intent filters change."
---

# Manifest And Permissions

## Purpose

Document Android fixture manifest paths, exported components, permissions, intent filters, and manifest verification steps.

## Source of truth

- `app/src/main/AndroidManifest.xml`

## Key facts

| Area | Value |
| --- | --- |
| Main manifest | `app/src/main/AndroidManifest.xml` |
| Main activity | `.MainActivity` |
| Main activity exported | `true` |
| Permissions | `android.permission.INTERNET` |
| Main intent action | `android.intent.action.MAIN` |
| Launcher category | `android.intent.category.LAUNCHER` |

## How to verify

```bash
./gradlew :app:processDemoDebugMainManifest
```

## Stale when

- Manifest entries change.
- Permissions change.
- Exported status changes.
- Intent filters change.
