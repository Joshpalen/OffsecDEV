# ⚙️ Tool Index

**Vault:** OffsecDEV_Root  
**Author:** Josh  
**Purpose:** Master reference for all operational tools used within the OffsecDEV environment — offensive, defensive, analytical, and administrative.  
**Last Updated:** {{date}}

---

## 🧭 Overview

This index catalogs all tools referenced across the vault.  
Each entry links to its detailed note, key usage context, and related workflows.  
Use this file to quickly navigate, audit, or update your toolkit.

---

## 🧩 Tool Taxonomy

| Category | Description | Example Tags |
|-----------|--------------|---------------|
| 🛠️ **Offensive** | Exploitation and post-exploitation frameworks | `#metasploit`, `#nmap` |
| 🧱 **Defensive / Monitoring** | IDS, firewalls, analysis tools | `#snort`, `#wireshark`, `#nids` |
| 🔍 **Scanning / Assessment** | Discovery and vulnerability scanning | `#nessus`, `#nmap` |
| 🧰 **Automation / Scripting** | Custom scripting and configuration | `#zsh`, `#docker`, `#packages` |
| 🧾 **Documentation / Organization** | Vault and Obsidian workflows | `#obsidian` |

---

## 🛠️ Offensive Security Tools

| Tool | Description | Note Link | Tag |
|------|--------------|-----------|------|
| **Metasploit Framework** | Exploitation and post-exploitation suite | [[Metasploit_Note]] | `#metasploit` |
| **Nmap** | Network discovery and port scanning | [[Nmap_Note]] | `#nmap` |
| **Nessus** | Vulnerability assessment and reporting | [[Nessus_Note]] | `#nessus` |

```dataview
TABLE file.name AS "Offensive Tools", file.mtime AS "Updated"
FROM "Notes"
WHERE any(contains(tags, "#metasploit"), contains(tags, "#nessus"), contains(tags, "#nmap"))
SORT file.mtime DESC
```

---

## 🧱 Defensive & Monitoring Tools

| Tool | Description | Note Link | Tag |
|------|--------------|-----------|------|
| **Wireshark** | Packet analysis and network forensics | [[Wireshark_Note]] | `#wireshark` |
| **Snort** | Intrusion detection and traffic monitoring | [[Snort_Note]] | `#snort` |
| **NIDS / ACID** | Detection and alert correlation systems | [[NIDS_Note]], [[ACID_Note]] | `#nids`, `#acid` |
| **Firewall Management** | Ruleset configuration and logging | [[Firewall_Note]] | `#firewall` |

```dataview
TABLE file.name AS "Defensive Tools", file.folder AS "Location"
FROM "Notes"
WHERE any(contains(tags, "#snort"), contains(tags, "#wireshark"), contains(tags, "#nids"), contains(tags, "#firewall"))
SORT file.mtime DESC
```

---

## 🧰 Automation & Environment Tools

| Tool | Description | Note Link | Tag |
|------|--------------|-----------|------|
| **Zsh** | Shell environment customization | [[Zsh_Note]] | `#zsh` |
| **Dockerfile / Docker** | Container builds and deployment | [[Dockerfile_Note]] | `#dockerfile` |
| **Packages** | Package tracking and management | [[Packages_Note]] | `#packages` |

```dataview
TABLE file.name AS "Automation Tools", file.mtime AS "Updated"
FROM "Notes"
WHERE any(contains(tags, "#zsh"), contains(tags, "#dockerfile"), contains(tags, "#packages"))
SORT file.mtime DESC
```

---

## 🧾 Documentation & Workflow Tools

| Tool | Description | Note Link | Tag |
|------|--------------|-----------|------|
| **Obsidian** | Vault management, templates, plugins, workflows | [[Obsidian_Note]] | `#obsidian` |
| **General Reading / Reference** | Used for research and document tracking | [[Reading Log]], [[General_Reading_Note]] | `#reference`, `#education` |

```dataview
TABLE file.name AS "Documentation Tools", file.mtime AS "Updated"
FROM "Notes"
WHERE contains(tags, "#obsidian")
SORT file.mtime DESC
```

---

## 🧩 Tool Relationships

| Tool | Related Tags | Linked Notes |
|------|---------------|--------------|
| Metasploit | `#pentesting`, `#exploitation`, `#tool` | [[Metasploit_Note]], [[Pentesting_Hub]] |
| Nmap | `#networking`, `#scanning`, `#tool` | [[Nmap_Note]], [[Networking_Hub]] |
| Nessus | `#report`, `#vulnerability`, `#assessment` | [[Nessus_Note]], [[Reports_Hub]] |
| Wireshark | `#forensics`, `#pcap`, `#analysis` | [[Wireshark_Note]], [[Evidence_Hub]] |
| Snort | `#ids`, `#alerting`, `#defense` | [[Snort_Note]], [[NIDS_Hub]] |
| Docker | `#automation`, `#devops`, `#container` | [[Dockerfile_Note]], [[Scripting_Hub]] |
| Zsh | `#automation`, `#shell`, `#environment` | [[Zsh_Note]] |

---

## 🧠 Integration with Core Indices

| Index | Description | Link |
|--------|--------------|------|
| 🏷️ **Tag Index** | Full tag dictionary | [[Tags/index]] |
| 🧬 **Taxonomy Reference** | Tag relationships and hierarchy | [[Tags/Taxonomy Reference]] |
| 🧭 **Master Index** | Global vault navigation | [[Master Index]] |
| 🧰 **Scripts_Hub** | PowerShell and Python automation scripts | [[Scripts_Hub]] |

---

## 🧩 Expansion Workflow

When adding a new tool:
1. Create a note using the **Tool_Note Template** (based on your standardized format).  
2. Tag appropriately (e.g., `#tool`, `#pentesting`, `#automation`).  
3. Add it to this index under the correct category.  
4. Update the `Tool Relationships` table if it connects to another hub.  
5. Cross-link from `Master Index.md`.

---

## 🧾 Dataview Master Query

```dataview
TABLE file.name AS "Tool Notes", file.folder AS "Path", file.mtime AS "Updated"
FROM "Notes"
WHERE contains(tags, "#tool")
SORT file.mtime DESC
```

---

## 🧠 Tool Governance

**Naming Convention:**  
Each tool note follows:  
`<ToolName>_Note.md` (e.g., `Metasploit_Note.md`, `Wireshark_Note.md`)

**Tagging Convention:**  
All tool notes must include:
```yaml
---
tags: [#tool, #core, #pentesting]
status: active
---
```

**Documentation Rule:**  
Include at least:
- Installation method  
- Usage examples  
- Related configurations  
- Evidence or log references (if applicable)

---

## 🧩 Future Additions

| Tool | Planned Focus | Tag |
|------|----------------|------|
| Burp Suite | Web proxy and testing | `#burp` |
| Suricata | Advanced NIDS/IPS | `#suricata` |
| Zeek | Network analysis and telemetry | `#zeek` |
| Git | Version control and automation | `#git` |
| Python | Scripting and automation core | `#python` |

---

## 🧰 Command Reference (PowerShell)

| Task | Command |
|------|----------|
| Sync vault to OneDrive | `C:\Users\joshp\Scripts\sync_offsecdev.ps1 -Execute` |
| List all tool notes | `Get-ChildItem -Recurse | Select-String "#tool"` |
| Search by tag | `grep -r "#metasploit" *` |
| Export tool summary | `grep -r "## Summary" * > Tool_Summary.txt` |

---

## 🧭 Summary

The **Tool Index** forms the operational layer of your OffsecDEV taxonomy.  
Every tool here links outward to:
- Its **domain hub** (`Pentesting_Hub`, `Networking_Hub`, etc.)  
- Its **evidence and reports**  
- The **taxonomy logic** under `/Tags/`

This ensures all tooling activity is traceable, documented, and connected to your wider system.

---

**End of Tool Index**
