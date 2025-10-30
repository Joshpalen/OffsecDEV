---
title: "<% tp.file.title %>"
tags:
  - review
  - questions
  - study
created: <% tp.date.now("YYYY-MM-DD") %>
topic: "<% tp.system.suggester(['Networking','Linux','OffSec','Programming','Tools','Exploitation','OSINT','IDS/IPS'], ['Networking','Linux','OffSec','Programming','Tools','Exploitation','OSINT','IDS/IPS']) %>"
difficulty: "<% tp.system.suggester(['Basic','Intermediate','Advanced'], ['Basic','Intermediate','Advanced']) %>"
source: "<% tp.system.prompt('Book/Tool/Concept Source?') %>"
status: "<% tp.system.suggester(['Unanswered','In Progress','Answered','Mastered'], ['Unanswered','In Progress','Answered','Mastered']) %>"
confidence: "<% tp.system.suggester(['Low','Medium','High'], ['Low','Medium','High']) %>"
review_interval_days: 7
next_review: <% tp.date.now("YYYY-MM-DD", +7) %>
cssclass: cs-note
---

# <% tp.file.title %>

> Purpose: Active-recall questions for reinforcing key concepts.

## Question Bank

### Core Concepts
| # | Question | Answer | Difficulty | Confidence |
|---|-----------|--------|------------|------------|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

### Application Scenarios
| # | Scenario / Case | Expected Reasoning / Answer |
|---|------------------|----------------------------|
| 1 |  |  |
| 2 |  |  |

### OffSec / Security-Specific
| # | Topic | Question | Expected Response |
|---|-------|----------|-------------------|
| 1 | Recon |  |  |
| 2 | Exploitation |  |  |
| 3 | Post-Exploitation |  |  |

## Quick Flashcards (inline syntax)
> For the Flashcards plugin (or for self-quiz later)

