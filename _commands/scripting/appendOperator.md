---
---

>\>
-----

'>>' is a shell operator that you can use to append the output in an existing file.

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

If the file does not exist, '>>' creates the file.

~~~ bash
$ echo line 1 >> example.txt
$ cat example.txt
line 1
~~~


