---
title: "hashcat"
type: tool-note
tool: hashcat
tags: [tool, pentesting, cracking]
cssclass: cs-note
---

# hashcat

## Objective
GPU-accelerated password cracking.

## Common Commands
```bash
hashcat -m 1000 hashes.txt rockyou.txt --force
hashcat -m 1000 hashes.txt -a 0 -r rules/best64.rule wordlist.txt
```

## Notes
Pick correct mode (-m). Use potfile for recovered hashes.

## References
- https://hashcat.net/hashcat/


