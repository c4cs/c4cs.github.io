---

I/O Redirection
---------------

The I/O redirection operators `<`, `>`, and `>>` allow us to read and write input and output from files.

~~~ bash
$ echo "I love bash!" > message.txt
$ cowsay -w < message.txt
$ echo "I love bash so much!" >> message.txt
$ cosway -w < message.txt
~~~

<!--more-->

### Basic Usage

#### `<` operator

