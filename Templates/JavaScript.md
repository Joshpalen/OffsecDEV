---
title: "JavaScript"
type: language
tags: [cs, language, javascript]
cssclass: cs-note
---

# JavaScript

## Overview
High-level, dynamic language for the web and Node.js. Event-driven and single-threaded with async primitives.

## Key Concepts
| Concept | Description | Example |
|---------|-------------|---------|
| Variable | let/const scoped | `let x = 1;` |
| Function | First-class functions | `const f = (x) => x+1;` |
| Promise | Async operations | `fetch(url).then(...)` |
| Module | ES modules | `import x from 'mod'` |

## Control Flow
```js
if (cond) { /* ... */ } else { /* ... */ }
for (const x of arr) { /* ... */ }
while (cond) { /* ... */ }
```

## Error Handling
```js
try { risky(); } catch (e) { console.error(e); } finally { cleanup(); }
```

## Node.js
| Task | Command |
|------|---------|
| Run | `node file.js` |
| Init | `npm init -y` |
| Install | `npm i <pkg>` |

## Related
[[Templates/Algorithm]] • [[Templates/Data_Structure]] • [[Templates/Concept]]

## Resources
- MDN: https://developer.mozilla.org/
- Node.js: https://nodejs.org/

