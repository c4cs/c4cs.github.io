---
---

chmod
--

'chmod' is the command to use when changing a file's access permissions.

~~~ bash
$ chmod +x mypythonscript.py
~~~

<!--more-->

### More advanced uses of chmod

chmod is most commonly used to give executable permissions to files, shown in the first example.  However there is a lot more to chmod than that.

Files can be given read, write, and executable permissions.  Specify the permissions with +x, +w, +r, or any combination of the three.

~~~ bash
$ chmod +xw mypythonscript.py
$ chmod +rw mypythonscript.py
~~~

Permissions can be removed with a -

~~~ bash
$ chmod -x mypythonscript.py
~~~

chmod also can assign permissions to various different users on a particular machine.  Users fall into three groups, "user" (the person who owns the file), "other" (other people on the machine), "group" (a list of people that you can specify).  To specify permissions for any or all of these groups, preface the + or - with either 'g', 'u', or 'o'.

~~~ bash
$ chmod o+xr mypythonscript.py
$ chmod u-x mypythonscript.py
~~~

For further reading check out,
~~~ bash
$ man chmod
~~~
