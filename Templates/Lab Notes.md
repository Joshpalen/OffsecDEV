# 🧪 Lab Notes

**Project / Campaign:**  
**Date:**  
**Author:**  
**Location / Environment:**  

---

## 🧭 Objective
Briefly describe the goal or purpose of this lab or test.  
*(Example: Test internal network segmentation and identify exploitable hosts.)*

---

## ⚙️ Environment / Setup
- **System(s):**  
- **Operating System:**  
- **Tools Used:**  
- **Network Segment / Target Range:**  
- **Credentials / Access Level:**  

*(Include relevant IPs, hostnames, or configs if applicable.)*

---

## 🧰 Methodology
1. Step-by-step description of what was done.  
2. Commands used or techniques applied.  
3. Tool configurations and versions.  
4. Reference to procedures or standards followed (e.g., MITRE ATT&CK, OSSTMM, PTES).

---

## 🧾 Observations / Results
| Step | Command / Action | Output / Notes |
|------|------------------|----------------|
| 1 | `nmap -sC -sV 10.0.0.5` | Found ports 22, 80 open |
| 2 | `dirb http://10.0.0.5` | `/admin/` directory discovered |
| 3 | `hydra -l admin -P passwords.txt` | Successful login found |

*(Include screenshots or evidence references, e.g., `Evidence/scan_results.txt`)*

---

## 💡 Analysis
Interpret your findings:
- What do the results imply?
- Did you achieve the lab objective?
- What unexpected behavior was observed?

---

## ⚠️ Issues / Errors
Document any challenges or anomalies:
- **Error Message:**  
- **Cause (if known):**  
- **Workaround / Resolution:**  

---

## ✅ Conclusions / Next Steps
- Summary of what was learned or confirmed.  
- Actions to take next (e.g., exploit, remediate, document).  
- Notes for follow-up testing.

---

## 📎 References / Evidence
- **Evidence Folder:** `./Evidence/`  
- **Related Notes:**  
- **External References:**  

---

**Signature / Initials:**  
