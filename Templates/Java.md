---
title: "Java"
type: language
tags: [cs, language, java]
cssclass: cs-note
---

# Java

## Overview
Object-oriented language targeting the JVM, used widely in enterprise and Android. Strong typing, GC, and rich ecosystem.

## Key Concepts
| Concept | Description | Example |
|---------|-------------|---------|
| Class/Object | Blueprint/instance | `class Car {}` / `new Car()` |
| Method | Behavior | `void drive() {}` |
| Interface | Contract | `interface Vehicle { void move(); }` |
| Package | Namespace | `package com.example;` |

## Control Flow
```java
if (x > 0) { /* ... */ } else { /* ... */ }
for (int i = 0; i < n; i++) { /* ... */ }
while (cond) { /* ... */ }
```

## Error Handling
```java
try { risky(); } catch (Exception e) { e.printStackTrace(); } finally { cleanup(); }
```

## Build/Run
| Task | Command |
|------|---------|
| Compile | `javac Main.java` |
| Run | `java Main` |
| Jar | `jar cf app.jar *.class` |

## Collections
List, Map, Set via `java.util` with generics: `List<String> xs = new ArrayList<>();`

## Related
[[Templates/Algorithm]] • [[Templates/Data_Structure]] • [[Templates/Concept]]

## Resources
- Docs: https://docs.oracle.com/en/java/
- OpenJDK: https://openjdk.org/

