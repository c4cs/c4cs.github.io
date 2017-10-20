---
---

wc
--

`wc` prints newline, word, and byte counts for each FILE, and a total if more than one FILE is specified. With no FILE, or when FILE is a dash ("-"), wc operates on standard input. (A word is a non-zero-length sequence of characters delimited by white space.)

~~~ bash
$ wc [OPTION]... [FILE]...
$ cd [OPTION]... --files0-from=F
~~~

<!--more-->

### Useful Options / Examples


#### `wc`

The `wc` command without passing any parameter will display a basic result of ”tecmint.txt file. The three numbers shown below are 12 (number of lines), 16 (number of words) and 112 (number of bytes) of the file.

~~~ bash
$ wc tecmint.txt
12  16 112 tecmint.txt
~~~


#### `wc -l`

To count number of newlines in a file use the option ‘-l‘, which prints the number of lines from a given file. Say, the following command will display the count of newlines in a file. In the output the first filed assigned as count and second field is the name of file.

~~~ bash
$ wc -l tecmint.txt
12 tecmint.txt
~~~

#### `wc -w`

Using ‘-w‘ argument with ‘wc‘ command prints the number of words in a file. Type the following command to count the words in a file.

~~~ bash
$ wc -w tecmint.txt
16 tecmint.txt
~~~

#### `wc -c`


Using ‘-c‘ with ‘wc‘ command will print the total number of bytes in a file.

~~~ bash
$ wc -c tecmint.txt
112 tecmint.txt
~~~

#### `wc -m`


Using ‘-m‘ with ‘wc‘ command will print the total number of characters in a file.

~~~ bash
$ wc -m tecmint.txt
112 tecmint.txt
~~~

#### `wc -L`


The ‘wc‘ command allow an argument ‘-L‘, it can be used to print out the length of longest (number of characters) line in a file. So, we have the longest character line (‘Scientific Linux‘) in a file.

~~~ bash
$ wc -L tecmint.txt
16 tecmint.txt
~~~
