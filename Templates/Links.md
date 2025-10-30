---
title: "<% tp.file.title %>"
tags: [links, reference, resource]
created: "<% tp.date.now('YYYY-MM-DD') %>"
category: "<% tp.system.suggester(['Documentation','Research','Tooling','Exploit','Learning','OSINT','Networking','Programming'], ['Documentation','Research','Tooling','Exploit','Learning','OSINT','Networking','Programming']) %>"
source_type: "<% tp.system.suggester(['Website','Video','PDF','Forum','GitHub','Blog','Paper'], ['Website','Video','PDF','Forum','GitHub','Blog','Paper']) %>"
status: "<% tp.system.suggester(['To Review','Reviewed','Archived'], ['To Review','Reviewed','Archived']) %>"
rating: "<% tp.system.suggester(['1','2','3','4','5'], ['1','2','3','4','5']) %>"
cssclass: cs-note
---

# <% tp.file.title %>

> Store a primary link with context, then add related resources and your takeaways.

## Primary Link
- URL: [<% tp.system.prompt('Paste main link here') %>](<% tp.file.cursor() %>)
- Title: 
- Author / Source: 
- Date Published: 
- Summary: 

## Related Resources
| Type | Title | URL | Notes |
|------|-------|-----|-------|
| Doc |  |  |  |
| Repo |  |  |  |
| Blog |  |  |  |
| Video |  |  |  |

## Key Takeaways
- 
- 

## Tags / Topics
- #networking
- #linux
- #offsec
- #python

## Related Notes
- [[00_Index/Master Index]]
- [[Tags/Index]]
- [[00_Index/Reading Log]]

