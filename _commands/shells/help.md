---
---

help
----
`help` is a program that takes a linux program as an input and prints a helpful message about the input program's behavior, its optional/required flags, and how to successfully use the program.

<!-- minimal example -->
~~~ bash
$ help echo
<info about echo>
$ help cd
<info about cd>
~~~

<!--more-->

### Useful Options / Examples

#### `help` -d

~~~ bash
$ help -d echo
echo - Write arguments to the standard output.
$ help -d cd
cd - Change the shell working directory.
~~~
Including the -d flag makes the help program print a short description of the input program.

#### `help` -s

~~~ bash
$ help -s echo
echo: echo [-neE] [arg ...]
$ help -s cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
~~~
Including the -s flag makes the help program print a short description of the input program's usage.

