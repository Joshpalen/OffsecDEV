---
tags: [networking, education]
cssclass: cs-note
---
# âš ï¸ Various Types of Vulnerabilities
**Tags:** #security #vulnerabilities #risk-management #reference #offsec  
**Vault:** OffsecDEV  
**Purpose:** Identify and explain common types of vulnerabilities that weaken systems, software, networks, and human defenses.

---

## ðŸ§­ Overview
A **vulnerability** is a weakness or flaw in a system that can be exploited by a threat actor to compromise confidentiality, integrity, or availability.  
Understanding the **categories and mechanisms** of vulnerabilities is key to assessing and mitigating risk.

Vulnerabilities may stem from:
- Poor design or insecure coding  
- Misconfigurations or weak policies  
- Unpatched software  
- Human error or social manipulation  

---

## ðŸ’» 1. Software Vulnerabilities
These are flaws in code or design that allow unintended behavior.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Buffer Overflow** | Data exceeds memory buffer limits, allowing code execution. | Exploit via crafted input to overflow stack. | Input validation, bounds checking, memory-safe languages. |
| **Injection Flaws** | Untrusted data sent to interpreters or databases. | SQL Injection, Command Injection, LDAP Injection. | Input sanitization, parameterized queries. |
| **Cross-Site Scripting (XSS)** | Malicious scripts injected into trusted sites. | JavaScript stealing session tokens. | Output encoding, CSP, input filtering. |
| **Cross-Site Request Forgery (CSRF)** | Unauthorized commands sent via a userâ€™s authenticated session. | Attacker causes victim to perform unintended actions. | CSRF tokens, same-site cookies. |
| **Deserialization Issues** | Untrusted data manipulated during deserialization. | Injected code runs during object reconstruction. | Use safe serializers, validate inputs. |
| **Improper Error Handling** | Leaking sensitive info through verbose errors. | Stack traces or database names exposed. | Generic error messages, logging without exposure. |

---

## ðŸŒ 2. Network Vulnerabilities
Exploitable weaknesses in communication channels or network configurations.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Open Ports & Services** | Unnecessary or unmonitored network services. | Exposed SSH, RDP, or SMB. | Port filtering, service minimization, firewalls. |
| **Unencrypted Traffic** | Data transmitted in plaintext. | HTTP instead of HTTPS; Telnet instead of SSH. | TLS/SSL, VPNs, encrypted protocols. |
| **Weak Network Segmentation** | Flat networks allow lateral movement. | Compromise in one area spreads quickly. | VLANs, zero trust, microsegmentation. |
| **DNS/ARP Spoofing** | Manipulation of network address resolution. | Redirect traffic to malicious endpoints. | DNSSEC, ARP inspection, static mappings. |

---

## ðŸ”’ 3. Configuration Vulnerabilities
Errors or oversights in system or application setup.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Default Credentials** | Factory usernames/passwords left unchanged. | â€œadmin/adminâ€ still active on routers. | Enforce password changes, credential rotation. |
| **Improper Access Controls** | Permissions set too broadly. | â€œEveryone: Full Controlâ€ on shared folders. | Role-based access control, least privilege. |
| **Unpatched Systems** | Missing security updates leave known flaws. | Outdated OS or applications. | Automated patch management. |
| **Directory Listing Enabled** | Web server reveals directory contents. | Sensitive files visible via browser. | Disable indexing, restrict file permissions. |
| **Insecure Cloud Configurations** | Misconfigured storage or IAM policies. | Public S3 buckets with sensitive data. | Use CSPM tools, review IAM permissions. |

---

## ðŸ‘¥ 4. Human / Social Vulnerabilities
The human element â€” often the weakest link.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Phishing & Social Engineering** | Manipulating people to gain access. | Fake emails or calls requesting credentials. | Awareness training, MFA, reporting channels. |
| **Poor Password Hygiene** | Weak or reused passwords. | Same password used across services. | Enforce password policies, password managers. |
| **Privilege Misuse** | Authorized users exceeding intended access. | Copying confidential data off-network. | Monitoring, DLP, least privilege. |
| **Lack of Security Awareness** | Employees unaware of security policy. | Clicking on suspicious attachments. | Regular training, simulated phishing. |

---

## ðŸ§  5. Hardware & Physical Vulnerabilities
Physical components or interfaces that can be tampered with or exploited.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Unsecured Ports** | Open USB or console ports. | Inserting rogue devices. | Port control, endpoint security policies. |
| **Hardware Backdoors** | Malicious implants or firmware code. | Compromised BIOS, infected chips. | Vendor vetting, firmware verification. |
| **Side-Channel Attacks** | Exploiting physical emissions (timing, power, RF). | Spectre, Meltdown. | Microcode updates, shielding, isolation. |
| **Theft or Tampering** | Devices stolen or physically altered. | Server room access breach. | Surveillance, locks, physical access control. |

---

## â˜ï¸ 6. Cloud & Virtualization Vulnerabilities
Arising from shared infrastructure or mismanagement of virtualized environments.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Insecure APIs** | Poorly secured endpoints. | API key exposure, lack of authentication. | API gateways, input validation. |
| **Hypervisor Escapes** | VM gains access to host system. | Exploit in hypervisor software. | Isolation, patch management, vendor updates. |
| **Over-Permissioned IAM Roles** | Excessive privileges to users/services. | Service accounts with admin-level access. | Principle of least privilege, periodic reviews. |
| **Data Residency Misconfigurations** | Data stored outside compliant regions. | Violation of GDPR/HIPAA. | Geo-restriction enforcement, compliance review. |

---

## ðŸ§¬ 7. Logical & Design Vulnerabilities
Weaknesses in the conceptual or architectural design of systems.

| Type | Description | Example | Mitigation |
|------|--------------|----------|-------------|
| **Race Conditions** | Simultaneous operations lead to privilege escalation. | Exploit timing of system calls. | Thread-safe coding, synchronization mechanisms. |
| **Business Logic Flaws** | Application behaves in unintended ways. | Bypassing checkout totals or authorization steps. | Security reviews during SDLC, unit testing. |
| **Improper Input Validation** | Lack of boundary checks or sanitation. | Integer overflow, path traversal. | Validate input size, type, and format. |

---

## ðŸ§© Integration with Security Operations
Identifying vulnerabilities is central to:
- **Risk Assessment** and **Vulnerability Management**  
- **Penetration Testing** and **Red Teaming**  
- **Patch Management Cycles**  
- **Change and Configuration Control**

Each vulnerability should map to a **control or mitigation** and be prioritized by **CVSS score, exploitability, and business impact.**

---

## ðŸ§¾ Summary
> Vulnerabilities are inevitable â€” unmanaged vulnerabilities are inexcusable.  

By categorizing, tracking, and continuously addressing vulnerabilities, organizations maintain resilience and reduce their exposure to threats.

---

*Maintained by:* **Josh Palen**  
*Repository:* `OffsecDEV_Root`  
*Category:* Security Reference  
*Version:* 1.0.0  
*Last Updated:* `{{date:YYYY-MM-DD}}`

