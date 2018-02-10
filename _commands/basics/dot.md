-bash-4.2$ echo "echo "hello world"" > hello
-bash-4.2$ . hello
hello world
~~~

<!--more-->

### Useful Options / Examples

~~~ bash
-bash-4.2$ help .
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