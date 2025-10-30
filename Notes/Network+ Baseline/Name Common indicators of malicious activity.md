---
tags: [networking, education]
cssclass: cs-note
---
# ðŸš¨ Common Indicators of Malicious Activity
**Tags:** #security #incident-response #forensics #detection #reference  
**Vault:** OffsecDEV  
**Purpose:** Identify common signs that a system, user account, or network may be compromised or under active attack.

---

## ðŸ§­ Overview
Indicators of malicious activity (IoAs/IoCs) are observable artifacts or behaviors suggesting unauthorized access, compromise, or exploitation.  
Recognizing these early helps analysts **detect, contain, and respond** to threats before they escalate.

---

## ðŸ’» 1. System-Level Indicators
| Indicator | Description | Possible Threat |
|------------|--------------|----------------|
| **Unexpected CPU / Memory Spikes** | Resource usage abnormally high without user activity. | Cryptojacking, malware infection. |
| **New or Unknown Processes** | Suspicious executables or background services running. | Malware, backdoor, rootkit. |
| **Modified System Files or Registry Keys** | Changes to startup scripts, registry, or kernel modules. | Persistence mechanisms. |
| **Disabled Security Controls** | AV, firewall, or EDR disabled without authorization. | Privilege escalation, lateral movement. |
| **Unusual Scheduled Tasks or Cron Jobs** | Malicious persistence scheduled to re-execute payloads. | System compromise, persistence. |
| **Unauthorized Software Installations** | Unknown programs or browser extensions. | Spyware, RATs, keyloggers. |

---

## ðŸŒ 2. Network-Level Indicators
| Indicator | Description | Possible Threat |
|------------|--------------|----------------|
| **Outbound Connections to Unknown IPs** | Systems connecting to unfamiliar domains or external IPs. | C2 (Command & Control) traffic. |
| **Abnormal Data Transfers** | Sudden large uploads or encrypted outbound traffic. | Data exfiltration. |
| **Frequent Failed Logins** | High volume of authentication errors. | Brute-force or credential-stuffing attacks. |
| **Unusual Port Activity** | Unexpected services running on non-standard ports. | Port binding, tunneling. |
| **DNS Tunneling or Beaconing Patterns** | Regular, patterned requests to obscure domains. | Stealthy malware communication. |
| **Spoofed or Altered Network Packets** | Header anomalies or forged IPs. | Man-in-the-Middle, packet injection. |

---

## ðŸ”‘ 3. User and Account Indicators
| Indicator | Description | Possible Threat |
|------------|--------------|----------------|
| **Login Attempts from Unusual Locations** | Geographic or temporal anomalies. | Account compromise. |
| **Privilege Escalation Without Justification** | Role changes or new admin rights. | Insider threat, compromised account. |
| **Out-of-Hours Access** | Access during holidays or odd times. | Lateral movement, exfiltration. |
| **Password Resets or MFA Changes** | Multiple or unexplained authentication changes. | Account hijacking. |
| **Unauthorized File Access** | Sensitive directories accessed by non-privileged users. | Data theft, reconnaissance. |

---

## ðŸ§± 4. Application Indicators
| Indicator | Description | Possible Threat |
|------------|--------------|----------------|
| **Unexpected Web Requests** | Abnormal HTTP POST/GET activity or long query strings. | Injection or data exfiltration. |
| **Unexplained Log Entries or Errors** | Repeated 404s, 500s, or unauthorized access attempts. | Reconnaissance or brute force. |
| **Code Tampering or File Integrity Failures** | Hash or signature mismatches. | Web shell, defacement, supply-chain attack. |
| **Suspicious Outbound Email Activity** | High outbound mail volume from one host. | Compromised account, spam relay. |

---

## ðŸ‘¥ 5. Behavioral and Human Indicators
| Indicator | Description | Possible Threat |
|------------|--------------|----------------|
| **User Complaints of Slow Systems or Pop-ups** | End-users noticing unusual performance. | Malware infection, adware. |
| **Reports of Phishing Emails** | Multiple users receiving similar suspicious messages. | Credential harvesting. |
| **Unexplained Credential Lockouts** | Accounts repeatedly disabled. | Password spraying, brute-force. |
| **Unexpected MFA Prompts** | Users receiving authentication pushes they didnâ€™t initiate. | MFA fatigue attack. |

---

## ðŸ§© 6. Log and Forensic Indicators
| Indicator | Description | Possible Threat |
|------------|--------------|----------------|
| **Anomalous Log Deletions** | Security or system logs missing or cleared. | Covering tracks post-attack. |
| **Correlated Alerts Across Hosts** | Same IP or hash across multiple endpoints. | Coordinated intrusion. |
| **Unsigned or Unknown Binaries** | Files lacking valid digital signatures. | Malware, trojanized software. |
| **Multiple Failed Service Starts** | Services repeatedly failing and restarting. | Rootkit behavior, privilege issues. |

---

## ðŸ” 7. Advanced Indicators (APT / Persistent Threats)
- **Beaconing behavior** with precise intervals (C2 check-ins).  
- **Credential dumping tools** (Mimikatz, LSASS access).  
- **PowerShell or WMI abuse** for stealthy execution.  
- **Use of legitimate admin tools (Living off the Land)** such as `psexec`, `wmic`, `netsh`.  
- **Lateral movement evidence** â€” repeated SMB or RDP connections between endpoints.  
- **Data staging** â€” sensitive files compressed and encrypted before exfiltration.

---

## ðŸ§  8. Correlation and Context
A single indicator rarely confirms a breach.  
Analysts must correlate **multiple weak signals** across:
- Host logs  
- Network telemetry  
- Identity access records  
- Threat intelligence feeds  

**Indicators become actionable** when combined to form a narrative:  
> Example: Failed logins â†’ new admin creation â†’ outbound C2 traffic â†’ data compression.

---

## ðŸ§¾ Summary
Early recognition of malicious indicators enables faster response and containment.  
Maintaining visibility across systems, networks, and users â€” supported by logging, SIEM, and continuous monitoring â€” is essential to detect and disrupt attacks before they succeed.

---

*Maintained by:* **Josh Palen**  
*Repository:* `OffsecDEV_Root`  
*Category:* Security Reference  
*Version:* 1.0.0  
*Last Updated:* `{{date:YYYY-MM-DD}}`

