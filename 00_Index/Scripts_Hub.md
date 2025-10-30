---
title: "Scripts Hub"
tags: [index, scripts]
cssclass: cs-note
---

# Scripts Hub

> Tip: Add short .md wrapper notes for important scripts with usage and examples, tagged `#script`.

```dataview
TABLE file.name AS "Script Note", file.folder AS "Location", file.mtime AS "Updated"
FROM ""
WHERE contains(tags, "#script")
SORT file.mtime DESC
```

Other script locations of interest:
- `Automation/Scripts`
- `Pentest Campaign/Reports/*/Scripts`

