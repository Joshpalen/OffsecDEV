---
title: "Reading Log"
tags: [index, reading]
cssclass: cs-note
---

# Reading Log

Track active and completed readings, link insights, and revisit sources.

## Active Reading Queue
```dataview
TABLE file.name AS "Active Reading", file.mtime AS "Updated"
FROM ""
WHERE type = "reading" AND (status = "active" OR status = "pending")
SORT file.mtime DESC
```

## Completed Readings
```dataview
TABLE file.name AS "Completed", file.mtime AS "Completed On"
FROM ""
WHERE type = "reading" AND status = "complete"
SORT file.mtime DESC
```

## Historical Log (optional)
| Date | Title | Source | Tags | Status |
|------|-------|--------|------|--------|
|  |  |  |  |  |

