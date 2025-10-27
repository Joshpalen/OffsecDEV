# 🧭 Master Index

**Vault:** OffsecDEV_Root  
**Author:** Josh  
**Purpose:** Root navigation hub for the entire OffsecDEV Vault — linking domains, tools, tags, templates, and active projects.  
**Last Updated:** {{date}}

---

## 🌌 Overview

This is the **central Map of Content (MOC)** for the OffsecDEV Knowledge System.  
Every section below acts as a hub connecting to relevant folders, tag groups, and Dataview dashboards.

Use this file as the **entry point** for navigation and knowledge graph expansion.

---

## 🧱 Core Navigation

| Category | Description | Link |
|-----------|--------------|------|
| 🧩 **Tag Index** | Complete reference of all tags | [[Tags/index]] |
| 🧬 **Taxonomy Reference** | Relationships & hierarchy between tags | [[Tags/Taxonomy Reference]] |
| 🗺️ **Core Map** | Visual overview of all active domain hubs | [[Core_Map]] |
| 🧠 **Templates** | Predefined note structures | [[Templates_Hub]] |
| 📊 **Reports** | Finished deliverables and findings | [[Reports_Hub]] |
| ⚙️ **Tools** | Operational toolset notes (Metasploit, Nmap, etc.) | [[Tools_Hub]] |
| 🧾 **Evidence** | Captures, PCAPs, logs, and screenshots | [[Evidence_Hub]] |
| 🧰 **Scripts** | Automation and custom code snippets | [[Scripts_Hub]] |

---

## 🧩 System Overview Map

```dataview
TABLE file.name AS "Core Files", file.folder AS "Location", file.mtime AS "Last Updated"
FROM ""
WHERE contains(tags, "#core")
SORT file.mtime DESC
```

---

## 🧠 Knowledge Domains

### 🛡️ Security & Offensive Operations
| Hub | Description |
|-----|--------------|
| [[Pentesting_Hub]] | Exploitation, payloads, and red-team ops |
| [[Networking_Hub]] | Protocols, routing, VLANs, and traffic analysis |
| [[Forensics_Hub]] | Incident response and evidence analysis |
| [[Malware_Hub]] | Reverse engineering, signatures, and behavioral study |
| [[Cryptography_Hub]] | Encryption, key management, and integrity systems |

```dataview
TABLE file.name AS "Security Notes"
FROM "Notes"
WHERE any(contains(tags, "#pentesting"), contains(tags, "#forensics"), contains(tags, "#networking"))
SORT file.mtime DESC
```

---

### ⚙️ Automation, Dev, & Systems
| Hub | Description |
|-----|--------------|
| [[Scripting_Hub]] | Python, Bash, PowerShell, automation workflows |
| [[Docker_Hub]] | Containerization, builds, and DevOps |
| [[Cloud_Hub]] | AWS, Azure, GCP configurations |
| [[Packages_Hub]] | Dependency management and package tracking |

```dataview
TABLE file.name AS "Automation Notes"
FROM "Notes"
WHERE any(contains(tags, "#scripting"), contains(tags, "#docker"), contains(tags, "#packages"))
SORT file.mtime DESC
```

---

### 🧰 Tools & Utilities
| Tool | Description | Link |
|------|--------------|------|
| Metasploit | Exploitation framework | [[Metasploit_Note]] |
| Nessus | Vulnerability scanning | [[Nessus_Note]] |
| Nmap | Network mapping and service discovery | [[Nmap_Note]] |
| Wireshark | Packet analysis | [[Wireshark_Note]] |
| Snort | Intrusion detection system | [[Snort_Note]] |
| Zsh | Shell and automation environment | [[Zsh_Note]] |
| Obsidian | Vault structure and configuration | [[Obsidian_Note]] |
| Dockerfile | Container build reference | [[Dockerfile_Note]] |

```dataview
TABLE file.name AS "Tool Notes"
FROM "Notes"
WHERE contains(tags, "#tool")
SORT file.mtime DESC
```

---

### 🔥 Infrastructure & Defense
| Hub | Description |
|-----|--------------|
| [[Firewall_Hub]] | Policy, ACL, and segmentation documentation |
| [[NIDS_Hub]] | Network intrusion detection systems and alerts |
| [[ACID_Hub]] | Alert correlation and dissemination |
| [[Networking_Hub]] | Physical and logical topology reference |

```dataview
TABLE file.name AS "Infra Notes"
FROM "Notes"
WHERE any(contains(tags, "#firewall"), contains(tags, "#ids"), contains(tags, "#nids"))
SORT file.mtime DESC
```

---

## 🗂️ Operational Areas

| Category | Description | Folder |
|-----------|--------------|--------|
| 🧩 Templates | Reusable formats for reports, notes, and logs | `/Templates` |
| 🧾 Reports | Campaign or assessment results | `/Reports` |
| 🧠 Notes | Working material and research | `/Notes` |
| 🧰 Evidence | Collected logs, captures, screenshots | `/Evidence` |
| 🧱 Tags | Metadata, structure, and vault governance | `/Tags` |
| 🧩 Scripts | PowerShell / Python automation | `/Scripts` |

---

## 🧭 Status Overview

```dataview
TABLE file.name AS "Active Work", status, file.mtime AS "Updated"
FROM ""
WHERE status != "archived" AND (contains(tags, "#project") OR contains(tags, "#report"))
SORT file.mtime DESC
```

---

## 🧠 Tag Clusters

| Cluster | Linked Tags |
|----------|--------------|
| 🛡️ Security | `#pentesting`, `#forensics`, `#networking`, `#malware` |
| ⚙️ Automation | `#scripting`, `#docker`, `#packages`, `#cloud` |
| 🧰 Tools | `#metasploit`, `#nmap`, `#wireshark`, `#nessus`, `#snort` |
| 🔥 Defense | `#firewall`, `#nids`, `#ids`, `#acid` |
| 🧩 Structure | `#core`, `#template`, `#reference`, `#workflow` |

---

## 🧩 Quick Access Queries

### 🔎 Recent Updates
```dataview
TABLE file.name AS "Recent Notes", file.folder AS "Location", file.mtime AS "Updated"
FROM ""
SORT file.mtime DESC
LIMIT 15
```

### 🧾 Pending Items
```dataview
TASK
FROM ""
WHERE contains(tags, "#pending") OR contains(tags, "#todo")
SORT file.mtime DESC
```

### 📚 Reading Queue
```dataview
TABLE file.name AS "Reading Materials", file.mtime AS "Added"
FROM "Notes"
WHERE contains(tags, "#education") OR contains(tags, "#reference")
SORT file.mtime DESC
```

---

## 🧠 Governance Reference

| Document | Purpose |
|-----------|----------|
| [[Tags/index]] | Tag dictionary and definitions |
| [[Tags/Taxonomy Reference]] | Hierarchy and relationships |
| [[Core_Map]] | Visual MOC linking all domains |
| [[General_Reading_Note]] | Template for study materials |
| [[Templates_Hub]] | All reusable note formats |

---

## 🧩 Maintenance Commands (Windows / PowerShell)

| Action | Command |
|--------|----------|
| Sync local → OneDrive | `C:\Users\joshp\Scripts\sync_offsecdev.ps1 -Execute` |
| Dry-run sync | `C:\Users\joshp\Scripts\sync_offsecdev.ps1` |
| Export Vault | `robocopy "C:\OffsecDEV\OffsecDEV_Root" "D:\Vault_Backup" /MIR` |
| Search Notes by Tag | `Get-ChildItem -Recurse | Select-String "#pentesting"` |

---

## 🧱 Core Philosophy

> “Structure enables discovery.  
> Discovery builds intelligence.  
> Intelligence empowers execution.”  
> — OffsecDEV Vault Principle

This vault is designed to evolve:  
- **Tags** define context  
- **Hubs** organize scope  
- **Dataview** generates dynamic connections  
- **This index** unifies them all

---

**End of Master Index**
