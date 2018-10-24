---
---
## help

#### **Description:**

`help`  takes a linux command as an input and outputs information about that command. 'help' can be used to learn more information about a command that a user is unfamilier with.

If no command is given as input, a list of help topics is printed.

There are three command line flags:

Options:
- -d output short description for the command
- -m display usage in pseudo-manpage format
- -s output only a short usage synopsis for the command

#### **Usage and Examples**
Generally, running 'help' on a linux command is not very helpful, as the information provided is extensive and hard to follow. Thus, running with the -d flag is easier to understand and is usually more applicable. Also, running help with the -s flag will output how to use the command.

Examples:

~~~ bash
$ help -d help
help - Display information about builtin commands
$ help -d cd
cd - Change the shell working directory
$ help -s help
help: help [-dms] [pattern ...]
$help -s cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
~~~

