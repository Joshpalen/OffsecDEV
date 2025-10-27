# 🐫 Perl Language Template

**Language:** Perl  
**Version:** 5.x (or applicable)  
**Author:**  
**Date:**  

---

## 📚 Overview
Perl is a high-level, interpreted scripting language known for its text processing power, flexibility, and strong regular expression support.  
It’s widely used in system administration, network programming, web development (CGI), and data parsing.

---

## 🧠 Key Concepts
| Concept | Description | Example |
|----------|--------------|----------|
| Scalar | Single value (string, number) | `$name = "Josh";` |
| Array | Ordered list of scalars | `@colors = ("red", "blue", "green");` |
| Hash | Key-value pairs | `%user = ("name" => "Josh", "role" => "Admin");` |
| Subroutine | Function definition | `sub greet { print "Hello!"; }` |
| Context | Determines behavior (scalar vs list) | `scalar(@array)` |

---

## 💬 Comments
    # Single-line comment

    =begin
    Multi-line comment block
    =end

---

## 🧮 Variables & Data Types
| Type | Prefix | Example | Notes |
|------|---------|----------|-------|
| Scalar | `$` | `$x = 42;` | Single value |
| Array | `@` | `@nums = (1, 2, 3);` | Indexed list |
| Hash | `%` | `%hash = ("key" => "value");` | Key-value pairs |
| Reference | `\` | `$ref = \@array;` | Pointer-like reference |

---

## ⚙️ Control Structures
### If / Else
    if ($x > 10) {
        print "High\n";
    } elsif ($x == 10) {
        print "Equal\n";
    } else {
        print "Low\n";
    }

### Loops
    # For loop
    for (my $i = 0; $i < 5; $i++) {
        print "$i\n";
    }

    # Foreach
    foreach my $color (@colors) {
        print "$color\n";
    }

    # While loop
    while ($count < 10) {
        $count++;
    }

---

## 🧰 Subroutines (Functions)
    sub greet {
        my ($name) = @_;
        print "Hello, $name!\n";
    }

    greet("Josh");

---

## 🧩 Common Commands / Snippets
| Task | Code | Description |
|------|------|-------------|
| Print text | `print "Hello\n";` | Output to console |
| Get input | `chomp($name = <STDIN>);` | Remove newline |
| Run file | `perl script.pl` | Execute program |
| Use strict mode | `use strict; use warnings;` | Enforce safe coding |
| Check version | `perl -v` | Show interpreter version |

---

## 🧱 Error Handling
    eval {
        risky_function();
    };
    if ($@) {
        print "Error: $@\n";
    }

---

## 🔧 File Operations
    # Read file
    open(my $fh, "<", "input.txt") or die "Cannot open file: $!";
    while (my $line = <$fh>) {
        print $line;
    }
    close($fh);

    # Write file
    open(my $out, ">", "output.txt") or die "Cannot write file: $!";
    print $out "Perl is awesome!\n";
    close($out);

---

## 🧩 Modules & Libraries
| Module | Purpose | Example |
|---------|----------|----------|
| strict / warnings | Safer code | `use strict; use warnings;` |
| File::Copy | Copy files | `copy("a.txt", "b.txt");` |
| File::Basename | Parse file paths | `basename($path)` |
| Getopt::Long | Parse CLI args | `GetOptions("file=s" => \$file)` |
| JSON | Parse JSON | `decode_json($json)` |
| LWP::Simple | Web requests | `get($url)` |
| Net::Ping | Network ping | `Net::Ping->new()->ping("host")` |

---

## 🔣 Regular Expressions
    my $string = "username:admin";
    if ($string =~ /admin/) {
        print "Match found!\n";
    }

    # Capture groups
    if ($string =~ /(\w+):(\w+)/) {
        print "User: $1, Role: $2\n";
    }

---

## 🧰 Best Practices
- Always `use strict; use warnings;`  
- Use `my` to declare local variables  
- Prefer lexical filehandles (`open(my $fh, ...)`)  
- Use modules instead of reinventing wheels  
- Validate input and sanitize output  
- Use references for complex structures  

---

## 🔍 Resources
- **Official Docs:** https://perldoc.perl.org/  
- **CPAN (Modules):** https://www.cpan.org/  
- **Perl Style Guide:** https://perldoc.perl.org/perlstyle  
- **Cheat Sheet:** https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/perl.md  

---

**Notes / Observations:**  
(Add your personal discoveries, quirks, or snippets here.)
