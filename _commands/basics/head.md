---
---

head
---

`head` is a command-line utility tool that outputs the first lines of a given file to the standard output. By default, `head` will return the first __10__ lines of the specified file.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ head helloworld.txt
Hi World!
Hey World!
Hello World!
Howdy-do World!
~~~

<!--more-->

### Useful Options / Examples

#### `head [file1, file2, ...]`
~~~ bash
$ head hello.txt world.txt
==> hello.txt <==
Hi
Hey
Hello
Howdy-do

==> world.txt <==
World!
My World!
Our World!
Your World!
~~~

* `head` gives the user the option to display the first lines of multiple files, where each file is preceded by a header consisting of the string _==> FILENAME <==_.


#### `head -n [count]`
~~~ bash
$ head -n 2 hello.txt world.txt
==> hello.txt <==
Hi
Hey

==> world.txt <==
World!
My World!
~~~

* The `-n [count]` option asks `head` to output the first `count` lines of each of the specified files.

#### `head -c [bytes]`
~~~ bash
$ head -c 8 helloworld.txt
Hi World!
Hey
~~~

* The `-n [bytes]` option asks `head` to output the first `bytes` bytes of each of the specified files.

#### `ls | head -n 7`
~~~ bash
$ ls | head -n 7
archive
_commands
_config.yml
deploy.sh
favicon.ico
Gemfile
Gemfile.lock
~~~

* `head` can also be piped with other commands. For example, we can retrieve the __First 7__ contents of a directory using `ls | head -n 7`.
