---
title: "Reports Hub"
tags: [index, reports]
cssclass: cs-note
---

# Reports Hub

```dataview
TABLE file.name AS "Report", file.folder AS "Folder", file.mtime AS "Updated"
FROM "Pentest Campaign/Reports"
SORT file.mtime DESC
```

