# 🕵️ Snort Note

**Date:**  
**Sensor / Host:**  
**Author:**  

---

## 🎯 Objective
(Rules tuning, alert review, baseline behavior, False Positive triage)

---

## ⚙️ Deployment Info
- Snort version:  
- Ruleset: (ET Pro / ET Open / custom)  
- Sensor interfaces:  

---

## 🧾 Recent Alerts / Notable Signatures
| Time | SID | Msg | Src -> Dst |
|------|-----|-----|------------|
|  |  |  |  |

---

## 🧩 Rule Examples / Tuning
    alert tcp any any -> $HOME_NET 80 (msg:"Example rule"; sid:1000001; rev:1;)

- False positive reasoning:  
- Action taken (disable, threshold, refine):  

---

## 🧰 Logs / Evidence
`/var/log/snort/alert` — relevant lines, pcap evidence

---

## 🧭 Next Steps
- Adjust rule X  
- Add suppression for Y  
- Re-evaluate after 24h

---

**References:**  
(Snort manual, rules writing guide)
