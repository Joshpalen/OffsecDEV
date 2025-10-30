---
title: "Scripting Hub"
tags: [hub, scripting, index]
cssclass: cs-note
---

# Scripting Hub

## Notes
```dataview
TABLE file.name AS "Note", file.mtime AS "Updated"
FROM ""
WHERE any(contains(file.tags, "#scripting"), contains(file.tags, "#python"), contains(file.tags, "#bash"), contains(file.tags, "#powershell"))
SORT file.mtime DESC
```
