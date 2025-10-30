---
title: "Master Index"
tags: [core, index]
cssclass: cs-note
---

# Master Index

Vault: OffsecDEV_Root  
Author: Josh  
Purpose: Root navigation hub linking domains, tools, tags, templates, and active projects.

## Core Navigation
| Category | Description | Link |
|---------|-------------|------|
| Tag Index | Complete reference of all tags | [[Tags/Index]] |
| Taxonomy Reference | Relationships & hierarchy between tags | [[Tags/Taxonomy Reference]] |
| Templates | Predefined note structures | [[Templates/Templates_Hub]] |
| Tools | Tool notes + usage | [[00_Index/Tools_Hub]] |
| Reports | Deliverables and findings | [[00_Index/Reports_Hub]] |
| Scripts | Script notes | [[00_Index/Scripts_Hub]] |
| Courses | Course pages + dashboards | [[00_Index/Courses_Hub]] |
| Algorithms | Algorithms index | [[00_Index/Algorithms_Index]] |
| Data Structures | DS index | [[00_Index/Data_Structures_Index]] |

## Quick Views
### Recent Updates
```dataview
TABLE file.name AS "Recent", file.folder AS "Location", file.mtime AS "Updated"
FROM ""
SORT file.mtime DESC
LIMIT 15
```

### Open Tasks
```dataview
TASK
FROM ""
WHERE !completed
SORT file.mtime DESC
```

### Reading Queue
```dataview
TABLE file.name AS "Reading", file.mtime AS "Added"
FROM ""
WHERE type = "reading" OR contains(tags, "#reading")
SORT file.mtime DESC
```

## Study Hubs
- [[Templates/Algorithm]] • [[Templates/Data_Structure]] • [[Templates/Concept]]
- [[Templates/Lecture_Note]] • [[Templates/Problem_Set]] • [[Templates/Exam_Review]]
- [[Templates/Reading_Summary]] • [[Templates/Links]]

## Domain Hubs
- [[00_Index/Pentesting_Hub]] • [[00_Index/Networking_Hub]] • [[00_Index/Forensics_Hub]]
- [[00_Index/Malware_Hub]] • [[00_Index/Cryptography_Hub]]
- [[00_Index/Scripting_Hub]] • [[00_Index/Docker_Hub]] • [[00_Index/Cloud_Hub]] • [[00_Index/Packages_Hub]]
- Evidence: [[00_Index/Evidence_Hub]] • Tools: [[00_Index/Tools_Hub]] • Reports: [[00_Index/Reports_Hub]]

## Maintenance (Windows / PowerShell)
| Action | Command |
|--------|---------|
| Sync local → OneDrive | `C:\Users\joshp\Scripts\sync_offsecdev.ps1 -Execute` |
| Dry-run sync | `C:\Users\joshp\Scripts\sync_offsecdev.ps1` |
| Export Vault | `robocopy "C:\OffsecDEV\OffsecDEV_Root" "D:\Vault_Backup" /MIR` |
| Search by Tag | `Get-ChildItem -Recurse | Select-String "#pentesting"` |

## Principle
Structure enables discovery. Discovery builds intelligence. Intelligence empowers execution.
