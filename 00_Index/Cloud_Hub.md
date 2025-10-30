---
title: "Cloud Hub"
tags: [hub, cloud, index]
cssclass: cs-note
---

# Cloud Hub

```dataview
TABLE file.name AS "Note", file.mtime AS "Updated"
FROM ""
WHERE any(contains(file.tags, "#cloud"), contains(file.tags, "#aws"), contains(file.tags, "#azure"), contains(file.tags, "#gcp"))
SORT file.mtime DESC
```
