---
---

grep
-------

`grep` is a program for searching text files for lines that match regular exprssions. It can be used for all sorts of pattern-matching and text-based query analysis.

<!-- more -->

~~~ bash
$ grep "wolf" animals.txt    // finds all animals containing "wolf" (wolf spider, grey wolf, wolfhound, etc.)
$ grep "^wolf" animals.txt   // finds all animals beginning with "wolf" (wolf spider, wolfhound, etc.)
$ grep "wolf$" animals.txt   // finds all animals ending with "wolf" (grey wolf, etc.)
$ grep "^c.\*$"              // finds all animals beginning with the letter "c"
$ grep "do+"                 // finds all animals containing a three-letter sequence that begins with "do"
~~~

By default, `grep` will print all the matching lines to standard output (the console) with the matching parts colored. This behavior can be modified by using one or more of the the command line options `grep` offers.

### Useful Options / Examples

#### -c, --count

##### Using the `-c` or `--count` option overrides the default output behavior of `grep`. Instead of printing all of the matches to the console, it will print the number of lines that match. This is a useful option if, for example, you only want to know if there are any matches (count &lt;&gt; 0) but aren't as concerned with what those matches actually are.

~~~ bash
$ grep -c "wolf" animals.txt
187
$ grep -c "^ll.\*" animals.txt
1
$ grep -c "axb" animals.txt
0
~~~

#### Example command

##### Break it down
