# ☕ Java Language Template

**Language:** Java  
**Version:** 17+ (or applicable)  
**Author:**  
**Date:**  

---

## 📚 Overview
Java is a high-level, object-oriented programming language designed for portability, reliability, and scalability.  
It runs on the Java Virtual Machine (JVM) and is widely used for enterprise applications, Android development, and backend systems.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Class | Blueprint for objects | `class Car {}` |
| Object | Instance of a class | `Car myCar = new Car();` |
| Method | Function within a class | `void drive() {}` |
| Variable | Data storage identifier | `int speed = 100;` |
| Inheritance | Extending another class | `class Truck extends Car {}` |
| Interface | Contract of methods | `interface Vehicle { void move(); }` |
| Package | Namespace grouping classes | `package com.example;` |

---

## 💬 Comments
    // Single-line comment

    /* Multi-line comment block */

    /**
     * JavaDoc comment for documenting classes and methods.
     * @param name the user's name
     * @return greeting message
     */

---

## 🧮 Data Types
| Category | Types | Example |
|-----------|--------|----------|
| Primitive | `int`, `float`, `boolean`, `char`, `double`, `byte`, `short`, `long` | `int x = 10;` |
| Reference | `String`, `Arrays`, `Objects`, `Classes` | `String name = "Josh";` |

---

## ⚙️ Control Structures
### If / Else
    if (score > 90) {
        System.out.println("Excellent");
    } else if (score >= 70) {
        System.out.println("Good");
    } else {
        System.out.println("Needs Improvement");
    }

### Loops
    // For loop
    for (int i = 0; i < 5; i++) {
        System.out.println(i);
    }

    // While loop
    int count = 0;
    while (count < 5) {
        System.out.println(count++);
    }

    // Enhanced for loop
    for (String color : colors) {
        System.out.println(color);
    }

---

## 🧰 Methods
    public class Example {
        public static void greet(String name) {
            System.out.println("Hello, " + name + "!");
        }

        public static int add(int a, int b) {
            return a + b;
        }
    }

    // Calling methods
    Example.greet("Josh");
    int result = Example.add(5, 10);

---

## 🧱 Object-Oriented Programming
### Class Example
    public class Car {
        private String model;
        private int year;

        // Constructor
        public Car(String model, int year) {
            this.model = model;
            this.year = year;
        }

        // Method
        public void start() {
            System.out.println(model + " is starting...");
        }

        // Getter
        public String getModel() {
            return model;
        }
    }

    Car myCar = new Car("Tesla", 2025);
    myCar.start();

### Inheritance Example
    public class ElectricCar extends Car {
        private int batteryLevel;

        public ElectricCar(String model, int year, int batteryLevel) {
            super(model, year);
            this.batteryLevel = batteryLevel;
        }

        public void charge() {
            System.out.println("Charging battery...");
        }
    }

---

## 🔩 Interfaces & Abstract Classes
### Interface
    interface Vehicle {
        void move();
    }

    class Bike implements Vehicle {
        public void move() {
            System.out.println("Bike is moving...");
        }
    }

### Abstract Class
    abstract class Machine {
        abstract void start();
        void stop() {
            System.out.println("Machine stopped.");
        }
    }

---

## 🧩 Common Commands / Snippets
| Task | Command | Description |
|------|----------|-------------|
| Compile file | `javac Main.java` | Compile Java source |
| Run program | `java Main` | Execute compiled class |
| View version | `java -version` | Show installed version |
| Create JAR | `jar cf app.jar *.class` | Package compiled files |
| Run JAR | `java -jar app.jar` | Execute packaged app |

---

## ⚡ Exception Handling
    try {
        int result = 10 / 0;
    } catch (ArithmeticException e) {
        System.out.println("Error: " + e.getMessage());
    } finally {
        System.out.println("Operation complete.");
    }

---

## 📦 Packages & Imports
    package com.example.project;

    import java.util.List;
    import java.util.Scanner;

    public class App {
        public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            System.out.print("Enter name: ");
            String name = input.nextLine();
            System.out.println("Welcome, " + name);
        }
    }

---

## 🧰 File I/O Example
    import java.io.*;

    public class FileDemo {
        public static void main(String[] args) throws IOException {
            BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"));
            writer.write("Hello from Java!");
            writer.close();

            BufferedReader reader = new BufferedReader(new FileReader("output.txt"));
            System.out.println(reader.readLine());
            reader.close();
        }
    }

---

## 🧩 Collections Framework
    import java.util.*;

    List<String> list = new ArrayList<>();
    list.add("Alpha");
    list.add("Beta");

    for (String item : list) {
        System.out.println(item);
    }

    Map<String, Integer> scores = new HashMap<>();
    scores.put("Josh", 100);
    System.out.println(scores.get("Josh"));

---

## 🧰 Best Practices
- Follow **Java naming conventions** (`PascalCase` for classes, `camelCase` for methods/variables).  
- Always include a `package` declaration for organized code.  
- Use `try-with-resources` for auto-closing I/O streams.  
- Avoid using raw types — prefer generics (`List<String>`).  
- Handle exceptions explicitly and avoid swallowing them.  
- Keep each class in its own file.  
- Use Javadoc for public classes and methods.  

---

## 🧱 Build Tools
| Tool | Purpose | Example Command |
|------|----------|-----------------|
| Maven | Build automation & dependency management | `mvn clean package` |
| Gradle | Build system for modern Java | `gradle build` |
| JAR | Package compiled code | `jar cf app.jar *.class` |

---

## 🔍 Resources
- **Official Docs:** https://docs.oracle.com/en/java/  
- **OpenJDK Docs:** https://openjdk.org/  
- **Maven Repository:** https://mvnrepository.com/  
- **Style Guide:** https://google.github.io/styleguide/javaguide.html  
- **Cheat Sheet:** https://introcs.cs.princeton.edu/java/11cheatsheet/  

---

**Notes / Observations:**  
(Add personal tips, syntax quirks, or JVM tuning notes here.)
