---
---

\>\>    {#appendOperator}
-----

'&gt;&gt;' is a shell operator that you can use to append the output in an existing file.

~~~ bash
$ echo line 1 >> example.txt
$ cat example.txt
line 1
$ echo line 2 >> example.txt
$ cat example.txt
line 1
line 2
~~~

<!--more-->

### Useful Options / Examples

* If the file does not exist, ">>" creates the file.

~~~ bash
$ echo line 1 >> example.txt
$ cat example.txt
line 1
~~~

* The appending operator allows for the appending of standard output and standard error to a file.

  * Appending stdout to the file is appending the output of a file to the end of the other file.

~~~ bash
$ cat output.txt
Before
$ cat random.py
print "Random text"
print 3 / 0
$ python random.py >> output.txt
Traceback (most recent call last):
  File "random.py", line 2, in <module>
    print 3 / 0
ZeroDivisionError: integer division or modulo by zero
$ cat output.txt
Before
Random text
~~~

  * In this example, we're redirecting stderr to stdout using the appending operator.
 

~~~ bash
$ cat output.txt
Before
Random text
$ python random.py >> output.txt 2>&1
$ cat output.txt
Before
Random text
Random text
Traceback (most recent call last):
  File "random.py", line 2, in <module>
    print 3 / 0
ZeroDivisionError: integer division or modulo by zero
~~~

