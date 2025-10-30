---
title: "Forensics Hub"
tags: [hub, forensics, index]
cssclass: cs-note
---

# Forensics Hub

## Quick Links
- Packet analysis: [[Templates/Wireshark_Note]]
- IDS: [[Templates/Snort_Note]] • [[00_Index/Tools_Hub]]

## Recent Forensics Notes
```dataview
TABLE file.name AS "Note", file.mtime AS "Updated"
FROM ""
WHERE any(contains(file.tags, "#forensics"), contains(file.tags, "#pcap"))
SORT file.mtime DESC
```
