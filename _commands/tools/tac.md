---
---

tac
--

`tac` concatenates each file or command line input to standard output in reverse (hence tac = cat in reverse).

~~~ bash
$ tac filename
~~~

<!--more-->

If a filename is provided, `tac` prints the contents of the file line-by-line, starting with the last line first.

If no filename is provided, or the filename is inputted as `-`, `tac` reads input from the command line and prints it in reverse.

### Additional Options/Examples

~~~ bash
$ tac [OPTION] [FILE]
~~~

By default, line separators are newlines and are placed after each line of output.  Use `-b` to place line separators before each line of output instead.

`--before`, `-b`

~~~bash
$ tac -b filename
~~~

To change the line separator to a provided string, use the command `-s` followed by the string. This feature is more commonly used when parsing command line input.

`--seperator=STRING`, `-s [string]`

For example: 

~~~bash
$ echo -n sam1I1am | tac -s "1"
~~~

The output would be: amI1sam1

The input can be broken up into 3 individual parts: 'sam' 'I' and 'am'.  `tac` begins by looking at 'am', and since 'am' is not followed by a line separator(a "1") in the command line input, 'am' is printed first without a trailing separator.  Second, I is printed.  However, because I is followed by a "1" in the command lie input, a "1" is printed after I.  Lastly, the 'sam' is printed, and since 'sam' is followed by a line separator, a "1" is placed after 'sam'.

~~~bash
$ echo -n sam1I1am | tac -b -s "1"
~~~

The output for this would be:  1am1Isam     

This is because in the above example, the line separator is placed after the string, whereas using the `-b` option puts the line separator before the string. 

`--regex`, `-r`

This flag tells `tac` to interpret the line separator as a regular expression.  This is commonly used with the `--seperator` flag.

### Applications

Error logs or any documents written in chronological order have the most recent information at the bottom of the file. `tac` can provide easy access to that information without having to scroll through the entire file.


  
