---
title: "Tag Index"
tags: [core, index]
cssclass: cs-note
---

# Tag Index

Purpose: central taxonomy and tag reference for the vault.

## Core Structural Tags
| Tag | Purpose |
|-----|---------|
| `#reference` | External docs, guides, cheat sheets |
| `#template` | Reusable note templates |
| `#report` | Formal deliverables |
| `#evidence` | Screenshots, logs, pcaps |
| `#log` | Lab or operational record |
| `#concept` | Theory or design notes |
| `#workflow` | Processes and procedures |
| `#project` | Active campaigns or efforts |
| `#archive` | Completed or deprecated items |

## Domain / Subject Tags
| Tag | Domain |
|-----|--------|
| `#networking` | Subnets, routing, packet analysis |
| `#pentesting` | Exploitation, recon, payloads |
| `#osint` | Open-source intelligence |
| `#forensics` | Evidence analysis, incident response |
| `#malware` | Reverse engineering, signatures, samples |
| `#cryptography` | Encryption, hashing, keys |
| `#scripting` | Python, Bash, PowerShell |
| `#firewall` | ACLs, rules, segmentation |
| `#ids` | IDS/IPS systems |
| `#docker` | Containers and orchestration |
| `#cloud` | AWS, Azure, GCP |
| `#linux` | Shell, packages, hardening |
| `#windows` | PowerShell, registry |
| `#ai` | AI, LLMs, automation |
| `#education` | Learning, courses, reading |

## Tool-Specific Tags
| Tag | Tool |
|-----|------|
| `#metasploit` | Metasploit |
| `#nessus` | Nessus |
| `#nmap` | Nmap |
| `#wireshark` | Wireshark |
| `#snort` | Snort |
| `#zsh` | Zsh |
| `#obsidian` | Obsidian |
| `#nids` | NIDS |
| `#acid` | ACID |
| `#packages` | Package management |
| `#dockerfile` | Docker builds |

## Meta-Organisational Tags
| Tag | Purpose |
|-----|---------|
| `#priority/high` | Needs attention soon |
| `#pending` | Work in progress |
| `#todo` | Tasks to complete |
| `#complete` | Finished items |
| `#core` | Foundational structure |

## Usage
- Prefer frontmatter tags for consistency:
```yaml
---
tags: [tool, pentesting, core]
---
```
- Inline tags are fine for quick linking.

## Suggested Folder Integration
| Folder | Example Tags |
|--------|--------------|
| `/Reports/` | `#report`, `#project`, `#evidence` |
| `/Templates/` | `#template`, `#reference` |
| `/Notes/` | `#log`, `#concept`, `#workflow` |
| `/Tags/` | `#core`, `#reference` |
| `/Evidence/` | `#evidence` |

## Tag Governance
Rules to prevent tag sprawl:
1. Use lowercase where possible (except hierarchical tags like `#priority/high`).
2. Keep tags short and meaningful.
3. Add tags only when existing ones do not fit.
4. Update this index when introducing new tags.
