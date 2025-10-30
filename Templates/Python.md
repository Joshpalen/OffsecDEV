---
title: "Python"
type: language
tags: [cs, language, python]
cssclass: cs-note
---

# Python

## Overview
Python is an interpreted, high-level language known for readability and an extensive ecosystem. Commonly used for scripting, automation, web, data, and security tooling.

## Key Concepts
| Concept | Description | Example |
|---------|-------------|---------|
| Variable | Named reference to data | `user = "admin"` |
| Function | Reusable block of code | `def greet(): ...` |
| Loop | Iterate over items | `for i in range(5):` |
| Conditional | Branch logic | `if x > 0:` |
| Module | File of Python code | `import os` |
| Package | Collection of modules | `import requests` |

## Comments
```python
# Single-line comment
"""
Multi-line comment or docstring
"""
```

## Data Types
| Type | Example | Notes |
|------|---------|-------|
| str | `"Hello"` | Text |
| int | `42` | Whole number |
| float | `3.14` | Decimal |
| bool | `True` | Logical |
| list | `[1,2,3]` | Ordered, mutable |
| tuple | `(1,2,3)` | Ordered, immutable |
| set | `{1,2,3}` | Unique elements |
| dict | `{ "k": 1 }` | Key-value |

## Control Flow
```python
if condition:
    do_this()
elif other:
    do_that()
else:
    fallback()

for item in items:
    print(item)

while cond:
    repeat()
```

## Error Handling
```python
try:
    risky()
except Exception as e:
    print(e)
finally:
    cleanup()
```

## File I/O
```python
with open("file.txt", "r") as f:
    data = f.read()
```

## Common Libraries
| Library | Purpose | Example |
|---------|---------|---------|
| os | System ops | `os.listdir()` |
| sys | Runtime info | `sys.argv` |
| re | Regex | `re.findall()` |
| requests | HTTP | `requests.get(url)` |
| json | JSON | `json.loads(data)` |
| argparse | CLI parsing | `ArgumentParser()` |

## Virtual Environments
```bash
python -m venv venv
# Activate: venv\Scripts\activate (Win) or source venv/bin/activate (Unix)
deactivate
```

## Best Practices
- Use venv for isolation
- Follow PEP 8
- Docstrings for functions/classes
- Prefer logging to print

## Related
[[Templates/Algorithm]] • [[Templates/Data_Structure]] • [[Templates/Concept]]

## Resources
- Docs: https://docs.python.org/3/
- PEP 8: https://peps.python.org/pep-0008/
- Cheat sheet: https://github.com/gto76/python-cheatsheet

