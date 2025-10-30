---
title: "Applied Statistics for STEM — Dashboard"
type: course-dashboard
course: "[[Applied Statistics for STEM ~SNHU Course Overview~]]"
tags: [course, dashboard]
cssclass: cs-note
---

# Applied Statistics for STEM — Dashboard

> [!meta]
> Course: [[Applied Statistics for STEM ~SNHU Course Overview~]]

## Lectures
```dataview
TABLE file.name AS "Lecture", date
FROM "Notes/Southern New Hampshire"
WHERE (type = "lecture") OR contains(file.name, "Lecture") OR contains(file.path, "Class Notes")
SORT date ASC
```

## Problem Sets
```dataview
TABLE file.name AS "Set", due
FROM "Notes/Southern New Hampshire"
WHERE type = "problem-set" OR contains(file.name, "Problem") OR contains(file.name, "Set")
SORT due ASC
```

## Readings
```dataview
TABLE file.name AS "Reading", year, authors
FROM "Notes/Southern New Hampshire"
WHERE type = "reading"
SORT file.ctime ASC
```

## Exam Reviews
```dataview
TABLE file.name AS "Exam", date
FROM "Notes/Southern New Hampshire"
WHERE type = "exam-review"
SORT date ASC
```

## Links
- Course Overview: [[Applied Statistics for STEM ~SNHU Course Overview~]]

