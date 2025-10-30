---
title: "Compare and Contrast Strategies to Protect Data"
tags: [networking, education, security, data-protection]
cssclass: cs-note
---

# Data Protection Strategies

## Overview
Protecting data is a core security objective. Effective programs combine multiple strategies across the data lifecycle — at rest, in transit, and in use — to achieve confidentiality, integrity, availability, and accountability.

## 1) Encryption
Turns plaintext into ciphertext to prevent unauthorized disclosure.

| Type | Description | Pros | Cons |
|------|-------------|------|------|
| Symmetric (AES) | One key to encrypt/decrypt | Fast, great for bulk | Key distribution
| Asymmetric (RSA/ECC) | Keypair (public/private) | Key exchange, signatures | Slower
| Full‑disk | Encrypts entire volumes | Device loss protection | Only protects when powered off
| App/Field | Encrypt specific fields | Fine‑grained | Key mgmt complexity
| Transport (TLS/IPsec) | Secures network comms | Prevents MITM/sniffing | Cert lifecycle

Principle: Confidentiality.

## 2) Access Control
Restricts who can view/modify data.

| Model | Description | Pros | Cons |
|------|-------------|------|------|
| RBAC | Role‑based access | Scalable | Role sprawl
| ABAC | Attribute‑based (context) | Fine‑grained/dynamic | Complex
| MAC | Labels/clearance | Strong policy | Rigid
| DAC | Owner decides | Simple | Risky decisions

Principle: Least privilege & need‑to‑know.

## 3) Masking & Tokenization
Reduces exposure in non‑prod/shared contexts.

| Technique | Description | Pros | Cons |
|-----------|-------------|------|------|
| Static masking | Irreversible obfuscation on copies | Safe for test/analytics | Not recoverable
| Dynamic masking | On‑the‑fly concealment | Live DB protection | Perf impact
| Tokenization | Reversible tokens in vault | PCI/PII friendly | Infra required

Principle: Data minimization.

## 4) DLP (Data Loss Prevention)
Monitors and blocks unauthorized movement of data.

| Approach | Function | Pros | Cons |
|---------|----------|------|------|
| Endpoint | Files/USB/print/email | Stops workstation leaks | Usability impact
| Network | Egress inspection | Detects bulk exfil | Encrypted traffic limits
| Cloud | SaaS/storage monitors | Controls cloud leaks | API coverage limits

Principle: Accountability & monitoring.

## 5) Integrity Controls
Ensures data remains accurate and untampered.

| Technique | Description | Pros | Cons |
|----------|-------------|------|------|
| Hashing | One‑way fingerprint | Detects change | No prevention
| Digital signatures | Hash + public key | Source + integrity | Key compromise risk
| Checksums/CRC | Transmission/storage checks | Detects corruption | Not crypto‑strong

Principle: Integrity.

## 6) Backup & Redundancy
Ensures recoverability and continuity.

| Method | Description | Pros | Cons |
|-------|-------------|------|------|
| Full | Complete copy | Simple restore | Storage heavy
| Incremental/Diff | Only changes | Efficient storage | Slower restore
| Replication | Real‑time copy | Near‑instant failover | Replicates corruption
| Immutable | Write‑once | Ransomware‑resistant | Mgmt overhead

Principle: Availability & recovery.

## 7) Classification & Lifecycle
Govern controls across data’s life.

| Phase | Example Control |
|-------|------------------|
| Creation | Label sensitivity (Public/Internal/Confidential) |
| Storage | Encrypt, restrict access, retention |
| Usage | Enforce policies, monitor DLP |
| Archival | Long‑term secure storage |
| Destruction | Secure wipe or physical destroy |

Principle: Governance.

## 8) Comparison Summary

| Strategy | Goal | Strengths | Best Used When |
|----------|------|-----------|----------------|
| Encryption | Confidentiality | Exposure control | External storage/transit |
| Access Control | Authorization | Limits access | Internal apps/systems |
| Mask/Tokenize | Privacy | Limits exposure | Lower envs/data sharing |
| DLP | Monitoring | Detects exfiltration | High‑risk environments |
| Integrity | Verification | Detects tampering | Critical transactions |
| Backup/DR | Continuity | Recovery | Disaster scenarios |
| Lifecycle | Governance | Aligns controls | Enterprise data mgmt |

## References
- NIST CSF, ISO 27001, CIS Controls v8
- OWASP, PCI DSS guidance
