---
---

nl
-------

`nl` is used to number the lines in a file.


~~~ bash
$ nl filename 
~~~

~~~ bash
$ echo "hello
> world
> hi" > hello.txt
$ nl hello.txt
   1  hello
   2  world
   3  hi
~~~

<!--more-->

### Useful Options / Examples

#### Example command

### nl -s
Through the `-s` option, any string can be added to act as a separator between line numbers and the line text.

~~~ bash
$ nl -s"--> " hello.txt
   1--> hello
   2--> world
   3--> hi
~~~

#### Example command

### nl -i
The `-i` flag can be used to override the default increment of line numbers.

~~~ bash
$ nl -i4 hello.txt 
   1  hello
   5  world
   9  hi
~~~

#### Example command

### nl -b 
The `-b` option has several flags to style numbering:

* `t` only numbers lines that are non-empty

* `a` numbers all the lines

* `n`  numbers no lines

* `pBRE` only numbers lines that match the basic regular expression, BRE

~~~ bash
$ echo "hello
> world
>
> hello
> again" > hello.txt

$ nl -ba hello.txt
   1  hello
   2  world
   3
   4  hello
   5  again
~~~

In the example above, all lines (including empty lines) are numbered.

~~~ bash
$ nl -t hello.txt
   1  hello
   2  world
   
   3  hello
   4  again
~~~ 

In the example above, only non-empty lines are numbered.

~~~ bash
$nl -bph hello.txt
   1  hello
      world
      
   2  hello
      again
~~~

In the example above, only lines starting with "h" are numbered.
