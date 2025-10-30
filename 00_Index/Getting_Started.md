---
title: "Getting Started"
tags: [core, guide]
cssclass: cs-note
---

# Getting Started

## 1) Install Plugins
- Dataview (required)
- Templater (required)
- Optional: QuickAdd, Tasks, Advanced Canvas, Tag Wrangler

## 2) Open Hubs
- Master Index → `00_Index/Master Index.md`
- Domain hubs (Pentesting, Networking, Forensics, …) under `00_Index/`

## 3) Create Notes (Templater)
- Use “Templater: Create new note from template”
- Common templates: Tool, Finding, Lecture, Problem Set, Algorithm, Data Structure, Concept, Reading Summary

## 4) Optional: QuickAdd Macros
If you install the QuickAdd plugin, you can import the provided config:
- File: `Automation/QuickAdd/quickadd.offsecdev.json`
- QuickAdd → Settings → Import → select the JSON

Macros provided:
- New Tool Note → uses `Templates/Tool_Template.md`
- New Finding → `Pentest Campaign/Reports/Example Campaign/06-Reporting/Findings/Finding_Template.md`
- New Lecture → `Templates/Lecture_Note.md`
- New Problem Set → `Templates/Problem_Set.md`
- New Algorithm → `Templates/Algorithm.md`
- New Data Structure → `Templates/Data_Structure.md`
- New Concept → `Templates/Concept.md`
- New Reading → `Templates/Reading_Summary.md`

## 5) Evidence & Findings
- Use the Evidence Finder script in `Pentest Campaign/Reports/Example Campaign/Scripts/`
- Generate findings from scans with `Generate_Findings_From_Scans.ps1`

