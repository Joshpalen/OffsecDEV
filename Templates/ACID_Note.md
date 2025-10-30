---
title: "<% tp.file.title %>"
type: process-note
process: ACID
created: "<% tp.date.now('YYYY-MM-DD') %>"
tags: [process, incident]
cssclass: cs-note
---

# <% tp.file.title %>

## Objective
Notes on Automated Collection, Identification, and Dissemination (or your org’s ACID process).

## Scope
Collection sources, triage steps, dissemination channels.

## Workflow / Checklist
1. Collect artifacts (pcaps, logs, alerts)  
2. Identify TTPs / extract IOCs  
3. Disseminate to stakeholders / blocklist feed

## Logs / Evidence
Storage locations: `/var/acid/`, SIEM indexes

## Automation Ideas
- Auto‑enrich with threat intel  
- Auto‑create tickets for critical alerts

## Next Steps
- Map ownership and SLAs

## References
IR playbooks, TI sources

