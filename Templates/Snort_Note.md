---
title: "<% tp.file.title %>"
type: tool-note
tool: Snort
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [tool, snort, ids]
cssclass: cs-note
---

# <% tp.file.title %>

> [!meta]
> Sensor/Host:  • Date: <% tp.date.now('YYYY-MM-DD') %>

## Objective
Rules tuning, alert review, baseline behavior, or FP triage.

## Deployment Info
- Version:  
- Ruleset: (ET Pro/Open/custom)  
- Interfaces:  

## Recent Alerts / Notable Signatures
| Time | SID | Msg | Src -> Dst |
|------|-----|-----|------------|
|  |  |  |  |

## Rule Examples / Tuning
```text
alert tcp any any -> $HOME_NET 80 (msg:"Example rule"; sid:1000001; rev:1;)
```

- FP reasoning:  
- Action (disable/threshold/refine):  

## Logs / Evidence
`/var/log/snort/alert` — relevant lines, pcap evidence

## Next Steps
- 

## References
Snort manual, rules writing guide

