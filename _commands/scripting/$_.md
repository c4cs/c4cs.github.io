---
---

$\_   {#dollarUnderscore}
-----

`$_` is a special shell variable which always holds the last argument of the most recent command.

~~~ bash
$ touch example.txt
$ echo $_
example.txt
~~~

<!--more-->

### Useful Options / Examples

Even if there were multiple arguments used, `$_` only contains the last one.

~~~ bash
$ gcc -pg main.c -o main
$ echo $_
main
~~~

`$_` is a variable, not a command so its main use is to save you some typing.

For example, say you want to create a new directory and go into it. You could use:

~~~ bash
$ mkdir mydir && cd $_
~~~

Note that at the beginning of a script, `$_` will return the name of the file being executed.

~~~ bash
$ cat test.sh
#!/bin/bash

echo $_
.
.
.

$ ./test.sh
./test.sh
~~~

