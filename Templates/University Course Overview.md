---
title: "<% tp.file.title %>"
type: course
code: "COURSE-000"
instructor: "Name"
institution: "University / College"
term: "Semester YYYY"
credits: 0
schedule: "Days & Times"
location: "Building / Room / Online"
tags: [cs, course]
cssclass: cs-note
created: "<% tp.date.now('YYYY-MM-DD') %>"
updated: "<% tp.date.now('YYYY-MM-DD') %>"
---

# <% tp.file.title %>

> [!meta]
> Code: COURSE-000 • Term: Semester YYYY • Credits: 0  
> Instructor: Name • Location: Building / Room / Online  
> Schedule: Days & Times

## Description
Brief summary of the course content, themes, and goals.

## Learning Objectives
- Understand …
- Apply …
- Analyze …
- Create …

## Course Structure
| Week | Topics | Readings | Assignments | Key Dates |
|------|--------|----------|-------------|-----------|
| 1 | Introduction to … | Chapter 1 | Assignment 1 due YYYY-MM-DD |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| … |  |  |  |  |

## Materials
- Textbook(s):  
  - Title by Author (Edition)
- Supplementary:  
  - Articles, websites, lecture notes, etc.

## Assignments & Projects
| Title | Description | Due Date | Status | Grade |
|-------|-------------|----------|--------|-------|
| Assignment 1 |  |  | [ ] |  |
| Midterm |  |  | [ ] |  |
| Final Project |  |  | [ ] |  |

## Assessment Breakdown
| Component | Weight | Notes |
|----------|--------|-------|
| Assignments |  |  |
| Midterm |  |  |
| Final Exam |  |  |
| Participation |  |  |

## Notes & Reflections
How does this course connect to your goals? Skills gained? Challenges?

## Links
- Syllabus (PDF)
- Course website
- Lecture recordings folder
- Discussion board

## Related Materials
> Add `course: [[<% tp.file.title %>]]` to lecture/assignment notes to auto-link.

### Lectures
```dataview
TABLE file.name AS "Lecture", date
FROM ""
WHERE type = "lecture" AND course = this.file.link
SORT date ASC
```

### Problem Sets
```dataview
TABLE file.name AS "Set", due
FROM ""
WHERE type = "problem-set" AND course = this.file.link
SORT due ASC
```

### Readings
```dataview
TABLE file.name AS "Reading", year, authors
FROM ""
WHERE type = "reading" AND course = this.file.link
SORT file.ctime ASC
```

### Exam Reviews
```dataview
TABLE file.name AS "Exam", date
FROM ""
WHERE type = "exam-review" AND course = this.file.link
SORT date ASC
```
