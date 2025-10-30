---
title: "<% tp.file.title %>"
type: infra-note
domain: firewall
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [firewall, networking]
cssclass: cs-note
---

# <% tp.file.title %>

## Objective
Ruleset review, troubleshooting, or new policy rollout.

## Device Info
- Vendor/Model:  
- OS/Firmware:  
- Mgmt IP:  

## Key Rules / Snippets
```text
! Example ACL (Cisco style)
access-list 101 permit tcp any host 10.0.0.5 eq 443
access-list 101 deny ip any any
```

## Observations
- Blocked flows:  
- NAT issues:  
- Policy conflicts:  

## Change Log
- Date / Change / Author / Reason

## Next Actions
- 

## References
Vendor docs, rule naming guidelines

