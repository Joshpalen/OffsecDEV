---
title: "Packages Hub"
tags: [hub, packages, index]
cssclass: cs-note
---

# Packages Hub

```dataview
TABLE file.name AS "Note", file.mtime AS "Updated"
FROM ""
WHERE any(contains(file.tags, "#packages"), contains(file.tags, "#dependency"))
SORT file.mtime DESC
```
