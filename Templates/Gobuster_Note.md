---
title: "gobuster"
type: tool-note
tool: gobuster
tags: [tool, pentesting, web]
cssclass: cs-note
---

# gobuster

## Objective
Enumerate directories, DNS, and vhosts.

## Common Commands
```bash
# gobuster dir
gobuster dir -u http://target -w wordlist.txt -x php,txt,html

# gobuster vhost
gobuster vhost -u http://target -w vhosts.txt

# gobuster dns
gobuster dns -d example.com -w subdomains.txt
```

## Notes
Mind status codes; whitelist relevant ones.

## References
- https://github.com/OJ/gobuster


