---
title: "Courses Hub"
tags: [index, courses]
cssclass: cs-note
---

# Courses Hub

```dataview
TABLE code, term, instructor
FROM ""
WHERE type = "course"
SORT code ASC
```

```dataview
TABLE course, file.name AS "Dashboard"
FROM ""
WHERE type = "course-dashboard"
SORT file.name ASC
```

## Class Notes (recent)
```dataview
TABLE file.name AS "Note", file.folder AS "Location", file.mtime AS "Updated"
FROM "Notes/Southern New Hampshire/Class Notes"
SORT file.mtime DESC
```

## Education‑Tagged Notes
```dataview
TABLE file.name AS "Note", file.folder AS "Location", file.mtime AS "Updated"
FROM ""
WHERE contains(file.tags, "#education")
SORT file.mtime DESC
```
