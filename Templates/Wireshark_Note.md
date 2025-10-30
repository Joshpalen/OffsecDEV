---
title: "<% tp.file.title %>"
type: tool-note
tool: Wireshark
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [tool, wireshark, networking]
cssclass: cs-note
---

# <% tp.file.title %>

> [!meta]
> Capture/Interface:  • Date: <% tp.date.now('YYYY-MM-DD') %>

## Objective
Packet capture, protocol analysis, IDS tuning, or pcap forensics.

## Capture Filters (BPF)
- `host 10.0.0.5`
- `net 192.168.1.0/24`
- `port 80`

## Display Filters
- `http`
- `tcp.port == 22`
- `ip.addr == 10.0.0.5`

## Observations
- Suspicious flows:  
- Retransmits:  
- Anomalies:  

## Analysis Notes
- Follow TCP stream  
- Export objects (HTTP, SMB)  
- IO graph for traffic patterns

## Evidence
`/Evidence/pcaps/` — pcap filename, key packet IDs/screenshots

## Next Steps
- Deep dive on stream X  
- Correlate with IDS logs

## References
Wireshark docs, BPF cheat sheets

