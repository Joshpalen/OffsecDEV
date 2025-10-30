---
title: "Tools Hub"
tags: [index, tool]
cssclass: cs-note
---

# Tools Hub

## Quick Links
- Metasploit → [[Templates/Metasploit_Note]]
- Nmap → [[Templates/Nmap_Note]]
- Wireshark → [[Templates/Wireshark_Note]]
- Snort → [[Templates/Snort_Note]]
- Burp Suite → [[Templates/Burp_Suite_Note]]
- ffuf → [[Templates/FFUF_Note]]
- gobuster → [[Templates/Gobuster_Note]]
- nikto → [[Templates/Nikto_Note]]
- hydra → [[Templates/Hydra_Note]]
- john → [[Templates/John_The_Ripper_Note]]
- hashcat → [[Templates/Hashcat_Note]]
- sqlmap → [[Templates/SQLMap_Note]]

```dataview
TABLE category, platforms, status
FROM ""
WHERE type = "tool" OR contains(tags, "#tool")
SORT file.name ASC
```

```dataview
TABLE tool, file.mtime AS "Updated"
FROM ""
WHERE type = "tool-note"
SORT file.mtime DESC
```
