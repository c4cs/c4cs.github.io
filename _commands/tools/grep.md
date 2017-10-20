---
---

grep
-------

`grep` is a program for searching text files for lines that match regular exprssions. It can be used for all sorts of pattern-matching and text-based query analysis.

~~~ bash
$ grep -i crab animals.txt
Crab
Crab-Eating Macaque
Hermit Crab
Horseshoe Crab
King Crab
~~~

<!--more-->

This reference page uses the [animals.txt](../static/commands/src/animals.txt) file for all of its examples. This list was taken from [Millie Bond's A-Z Index of Animals](https://a-z-animals.com/animals/).

Below are a sample of possible patterns you can match using `grep`:

~~~ bash
$ grep Wolf animals.txt             // list all animals containig "Wolf"
Arctic Wolf
Irish WolfHound
Red Wolf
Wolf
Wolf Spider
$ grep ^Wolf animals.txt            // list all animals beginning with "Wolf"
Wolf
Wolf Spider
$ grep Wolf$ animals.txt            // list all animals ending with "Wolf"
Arctic Wolf
Red Wolf
Wolf
~~~

By default, `grep` will print all the matching lines to standard output (the console) in the same order they appear in the source with the matching parts colored. This behavior can be modified by using one or more of the the command line options `grep` offers.

### Useful Options / Examples

#### -c, -&#45;count

##### Using the `-c` or `--count` option overrides the default output behavior of `grep`. Instead of printing all of the matches to the console, it will print the number of lines that match. This is a useful option if, for example, you only want to know if there are any matches (count &gt; 0) but aren't as concerned with what those matches actually are.

~~~ bash
$ grep -c ^B animals.txt            // count the number of animals beginning with "B"
66
$ grep -c [Ll]l animals.txt         // count the number of animals containing "ll" or "Ll"
46
$ grep -c end$ animals.txt          // count the number of animals ending with "end"
0
~~~

#### -v, -&#45;invert-match

##### Regular expressions can be tricky to use, especially when you want to find text that doesn't match a particular regex. This is made easier by the `-v` or `--invert-match` option, which finds lines in the target input that do not match the given regular expression.

~~~ bash
$ grep -v ^[AEIOU] animals.txt    // list all animals that don't start with a vowel
Baboon
Bactrian Camel
Badger
...
Zebu
Zonkey
Zorse
$ grep -c -v s animals.txt        // count all animals that don't contain an "s"
427
~~~

#### -i, -&#45;ignore-case

##### Regular expressions, by their nature, are case sensitive. Sometimes, it can be annoying to construct a regex that inherently ignores case differences between letters; this can be especially true when working with extended ASCII or Unicode characters. The `-i` or `--ignore-case` option handles this automatically.

~~~ bash
$ grep -i m[aeiou]n animals.txt        // list all animals that contain "m" or "M", then a vowel, then "n" or "N"
Birman
Caiman
...
Mongoose
Mongrel
Monitor Lizard
...
Tiger Salamander
Vervet Monkey
Woolly Monkey
~~~

#### Other Useful Options

##### `-n`, `--line-number` will list the line number of the matching line before the contents
`-l`, `--files-with-matches` will list the input files that contain a matching line, not the matching lines themselves

### Input/Output

##### `grep` can be used with one file or with multiple files by listing more than one in the input position for the command. You can even use regular expressions to match multiple files!

~~~ bash
$ grep "umich" file1.txt file2.txt       // search two files explicitly
// output here
$ grep "umich" *.txt                     // search all .txt files in the current directory
// output here
$ grep "umich" .                         // search all files in the current directory
~~~

Input can also be piped into `grep` from another program or redirected using &lt;. Likewise, the output of `grep` can be piped into another program (including another `grep`) or redirected using &gt;

### Regular Expression Basics

##### Here are some useful symbols and techniques for regular expressions. This is just a very basic overview; regular expressions are extremely powerful if you know how to wield them.
* `^` matches the beginning of a line
    * `^A` will match all lines beginning with a capital "A"
* `$` matches the end of a line
    * `e$` will match all lines ending with a lower-case "e"
* `.` matches any single character (including whitespace)
    * `b.b` will match all lines that contain two lower-case "b"s separated by a single character (i.e. "bob" or "b&b")
	* `^...$` will match all lines that are exactly three characters long
* `*` will match the preceding character zero or more times
    * `a*b` will match all lines that contain any number of lower-case "a"s (including 0) followed by a lower-case "b"
    * `blue.*green` will match all lines that contain "blue" followed at some point later (maybe immediately) by "green"
* `+` will match the preceding character one or more times
    * `a+b` will match all lines that contain at least one (but possibly more) lower-case "a" immediately followed by a lower-case "b"
    * `blue.+green` will match all lines that contain "blue" followed later by "green" with at least one character in between
* `\w` will match any letter, digit, or the underscore
* `\d` will match any digit
* `\s` will match any whitespace (space, tab, newline, etc.)
* To match any of a group of characters, place them in `[]`
    * `[aeiou]$` will match all lines that end in a vowel
* To match any of a range of characters, place them in `[]` separated by a `-`
    * `^[1-9][0-9]$` will match all lines that are numbers between 10 and 99 inclusive
    * `^[A-Z][a-z]+$` will match all lines that start with a capital followed by at leaste on lower-case letter, and only contains letters

##### Here are some good resources if you want to learn more about regular expressions or get practice:
* [Regular-Expressions.info](http://www.regular-expressions.info/)
* [W3Schools (for JavaScript specifically, but has a good general syntax reference)](https://www.w3schools.com/jsref/jsref_obj_regexp.asp)
* [RegEx Golf](https://alf.nu/RegexGolf)
