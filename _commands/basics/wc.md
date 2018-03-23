---
---

wc
--

`wc` prints newline, word, and byte counts for each `FILE`.

~~~ bash
$ wc tecmint.txt
12  16 112 tecmint.txt
~~~

<!--more-->

### Useful Options / Examples

#### `wc -l`

To count number of newlines in a file use the option `-l`, which prints the number of lines from a given file.

~~~ bash
$ wc -l tecmint.txt
12 tecmint.txt
~~~

#### `wc -w`

Using `-w` argument with `wc` command prints the number of words in a file.

~~~ bash
$ wc -w tecmint.txt
16 tecmint.txt
~~~

#### `wc -c`

Using `-c` with `wc` command will print the total number of bytes in a file.

~~~ bash
$ wc -c tecmint.txt
112 tecmint.txt
~~~

#### `wc -m`

Using `-m` with `wc` command will print the total number of characters in a file.

~~~ bash
$ wc -m tecmint.txt
112 tecmint.txt
~~~

#### `wc -L`

The ‘wc‘ command allow an argument ‘-L‘, it can be used to print out the length of longest (number of characters) line in a file.

~~~ bash
$ wc -L tecmint.txt
16 tecmint.txt
~~~
