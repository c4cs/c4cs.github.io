---
---

true
--

`true` a command that returns the logical value of truth, which is `0`.

~~~ bash
#!/usr/bin/env bash
# The value of $? is the exit status code of the last program/command to run
$ true
$ echo $?
0
$ false 
$ echo $?
1
~~~

<!--more-->

### Useful Options / Examples

#### `yes | true`

~~~ bash
#!/usr/bin/env bash
# `yes` is a command that will keep printing out "y" to standard output
$ yes | true
$ echo $?
0
~~~

##### Break it down

 * The `yes` command keeps printing out "y" to the standard output but the pipeline symbol `|` connects it with `true`, which will exit right away with an exit code 0
 * A return value of 0 means the previous command/program has exited successfully. An exit code that is non-zero usually means an error has occured
 * Notice that in Bash, true is implemented as a function, they are used like the logical boolean values in other languages like C++, python, and Java. The only difference is that the value of the function is its return value.
