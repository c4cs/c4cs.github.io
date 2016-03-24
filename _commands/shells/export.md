---
---

export
-------

`export` marks an environment variable to be exported with any child process. Any child process will will inherit the variable along with any other marked variables

~~~ bash
$ NAME=alice
$ echo $NAME
alice
$ cat test.sh
#!/usr/bin/env/bash
echo $NAME
$ ./test.sh

$ export NAME
$ ./test.sh
alice
$ export NAME=bob
$ ./test.sh
bob
~~~

<!--more-->

### Useful Options / Examples

#### `export -p`

~~~ bash
$ export -p
declare -x SHELL="/bin/bash"
declare -x USER="username"
declare -x VAR="value"
...
~~~

##### Break it down
Will list all variables that are currently marked to be exported

