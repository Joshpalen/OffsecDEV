# 🧺 Wireshark Note

**Date:**  
**Capture / Interface:**  
**Author:**  

---

## 🎯 Objective
(Packet capture for troubleshooting, protocol analysis, IDS tuning, pcap forensics)

---

## ⚙️ Capture Filters (BPF)
- `host 10.0.0.5`  
- `net 192.168.1.0/24`  
- `port 80`

## 🔍 Display Filters
- `http`  
- `tcp.port == 22`  
- `ip.addr == 10.0.0.5`

---

## 🧾 Observations
- Suspicious flows:  
- Repeated retransmits:  
- Protocol anomalies:  

(Reference packet numbers / timestamps)

---

## 🧩 Analysis Notes
- Follow TCP stream: `Follow → TCP Stream`  
- Export objects (HTTP, SMB) for evidence  
- Use IO graph for traffic patterns

---

## 🧰 Evidence
`/Evidence/pcaps/` — pcap filename, key packet IDs/screenshots

---

## 🧭 Next Steps
- Deep dive on stream X  
- Correlate with IDS logs

---

**References:**  
(Wireshark docs, BPF cheat sheet)
