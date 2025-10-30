---
title: "<% tp.file.title %>"
type: tool
created: "<% tp.date.now('YYYY-MM-DD') %>"
category: "<% tp.system.suggester(['Scanner','Exploit','Post-Exploitation','Forensics','Enumeration','Reporting','IDS/IPS','Automation','OSINT','Privilege Escalation'], ['Scanner','Exploit','Post-Exploitation','Forensics','Enumeration','Reporting','IDS/IPS','Automation','OSINT','Privilege Escalation']) %>"
platforms: "<% tp.system.suggester(['Linux','Windows','macOS','Cross-Platform','Cloud','Mobile'], ['Linux','Windows','macOS','Cross-Platform','Cloud','Mobile']) %>"
language: "<% tp.system.suggester(['Python','C','C++','Go','Perl','Ruby','PowerShell','Bash','Java','Other'], ['Python','C','C++','Go','Perl','Ruby','PowerShell','Bash','Java','Other']) %>"
license: "<% tp.system.suggester(['GPL','MIT','Proprietary','BSD','Apache','Unknown'], ['GPL','MIT','Proprietary','BSD','Apache','Unknown']) %>"
status: "<% tp.system.suggester(['Installed','Not Installed','Deprecated','Testing','Favorite'], ['Installed','Not Installed','Deprecated','Testing','Favorite']) %>"
version: "<% tp.system.prompt('Tool version? (optional)') %>"
source_url: "<% tp.system.prompt('Project / repo URL?') %>"
tags: [tool]
cssclass: cs-note
---

# <% tp.file.title %>

## Overview
**Category:** <% tp.frontmatter.category %>  
**Platforms:** <% tp.frontmatter.platforms %>  
**Language:** <% tp.frontmatter.language %>  
**License:** <% tp.frontmatter.license %>

### Description
What the tool does, when to use it, and the problem it solves.

## Installation
```bash
# Linux
sudo apt install <tool>
# macOS
brew install <tool>
```

## Usage
| Task | Command |
|------|---------|
|  |  |

## Cheatsheet
- Flag X — purpose  
- Flag Y — purpose

## Examples
```bash
<tool> -x -y target
```

## Notes
- 

## References
- Repo: <% tp.frontmatter.source_url %>
- Docs: 

