# 🔄 Workflow Index

**Vault:** OffsecDEV_Root  
**Author:** Josh  
**Purpose:** Central repository of operational, analytical, and administrative workflows within the OffsecDEV ecosystem.  
**Last Updated:** {{date}}

---

## 🧭 Overview

Workflows define **how** tasks are performed — step-by-step, repeatable methods used throughout your campaigns, research, or maintenance tasks.  
This file acts as your master directory for all procedural documents, lab sequences, and automation scripts.

Use this index to:
- Standardize repeatable actions  
- Quickly recall tool usage sequences  
- Map dependencies between tools, vulnerabilities, and reports  
- Enable faster onboarding or task recovery  

---

## 🧩 Workflow Categories

| Category | Description | Example Tags |
|-----------|--------------|---------------|
| 🧱 **Infrastructure** | Network, system, and environment setup | `#networking`, `#docker`, `#cloud` |
| 🧠 **Offensive / Red Team** | Recon, exploitation, privilege escalation | `#pentesting`, `#metasploit`, `#nmap` |
| 🛡️ **Defensive / Blue Team** | Detection, analysis, and alert tuning | `#forensics`, `#snort`, `#ids` |
| 🧾 **Reporting / Documentation** | Reporting, tagging, syncing, and archival | `#report`, `#reference`, `#template` |
| ⚙️ **Automation / Scripts** | PowerShell, Python, or scheduled processes | `#automation`, `#scripting`, `#packages` |

---

## 🧰 Workflow Template

> Use this format when creating new workflow notes (e.g., `Recon_Workflow.md`, `Exploit_Workflow.md`, etc.)

```markdown
# 🔄 Workflow: <Title>

**Domain:** (e.g., Pentesting / Analysis / Reporting)  
**Created:** {{date}}  
**Tags:** [#workflow, #pentesting, #tool]  
**Status:** Active / Archived  

---

## 🎯 Objective
(Define the workflow’s purpose and expected outcome.)

---

## 🧱 Prerequisites
- Tools required: [[Tool Index]]  
- Environment setup: [[Networking_Hub]] / [[Docker_Hub]]  
- Permissions / Access:  

---

## ⚙️ Procedure
1.  
2.  
3.  

---

## 🧠 Notes / Observations
-  
-  

---

## 🧾 Evidence / Output
- File path: `/Evidence/Workflows/<Name>/`
- Logs or screenshots:  

---

## 🧰 Related Tools
[[Metasploit_Note]] | [[Nmap_Note]] | [[Wireshark_Note]]

---

## 🧩 Related Vulnerabilities
[[Vulnerability Index]]

---

## 📘 References
- External guide or article:  
- Internal report:  

---

## ✅ Completion
**Success Criteria:**  
- [ ] Objective achieved  
- [ ] Data stored in Evidence folder  
- [ ] Report updated  
```

---

## 🧠 Core Operational Workflows

| Workflow | Description | Link | Tags |
|-----------|--------------|------|------|
| Reconnaissance | Host discovery and enumeration | [[Recon_Workflow]] | `#pentesting`, `#nmap` |
| Exploitation | Targeted vulnerability exploitation | [[Exploit_Workflow]] | `#pentesting`, `#metasploit` |
| Post-Exploitation | Privilege escalation, pivoting, and persistence | [[Post_Exploitation_Workflow]] | `#pentesting`, `#access` |
| Log Analysis | Parsing and correlating alerts | [[Forensic_Analysis_Workflow]] | `#forensics`, `#ids` |
| Report Generation | Markdown or export automation | [[Reporting_Workflow]] | `#report`, `#template` |
| Evidence Sync | File organization and sync automation | [[Evidence_Workflow]] | `#workflow`, `#sync` |

```dataview
TABLE file.name AS "Workflows", file.mtime AS "Updated", tags
FROM "Notes"
WHERE contains(tags, "#workflow")
SORT file.mtime DESC
```

---

## ⚙️ Automation Workflows

| Script / Tool | Purpose | Note Link |
|----------------|----------|-----------|
| **Sync Script** | Sync vault between local and OneDrive | [[Scripts/sync_offsecdev.ps1]] |
| **Automation Hub** | Reference for PowerShell / Python scripts | [[Scripts_Hub]] |
| **Scheduled Tasks** | Task Scheduler XML or Windows scripts | [[Automation_Workflow]] |

---

## 🧰 Reporting Workflows

| Workflow | Description | Tags |
|-----------|--------------|------|
| Report Assembly | Combine findings and metadata into export | `#report`, `#template` |
| Evidence Archival | Structure data by campaign or system | `#evidence`, `#workflow` |
| Tag Maintenance | Update vault taxonomy after campaign | `#core`, `#tags` |

```dataview
TABLE file.name AS "Reporting Workflows", file.mtime AS "Updated"
FROM "Notes"
WHERE any(contains(tags, "#report"), contains(tags, "#reference"))
SORT file.mtime DESC
```

---

## 🧱 Infrastructure Workflows

| Workflow | Description | Tags |
|-----------|--------------|------|
| Network Build | Create and segment lab environments | `#networking`, `#docker` |
| IDS Deployment | Configure and validate detection | `#snort`, `#nids` |
| Firewall Ruleset Update | Apply and test security policy changes | `#firewall`, `#config` |

---

## 🧩 Linked Indices

| Index | Purpose | Link |
|--------|----------|------|
| [[Master Index]] | Global vault map |
| [[Tool Index]] | Operational tools reference |
| [[Vulnerability Index]] | Vulnerability catalog |
| [[Tags/index]] | Tag dictionary |
| [[Tags/Taxonomy Reference]] | Structural hierarchy and relationships |

---

## 🧠 Workflow Governance

**Naming Convention:**  
`<Action>_Workflow.md`  
Examples:  
- `Recon_Workflow.md`  
- `Exploit_Workflow.md`  
- `Report_Workflow.md`  

**Tagging Convention:**  
All workflow notes must include:
```yaml
---
tags: [#workflow, #core]
status: active
---
```

**Version Control:**  
- Each change should include date/version header.  
- Use `status: archived` when deprecated.  
- Cross-link any affected scripts or tools.  

---

## 🧩 Dataview Summary

```dataview
TABLE file.name AS "Workflow", file.folder AS "Path", file.mtime AS "Last Updated"
FROM "Notes"
WHERE contains(tags, "#workflow")
SORT file.mtime DESC
```

---

## 🧭 Expansion Workflow

When creating a new workflow:
1. Duplicate from the **Workflow Template**.  
2. Add domain and context tags.  
3. Link to relevant tools and vulnerabilities.  
4. Store outputs in `/Evidence/Workflows/<Name>/`.  
5. Update this index and verify it appears in the Dataview dashboard.  

---

## 📜 Summary

The **Workflows Index** defines the procedural architecture of OffsecDEV.  
It ensures every recurring process — technical, administrative, or analytical — is documented, versioned, and connected to the vault’s taxonomy.

> “A workflow written once saves a hundred hours later.”  
> — OffsecDEV Principle

---

**End of Workflows Index**
