---
---

which
-------

`which` will show you the location of  the file/command in `$PATH`

~~~ bash
$ which ls
/bin/ls
~~~

<!--more-->

### Useful Options / Examples

#### Example command

'which -a [command]'

`which` with the `-a` flag will give the location of all executables with the given name using

~~~bash
$ which -a less
/usr/bin/less
/bin/less
~~~

##### Break it down
This shows all the locations where an executable called 'less' is located

#### Example command
`which -a [command] [command] [command]`

`which` can be used with multiple executables at the same time

~~~bash
$ which less echo ls
/usr/bin/less
/bin/echo
/bin/ls
~~~

##### Break it down
It gives the locations of all the executables you gave it as arguments in a list



