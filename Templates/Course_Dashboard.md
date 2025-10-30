---
title: "<% tp.file.title %>"
type: course-dashboard
course: "[[<% tp.system.prompt('Link to course page (or name)') %>]]"
tags: [course, dashboard]
cssclass: cs-note
---

# <% tp.file.title %>

> [!meta]
> Course: <% tp.frontmatter.course %>

## Lectures
```dataview
TABLE file.name AS "Lecture", date
FROM ""
WHERE type = "lecture" AND course = this.course
SORT date ASC
```

## Problem Sets
```dataview
TABLE file.name AS "Set", due
FROM ""
WHERE type = "problem-set" AND course = this.course
SORT due ASC
```

## Readings
```dataview
TABLE file.name AS "Reading", year, authors
FROM ""
WHERE type = "reading" AND course = this.course
SORT file.ctime ASC
```

## Exam Reviews
```dataview
TABLE file.name AS "Exam", date
FROM ""
WHERE type = "exam-review" AND course = this.course
SORT date ASC
```

## Links
- Course Overview: <% tp.frontmatter.course %>

