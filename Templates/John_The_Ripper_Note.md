---
title: "John the Ripper"
type: tool-note
tool: john
tags: [tool, pentesting, cracking]
cssclass: cs-note
---

# John the Ripper

## Objective
Password cracking (offline) with wordlists and rules.

## Common Commands
```bash
john --wordlist=rockyou.txt --format=NT hashes.txt
john --show --format=NT hashes.txt
```

## Notes
Use --fork for multicore; ensure correct hash format.

## References
- https://www.openwall.com/john/


