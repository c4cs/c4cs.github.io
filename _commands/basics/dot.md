---
---

dot (.)
-------
The period (dot) is short hand for the bash built in "source". It will read and execute commands from a file in the current environment and return the exit status of the last command executed.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ echo "echo "hello world"" > hello
$ . hello
hello world
~~~

<!--more-->

### Useful Options / Examples

~~~ bash
$ help .
.: . filename [arguments]
    Execute commands from a file in the current shell.

    Read and execute commands from FILENAME in the current shell.  The
    entries in $PATH are used to find the directory containing FILENAME.
    If any ARGUMENTS are supplied, they become the positional parameters
    when FILENAME is executed.

    Exit Status:
    Returns the status of the last command executed in FILENAME; fails if
    FILENAME cannot be read.
~~~
