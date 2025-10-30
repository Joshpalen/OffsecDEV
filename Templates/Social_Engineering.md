---
title: "<% tp.file.title %>"
tags: [social-engineering, red-team, playbook]
created: <% tp.date.now("YYYY-MM-DD") %>
client: "<% tp.system.prompt('Client Name?') %>"
authorization_reference: "<% tp.system.prompt('Auth Doc / ROE ID?') %>"
campaign_type: "<% tp.system.suggester(['Phishing','Vishing','Physical Access','Pretexting','Baiting','Tailgating','BEC','Awareness Training'], ['Phishing','Vishing','Physical Access','Pretexting','Baiting','Tailgating','BEC','Awareness Training']) %>"
target_scope: "<% tp.system.prompt('Target scope (emails/domains/locations)?') %>"
planned_start: "<% tp.system.prompt('Planned start date (YYYY-MM-DD)?') %>"
planned_end: "<% tp.system.prompt('Planned end date (YYYY-MM-DD)?') %>"
status: "<% tp.system.suggester(['Planned','In Progress','Completed','Paused','Cancelled'], ['Planned','In Progress','Completed','Paused','Cancelled']) %>"
classification: "Confidential"
ethics_confirmed: false
cssclass: cs-note
---

# Social Engineering Playbook — <% tp.file.title %>

> [!warning] Safety & Authorization
> Ensure authorization_reference is present and signed, scope approved, and ethics_confirmed is true. Pause and escalate on any deviation.

## 0. Campaign Metadata
- Client: <% tp.frontmatter.client %>  
- Authorization / ROE: <% tp.frontmatter.authorization_reference %>  
- Type: <% tp.frontmatter.campaign_type %>  
- Scope: <% tp.frontmatter.target_scope %>  
- Window: <% tp.frontmatter.planned_start %> → <% tp.frontmatter.planned_end %>  
- Status: <% tp.frontmatter.status %>  
- Owner / Operator: <% tp.system.prompt('Operator / Red-team member?') %>

## 1. Objectives & Success Criteria
- Primary objective:  
- Success metrics:  
- Allowed impact / limits:  
- Fallback / kill-switch:  

## 2. Legal & Ethical Checklist
- [ ] Written authorization attached  
- [ ] Scope assets listed  
- [ ] PII handling plan approved  
- [ ] Incident reporting defined  
- [ ] Escalation contacts provided  
- [ ] Client POC available during window  

## 3. Target Profiles
Use one profile per target (link separate notes if many).

### Target: `<% tp.system.prompt('Target name / role?') %>`
- Department / Location:  
- Role & privileges:  
- Typical comms: email, chat, phone  
- Known tools / software:  
- Linked notes: [[Target - <% tp.file.title %> - Profile]]

## 4. Pretext & Narrative
- Pretext summary:  
- Persona details: name, role, company, backstory  
- Supporting artifacts: signature, profile, voicemail, ticket ID  
- Delivery channels: email, phone, SMS, in-person  

## 5. Message / Script Templates
### Email (Phishing)
From: "Support Team" support@example.com  
To: <% tp.system.prompt('Target email?') %>  
Subject: <% tp.system.prompt('Subject?') %>

Hi <% tp.system.prompt('Target first name?') %>,

[One-line reason]. Please review and confirm via the link below:

Action: https://example.test/action?id=abc123

Thanks,  
<Signature>

### Vishing (Phone)
- Opening line:  
- Verification pretext:  
- Ask to perform action:  
- Acceptance phrases:  
- Abort conditions:  

### Physical (Tailgating / Baiting)
- Cover story:  
- Props / badges:  
- Entry approach:  
- Observer & exit strategy:  

## 6. Infrastructure & Tooling
- Phishing domains / hosting:  
- SMTP provider:  
- Call spoofing / VOIP:  
- Payload hosts / redirectors:  
- Tracking / telemetry:  
- Logging & evidence capture: PCAP, recordings, screenshots  
- Safety controls: captive/test accounts only  

## 7. Detection & Monitoring
- Blue-team POCs:  
- SIEM rules to watch:  
- Canaries & kill-switch monitors:  
- Expected alerts:  
- Data retention policy:  

## 8. Data Handling & Evidence
- Storage location:  
- File naming convention:  
- Access control:  
- Redaction policy for PII:  
- Retention & deletion schedule:  

## 9. Post-Engagement
- Immediate reporting to client POC  
- Debrief within 48 hours  
- Remediation recommendations  
- Retest window  
- Lessons learned & training materials  

## 10. Results & Findings
- Total contacts:  
- Click rate:  
- Credential captures (test accounts only):  
- Calls answered / success:  
- Physical access attempts: success/fail  
- Notable behaviors:  

## 11. Findings / Evidence Log
- [[SE-Finding-001-PhishClick]]  
- [[SE-Finding-002-VishSuccess]]  
- [[SE-Finding-003-Tailgate]]

## 12. Risk / Mitigation Recommendations
- Quick wins:  
- Policy changes:  
- Technical controls:  
- Training & awareness:  
- KPIs for future measurement:  

## 13. Signatures
- Operator: <% tp.system.prompt('Operator initials?') %>  
- Client approver: <% tp.system.prompt('Client approver initials?') %>  
- Date: <% tp.date.now("YYYY-MM-DD") %>

