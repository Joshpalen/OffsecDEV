---
title: "<% tp.file.title %>"
tags:
  - tool
  - offsec
created: <% tp.date.now("YYYY-MM-DD") %>
category: "<% tp.system.suggester(['Scanner','Exploit','Post-Exploitation','Forensics','Enumeration','Reporting','IDS/IPS','Automation','OSINT','Privilege Escalation'], ['Scanner','Exploit','Post-Exploitation','Forensics','Enumeration','Reporting','IDS/IPS','Automation','OSINT','Privilege Escalation']) %>"
platforms: "<% tp.system.suggester(['Linux','Windows','macOS','Cross-Platform','Cloud','Mobile'], ['Linux','Windows','macOS','Cross-Platform','Cloud','Mobile']) %>"
language: "<% tp.system.suggester(['Python','C','C++','Go','Perl','Ruby','PowerShell','Bash','Java','Other'], ['Python','C','C++','Go','Perl','Ruby','PowerShell','Bash','Java','Other']) %>"
license: "<% tp.system.suggester(['GPL','MIT','Proprietary','BSD','Apache','Unknown'], ['GPL','MIT','Proprietary','BSD','Apache','Unknown']) %>"
status: "<% tp.system.suggester(['Installed','Not Installed','Deprecated','Testing','Favorite'], ['Installed','Not Installed','Deprecated','Testing','Favorite']) %>"
version: "<% tp.system.prompt('Tool version? (optional)') %>"
source_url: "<% tp.system.prompt('Project / repo URL?') %>"
---
# 🧰 <% tp.file.title %>

> Purpose: Document setup, capabilities, and usage patterns for each offensive or defensive tool in your OffsecDEV environment.

---

## ⚙️ Overview
**Category:** <% tp.frontmatter.category %>  
**Primary Platform:** <% tp.frontmatter.platforms %>  
**Language:** <% tp.frontmatter.language %>  
**License:** <% tp.frontmatter.license %>  

### Description
> Write a concise overview of what the tool does, when to use it, and what problem it solves.

---

## 🧩 Installation
### Linux
```bash
sudo apt install <tool>     # or build from source
