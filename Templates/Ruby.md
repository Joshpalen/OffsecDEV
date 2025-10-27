# 💎 Ruby Language Template

**Language:** Ruby  
**Version:** 3.x (or applicable)  
**Author:**  
**Date:**  

---

## 📚 Overview
Ruby is a dynamic, open-source, object-oriented programming language designed for simplicity and productivity.  
It’s often used for scripting, automation, and web development (especially with Ruby on Rails).

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Variable | Named reference to data | `user = "admin"` |
| Method | Function attached to an object | `def greet; puts "hi"; end` |
| Block | Anonymous code chunk | `[1,2,3].each { |n| puts n }` |
| Class | Blueprint for objects | `class Person; end` |
| Module | Namespaced collection of methods | `module Tools; end` |

---

## 💬 Comments
    # Single-line comment

    =begin
    Multi-line comment or documentation block
    =end

---

## 🧮 Variables & Data Types
| Type | Example | Notes |
|------|----------|-------|
| String | `"Hello"` | Immutable text |
| Integer | `42` | Whole number |
| Float | `3.14` | Decimal number |
| Boolean | `true` / `false` | Logical values |
| Array | `[1, 2, 3]` | Ordered list |
| Hash | `{ "key" => "value" }` | Key-value pairs |
| Symbol | `:name` | Lightweight immutable identifier |
| Nil | `nil` | Represents “nothing” |

---

## ⚙️ Control Structures
### If / Else
    if condition
      do_something
    elsif other_condition
      do_something_else
    else
      fallback
    end

### Loops
    # While loop
    while condition
      puts "Repeating"
    end

    # Until loop
    until condition
      puts "Repeating until done"
    end

    # For loop
    for i in 0..5
      puts i
    end

    # Each iterator
    [1,2,3].each do |num|
      puts num
    end

---

## 🧰 Methods
    def greet(name)
      puts "Hello, #{name}!"
    end

    greet("Josh")

---

## 🧩 Common Commands / Snippets
| Task | Code | Description |
|------|------|-------------|
| Print to console | `puts "Hello"` | Outputs text with newline |
| Inline print | `print "Hello"` | No newline |
| Get user input | `name = gets.chomp` | Reads input |
| Run file | `ruby script.rb` | Executes script |
| View version | `ruby -v` | Shows interpreter version |

---

## 🧱 Error Handling
    begin
      risky_operation
    rescue => e
      puts "Error: #{e.message}"
    ensure
      puts "Cleanup actions"
    end

---

## 🔧 File Operations
    # Read file
    File.open("file.txt", "r") do |f|
      puts f.read
    end

    # Write file
    File.open("output.txt", "w") do |f|
      f.puts "Hello World"
    end

---

## 🧩 Modules & Libraries
| Library | Purpose | Example |
|----------|----------|----------|
| File | File operations | `File.read("file.txt")` |
| Net::HTTP | Web requests | `Net::HTTP.get(URI(url))` |
| JSON | Parse / generate JSON | `JSON.parse(data)` |
| OpenSSL | Encryption | `OpenSSL::Cipher.new("AES-256-CBC")` |
| Digest | Hashing | `Digest::SHA256.hexdigest("text")` |

---

## 💎 Object-Oriented Example
    class Person
      attr_accessor :name, :role

      def initialize(name, role)
        @name = name
        @role = role
      end

      def greet
        puts "Hello, I'm #{@name}, the #{@role}."
      end
    end

    user = Person.new("Josh", "Developer")
    user.greet

---

## 🧰 Best Practices
- Follow the Ruby style guide (snake_case methods, 2-space indentation)  
- Use symbols for hash keys when possible (`{ name: "Josh" }`)  
- Prefer `each`, `map`, and iterators over manual loops  
- Handle exceptions gracefully with `rescue`  
- Keep methods short and focused  
- Use `puts` for output, `p` for debugging  

---

## 🔍 Resources
- **Official Docs:** https://www.ruby-lang.org/en/documentation/  
- **Ruby Style Guide:** https://rubystyle.guide/  
- **RubyGems:** https://rubygems.org/  
- **Cheat Sheet:** https://devhints.io/ruby  

---

**Notes / Observations:**  
(Add your personal findings, snippets, or gotchas here.)
