---
---

diff
-------

`diff` is a tool used to compare files line by line.

~~~ bash
$ diff [option]... [file1] [file2] 
~~~

<!--more-->

### Useful Options / Examples

#### Example command

#### `diff -y -W 80 -q test1.txt test2.txt`
~~~ bash
$ diff -y test1.txt test2.txt
this is line one of a file           this is line one of a file
this line differs                  | this line is different
the line is the same                 the line is the same
~~~
~~~ bash
$ diff test1.txt test2.txt
2c2
< this line differs
--
> this line is different
~~~
~~~ bash
$ diff -y -W 80 test3.txt test4.txt
this is line one of a file           this is line one of a file
this line differs                  | this line is different
this is an additional line         <
the line is the same                 the line is the same
~~~
~~~ bash 
$ diff test3.txt test4.txt
2,3c2
< this line differs
< this is an additional line
--
> this line is different
~~~
~~~ bash
$ diff -q test3.txt test4.txt
Files test3.txt and test4.txt differ
~~~

##### Break it down

* The `-y` or `--side-by-side` flag prints the output in two columns. Regular output from diff can be a little hard to read, as you can see by the output when we do not provide the flag. The output `2c2` and `2,3c2` are commands for `patch` which is a tool often used with `diff` and can be ignored. The `<` symbol means the line is missing from file2, and `>` means the line is missing from file1.
* The `-W <N>` or `--width=NUM` flag gives a maximum output width, which is useful if your two column output is wrapping around the end of your console.
* The `-q` or `--brief` flag used in the last example just reports when two files are different giving no feedback on specific lines.

#### Example command

#### `diff -r dir1/ dir2/`
~~~ bash
$ diff -r dir1/ dir2/
diff -r dir1/nested/test.txt dir2/nested/test.txt
2a3
> this is a line added only to the test.txt in dir2/nested
~~~
~~~ bash
$ diff -r dir1/ dir2/
Common subdirectories: dir1/nested and dir2/nested
~~~

##### Break it down

* The `-r` or `--recursive` flag explores any common subdirectories found in the directoies given as arguments to `diff`.
