
---
title: "<% tp.file.title %>"
tags:
  - links
  - reference
  - resource
created: <% tp.date.now("YYYY-MM-DD") %>
category: "<% tp.system.suggester(['Documentation','Research','Tooling','Exploit','Learning','OSINT','Networking','Programming'], ['Documentation','Research','Tooling','Exploit','Learning','OSINT','Networking','Programming']) %>"
source_type: "<% tp.system.suggester(['Website','Video','PDF','Forum','GitHub','Blog','Paper'], ['Website','Video','PDF','Forum','GitHub','Blog','Paper']) %>"
status: "<% tp.system.suggester(['To Review','Reviewed','Archived'], ['To Review','Reviewed','Archived']) %>"
rating: "<% tp.system.suggester(['⭐','⭐⭐','⭐⭐⭐','⭐⭐⭐⭐','⭐⭐⭐⭐⭐'], ['⭐','⭐⭐','⭐⭐⭐','⭐⭐⭐⭐','⭐⭐⭐⭐⭐']) %>"
---
# <% tp.file.title %>

> Quick reference link collection with metadata for Dataview filtering and retrieval.

## 🔗 Primary Link
- URL: [<% tp.system.prompt('Paste main link here') %>](<% tp.file.cursor() %>)
- Title: 
- Author / Source: 
- Date Published: 
- Summary: 

---

## 🗂️ Related Resources
| Type | Title | URL | Notes |
|------|--------|-----|-------|
| Doc |  |  |  |
| Repo |  |  |  |
| Blog |  |  |  |
| Video |  |  |  |

---

## 📘 Key Takeaways
- 
- 

---

## 📎 Tags / Topics
- #networking
- #linux
- #offsec
- #python
- (Add relevant topic tags here)

---

## 🧩 Related Notes
- [[Master Index]]
- [[Tool Index]]
- [[Reading Log]]
- Related Book: [[Networking_All_in_One]]
- Related Tool: [[Nessus]]

---

## 🧠 Dataview Example Queries (optional)
> Add these to your Master Index to dynamically list all your link notes.
```dataview
table category, source_type, rating, status
from "Source Material"
where contains(file.tags, "#links")
sort created desc
