---
---

join
--
'join' is a command works for joining lines of two files on a common field. The two files can be selected within the line and the result is written to standard output.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$cat hello.txt
a hello
b hey

$cat world.txt
a world
b world!

$join hello.txt world.txt
a hello world 
b hey world!
~~~

<!--more-->

### Useful Options / Examples
#### Example command
The default join field is the first field of each line in the file. But the join field can be specified to join the file with options like '-1' '-2'.
~~~ bash
$cat hello.txt
, hello there,
, hey there,

$cat world.txt
hello world
hey world!

$join -1 2 -1 1 hello.txt world.txt
hello , there, world
hey , there, world!
~~~

#### Example command
The default delimiter is blank, but option '-t' can be used to specified a special delimiter like ',' shown below.
~~~ bash
$cat hello.txt
1, hello there, this is
2, hey there, this is

$cat world.txt
hello there, world
hey there, world!

$join -1 2 -1 1 -t , hello.txt world.txt
hello there, 1, this is, world
hey there, 2, this is, world!
~~~

#### Example command
The order of output can also be modified.
~~~ bash
$cat hello.txt
1, hello there, this is
2, hey there, this is

$cat world.txt
hello there, world
hey there, world!

$join -1 2 -1 1 -t -o 1.1,1.2,1.3,2.2 hello.txt world.txt
1, hello there, this is, world
2, hey there, this is, world!
~~~

