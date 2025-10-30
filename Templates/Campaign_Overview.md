---
title: "<% tp.file.title %>"
type: campaign
client: "<client>"
scope: "<in-scope assets>"
window: "<YYYY-MM-DD – YYYY-MM-DD>"
status: planned
tags: [campaign, pentesting]
cssclass: cs-note
---

# <% tp.file.title %> — Overview

> [!meta]
> Client: <client> • Window: <YYYY-MM-DD – YYYY-MM-DD> • Status: planned

## Links
- ROE: [[01-Admin/ROE/ROE Signed.pdf]]
- Scope: [[01-Admin/Scope]]
- Assets: [[01-Admin/Asset_Inventory]]
- Contacts: [[01-Admin/Contacts]]
- Report: [[06-Reporting/Final_Report]]

## Phases
- Planning: ☐  
- Recon: ☐  
- Enumeration: ☐  
- Exploitation: ☐  
- Post‑Exploitation: ☐  
- Reporting: ☐

## Findings (live)
```dataview
TABLE severity, status, affected AS "Asset", reference
FROM this.file.folder
WHERE contains(file.path, "/06-Reporting/Findings/") AND type = "finding"
SORT severity DESC, file.name ASC
```

