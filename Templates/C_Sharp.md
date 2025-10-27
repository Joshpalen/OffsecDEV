# 🧱 C# Language Template

**Language:** C#  
**Version:** .NET 6+  
**Author:**  
**Date:**  

---

## 📚 Overview
C# (pronounced “C-Sharp”) is a modern, object-oriented programming language developed by Microsoft for the .NET platform.  
It’s used for desktop, web, cloud, mobile, and game development (Unity).  
C# combines the performance of compiled languages with the productivity of managed code.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Variable | Named data container | `int score = 100;` |
| Method | Reusable block of code | `void Greet() { Console.WriteLine("Hi"); }` |
| Class | Blueprint for objects | `class Car { }` |
| Object | Instance of a class | `Car myCar = new Car();` |
| Property | Encapsulated field | `public string Name { get; set; }` |
| Namespace | Logical grouping of classes | `namespace Project.Core { }` |
| Interface | Defines contract of methods | `interface IVehicle { void Drive(); }` |

---

## 💬 Comments
    // Single-line comment

    /* Multi-line
       comment block */

    /// XML Documentation
    /// <summary>
    /// Describes a method or class.
    /// </summary>

---

## 🧮 Data Types
| Category | Types | Example |
|-----------|--------|----------|
| Value Types | `int`, `double`, `bool`, `char`, `float`, `decimal` | `int x = 10;` |
| Reference Types | `string`, `object`, `array`, `class` | `string name = "Josh";` |
| Nullable Types | `int? age = null;` | Allows null on value types |
| Enum | `enum Role { Admin, User }` | Named constants |

---

## ⚙️ Control Structures
### If / Else
    if (score > 90) {
        Console.WriteLine("Excellent");
    } else if (score >= 70) {
        Console.WriteLine("Good");
    } else {
        Console.WriteLine("Try again");
    }

### Loops
    // For loop
    for (int i = 0; i < 5; i++) {
        Console.WriteLine(i);
    }

    // While loop
    int n = 0;
    while (n < 3) {
        Console.WriteLine(n++);
    }

    // Foreach
    string[] colors = {"Red", "Blue", "Green"};
    foreach (var color in colors) {
        Console.WriteLine(color);
    }

---

## 🧰 Methods
    public class Example {
        public static void Greet(string name) {
            Console.WriteLine($"Hello, {name}!");
        }

        public int Add(int a, int b) {
            return a + b;
        }
    }

    Example.Greet("Josh");

---

## 🧱 Classes & Objects
    public class Car {
        // Fields
        private string model;
        private int year;

        // Constructor
        public Car(string model, int year) {
            this.model = model;
            this.year = year;
        }

        // Property
        public string Model {
            get { return model; }
            set { model = value; }
        }

        // Method
        public void Start() {
            Console.WriteLine($"{model} ({year}) is starting...");
        }
    }

    Car myCar = new Car("Tesla", 2025);
    myCar.Start();

---

## 🧩 Inheritance & Polymorphism
    public class Vehicle {
        public virtual void Move() {
            Console.WriteLine("Vehicle moving...");
        }
    }

    public class Car : Vehicle {
        public override void Move() {
            Console.WriteLine("Car driving...");
        }
    }

    Vehicle v = new Car();
    v.Move();

---

## ⚡ Interfaces & Abstract Classes
### Interface
    interface IVehicle {
        void Drive();
    }

    class Bike : IVehicle {
        public void Drive() {
            Console.WriteLine("Bike is driving...");
        }
    }

### Abstract Class
    abstract class Machine {
        public abstract void Start();
        public void Stop() {
            Console.WriteLine("Machine stopped.");
        }
    }

---

## 🧩 Properties & Auto-Implemented Properties
    public class Person {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    var user = new Person { Name = "Josh", Age = 30 };
    Console.WriteLine(user.Name);

---

## 🔩 Collections
    using System.Collections.Generic;

    List<string> names = new List<string> { "Alice", "Bob" };
    names.Add("Charlie");
    foreach (var n in names) Console.WriteLine(n);

    Dictionary<string, int> scores = new Dictionary<string, int> {
        {"Josh", 100},
        {"Sam", 90}
    };
    Console.WriteLine(scores["Josh"]);

---

## 🧱 Exception Handling
    try {
        int x = 5 / 0;
    } catch (DivideByZeroException ex) {
        Console.WriteLine("Error: " + ex.Message);
    } finally {
        Console.WriteLine("Cleanup complete.");
    }

---

## 🧰 File I/O
    using System.IO;

    File.WriteAllText("data.txt", "Hello, C#!");
    string content = File.ReadAllText("data.txt");
    Console.WriteLine(content);

---

## ⚙️ LINQ (Language Integrated Query)
    using System.Linq;

    int[] numbers = {1, 2, 3, 4, 5};
    var even = numbers.Where(n => n % 2 == 0);
    foreach (var n in even) Console.WriteLine(n);

---

## 🧱 Async & Await
    using System.Threading.Tasks;

    async Task FetchData() {
        await Task.Delay(1000);
        Console.WriteLine("Data loaded!");
    }

    await FetchData();

---

## 🧩 Common Commands / Snippets
| Task | Command | Description |
|------|----------|-------------|
| Create project | `dotnet new console -n MyApp` | New .NET app |
| Build project | `dotnet build` | Compile code |
| Run app | `dotnet run` | Execute app |
| Add package | `dotnet add package Newtonsoft.Json` | Install NuGet package |
| List SDKs | `dotnet --list-sdks` | View SDKs installed |
| Publish app | `dotnet publish -c Release` | Create deployable build |

---

## 🧰 Best Practices
- Use **PascalCase** for class/method names and **camelCase** for variables.  
- Favor properties over public fields.  
- Use `var` for inferred types when obvious.  
- Prefer `async/await` over callbacks.  
- Always handle exceptions gracefully.  
- Keep classes single-responsibility (SRP).  
- Use `using` statements for IDisposable resources.  
- Follow .NET coding conventions and XML documentation for APIs.  

---

## 🧠 Namespaces & Imports
    using System;
    using System.Collections.Generic;

    namespace DemoApp {
        class Program {
            static void Main(string[] args) {
                Console.WriteLine("Hello, C# World!");
            }
        }
    }

---

## 🧰 Build Tools
| Tool | Purpose | Example |
|------|----------|----------|
| dotnet CLI | Manage .NET projects | `dotnet run` |
| MSBuild | Build automation | `msbuild MyApp.csproj` |
| NuGet | Dependency management | `nuget install PackageName` |
| Visual Studio / VS Code | IDEs for development | — |

---

## 🔍 Resources
- **Microsoft Docs:** https://learn.microsoft.com/en-us/dotnet/csharp/  
- **.NET CLI Guide:** https://learn.microsoft.com/en-us/dotnet/core/tools/  
- **C# Style Guide:** https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/  
- **Cheat Sheet:** https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/csharp.md  
- **LINQ Examples:** https://linqsamples.com/  

---

**Notes / Observations:**  
(Add any custom syntax tricks, performance notes, or Unity-specific patterns here.)
