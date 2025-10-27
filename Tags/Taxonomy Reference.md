# 🧬 Taxonomy Reference

**Vault:** OffsecDEV_Root  
**Author:** Josh  
**Purpose:** Defines the conceptual structure, relationships, and metadata schema of the OffsecDEV vault.  
**Last Updated:** {{date}}

---

## 🧭 Overview

This document describes how information is categorized, related, and retrieved within the vault.  
It complements the `index.md` tag reference by explaining *why* tags exist, *how* they interconnect, and *what metadata structure* governs content relationships.

The goal is to maintain a **semantic, scalable knowledge graph** for all projects, reports, tools, and references.

---

## 🧱 Hierarchical Model

The vault’s taxonomy follows a **three-tiered hierarchy**:

| Tier | Purpose | Example |
|------|----------|---------|
| **1️⃣ Core Layer** | Universal foundations used across all content | `#core`, `#reference`, `#template` |
| **2️⃣ Domain Layer** | Subject matter categories (security, networking, scripting, etc.) | `#pentesting`, `#networking`, `#scripting` |
| **3️⃣ Context Layer** | Contextual or situational metadata (tools, systems, states) | `#metasploit`, `#firewall`, `#pending`, `#complete` |

Each new note should align with one tag from each relevant tier where possible.  
This keeps semantic linking consistent across the vault.

---

## 🧩 Tag Relationships

### 🔗 Core Relationships
| Relation | Example | Meaning |
|-----------|----------|---------|
| `#project → #report` | “Project produces a report” | Work-product relationship |
| `#report → #evidence` | “Report is backed by evidence” | Supporting data |
| `#workflow → #tool` | “Workflow uses tool” | Operational dependency |
| `#concept → #reference` | “Concept explained by reference” | Theoretical link |
| `#template → #report` | “Report follows template” | Structural inheritance |

---

## 🧠 Semantic Clusters

### 🛡️ **Security Cluster**
`#pentesting` ↔ `#networking` ↔ `#firewall` ↔ `#ids` ↔ `#nids`

**Core relationship:**
Security testing → network surface → detection → alerting → analysis

### ⚙️ **Tooling Cluster**
`#tool` ↔ `#metasploit` ↔ `#nmap` ↔ `#nessus` ↔ `#wireshark` ↔ `#snort`

**Core relationship:**
Tool is subtype of `#tool` tag, inheriting its attributes in semantic queries.

### 🧰 **Automation / Development Cluster**
`#scripting` ↔ `#python` ↔ `#bash` ↔ `#powershell` ↔ `#docker` ↔ `#packages`

**Core relationship:**
Automation and development environment cohesion.

### 🧱 **Infrastructure Cluster**
`#networking` ↔ `#firewall` ↔ `#ids` ↔ `#cloud` ↔ `#docker`

**Core relationship:**
Stack-level correlation — from local host configs to distributed containerized environments.

---

## 🗂️ Folder-to-Tag Mapping

| Folder | Default Tags | Purpose |
|---------|--------------|----------|
| `/Reports/` | `#report`, `#evidence` | Deliverables and supporting proof |
| `/Templates/` | `#template`, `#reference` | Base markdown structures |
| `/Tags/` | `#core`, `#reference` | Taxonomic and organizational metadata |
| `/Notes/` | `#concept`, `#log`, `#workflow` | Active thinking and technical logs |
| `/Evidence/` | `#evidence`, `#forensics` | Captures, PCAPs, logs, screenshots |

---

## 🧩 Metadata Standards

Each note should include standardized **YAML frontmatter** for alignment and automation:

```yaml
---
tags: [#pentesting, #tool, #metasploit]
aliases: [msfconsole, exploit framework]
created: {{date}}
modified: {{date}}
author: Josh
status: active
---
```

**Metadata Keys**
| Key | Purpose |
|-----|----------|
| `tags` | Define semantic relationships |
| `aliases` | Alternate identifiers for link discovery |
| `created` / `modified` | Audit trail for versioning |
| `author` | Ownership metadata |
| `status` | One of: `active`, `pending`, `complete`, `archived` |

---

## 🧭 Cross-Linking Strategy

- Use **wikilinks** (`[[NoteName]]`) to connect between related notes.
- Each domain should have a **Hub or MOC** file (e.g., `Pentesting_Hub.md`, `Networking_Hub.md`).
- Every Hub lists its subordinate notes automatically via Dataview.

**Example:**
```dataview
TABLE file.name AS "Pentesting Files"
FROM "Notes"
WHERE contains(tags, "#pentesting")
SORT file.mtime DESC
```

---

## 🧱 Dataview Integration

To visualize taxonomy and tag relationships, embed queries like these:

### Domain Breakdown
```dataview
TABLE length(file.tags) AS "Tag Count"
FROM ""
GROUP BY file.folder
SORT Tag Count DESC
```

### Active Projects
```dataview
TABLE file.name AS "Active Projects", file.mtime AS "Last Updated"
WHERE contains(tags, "#project") AND status = "active"
SORT file.mtime DESC
```

### Cross-Link Summary
```dataview
TABLE file.inlinks AS "Linked From", file.outlinks AS "Linked To"
FROM ""
WHERE contains(tags, "#core")
```

---

## 🧩 Expansion Guidelines

**When adding new tags:**
1. Confirm it doesn’t already exist under another synonym.  
2. Define its meaning here in the taxonomy or in `/Tags/index.md`.  
3. Tag at least **one Core**, **one Domain**, and **one Context** type per new note.

**When adding new folders:**
1. Assign a default tag for automation and filtering.  
2. Update the Folder-to-Tag mapping above.  

---

## 🧠 Semantic Principles

- **Atomic Notes:** Each note should represent one primary concept or asset.  
- **Contextual Linking:** Use tags for classification, links for relationships.  
- **Bidirectional Structure:** Every Hub or index should link both *upstream* (to parent domains) and *downstream* (to sub-notes).  
- **Progressive Granularity:** Broader topics connect to specific instances (e.g., `#pentesting` → `#metasploit` → `#exploit`).  

---

## 🧩 Future Taxonomic Layers

| Future Layer | Purpose |
|---------------|----------|
| **#incident** | Map IR data into the knowledge base |
| **#ioc** | Track indicators of compromise |
| **#mitre** | ATT&CK framework mapping |
| **#compliance** | Regulatory frameworks and policies |
| **#asset** | Systems or hosts under test |
| **#vulnerability** | Discovered flaws or exposures |

---

## 📜 Summary

The **Taxonomy Reference** and **Tag Index** together define:

- **What** exists → (`index.md`)
- **Why** and **How** it connects → (`Taxonomy Reference.md`)

They form the *knowledge schema* for OffsecDEV — every note, tag, or folder ultimately maps back to this document.

---

**End of File**
