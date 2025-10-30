---
title: "C++"
type: language
tags: [cs, language, cpp]
cssclass: cs-note
---

# C++

## Overview
Compiled, high-performance language supporting procedural, object-oriented, and generic paradigms. Used for systems and performance-critical software.

## Key Concepts
| Concept | Description | Example |
|---------|-------------|---------|
| Variable | Data container | `int x = 5;` |
| Function | Reusable code | `int add(int a,int b){return a+b;}` |
| Class | Blueprint | `class Car { ... };` |
| Pointer | Address | `int* p = &x;` |
| Reference | Alias | `int& r = x;` |

## Control Flow
```cpp
if (x>0) { /*...*/ } else { /*...*/ }
for (int i=0;i<n;i++) { /*...*/ }
while (cond) { /*...*/ }
```

## Build/Run
| Task | Command |
|------|---------|
| Compile | `g++ -std=c++20 main.cpp -O2 -o app` |
| Run | `./app` |

## STL Basics
`vector`, `map`, algorithms like `sort`, `find`.

## Related
[[Templates/Algorithm]] • [[Templates/Data_Structure]] • [[Templates/Concept]]

## Resources
- cppreference: https://en.cppreference.com/
- Core Guidelines: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

