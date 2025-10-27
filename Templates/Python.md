# 🐍 Python Language Template

**Language:** Python  
**Version:** 3.x  
**Author:**  
**Date:**  

---

## 📚 Overview
Python is an interpreted, high-level, general-purpose programming language known for its readability and extensive library ecosystem.  
It’s used for scripting, automation, web development, data analysis, and penetration testing.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Variable | Named reference to data | `user = "admin"` |
| Function | Reusable block of code | `def greet(): print("hi")` |
| Loop | Iteration construct | `for i in range(5): print(i)` |
| Conditional | Logic branching | `if user == "admin": access()` |
| Module | File containing Python code | `import os` |
| Package | Collection of modules with __init__.py | `import requests` |

---

## 💬 Comments
    # Single-line comment

    """
    Multi-line comment or docstring
    Describes function or module purpose
    """

---

## 🧮 Variables & Data Types
| Type | Example | Notes |
|------|----------|-------|
| String | `"Hello"` | Text sequence |
| Integer | `42` | Whole number |
| Float | `3.14` | Decimal number |
| Boolean | `True` / `False` | Logical values |
| List | `[1, 2, 3]` | Ordered, mutable |
| Tuple | `(1, 2, 3)` | Ordered, immutable |
| Set | `{1, 2, 3}` | Unordered, unique |
| Dict | `{"user": "admin", "id": 1}` | Key-value pairs |

---

## ⚙️ Control Structures
### If / Else
    if condition:
        do_this()
    elif other_condition:
        do_that()
    else:
        fallback()

### Loops
    for item in collection:
        print(item)

    while condition:
        repeat_action()

---

## 🧰 Functions
    def function_name(param1, param2="default"):
        """Describe what this function does."""
        return param1 + param2

---

## 🧩 Common Commands / Snippets
| Task | Code | Description |
|------|------|--------------|
| Print to console | `print("Hello")` | Display text |
| Get user input | `input("Enter value: ")` | Reads string input |
| Run script | `python script.py` | Executes file |
| Import module | `import os` | Bring in library |
| Check version | `python --version` | View interpreter version |

---

## 🧱 Error Handling
    try:
        risky_operation()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cleanup()

---

## 🔧 File Operations
    with open("file.txt", "r") as f:
        data = f.read()

    with open("output.txt", "w") as f:
        f.write("Saved content")

---

## 🧩 Modules & Libraries
| Library | Purpose | Example |
|----------|----------|----------|
| os | System operations | `os.listdir()` |
| sys | System info | `sys.argv` |
| re | Regular expressions | `re.findall()` |
| requests | HTTP requests | `requests.get(url)` |
| json | JSON handling | `json.loads(data)` |
| argparse | CLI parsing | `argparse.ArgumentParser()` |

---

## 🧱 Virtual Environments
    # Create
    python -m venv venv
    # Activate
    venv\Scripts\activate   # Windows
    source venv/bin/activate  # Linux
    # Deactivate
    deactivate

---

## 🧰 Best Practices
- Use `venv` for project isolation  
- Follow **PEP 8** style guidelines  
- Add docstrings for functions/classes  
- Handle exceptions properly  
- Use logging instead of print() in production  
- Keep functions small and focused  

---

## 🔍 Resources
- **Official Docs:** https://docs.python.org/3/  
- **PEP 8 Style Guide:** https://peps.python.org/pep-0008/  
- **PyPI:** https://pypi.org/  
- **Cheat Sheet:** https://github.com/gto76/python-cheatsheet  

---

**Notes / Observations:**  
(Add your own discoveries, tricks, or quirks here.)
