---
---

grep
-------

`grep` is a program for searching text files for lines that match regular exprssions. It can be used for all sorts of pattern-matching and text-based query analysis.

<!--more-->

~~~ bash
$ grep "wolf" animals.txt
// finds and prints all animals containing "wolf" (wolf spider, grey wolf, wolfhound, etc.)
$ grep "^wolf" animals.txt
// finds and prints  all animals beginning with "wolf" (wolf spider, wolfhound, etc.)
$ grep "wolf$" animals.txt
// finds and prints all animals ending with "wolf" (grey wolf, etc.)
$ grep "^c.*$"
// finds and prints all animals beginning with the letter "c"
$ grep "do+"
// finds and prints all animals containing a three-character sequence that begins with "do"
~~~

By default, `grep` will print all the matching lines to standard output (the console) with the matching parts colored. This behavior can be modified by using one or more of the the command line options `grep` offers.

### Useful Options / Examples

#### -c, -&#45;count

##### Using the `-c` or `--count` option overrides the default output behavior of `grep`. Instead of printing all of the matches to the console, it will print the number of lines that match. This is a useful option if, for example, you only want to know if there are any matches (count &lt;&gt; 0) but aren't as concerned with what those matches actually are.

~~~ bash
$ grep -c "wolf" animals.txt        // counts all animals containing "wolf"
187
$ grep -c "^ll.*" animals.txt      // counts all animals that begin with "ll"
1
$ grep -c "axb$" animals.txt        // counts all animals that end "axb"
0
~~~

#### -v, -&#45;invert-match

##### Regular expressions can be tricky to use, especially when you want to find text that doesn't match a particular regex. This is made easier by the `-v` or `--invert-match` option, which finds lines in the target input that do not match the given regular expression.

~~~ bash
$ grep -v "^[aeiou]" animals.txt
// finds and prints all animals that do not begin with a vowel
$ grep -c -v "s" animals.txt        // counts all animals that don't contain an "s"
17460
~~~
