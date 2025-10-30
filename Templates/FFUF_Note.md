---
title: "ffuf"
type: tool-note
tool: ffuf
tags: [tool, pentesting, web]
cssclass: cs-note
---

# ffuf

## Objective
Fuzz for web content, parameters, and vhosts.

## Common Commands
```bash
# Directory fuzzing
ffuf -w wordlist.txt -u http://target/FUZZ -mc 200,204,301,302,307,401,403

# Vhost fuzzing
ffuf -w vhosts.txt -u http://target -H 'Host: FUZZ.target' -mc 200
```

## Notes
Tune filters: -fs (size), -fw (words), -fc (status). Respect scope.

## References
- https://github.com/ffuf/ffuf

