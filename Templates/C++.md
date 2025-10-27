# ⚙️ C++ Language Template

**Language:** C++  
**Version:** C++17 / C++20  
**Author:**  
**Date:**  

---

## 📚 Overview
C++ is a high-performance, compiled, general-purpose programming language that supports procedural, object-oriented, and generic programming.  
It’s widely used for systems programming, game development, embedded systems, and performance-critical applications.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Variable | Data container | `int x = 5;` |
| Function | Block of reusable code | `int add(int a, int b) { return a + b; }` |
| Class | Blueprint for objects | `class Car { ... };` |
| Object | Instance of a class | `Car myCar;` |
| Pointer | Stores memory address | `int* ptr = &x;` |
| Reference | Alias to variable | `int& ref = x;` |
| Template | Generic programming feature | `template<typename T> T add(T a, T b);` |

---

## 💬 Comments
    // Single-line comment

    /* Multi-line
       comment block */

---

## 🧮 Data Types
| Type | Example | Notes |
|------|----------|-------|
| int | `int a = 10;` | Integer |
| float | `float b = 3.14;` | Decimal (32-bit) |
| double | `double c = 2.718;` | Double-precision float |
| char | `char d = 'A';` | Single character |
| string | `string s = "Hello";` | Text (from `<string>`) |
| bool | `bool flag = true;` | Boolean |
| array | `int arr[3] = {1,2,3};` | Fixed-size list |
| vector | `vector<int> nums = {1,2,3};` | Dynamic array |

---

## ⚙️ Control Structures
### If / Else
    if (x > 0) {
        cout << "Positive";
    } else if (x == 0) {
        cout << "Zero";
    } else {
        cout << "Negative";
    }

### Loops
    // For loop
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }

    // While loop
    int n = 0;
    while (n < 5) {
        cout << n++ << endl;
    }

    // Do-while loop
    do {
        cout << "Running..." << endl;
    } while (false);

---

## 🧰 Functions
    #include <iostream>
    using namespace std;

    int add(int a, int b) {
        return a + b;
    }

    int main() {
        cout << add(5, 3);
        return 0;
    }

---

## 🧱 Classes & Objects
    #include <iostream>
    using namespace std;

    class Car {
    private:
        string model;
        int year;

    public:
        Car(string m, int y) {
            model = m;
            year = y;
        }

        void start() {
            cout << model << " (" << year << ") started." << endl;
        }
    };

    int main() {
        Car myCar("Tesla", 2025);
        myCar.start();
        return 0;
    }

---

## 🧩 Inheritance & Polymorphism
    class Vehicle {
    public:
        virtual void move() {
            cout << "Vehicle moving..." << endl;
        }
    };

    class Car : public Vehicle {
    public:
        void move() override {
            cout << "Car driving..." << endl;
        }
    };

    int main() {
        Vehicle* v = new Car();
        v->move();
        delete v;
        return 0;
    }

---

## 🧮 Pointers & References
    int x = 10;
    int* ptr = &x;
    cout << "Value: " << *ptr << endl;  // Dereference pointer

    int& ref = x;
    ref = 20;
    cout << x << endl; // 20

---

## 🔩 Templates
    template<typename T>
    T add(T a, T b) {
        return a + b;
    }

    int main() {
        cout << add<int>(3, 5);
        cout << add<double>(2.5, 4.1);
        return 0;
    }

---

## 🧰 Common Commands / Snippets
| Task | Command | Description |
|------|----------|-------------|
| Compile source | `g++ main.cpp -o main` | Compile program |
| Run program | `./main` | Execute binary |
| Check compiler version | `g++ --version` | Show GCC version |
| Add warnings | `g++ -Wall main.cpp` | Enable warnings |
| Use standard version | `g++ -std=c++20 main.cpp` | Specify C++ version |

---

## ⚡ Exception Handling
    #include <iostream>
    using namespace std;

    int main() {
        try {
            throw runtime_error("Something went wrong!");
        } catch (const exception& e) {
            cout << "Error: " << e.what() << endl;
        }
        return 0;
    }

---

## 🧰 File I/O
    #include <iostream>
    #include <fstream>
    using namespace std;

    int main() {
        ofstream out("output.txt");
        out << "Hello from C++!" << endl;
        out.close();

        ifstream in("output.txt");
        string line;
        getline(in, line);
        cout << line << endl;
        in.close();

        return 0;
    }

---

## 🧩 STL (Standard Template Library)
| Category | Example | Description |
|-----------|----------|-------------|
| Containers | `vector`, `map`, `set`, `queue` | Data structures |
| Algorithms | `sort()`, `find()`, `count()` | Common operations |
| Iterators | `begin()`, `end()` | Traverse containers |
| Utilities | `pair`, `tuple`, `optional` | General helpers |

### Example
    #include <vector>
    #include <algorithm>
    #include <iostream>
    using namespace std;

    int main() {
        vector<int> nums = {5, 1, 3, 2};
        sort(nums.begin(), nums.end());
        for (int n : nums) cout << n << " ";
        return 0;
    }

---

## 🧰 Memory Management
    int* data = new int[5];
    for (int i = 0; i < 5; i++) data[i] = i;
    delete[] data; // Always free heap memory

    // Smart pointer example (C++11+)
    #include <memory>
    auto ptr = make_unique<int>(42);
    cout << *ptr << endl;

---

## 🧰 Best Practices
- Always initialize variables  
- Prefer `std::string` over C-style strings  
- Use smart pointers (`unique_ptr`, `shared_ptr`) for memory safety  
- Avoid raw pointer ownership  
- Use `const` wherever possible  
- Use range-based `for` loops for cleaner iteration  
- Keep headers minimal; include only what you need  
- Use RAII (Resource Acquisition Is Initialization) for resource management  

---

## 🔍 Resources
- **C++ Reference:** https://en.cppreference.com/  
- **ISO C++ Guidelines:** https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines  
- **STL Overview:** https://cplusplus.com/reference/stl/  
- **Cheat Sheet:** https://github.com/mortennobel/cpp-cheatsheet  
- **Compiler Explorer:** https://godbolt.org/  

---

**Notes / Observations:**  
(Add your performance notes, memory handling quirks, or STL tips here.)
