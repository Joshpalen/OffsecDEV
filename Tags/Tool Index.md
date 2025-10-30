---
title: "Tool Index"
tags: [core, index, tool]
cssclass: cs-note
---

# Tool Index

Master reference for all operational tools used in the vault.

## Offensive Security Tools
| Tool | Description | Note |
|------|-------------|------|
| Metasploit | Exploitation & post-exploitation | [[Templates/Metasploit_Note]] |
| Nmap | Discovery and port scanning | [[Templates/Nmap_Note]] |
| Nessus | Vulnerability assessment | [[Templates/Nessus_Note]] |

```dataview
TABLE file.name AS "Offensive Tools", file.mtime AS "Updated"
FROM ""
WHERE any(type = "tool", type = "tool-note") AND any(contains(tags, "metasploit"), contains(tags, "nmap"), contains(tags, "nessus"))
SORT file.mtime DESC
```

## Defensive & Monitoring Tools
| Tool | Description | Note |
|------|-------------|------|
| Wireshark | Packet analysis and forensics | [[Templates/Wireshark_Note]] |
| Snort | IDS and traffic monitoring | [[Templates/Snort_Note]] |
| Firewall | Policy and ACL management | [[Templates/Firewall_Note]] |

```dataview
TABLE file.name AS "Defensive Tools", file.folder AS "Location"
FROM ""
WHERE any(type = "tool", type = "tool-note") AND any(contains(tags, "snort"), contains(tags, "wireshark"), contains(tags, "nids"), contains(tags, "firewall"))
SORT file.mtime DESC
```

## Automation & Environment
| Tool | Description | Note |
|------|-------------|------|
| Zsh | Shell environment | [[Templates/Zsh_Note]] |
| Docker | Container builds | [[Templates/Dockerfile_Note]] |
| Packages | Package tracking | [[Templates/Packages_Note]] |

```dataview
TABLE file.name AS "Automation Tools", file.mtime AS "Updated"
FROM ""
WHERE any(type = "tool", type = "tool-note") AND any(contains(tags, "zsh"), contains(tags, "docker"), contains(tags, "packages"))
SORT file.mtime DESC
```

