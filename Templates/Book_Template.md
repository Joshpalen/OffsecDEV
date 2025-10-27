---
title: "<% tp.file.title %>"
aliases: []
tags:
  - book
  - reading
created: <% tp.date.now("YYYY-MM-DD") %>
author: "<% tp.system.prompt('Author?') %>"
edition: "<% tp.system.prompt('Edition/Year?') %>"
source: "<% tp.system.suggester(['Print','PDF','eBook','Web'], ['Print','PDF','eBook','Web']) %>"
status: "<% tp.system.suggester(['Not started','In progress','Completed'], ['Not started','In progress','Completed']) %>"
subject: "<% tp.system.suggester(['Networking','Linux','OffSec','Programming','Windows','Android'], ['Networking','Linux','OffSec','Programming','Windows','Android']) %>"
progress: 0
---
# <% tp.file.title %>

> purpose:: High-yield reading with labs that map directly to OffSec skills.

## Summary (3–5 sentences)
- 

## High-Yield Concepts
- 

## Chapter Index
- [[<% tp.file.title %> — Ch01]]
- [[<% tp.file.title %> — Ch02]]
- [[<% tp.file.title %> — Ch03]]

## Action Items
- [ ] Build lab environment for this book
- [ ] Extract top 20 commands to a [[Cheat Sheet – <% tp.file.title %>]]

## Related
- [[Master Index]]  [[Reading Log]]

