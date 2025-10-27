---
title: "<% tp.file.title %>"
tags:
  - social-engineering
  - red-team
  - playbook
created: <% tp.date.now("YYYY-MM-DD") %>
client: "<% tp.system.prompt('Client / Organization (Name)?') %>"
authorization_reference: "<% tp.system.prompt('Auth Doc / ROE ID (attach or reference)?') %>"
campaign_type: "<% tp.system.suggester(['Phishing','Vishing','Physical Access','Pretexting','Baiting','Tailgating','BEC','Awareness Training'], ['Phishing','Vishing','Physical Access','Pretexting','Baiting','Tailgating','BEC','Awareness Training']) %>"
target_scope: "<% tp.system.prompt('Target scope (emails/domains/locations)?') %>"
planned_start: "<% tp.system.prompt('Planned start date (YYYY-MM-DD)?') %>"
planned_end: "<% tp.system.prompt('Planned end date (YYYY-MM-DD)?') %>"
status: "<% tp.system.suggester(['Planned','In Progress','Completed','Paused','Cancelled'], ['Planned','In Progress','Completed','Paused','Cancelled']) %>"
classification: "Confidential"
ethics_confirmed: false
---
# Social Engineering Playbook — <% tp.file.title %>

> ⚠️ **Safety & Authorization**  
> Before proceeding: ensure `authorization_reference` is present and signed, legal counsel and client have approved the scope, and ethics_confirmed is set to `true`. Any deviation must be paused and escalated.

---

## 0 — Campaign Metadata
- **Client:** <% tp.frontmatter.client %>
- **Authorization / ROE:** <% tp.frontmatter.authorization_reference %>
- **Campaign type:** <% tp.frontmatter.campaign_type %>
- **Scope:** <% tp.frontmatter.target_scope %>
- **Window:** <% tp.frontmatter.planned_start %> → <% tp.frontmatter.planned_end %>
- **Status:** <% tp.frontmatter.status %>
- **Created:** <% tp.frontmatter.created %>
- **Owner / Operator:** <% tp.system.prompt('Operator / Red-team member?') %>

---

## 1 — Objectives & Success Criteria
- **Primary objective:** (e.g., test employee susceptibility, validate detection/responses, access physical area)
- **Success metrics:** (e.g., click rate > X%, credential capture, physical access obtained)
- **Allowed impact / limits:** (no credential exfil beyond test accounts, no destructive actions, etc.)
- **Fall-back / kill-switch:** (contact + codeword, immediate stop conditions)

---

## 2 — Legal & Ethical Checklist (MUST COMPLETE)
- [ ] Written authorization attached
- [ ] Scope and assets explicitly listed
- [ ] PI/Personal Data handling plan approved
- [ ] Incident reporting procedure defined
- [ ] Escalation contacts provided
- [ ] Client point-of-contact (POC) available during window

---

## 3 — Target Profile(s)
Use one profile per target (create a linked note per target if many).

### Target: `<% tp.system.prompt('Target name / role (e.g., Finance Analyst)?') %>`
- Department / Location:
- Role & privileges:
- Typical communications (email, slack, phone):
- Known tools / software:
- Linked notes: [[Target - <% tp.file.title %> - Profile]]

---

## 4 — Pretext & Narrative
- **Pretext summary:** (short story / reason for contact)
- **Persona name & details:** (name, role, company, backstory)
- **Supporting artifacts to craft:** (email signature, LinkedIn profile, voicemail greeting, fake ticket ID)
- **Delivery channel(s):** (email, phone, SMS, in-person)

---

## 5 — Message / Script Templates
Create concrete scripts for each channel. Keep versions for variants & A/B testing.

### Email (Phishing) Template
From: "Support Team" support@trusted-example.com  
To: <% tp.system.prompt('Target email?') %>  
Subject: <% tp.system.prompt('Email subject (urgent/action required)?') %>

Hi <% tp.system.prompt('Target first name?') %>,

[One-line reason for contact]. Please review the attached task and confirm by clicking the link below:

[Action Link] -> https://example.test/action?id=abc123

If you have any questions, reply to this message.

Thanks,  
<Signature>

### Vishing Script (Phone)
- Opening line:
- Verification pretext:
- Ask to perform action:
- Expected acceptance phrases:
- Abort conditions:

### Physical/Social (Tailgating / Baiting)
- Cover story:
- Props / badges:
- Entry approach:
- Observer positioning & exit strategy:

---

## 6 — Infrastructure & Tooling
- **Phishing domains / hosting:** (list test domains)
- **Mail server / SMTP provider:** 
- **Call spoofing / VOIP provider:** (if authorized)
- **Payload hosts / redirectors:** 
- **Tracking / telemetry:** (unique links, tracking pixels, form collectors)
- **Logging & evidence capture:** (PCAP, call recordings, screenshots)
- **Safety controls:** (no live creds; use captive/test accounts)

---

## 7 — Detection & Monitoring Plan
- **Blue-team contacts / POCs:**
- **SIEM rules to watch:** (names / examples)
- **Canaries & kill-switch monitors:** (how you’ll detect escalation)
- **Expected alerts:** (email click, suspicious login, anomalous traffic)
- **Data retention policy for captured artifacts**

---

## 8 — Data Handling & Evidence
- Evidence storage location:
- File naming convention:
- Access control for artifacts:
- Redaction policy for PII:
- Retention & deletion schedule:

---

## 9 — Post-Engagement Procedures
- **Immediate reporting:** To client POC & legal if required.
- **Debriefing:** Schedule within 48 hours (operator, client, defender).
- **Remediation support:** Provide prioritized recommendations, templates.
- **Retest window:** (date range)
- **Lessons learned & training materials:** (link to training deck)

---

## 10 — Results & Findings (to fill post-run)
- Total contacts made:
- Click rate:
- Credential captures (test accounts only):
- Calls answered / success:
- Physical access attempts: success/fail
- Notable human behaviors observed:

---

## 11 — Findings / Evidence Log (linked notes)
- [[SE-Finding-001-PhishClick]]
- [[SE-Finding-002-VishSuccess]]
- [[SE-Finding-003-Tailgate]]

Each finding note should use the Vulnerability_Record or Finding template and include evidence, timestamps, and remediation suggestions.

---

## 12 — Risk / Mitigation Recommendations
- Short-term quick wins:
- Policy changes:
- Technical controls:
- Training & awareness items:
- Suggested KPIs for future measurement:

---

## 13 — Lessons Learned / After Action Review
- What worked:
- What failed:
- Unexpected consequences:
- Improvements for next campaign:

---

## 14 — Audit Trail & Signatures
- Operator signature: <% tp.system.prompt('Operator initials?') %>
- Client approver: <% tp.system.prompt('Client approver initials?') %>
- Date signed: <% tp.date.now("YYYY-MM-DD") %>

---

## 15 — Dataview Friendly Inline Fields (for tracking)
- last_run:: <% tp.date.now("YYYY-MM-DD") %>
- next_planned:: <% tp.file.cursor() %>
- success_rate:: 
- evidence_count:: 0
- auth_ref:: <% tp.frontmatter.authorization_reference %>

---

### How to use this template
1. Put the file in `Templates/` as `Social_Engineering_Template.md`.  
2. Create a new note in your `Source Material/Tools/` or `Automation/` (or a `Reports/SE_Campaigns/` folder).  
3. Insert via **Templater → Insert template → Social_Engineering_Template.md**.  
4. Fill all authorization and legal checklist items *before* execution.  
5. Create one target profile note per target and link it under *Target Profile(s)*.  
6. After the campaign, create individual finding notes and link them in section 11.

---

