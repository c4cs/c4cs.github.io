---
---

\> (standard output redirection operator)
-------

`command1 -[options] [arguments] > <output file name>` 

The standard output redirection operator is used in bash to redirect the output of one command to a specified file.

~~~ bash
./a.out > output.txt
~~~

<!--more-->

### Useful Options / Examples

#### Combining with `diff`
~~~ bash
$ ./p3 > outfile.txt | diff outfile.txt correct.txt
1c1
< Hello World!
---
> Hello World!!
~~~

##### Break it down

* Sometimes it's helpful to diff a program's output with a different file, as is the case in many EECS projects at UMich. In the above example, the output of 'p3' is redirected to the file `outfile.txt`, and then diff is called to compare the contents of `outfile.txt` to the contents of `correct.txt`. The output that follows the command indicates that the contents of the two files do not match.
 

#### Splitting stdout and stderr
~~~ bash
$ ./a.out
Hello from cerr!
Hello World!
$ ./a.out > std
Hello from cerr!
~~~
