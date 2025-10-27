# 📚 Reading Log

**Vault:** OffsecDEV_Root  
**Author:** Josh  
**Purpose:** Record and organize all readings, articles, and documents reviewed for research, study, or inspiration.  
**Last Updated:** {{date}}

---

## 🧭 Overview

This log tracks ongoing and completed readings related to cybersecurity, networking, AI, and systems research.  
Each entry links to key insights, connected tags, and related notes.  

Use it to:
- Maintain continuity of learning  
- Cross-link important concepts  
- Identify trends and revisit sources  

---

## 🧩 Reading Entry Template

> Copy this block for each new reading entry

```markdown
### 📖 Title:
*(Full title of article, paper, book, or report)*

**Source / Author:**  
**Date Accessed:** {{date}}  
**Tags:** [#education, #reference]  
**Related Notes:** [[General_Reading_Note]]  

**Summary:**  
(Brief description of what this covers)

**Key Points:**  
-  
-  
-  

**Takeaways / Insights:**  
(What did you learn? How does it connect to your projects or other notes?)

**Follow-Up Actions:**  
- [ ] Review again  
- [ ] Create concept note on related topic  
- [ ] Add related tag to [[Tags/index]]  

**Attachment(s):**  
(If applicable: PDFs, screenshots, or saved links)
```

---

## 🧠 Active Reading Queue

```dataview
TABLE file.name AS "Active Reading", file.mtime AS "Updated"
FROM "Notes"
WHERE contains(tags, "#education") AND (status = "active" OR status = "pending")
SORT file.mtime DESC
```

---

## ✅ Completed Readings

```dataview
TABLE file.name AS "Completed", file.mtime AS "Completed On"
FROM "Notes"
WHERE contains(tags, "#education") AND status = "complete"
SORT file.mtime DESC
```

---

## 🧾 Historical Log

| Date | Title | Source | Tags | Status |
|------|--------|---------|-------|---------|
|  |  |  |  |  |
|  |  |  |  |  |

*(Optional manual table for chronological tracking — useful for printing or quick review.)*

---

## 🧠 Insights Extracted

Use this section for summarizing key insights or recurring themes you notice as you read.

| Theme | Summary | Related Notes |
|--------|----------|---------------|
|  |  |  |
|  |  |  |

---

## 🧩 Reference Integration

Link major reading entries to foundational vault components:  
- **Tag Index:** [[Tags/index]]  
- **Taxonomy Reference:** [[Tags/Taxonomy Reference]]  
- **Master Index:** [[Master Index]]  

---

## 🧰 Commands (PowerShell / Automation)

| Task | Command |
|------|----------|
| Search all notes tagged as reading | `Get-ChildItem -Recurse | Select-String "#education"` |
| Export summaries | `grep -r "## Summary" * > reading_summaries.txt` |
| Sync readings | `C:\Users\joshp\Scripts\sync_offsecdev.ps1` |

---

## 🧱 Reading Philosophy

> “Information becomes intelligence only when connected.”  
> — OffsecDEV Principle

This log is not just a record — it’s a **living memory system**.  
Use it to interconnect what you study with what you build, test, or document in your environment.

---

**End of Reading Log**
