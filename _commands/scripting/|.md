---
---

| (pipe operator)
-------

`command1 | command2 [| command3 ...]`

The pipe operator is used in bash to chain multiple commands together. The two commands are run sequentially and the ouput of command1 becomes the input of command2.

~~~ bash
ls | wc -l
3
~~~

<!--more-->

### Useful Options / Examples

#### `ls | grep`
~~~ bash
$ ls | grep hello
hello.cpp
~~~

##### Break it down

 * The pipe operator is often used to connect a command and `grep` to search for things in output. In the above example, `ls` would usually output "hello.cpp goodbye.cpp" - this output is passed to `grep`, which searches it for the string "hello"and outputs the matching word, "hello.cpp".

#### `cat | wc`
~~~ bash
$ cat * | wc -l
10390
~~~ 

##### Break it down

 * The pipe will take the output from `cat *` (the text of every file in the current folder) and pass it to the `wc` command to count the number of lines in that output.

#### `sort | uniq`
~~~ bash
$ sort breakfast.txt | uniq
bacon
cheese
eggs
sausage
~~~

 * If we assume breakfast.txt contains the following:
   * eggs
   * bacon
   * cheese
   * sausage
   * eggs
 * the pipe operator `sort`s the file alphabetically and passes the output to `uniq`, which requires sorted input. `Uniq` then filters out the repeated lines (in this case, "eggs") and prints out the resulting sorted list.
