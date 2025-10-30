---
title: "Evidence Hub"
tags: [hub, evidence, index]
cssclass: cs-note
---

# Evidence Hub

## Evidence Indexes
```dataview
TABLE file.folder AS "Campaign", file.mtime AS "Updated"
FROM ""
WHERE file.name = "Evidence_Index.md"
SORT file.mtime DESC
```

## Evidence Manifests
```dataview
TABLE file.folder AS "Campaign", file.mtime AS "Updated"
FROM ""
WHERE file.name = "evidence_manifest.json"
SORT file.mtime DESC
```

