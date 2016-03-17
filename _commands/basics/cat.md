---
---

cat
--

`cat` is used to concatenate files and print on the standard output

~~~ bash
$ echo haha > file1
$ echo lol > file2
$ cat file1 file2
haha
lol
~~~

<!--more-->

### Useful Options / Examples

#### `cat filename`

display the content of the file on standard output

~~~ bash
$ echo "I love C4CS" > file1
$ cat file1
I love C4CS
~~~ 

#### `cat -n`

number all output lines

~~~ bash
$ echo haha > file1
$ echo lol > file2
$ cat file1 file2
1  haha
2  lol
~~~

#### `cat - filename1 > filename2`

concatenate keyboard input and file, output to another file

~~~ bash
$ echo "demo" > file1
$ cat - file1 > file2
This is a (input the message, press C-d to finish)
$ cat file2
This is a (input the message, press C-d to finish)
demo
~~~

