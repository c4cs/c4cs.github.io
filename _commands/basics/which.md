---
---

which
--

`which` returns the first matching command(s) in $PATH

~~~ bash 
$ which echo
/bin/echo
~~~

<!--more-->

### Useful Options / Examples

`which -a [command(s)]`

`which` can be used with the flag `-a` to display all matching commands in `$PATH`, not just the first

~~~bash
$ which -a less
/usr/bin/less
/bin/less
~~~

`which [program]`

`which` can be used with certain programs


~~~bash
$ which nano
/usr/bin/nano
~~~

`which [commands]`

`which` can be with multiple input commands at once

~~~bash
$ which less nano
/usr/bin/less
/usr/bin/nano
~~~

#### Putting it all together

~~~bash
$ which -a less nano
/usr/bin/less
/bin/less
/usr/bin/nano
/bin/nano
~~~

The command will display all paths in the order they are found. In this case, all locations of `less` are listed in order first and then the same for `nano`
