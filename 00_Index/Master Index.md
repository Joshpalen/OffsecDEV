---
title: "Master Index"
tags: [core, index]
cssclass: simple-note
---

# Welcome

This vault is meant to make note-taking easy. Use the links below to jump to the places you'll update most often.

## Start Here
- [[00_Index/Getting_Started]] - plugin setup, capture shortcuts, and quick tips
- [[README]] - overview of the structure and how the notebook is organised

## Take Notes
- General note template: `Templates/All_Purpose_Note.md`
- Course / lecture note: `Templates/Lecture_Note.md`
- Quick reading summary: `Templates/Reading_Summary.md`
- Pentest session log: `Templates/Pentest_Session_Note.md`

> Tip: use QuickAdd (if installed) for "New Note", "New Course Note", or "New Pentest Note".

## Current Projects
- Example pentest campaign: [[Pentest Campaign/Reports/Example Campaign/Overview]]
- Burp Suite practice area: [[Pentest Campaign/Projects/Burp Suite Playground/README]]
- Scripts & automations: `Automation/`

## Reference & Resources
- Tags and taxonomy: [[Tags/Index]]
- Templates index: [[Templates/Templates_Hub]]
- Tools list: [[00_Index/Tools_Hub]]
- Reports and findings: [[00_Index/Reports_Hub]]
- Courses and class notes: [[00_Index/Courses_Hub]]

## Helpful Commands
- Sync vault: `C:\Users\joshp\Scripts\sync_offsecdev.ps1 -Execute`
- Backup: `robocopy "C:\OffsecDEV\OffsecDEV_Root" "D:\Vault_Backup" /MIR`
- Find text: `Get-ChildItem -Recurse | Select-String "search term"`

Keep your notes short, clear, and linked. If a page starts to feel heavy, break it into smaller notes and connect them with `[[links]]`.
