---
title: "<% tp.file.title %>"
type: packages
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [packages]
cssclass: cs-note
---

# <% tp.file.title %>

## Objective
Track installed packages, versions, updates, and CVE checks.

## Environment
- OS/Distro:  
- Package manager: (apt / dnf / pip / npm / gem)

## Commands
```bash
# Debian/Ubuntu
apt update && apt list --upgradable

# Python
pip list --outdated

# Node
npm outdated
```

## Notable Packages & Versions
| Package | Current | Latest | Notes |
|---------|---------|--------|-------|
|  |  |  |  |

## Security / Updates
- CVEs affecting packages:  
- Planned updates / rollback plan:

## Next Steps
- Schedule patching  
- Test update on staging

## References
Vendor pages, package repos


