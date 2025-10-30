---
title: "C#"
type: language
tags: [cs, language, csharp]
cssclass: cs-note
---

# C#

## Overview
Modern, object-oriented language for .NET. Used for desktop, web, cloud, and game dev (Unity).

## Key Concepts
| Concept | Description | Example |
|---------|-------------|---------|
| Class/Object | Blueprint/instance | `class Car {}` / `new Car()` |
| Property | Encapsulated field | `public string Name { get; set; }` |
| Interface | Contract | `interface IVehicle { void Drive(); }` |
| Namespace | Grouping | `namespace Project.Core { }` |

## Control Flow
```csharp
if (x > 0) { /* ... */ } else { /* ... */ }
for (int i = 0; i < n; i++) { /* ... */ }
while (cond) { /* ... */ }
```

## Error Handling
```csharp
try { risky(); } catch (Exception ex) { Console.WriteLine(ex); } finally { cleanup(); }
```

## dotnet CLI
| Task | Command |
|------|---------|
| New console | `dotnet new console -n App` |
| Restore/Build/Run | `dotnet restore` -$ `dotnet build` -$ `dotnet run` |
| Add package | `dotnet add package <Name>` |

## Related
[[Templates/Algorithm]] -$ [[Templates/Data_Structure]] -$ [[Templates/Concept]]

## Resources
- Docs: https://learn.microsoft.com/dotnet/csharp/
- .NET CLI: https://learn.microsoft.com/dotnet/core/tools/



