# OffsecDEV — Obsidian Pentesting Vault

[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-483699?logo=obsidian&logoColor=white)](#)
[![Beginner Friendly](https://img.shields.io/badge/Beginner_Friendly-Yes-brightgreen)](#)
[![Focus](https://img.shields.io/badge/Focus-Pentesting_%26_Operations-red)](#)
[![Requires](https://img.shields.io/badge/Requires-Dataview-blue)](#)
[![Requires](https://img.shields.io/badge/Requires-Templater-blue)](#)
[![Last commit](https://img.shields.io/github/last-commit/Joshpalen/OffsecDEV)](https://github.com/Joshpalen/OffsecDEV/commits)
[![Open issues](https://img.shields.io/github/issues/Joshpalen/OffsecDEV)](https://github.com/Joshpalen/OffsecDEV/issues)

A complete, opinionated Obsidian knowledge system for offensive security, networking, and automation. It’s built to guide true beginners into the field while staying useful for seasoned professionals during real assessments.

- Central “Map of Content” indexes that tie everything together
- Production-ready templates for tools, workflows, vulnerabilities, and reports
- Automation for evidence collection and campaign organization
- Compatible with Obsidian community plugins (Dataview, Templater)

> Goal: Turn scattered learning and ad‑hoc notes into a coherent, searchable operational knowledge system you can actually run campaigns with.

---

## Quickstart

1) Install Obsidian and enable community plugins (Settings → Community Plugins)
- Recommended: Dataview, Templater, (optional) QuickAdd

2) Clone this repository and open it as a vault:
- `git clone https://github.com/Joshpalen/OffsecDEV C:\OffsecDEV\OffsecDEV_Root`
- In Obsidian: Open folder as vault → select `C:\OffsecDEV\OffsecDEV_Root`

3) Start at the hub:
- Open [Master Index](00_Index/Master%20Index.md)
- Browse [Vulnerability Index](00_Index/Vulnerability%20index.md) and [Workflow Index](00_Index/Workflow.md)

4) Create notes with templates:
- Use Templater to instantiate items from the [Templates](Templates) folder

---

## What’s Inside

- 00_Index — Master navigation and dashboards
  - Master Index (Map of Content)
  - Vulnerability Index (catalog + taxonomy + Dataview dashboards)
  - Workflow Index (procedures + governance + roll‑ups)
  - Reading Log (structured learning tracker)
- Templates — Ready‑to‑use structures for:
  - Tools: Nmap, Metasploit, Wireshark, Snort, Zsh, Dockerfile
  - Languages: Python, JavaScript, C#, C++, Ruby, Zsh
  - Reports: Pentest report, Findings blocks, Lab notes, Flowcharts
  - Knowledge: General reading, Links, Networking, Firewall, NIDS
- Automation — Evidence and campaign helpers
  - `Automation/Scripts/se_evidence_finder_copy.py`
  - Example runner: `Pentest Campaign/Reports/Example Campaign/Scripts/Run_Evidence_Finder.ps1`
- Pentest Campaign — Example structure for running assessments
- Flowcharts — Obsidian Canvas maps for workflows and architecture
- Tags — Tag index and taxonomy reference for consistent metadata
- Notes — Your working knowledge base and research

---

## Core Ideas and Workflow

- Map‑of‑Content First: Use the [Master Index](00_Index/Master%20Index.md) as your control tower. Each hub links out to tools, domains, and dashboards.
- Templates Everywhere: Every recurring thing has a template — tools, workflows, vulnerabilities, reports — so your notes stay consistent.
- Evidence is a First‑Class Citizen: Automation scripts collect and normalize raw evidence into `Reports/<Campaign>/Evidence/` with a Markdown index.
- Metadata + Queries: Dataview turns metadata into dashboards (active vulns, workflows, reading queues) to keep you oriented.
- Campaign‑Ready: Move from reconnaissance → exploitation → reporting with a structure that mirrors how real assessments are run.

---

## Key Templates (Selected)

- Pentest_Report_Template.md — Assessment structure, findings tables, methodology, and summary sections ready to fill.
- Tool_Template.md — Standardized way to document any tool: install, usage, flags, examples.
- Nmap_Note.md / Metasploit_Note.md — Focused operator checklists with copy‑paste commands and result fields.
- General_Reading_Note.md — Capture structured insights, tags, and follow‑ups from any source.

All templates live in [Templates](Templates) and are compatible with Templater prompts.

---

## Automation: SE Evidence Finder

Python utility to copy and normalize social‑engineering or campaign evidence into the vault with an index and JSON manifest.

- Input: any `--src` folder (images, pcaps, logs, emails, audio, docs)
- Output: `Reports/<campaign>/Evidence/{images,pcap,logs,emails,attachments,audio,other}`
- Index: `Evidence_Index.md` + `evidence_manifest.json`

Usage:
```
python Automation/Scripts/se_evidence_finder_copy.py --src C:\path\to\raw_evidence --campaign MyCampaign --vault C:\OffsecDEV\OffsecDEV_Root
```

Tip: Keep originals — this script copies by default.

---

## Learning Path (Use the Vault As Your Syllabus)

- Foundations: Networking basics, Linux/Windows essentials, scripting (see Notes + Templates)
- Discovery: Nmap fundamentals → service fingerprints → targeted enumeration
- Exploitation: Metasploit workflow → PoCs → post‑exploitation checkpoints
- Analysis: Wireshark/Snort workflows → evidence capture and correlation
- Reporting: Findings → recommendations → export from report templates
- Automation: Add your own scripts and link them into Workflows

Each step links back into the vault’s indices and templates to reinforce a single, coherent workflow.

---

## Plugins and Compatibility

- Dataview: Drives dashboards and indexes (queries are included in index pages)
- Templater: Prompts and dynamic frontmatter for templates
- Canvas: Flowcharts in `/Flowcharts` (.canvas files)

Everything works offline with Obsidian. No vendor lock‑in; it’s just Markdown.

---

## Contributing / Personalizing

- Fork the repo, or clone and iterate locally
- Adjust tags to your taxonomy (see `Tags/Index.md` and `Tags/Taxonomy Reference.md`)
- Add tools and workflows by copying templates
- Keep sensitive items out if publishing publicly (e.g., real client data)

If you’re new: start by reading, templating one tool, and writing one mini‑workflow. Iterate daily.

---

## Folder Map (High‑Level)

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


---

## Recommended Community Plugins

- Dataview: Query notes to build dashboards, tables, and task views. Used across all index pages to surface “active” content from metadata.
- Templater: Powerful templating and prompts that generate consistent frontmatter and scaffolds. This vault’s templates are Templater-ready.
- QuickAdd (optional): Create capture commands to instantly spawn Tool, Vulnerability, Workflow, and Reading notes from templates.
- Tag Wrangler (optional): Rename and merge tags safely, keeping your taxonomy consistent.
- Canvas / Advanced Canvas: Visualize architectures and workflows. This repo includes .canvas files under Flowcharts/.
- Tasks (optional): Rich task management in Markdown; great for campaign checklists.
- Admonition (optional): Clean callout blocks for warnings, tips, and notes in reports and guides.
- Obsidian Git (optional): Version your vault directly from Obsidian if you prefer in‑app commits.

Setup tips
- Enable Dataview and Templater first; most dashboards and templates depend on them.
- In Templater settings, enable “Trigger Templater on new file creation” for smooth template workflows.
- With QuickAdd, create capture macros mapped to the Templates folder to speed up note creation.

## Screenshots / GIFs

Drop your screenshots into `images/` and use these filenames (or tell me new names and I will update links):

![Master Index (Map of Content)](images/master-index.gif)

![Vulnerability Index Dashboard](images/vuln-dashboard.gif)



### Additional Visuals

- Vault structure (Obsidian sidebar):

![Vault Structure (Obsidian Sidebar)](images/vault-structure.png)

- Knowledge graph (Obsidian Graph View):

![Knowledge Graph (Obsidian Graph View)](images/graph-view.gif)

