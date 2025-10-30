# OffsecDEV - Obsidian Pentesting Vault

[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-483699?logo=obsidian&logoColor=white)](#)
[![Beginner Friendly](https://img.shields.io/badge/Beginner_Friendly-Yes-brightgreen)](#)
[![Focus](https://img.shields.io/badge/Focus-Pentesting_%26_Operations-red)](#)

A complete, opinionated Obsidian knowledge system for offensive security, networking, and automation. It is built to guide beginners while staying useful for real assessments.

- Central hub pages that keep navigation simple
- Practical templates for tools, workflows, vulnerabilities, and reports
- Automation for evidence collection and campaign organisation
- Works with Obsidian community plugins (Dataview, Templater)

> Goal: turn scattered learning and ad-hoc notes into a coherent, searchable operational knowledge system you can run campaigns with.

---

## Quickstart

1. Install Obsidian and enable community plugins (Settings -> Community Plugins).
   - Required: Dataview, Templater
   - Recommended: QuickAdd, Advanced Canvas, Tag Wrangler, Tasks
2. Open this folder as a vault in Obsidian.
   - Clone or copy to a local path (for example `C:\OffsecDEV\OffsecDEV_Root`)
   - In Obsidian choose `Open folder as vault` and select the folder
3. Start at the hub.
   - Open `00_Index/Master Index.md`
   - Explore the domain hubs (Pentesting, Networking, Forensics, and others)
4. Create notes with templates.
   - Use the Templater command palette to create notes from anything in `Templates/`

`00_Index/Getting_Started.md` has plugin import steps and capture shortcuts.

---

## Navigation

This vault is organised around a small set of hubs and indices:

- Master Index (`00_Index/Master Index.md`) - central launch pad
- Domain hubs (`00_Index/*_Hub.md`) - Pentesting, Networking, Forensics, Malware, Crypto, Scripting, Docker, Cloud, Packages
- Tools Hub (`00_Index/Tools_Hub.md`) - tool notes and operator references
- Reports Hub (`00_Index/Reports_Hub.md`) - finished deliverables and campaign reports
- Scripts Hub (`00_Index/Scripts_Hub.md`) - automation and helper scripts
- Evidence Hub (`00_Index/Evidence_Hub.md`) - manifests and storage guidance
- Courses Hub (`00_Index/Courses_Hub.md`) - coursework dashboards and class notes

Use the hubs and Dataview tables to surface what matters now based on note metadata.

---

## Core Workflow

- Map-of-content first: start at the Master Index and dive into hubs
- Templates everywhere: consistent frontmatter keeps dashboards clean
- Evidence first-class: scripts normalise raw evidence into `Reports/<Campaign>/Evidence/`
- Metadata plus queries: Dataview builds live dashboards from consistent fields
- Campaign-ready: structure mirrors Recon -> Enumeration -> Exploitation -> Post-Exploitation -> Reporting

---

## Learning Flow

1. Study a topic using templates (Algorithm, Data Structure, Concept, Reading Summary)
2. Practise with tool notes (Nmap, Metasploit, ffuf, Burp, and others)
3. Run a practice campaign (see `Pentest Campaign/Reports/Example Campaign`)
4. Capture evidence with scripts and generate finding stubs from scans
5. Compile a final report using the report template

Each step is linked from the Master Index and domain hubs so you can move smoothly from study to practice to portfolio.

---

## Template Highlights

Programming and systems:
- Python (`Templates/Python.md`, `Templates/Python_Note.md`)
- JavaScript (`Templates/JavaScript.md`, `Templates/JavaScript_Note.md`)
- Java (`Templates/Java.md`, `Templates/Java_Note.md`)
- C# (`Templates/C_Sharp.md`, `Templates/C_Sharp_Note.md`)
- C++ (`Templates/C++.md`, `Templates/C++_Note.md`)
- Ruby (`Templates/Ruby.md`, `Templates/Ruby_Note.md`)
- Perl (`Templates/Perl.md`, `Templates/Perl_Note.md`)
- Zsh (`Templates/Zsh_Note.md`)
- Dockerfile (`Templates/Dockerfile.md`, `Templates/Dockerfile_Note.md`)

Pentesting tools:
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

Reports and operations:
- Pentest report (`Templates/Pentest_Report_Template.md`)
- Finding template (`Pentest Campaign/Reports/Example Campaign/06-Reporting/Findings/Finding_Template.md`)
- Lab notes (`Templates/Lab Notes.md`)
- Exploit record (`Templates/Exploit_Template.md`)
- Flowcharts (`Templates/Flowchart_Template.md`)

Study and organisation:
- Algorithm, Data Structure, Concept, Reading Summary, Exam Review
- Course overview and dashboard (`Templates/University Course Overview.md`, `Templates/Course_Dashboard.md`)
- General note (`Templates/All_Purpose_Note.md`)
- Links page (`Templates/Links.md`)

---

## Automation

Evidence archiver (copy or move) standardises raw artefacts:
- PowerShell wrapper: `Pentest Campaign/Reports/Example Campaign/Scripts/Run_Evidence_Finder.ps1`
- Python core: `Automation/Scripts/se_evidence_finder_copy.py`

Generate finding stubs from scans:
- Python: `Pentest Campaign/Reports/Example Campaign/Scripts/generate_findings.py`
- Bulk runner: `Pentest Campaign/Reports/Example Campaign/Scripts/Generate_Findings_From_Scans.ps1`
- Output written to `06-Reporting/Findings/`

New campaign scaffold:
- PowerShell: `Automation/Scripts/new_campaign.ps1 -Name "My Campaign"`
- QuickAdd capture: "New Campaign (Overview)" (optional plugin)

---

## Tags and Taxonomy

Consistent tags make Dataview dashboards work. Useful references:
- Tag dictionary: `Tags/Index.md`
- Taxonomy reference: `Tags/Taxonomy Reference.md`

Use frontmatter tags such as `pentesting`, `networking`, `tool`, `education`, `reading`, `vulnerability`, `workflow` to keep content discoverable.

---

## Styling and Plugins

- CSS snippets are enabled (see `.obsidian/appearance.json`). Most templates use `cssclass: cs-note` for a consistent look.

### Required Plugins
- Dataview: query notes to build dashboards
- Templater: generate consistent frontmatter and scaffolds

### Recommended Plugins
- QuickAdd: capture shortcuts (config in `Automation/QuickAdd/`)
- Advanced Canvas: diagrams and flows
- Tag Wrangler: maintain tag hygiene
- Tasks: rich task tracking in Markdown

Setup tips:
- Enable Dataview and Templater first
- In Templater enable "Trigger Templater on new file creation"
- QuickAdd -> Settings -> Import -> `Automation/QuickAdd/quickadd.offsecdev.json`
- Use the included choices (New Tool Note, New Finding, New Burp Log, New Campaign Overview, and more)

---

## Folder Map (High Level)

- `00_Index/` - navigation, dashboards, governance
- `Templates/` - reusable formats for notes
- `Automation/` - scripts and helpers
- `Pentest Campaign/` - projects, evidence, reporting
- `Flowcharts/` - Obsidian Canvas diagrams
- `Tags/` - tag index and taxonomy
- `Notes/` - study notes and general knowledge

---

## Licence and Use

This vault is an educational and operational structure intended to accelerate learning and standardise execution. Use responsibly and ethically.
