---
tags: [networking, education]
cssclass: cs-note
---
# ðŸ§  Essential Security Concepts
**Tag:** #security #fundamentals #reference  
**Vault:** OffsecDEV  
**Purpose:** Core principles and terminology for cybersecurity operations, training, and documentation.

---

## ðŸ” 1. Confidentiality, Integrity, Availability (CIA Triad)
The foundation of all security frameworks:
- **Confidentiality** â€” Prevent unauthorized disclosure of data.  
  _Examples:_ Encryption, access control lists, data classification.
- **Integrity** â€” Prevent unauthorized modification or destruction of data.  
  _Examples:_ Hashing, checksums, digital signatures.
- **Availability** â€” Ensure timely and reliable access to data and resources.  
  _Examples:_ Redundancy, fault tolerance, backups, DDoS mitigation.

---

## ðŸ§© 2. Authentication, Authorization, and Accounting (AAA)
- **Authentication:** Verify identity (passwords, MFA, biometrics).  
- **Authorization:** Grant permissions based on role or policy.  
- **Accounting (Auditing):** Track and log activity for traceability and non-repudiation.

---

## ðŸ§± 3. Defense in Depth
A layered approach ensures multiple barriers between threat and asset.

| Layer | Example Controls |
|-------|------------------|
| Network | Firewalls, IDS/IPS, segmentation |
| Host | EDR, antivirus, patch management |
| Application | Input validation, secure coding, WAF |
| Data | Encryption, DLP, tokenization |
| Human | Awareness training, policy enforcement |

---

## ðŸ§  4. Least Privilege & Need-to-Know
Principles that limit exposure and reduce attack surface:
- Assign only the access rights essential to a task.
- Periodically review privileges and revoke unused accounts.
- Apply â€œseparation of dutiesâ€ wherever possible.

---

## ðŸ§¬ 5. Threats, Vulnerabilities, and Risks
- **Threat:** Potential cause of an unwanted event.  
- **Vulnerability:** Weakness that can be exploited.  
- **Risk:** The likelihood Ã— impact of a threat exploiting a vulnerability.  

_Risk = Threat Ã— Vulnerability Ã— Impact_

---

## ðŸ§® 6. Risk Management Lifecycle
1. **Identify** assets, threats, and vulnerabilities.  
2. **Assess** likelihood and impact.  
3. **Mitigate** using appropriate controls.  
4. **Monitor** for changes or new threats.  
5. **Review** and update policies continuously.

---

## ðŸ” 7. Security Controls
| Type | Function | Example |
|------|-----------|---------|
| Preventive | Stop incidents before they occur | Firewalls, MFA |
| Detective | Identify incidents during/after | SIEM, IDS logs |
| Corrective | Repair damage after incident | Backups, reimaging |

---

## ðŸ’£ 8. Common Attack Vectors
- **Phishing & Social Engineering**
- **Malware** (viruses, trojans, ransomware)
- **Exploits** (SQLi, XSS, buffer overflows)
- **DoS/DDoS**
- **Insider Threats**
- **Man-in-the-Middle (MitM)**  
_Defense:_ user training, IDS, endpoint protection, and segmentation.

---

## ðŸ§° 9. Cryptography Basics
| Concept | Description | Example |
|----------|--------------|---------|
| Symmetric Encryption | Same key used to encrypt/decrypt | AES |
| Asymmetric Encryption | Public/private key pairs | RSA, ECC |
| Hashing | One-way function for integrity | SHA-256 |
| Digital Signatures | Integrity + authentication | PKI, certificates |

---

## ðŸ“‹ 10. Security Policies & Compliance
Defines the â€œrules of engagementâ€ for security.
- Policies: overarching rules  
- Standards: technical requirements  
- Procedures: step-by-step instructions  
- Guidelines: recommended practices  

_Frameworks:_ ISO/IEC 27001, NIST SP 800-53, GDPR, HIPAA.

---

## ðŸš¨ 11. Incident Response & Recovery
**Phases:**
1. **Preparation** â€“ Build IR plan, tools, and teams.  
2. **Detection & Analysis** â€“ Identify anomalies or alerts.  
3. **Containment** â€“ Isolate affected systems.  
4. **Eradication** â€“ Remove root cause.  
5. **Recovery** â€“ Restore systems to normal operation.  
6. **Lessons Learned** â€“ Document, adapt, and improve.

---

## ðŸ§­ 12. Zero Trust Architecture
Core idea: **â€œNever trust, always verify.â€**
- Authenticate every connection.  
- Use microsegmentation.  
- Continuously validate trust based on behavior, not location.

---

## ðŸ§© 13. Security Domains Overview
- **Network Security** â€“ Firewalls, VPNs, IDS/IPS.  
- **Application Security** â€“ Secure coding, SDLC, WAF.  
- **Endpoint Security** â€“ AV, EDR, hardening.  
- **Data Security** â€“ Encryption, masking, DLP.  
- **Cloud Security** â€“ Shared responsibility, IAM, CSPM.  
- **Physical Security** â€“ Badging, surveillance, environmental controls.  

---

## ðŸ§¾ References
- NIST Cybersecurity Framework (CSF)
- ISO/IEC 27001: Information Security Management Systems
- CIS Controls v8
- OWASP Top 10

---

*Maintained by:* **Josh Palen**  
*Repository:* `OffsecDEV_Root`  
*Category:* Security Reference  
*Version:* 1.0.0  
*Last Updated:* `{{date:YYYY-MM-DD}}`

