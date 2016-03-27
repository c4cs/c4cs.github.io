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

#### `diff test1.txt test2.txt`

Running `diff` with two files prints lines that are in one file but not the other file. This output can be a little hard to read, as you can see by the first example.

* The output `2c2` and `2,3c2` are commands for `patch` which is a tool often used with `diff` and can be ignored.

* The `<` symbol means the line is missing from the first file, and `>` means the line is missing from the second file.

~~~ bash
$ diff test1.txt test2.txt
2c2
< this line differs
--
> this line is different
~~~
~~~ bash
$ diff -y test1.txt test2.txt
this is line one of a file                this is line one of a file
this line differs                       | this line is different
the line is the same                      the line is the same
~~~
##### Break it down

* The `-y` or `--side-by-side` flag prints the output in two columns. 

~~~ bash 
$ diff test3.txt test4.txt
2,3c2
< this line differs
< this is an additional line
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
$ diff -q test3.txt test4.txt
Files test3.txt and test4.txt differ
~~~

##### Break it down

* The `-W <N>` or `--width=NUM` flag gives a maximum output width, which is useful if your two column output is wrapping around the end of your console.
* The `-q` or `--brief` flag used in the last example just reports when two files are different giving no feedback on specific lines.

#### `diff -r dir1/ dir2/`
~~~ bash
$ diff -r dir1/ dir2/
$ diff -r dir1/nested/test.txt dir2/nested/test.txt
2a3
> this is a line added only to the test.txt in dir2/nested
Only in dir1/: file1
~~~
~~~ bash
$ diff  dir1/ dir2/
Common subdirectories: dir1/nested and dir2/nested
Only in dir1: file1
~~~

##### Break it down

* The `-r` or `--recursive` flag explores any common subdirectories found in the directories given as arguments to `diff`. By default diff will compare files of the same name in the given directories, output common subdirectories, and output any other files that exist in only one directory.
