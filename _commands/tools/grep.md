---
---

grep
-------

`grep` is a program for searching text files for lines that match regular exprssions. It can be used for all sorts of pattern-matching and text-based query analysis.

~~~ bash
grep "wolf" animals.txt    // finds all animals containing "wolf" (wolf spider, grey wolf, wolfhound, etc.)
grep "^wolf" animals.txt   // finds all animals beginning with "wolf" (wolf spider, wolfhound, etc.)
grep "wolf$" animals.txt   // finds all animals ending with "wolf" (grey wolf, etc.)
grep "^c.\*$"              // finds all animals beginning with the letter "c"
grep "do+"                 // finds all animals containing a three-letter sequence that begins with "do"
~~~

By default, `grep` will print all the matching lines to standard output (the console) with the matching parts colored. This behavior can be modified by using one or more of the the command line options `grep` offers.

<!--more-->

### Useful Options / Examples

#### Example command

##### Break it down

#### Example command

##### Break it down
