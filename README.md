# OffsecDEV — Obsidian Pentesting Vault

[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-483699?logo=obsidian&logoColor=white)](#)
[![Beginner Friendly](https://img.shields.io/badge/Beginner_Friendly-Yes-brightgreen)](#)
[![Focus](https://img.shields.io/badge/Focus-Pentesting_%26_Operations-red)](#)

A complete, opinionated Obsidian knowledge system for offensive security, networking, and automation. It’s built to guide beginners while staying useful for real assessments.

- Central Map-of-Content hubs that tie everything together
- Production-ready templates for tools, workflows, vulnerabilities, and reports
- Automation for evidence collection and campaign organization
- Works with Obsidian community plugins (Dataview, Templater)

> Goal: Turn scattered learning and ad-hoc notes into a coherent, searchable operational knowledge system you can actually run campaigns with.

---

## Quickstart

1) Install Obsidian and enable community plugins (Settings → Community Plugins)
- Required: Dataview, Templater
- Recommended: QuickAdd, Advanced Canvas, Tag Wrangler, Tasks

2) Open this folder as a vault in Obsidian
- Clone or copy to a local path (e.g., `C:\OffsecDEV\OffsecDEV_Root`)
- In Obsidian: “Open folder as vault” → select the folder

3) Start at the hub
- Open `00_Index/Master Index.md`
- Explore the domain hubs (Pentesting, Networking, Forensics, etc.)

4) Create notes with templates
- Use Templater to instantiate items from the `Templates/` folder

See also: `00_Index/Getting_Started.md` for captures and shortcuts.

---

## Navigation: How This Vault Fits Together

This vault is organized around a small set of “hubs” and indices:

- Master Index (`00_Index/Master Index.md`) — Control tower with links to all hubs
- Domain hubs (`00_Index/*_Hub.md`) — Pentesting, Networking, Forensics, Malware, Crypto, Scripting, Docker, Cloud, Packages
- Tools Hub (`00_Index/Tools_Hub.md`) — All tooling and operator notes
- Reports Hub (`00_Index/Reports_Hub.md`) — Finished deliverables and campaign reports
- Scripts Hub (`00_Index/Scripts_Hub.md`) — Script notes and locations
- Evidence Hub (`00_Index/Evidence_Hub.md`) — Evidence manifests and indexes
- Courses/Study Hubs (`00_Index/Courses_Hub.md`) — Coursework dashboards & class notes
- Algorithms/Data Structures indices — CS learning indexes

Use the hubs + Dataview tables to surface “what matters now” automatically from note metadata.

---

## Core Ideas and Workflow

- Map-of-Content first: start at the Master Index; navigate into hubs and dashboards
- Templates everywhere: everything has a template so notes stay consistent
- Evidence is first-class: scripts normalize raw evidence into `Reports/<Campaign>/Evidence/`
- Metadata + queries: Dataview turns metadata into live dashboards
- Campaign-ready: structure mirrors Recon → Enumeration → Exploitation → Post-Exploitation → Reporting

---

## Learning and Development Flow

1) Study a topic using templates (Algorithms, Data Structures, Concept, Reading)
2) Practice with tool notes (Nmap, Metasploit, ffuf, Burp, etc.)
3) Run a practice campaign (see `Pentest Campaign/Reports/Example Campaign`)
4) Capture evidence with scripts and generate finding stubs from scans
5) Compile a final report from the report template

All steps are linked from the Master Index and domain hubs so you can move smoothly from study → practice → portfolio.

---

## Templates Overview

Programming & Systems
- Python (`Templates/Python.md`, `Templates/Python_Note.md`)
- JavaScript (`Templates/JavaScript.md`, `Templates/JavaScript_Note.md`)
- Java (`Templates/Java.md`, `Templates/Java_Note.md`)
- C# (`Templates/C_Sharp.md`, `Templates/C_Sharp_Note.md`)
- C++ (`Templates/C++.md`, `Templates/C++_Note.md`)
- Ruby (`Templates/Ruby.md`, `Templates/Ruby_Note.md`)
- Perl (`Templates/Perl.md`, `Templates/Perl_Note.md`)
- Zsh (`Templates/Zsh_Note.md`)
- Dockerfile (`Templates/Dockerfile.md`, `Templates/Dockerfile_Note.md`)

Pentesting Tools (operator notes)
- Metasploit (`Templates/Metasploit_Note.md`)
- Nmap (`Templates/Nmap_Note.md`)
- Wireshark (`Templates/Wireshark_Note.md`)
- Snort (`Templates/Snort_Note.md`)
- Burp Suite (`Templates/Burp_Suite_Note.md`)
- ffuf (`Templates/FFUF_Note.md`)
- gobuster (`Templates/Gobuster_Note.md`)
- nikto (`Templates/Nikto_Note.md`)
- hydra (`Templates/Hydra_Note.md`)
- John the Ripper (`Templates/John_The_Ripper_Note.md`)
- hashcat (`Templates/Hashcat_Note.md`)
- sqlmap (`Templates/SQLMap_Note.md`)

Reports & Operations
- Pentest report (`Templates/Pentest_Report_Template.md`)
- Finding template (`Pentest Campaign/Reports/Example Campaign/06-Reporting/Findings/Finding_Template.md`)
- Lab notes (`Templates/Lab Notes.md`)
- Exploit record (`Templates/Exploit_Template.md`)
- Flowcharts (`Templates/Flowchart_Template.md`)

Study & Organization
- Algorithm, Data Structure, Concept, Reading Summary, Exam Review
- Course overview & dashboard (`Templates/University Course Overview.md`, `Templates/Course_Dashboard.md`)
- General note (`Templates/All_Purpose_Note.md`), Links (`Templates/Links.md`)

---

## Automation: Evidence & Findings

Evidence archiver (copy or move) — normalizes and indexes raw artifacts
- PowerShell wrapper: `Pentest Campaign/Reports/Example Campaign/Scripts/Run_Evidence_Finder.ps1`
- Python core: `Automation/Scripts/se_evidence_finder_copy.py`

Generate finding stubs from scans
- Python: `Pentest Campaign/Reports/Example Campaign/Scripts/generate_findings.py`
- Bulk runner: `Pentest Campaign/Reports/Example Campaign/Scripts/Generate_Findings_From_Scans.ps1`
- Output: `06-Reporting/Findings/*.md` (ready for editing)

New Campaign scaffold
- PowerShell: `Automation/Scripts/new_campaign.ps1 -Name "My Campaign"`
- QuickAdd capture (creates Overview only): QuickAdd → “New Campaign (Overview)”

---

## Tags and Taxonomy

Consistent tags make Dataview dashboards work. See:
- Tag dictionary: `Tags/Index.md`
- Taxonomy reference: `Tags/Taxonomy Reference.md`

Use frontmatter tags like `pentesting`, `networking`, `tool`, `education`, `reading`, `vulnerability`, `workflow` to keep content discoverable. Course/class notes and Network+ Baseline are tagged to populate Courses Hub.

---

## Styling and Plugins

- CSS snippets are enabled (see `.obsidian/appearance.json`). New templates use `cssclass: cs-note` for consistent look-and-feel.

### Required & Recommended Plugins
- Required
  - Dataview: Query notes to build dashboards and tables
  - Templater: Generate consistent frontmatter and scaffolds
- Recommended
  - QuickAdd: Capture commands (config under `Automation/QuickAdd/`)
  - Advanced Canvas: Visual diagrams and flows
  - Tag Wrangler: Keep taxonomy clean as you grow
  - Tasks: Rich task management in Markdown

Setup tips
- Enable Dataview and Templater first
- In Templater, enable “Trigger Templater on new file creation”
- QuickAdd → Settings → Import → `Automation/QuickAdd/quickadd.offsecdev.json`
- Use the included choices: New Tool Note, New Finding, New Burp Log, New Campaign (Overview), etc.

---

## Folder Map (High-Level)

- `00_Index/` — Global navigation, dashboards, and governance
- `Templates/` — Reusable formats (tools, reports, languages, workflows)
- `Automation/` — Scripts and helpers for evidence/campaigns
- `Pentest Campaign/` — Project/campaign organization and examples
- `Flowcharts/` — Obsidian Canvas visual maps
- `Tags/` — Tag index and taxonomy
- `Notes/` — Your knowledge base

---

## License and Use

This is an educational and operational structure intended to accelerate learning and standardize execution. Use responsibly and ethically.

