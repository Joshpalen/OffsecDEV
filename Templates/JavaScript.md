# ⚡ JavaScript Language Template

**Language:** JavaScript  
**Version:** ES6+  
**Author:**  
**Date:**  

---

## 📚 Overview
JavaScript is a high-level, interpreted programming language primarily used for web development.  
It enables dynamic, interactive, and event-driven functionality in browsers and also runs server-side via Node.js.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Variable | Named data container | `let user = "Josh";` |
| Function | Reusable block of code | `function greet() { console.log("Hi"); }` |
| Object | Key-value pair structure | `let person = { name: "Josh", role: "Dev" };` |
| Array | Ordered list of values | `let colors = ["red", "blue"];` |
| Promise | Asynchronous operation | `fetch(url).then(res => res.json());` |
| Arrow Function | Shorter function syntax | `const add = (a,b) => a+b;` |

---

## 💬 Comments
    // Single-line comment

    /*
      Multi-line comment block
      Describes logic or function
    */

---

## 🧮 Variables & Data Types
| Type | Example | Notes |
|------|----------|-------|
| String | `"Hello"` | Text sequence |
| Number | `42`, `3.14` | Integer or float |
| Boolean | `true` / `false` | Logical values |
| Array | `[1, 2, 3]` | Ordered list |
| Object | `{key: "value"}` | Key-value pairs |
| Null | `null` | Explicit empty value |
| Undefined | `undefined` | Uninitialized variable |
| Symbol | `Symbol("id")` | Unique immutable identifier |

---

## ⚙️ Variable Declarations
    var name = "old style";     // Function-scoped
    let user = "Josh";          // Block-scoped (preferred)
    const ROLE = "Admin";       // Constant, cannot be reassigned

---

## 🔁 Control Structures
### If / Else
    if (score > 90) {
        console.log("Excellent");
    } else if (score >= 70) {
        console.log("Good");
    } else {
        console.log("Needs Improvement");
    }

### Loops
    // For loop
    for (let i = 0; i < 5; i++) {
        console.log(i);
    }

    // For...of
    for (let color of colors) {
        console.log(color);
    }

    // For...in
    for (let key in person) {
        console.log(key, person[key]);
    }

    // While loop
    while (condition) {
        doSomething();
    }

---

## 🧰 Functions
    // Function declaration
    function greet(name) {
        console.log(`Hello, ${name}!`);
    }

    // Function expression
    const greetUser = function(name) {
        return `Welcome, ${name}!`;
    };

    // Arrow function
    const add = (a, b) => a + b;

---

## ⚡ Asynchronous JavaScript
    // Callback
    setTimeout(() => console.log("Done!"), 1000);

    // Promise
    fetch("https://api.example.com/data")
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(err => console.error(err));

    // Async/Await
    async function loadData() {
        try {
            const response = await fetch("https://api.example.com/data");
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error(error);
        }
    }

---

## 🔧 Objects & Arrays
    // Object
    const user = {
        name: "Josh",
        role: "Developer",
        greet() {
            console.log(`Hi, I'm ${this.name}`);
        }
    };

    // Array methods
    const nums = [1, 2, 3, 4];
    nums.forEach(n => console.log(n));
    let doubled = nums.map(n => n * 2);
    let even = nums.filter(n => n % 2 === 0);
    let total = nums.reduce((sum, n) => sum + n, 0);

---

## 🧩 Common Commands / Snippets
| Task | Code | Description |
|------|------|-------------|
| Print to console | `console.log("Hello")` | Output text |
| Template literal | `` `Name: ${name}` `` | String interpolation |
| Import module (ESM) | `import fs from 'fs';` | Modern syntax |
| Import (CommonJS) | `const fs = require('fs');` | Node.js classic syntax |
| Run file | `node script.js` | Execute JavaScript |
| Check version | `node -v` | Node.js version |

---

## 🧱 Error Handling
    try {
        riskyOperation();
    } catch (error) {
        console.error("Error:", error.message);
    } finally {
        console.log("Cleanup complete");
    }

---

## 🌐 DOM Manipulation (Browser)
    document.getElementById("demo").innerText = "Updated!";
    document.querySelectorAll(".item").forEach(el => el.style.color = "red");
    document.addEventListener("click", () => alert("Clicked!"));

---

## 🔩 Modules & Libraries
| Library | Purpose | Example |
|----------|----------|----------|
| fs | File operations (Node.js) | `fs.readFileSync("file.txt")` |
| path | File paths | `path.join(__dirname, "file.txt")` |
| http | Web server | `http.createServer(...).listen(8080)` |
| axios | HTTP client | `axios.get(url)` |
| express | Web framework | `app.get("/", (req,res)=>res.send("Hi"))` |
| chalk | Console colors | `chalk.green("Success!")` |
| dotenv | Env variables | `require('dotenv').config()` |

---

## 🧰 Best Practices
- Always use `let` and `const` (avoid `var`)  
- Use strict mode (`"use strict";`)  
- Modularize code using imports/exports  
- Handle promises with `try...catch` in async functions  
- Avoid callback hell — prefer Promises or async/await  
- Use meaningful variable and function names  
- Validate user input before processing  

---

## 🔍 Resources
- **MDN Docs:** https://developer.mozilla.org/en-US/docs/Web/JavaScript  
- **Node.js Docs:** https://nodejs.org/en/docs/  
- **JavaScript Info:** https://javascript.info/  
- **Cheat Sheet:** https://htmlcheatsheet.com/js/  

---

**Notes / Observations:**  
(Add your personal discoveries, quirks, or snippets here.)
