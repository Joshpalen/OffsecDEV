---
title: "Taxonomy Reference"
tags: [core, index]
cssclass: cs-note
---

# Taxonomy Reference

Defines the conceptual structure, relationships, and metadata schema of the vault. Goal: maintain a semantic, scalable knowledge graph.

## Hierarchical Model
| Tier | Purpose | Example |
|------|---------|---------|
| Core | Foundations across all content | `core`, `reference`, `template` |
| Domain | Subject categories | `pentesting`, `networking`, `scripting` |
| Context | Situational metadata | `metasploit`, `firewall`, `pending` |

Each note should align with at least one domain tag and optional context tags.

## Relationships
| Relation | Meaning |
|---------|---------|
| project + report | Work produces deliverable |
| report + evidence | Report backed by proof |
| workflow + tool | Procedure uses tool |
| concept + reference | Theory supported by docs |

## Metadata Standards
Frontmatter keys for alignment and automation:
```yaml
---
tags: [pentesting, tool]
aliases: []
created: 2025-01-01
status: active
---
```
| Key | Purpose |
|-----|---------|
| tags | Semantic relationships |
| aliases | Alternate identifiers |
| created | Audit trail |
| status | active/pending/complete/archived |

## Cross-Linking
- Use wikilinks `[[NoteName]]` liberally.
- Create Hubs/MOCs per domain, listing children via Dataview.
```dataview
TABLE file.name AS "Pentesting Files"
FROM "Notes"
WHERE contains(tags, "pentesting")
SORT file.mtime DESC
```

## Tool Relationships
| Tool | Related Tags |
|------|--------------|
| Metasploit | pentesting, exploit |
| Nmap | networking, scanning |
| Nessus | report, vulnerability |
| Wireshark | forensics, pcap |
| Snort | ids, alerting |

## Governance
Naming conventions, tagging rules, and documentation requirements:
- Keep names descriptive and consistent.
- Include installation/usage/evidence where relevant.
- Prefer small, focused notes linked into hubs.

