---
title: "<% tp.file.title %>"
type: tool-note
tool: Nmap
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [tool, nmap, networking]
cssclass: cs-note
---

# <% tp.file.title %>

> [!meta]
> Target/Range:  • Date: <% tp.date.now('YYYY-MM-DD') %>

## Objective
Port discovery, version detection, OS fingerprinting, script scan, stealth scan.

## Common Commands
```bash
# Quick scan
nmap -sS -Pn 10.0.0.0/24
# Service/version
nmap -sV -p- 10.0.0.5
# OS detection and scripts
nmap -A -T4 10.0.0.5
# NSE scripts
nmap --script vuln 10.0.0.5
```

## Output / Notes
- Open ports:  
- Services/Versions:  
- OS guess:  

Attach output file: `nmap_target.xml`

## Tips / Flags Used
- `-sS` stealth SYN scan
- `-Pn` skip host discovery
- `-p-` full port sweep
- `-oA` save all formats

## Next Steps
- Run targeted NSE scripts  
- Pivot to service-specific testing

## References
Nmap docs, NSE script docs

