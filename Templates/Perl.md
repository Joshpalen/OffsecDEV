---
title: "Perl"
type: language
tags: [cs, language, perl]
cssclass: cs-note
---

# Perl

## Overview
High-level scripting language known for powerful text processing and regex.

## Key Concepts
| Concept | Description | Example |
|---------|-------------|---------|
| Scalar | Single value | `$x = 42;` |
| Array | Ordered list | `@a = (1,2,3);` |
| Hash | Key-value | `%h = (k => v);` |
| Subroutine | Function | `sub f { ... }` |

## Control Flow
```perl
if ($x > 0) { print "pos\n"; } else { print "neg\n"; }
for (my $i=0; $i<5; $i++) { print "$i\n"; }
```

## File I/O
```perl
open(my $fh, '<', 'input.txt') or die $!;
while (my $line = <$fh>) { print $line; }
close $fh;
```

## Tools
| Task | Command |
|------|---------|
| Run | `perl script.pl` |
| Install | `cpan <module>` |

## Related
[[Templates/Algorithm]] -$ [[Templates/Data_Structure]] -$ [[Templates/Concept]]

## Resources
- Docs: https://perldoc.perl.org/
- CPAN: https://www.cpan.org/



