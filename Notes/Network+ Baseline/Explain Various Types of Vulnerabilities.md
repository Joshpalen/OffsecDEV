---
title: "Types of Vulnerabilities"
tags: [networking, education]
cssclass: simple-note
---

# Types of Vulnerabilities

## Categories
- **Software bugs** - coding errors (buffer overflow, SQL injection, cross-site scripting)
- **Configuration weaknesses** - default passwords, unnecessary services, open shares
- **Authentication / authorization gaps** - weak credentials, missing MFA, excessive privileges
- **Patch gaps** - outdated OS, applications, firmware
- **Physical security** - unlocked racks, unmonitored workstations, exposed ports
- **Third-party / supply chain** - vulnerable libraries, compromised updates, vendor access

## Lifecycle
1. Discovery (internal testing, external researchers, bug bounty)
2. Disclosure (responsible disclosure vs. full disclosure)
3. Remediation (patch, configuration change, compensating control)
4. Verification (testing, scanning, monitoring)

## Mitigation Tips
- Inventory assets and software versions
- Prioritise fixes based on severity and exposure
- Use defense-in-depth (firewalls, segmentation, monitoring)
- Educate staff about social engineering and safe practices
