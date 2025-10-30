---
title: "Workflow Index"
tags: [index, workflow]
cssclass: cs-note
---

# Workflow Index

Directory of procedural documents, lab sequences, and automation scripts.

## Core Workflows
| Workflow | Description | Link |
|----------|-------------|------|
| Reconnaissance | Host discovery and enumeration | [[Recon_Workflow]] |
| Exploitation | Targeted vulnerability exploitation | [[Exploit_Workflow]] |
| Post-Exploitation | Privilege escalation, pivoting, persistence | [[Post_Exploitation_Workflow]] |
| Log Analysis | Parsing and correlating alerts | [[Forensic_Analysis_Workflow]] |
| Reporting | Assemble findings and export | [[Reporting_Workflow]] |
| Evidence Sync | File organization and sync | [[Evidence_Workflow]] |

```dataview
TABLE file.name AS "Workflows", file.mtime AS "Updated"
FROM ""
WHERE contains(tags, "workflow")
SORT file.mtime DESC
```

