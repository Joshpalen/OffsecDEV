# 🏷️ Tag Index

**Vault:** OffsecDEV_Root  
**Author:** Josh  
**Purpose:** Central taxonomy and tag reference for the entire vault.  
**Last Updated:** {{date}}

---

## 🧭 Overview

This file defines and standardizes **all tags** used throughout the vault.  
Tags are used to interlink notes, organize topics, and fuel Dataview queries for dynamic navigation.  
Each section below lists the tag’s **meaning**, **scope**, and an optional **Dataview query example**.

---

## 🧩 Core Structural Tags

| Tag | Purpose |
|-----|----------|
| `#reference` | External documentation, guides, cheat sheets |
| `#template` | Note or file template for reuse |
| `#report` | Formal deliverable or campaign output |
| `#evidence` | Screenshots, logs, pcaps, forensic data |
| `#log` | Lab or operational activity record |
| `#concept` | Theoretical or design-level notes |
| `#workflow` | Process or procedure documentation |
| `#project` | Active campaigns or major efforts |
| `#archive` | Completed or deprecated content |

**Example Dataview**
```dataview
TABLE file.name AS "Reference Files"
FROM ""
WHERE contains(tags, "#reference")
SORT file.name ASC
```

---

## 🧠 Domain / Subject Tags

| Tag | Domain Area |
|-----|--------------|
| `#networking` | Subnets, routing, VLANs, packet analysis |
| `#pentesting` | Exploitation, recon, payloads, red teaming |
| `#osint` | Open-source intelligence, recon collection |
| `#forensics` | Evidence analysis, triage, incident response |
| `#malware` | Reverse engineering, signatures, samples |
| `#cryptography` | Encryption, hashing, key management |
| `#scripting` | Code snippets and automation (Python, Bash, etc.) |
| `#firewall` | ACLs, rules, security zoning |
| `#ids` | IDS/IPS systems (Snort, Suricata, Zeek) |
| `#docker` | Container builds, orchestration |
| `#cloud` | AWS, Azure, GCP configuration and notes |
| `#linux` | Configs, shell, packages, hardening |
| `#windows` | Registry, PowerShell, event logs |
| `#ai` | Artificial intelligence or automation usage |
| `#education` | Learning resources, reading, courses |

**Example Dataview**
```dataview
TABLE file.name AS "Pentesting Notes", file.folder AS "Path"
FROM ""
WHERE contains(tags, "#pentesting")
SORT file.name ASC
```

---

## ⚙️ Tool-Specific Tags

| Tag | Tool |
|-----|------|
| `#metasploit` | Exploitation framework notes |
| `#nessus` | Vulnerability scanner results |
| `#nmap` | Network scanning and discovery |
| `#wireshark` | Packet capture analysis |
| `#snort` | Intrusion detection rules / alerts |
| `#zsh` | Shell configuration and customization |
| `#obsidian` | Vault, plugin, and workflow notes |
| `#nids` | Network intrusion detection systems |
| `#acid` | Alert correlation / incident dissemination |
| `#firewall` | Security zones and rulebases |
| `#packages` | OS / language package management |
| `#dockerfile` | Docker builds and syntax |

**Example Dataview**
```dataview
TABLE file.name AS "Tool Notes", file.path AS "Location"
FROM ""
WHERE any(contains(tags, "#metasploit"), contains(tags, "#nmap"), contains(tags, "#wireshark"))
SORT file.mtime DESC
```

---

## 🧱 Meta-Organizational Tags

| Tag | Purpose |
|-----|----------|
| `#priority/high` | Needs attention or review soon |
| `#pending` | Work in progress, not finalized |
| `#todo` | Tasks to complete |
| `#complete` | Finished and reviewed |
| `#core` | Foundational to vault structure |

**Example Dataview**
```dataview
TASK
FROM ""
WHERE contains(tags, "#todo") OR contains(tags, "#pending")
SORT file.name ASC
```

---

## 🧩 Usage Convention

- Tags appear in front-matter for all notes:
  ```yaml
  ---
  tags: [#tool, #pentesting, #core]
  aliases: [nmap, recon]
  ---
  ```

- Inline tags can also be used for quick linking:  
  `The results were validated using [[Nmap_Note]] #pentesting #tool`

---

## 📊 Suggested Folder Integration

| Folder | Example Tags |
|---------|---------------|
| `/Reports/` | `#report`, `#project`, `#evidence` |
| `/Templates/` | `#template`, `#reference` |
| `/Notes/` | `#log`, `#concept`, `#workflow` |
| `/Tags/` | `#core`, `#reference` |
| `/Evidence/` | `#evidence` |

---

## 🧠 Tag Governance

**Purpose:**  
To prevent tag sprawl and maintain consistency across the vault.

**Rules:**
1. Always use lowercase tags (except hierarchical tags like `#priority/high`).  
2. Keep tags short, semantic, and re-usable.  
3. Add new tags only if existing ones don’t capture meaning.  
4. Update this file whenever a new tag is introduced.  

---

## 🧭 Future Enhancements
- Add Dataview dashboards per domain (`Pentesting_Index.md`, `Networking_Index.md`)  
- Auto-generate tag summary tables using Templater scripts  
- Implement color-coded tag CSS snippets in Obsidian for visual clusters  

---

**End of Index**
