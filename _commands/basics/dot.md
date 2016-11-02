---
---

dot (.)
-------

A full stop can be synonymous for `source` in a shell, can reference a relative
directory path, or indicate a hidden file.

<!--more-->

#### As a POSIX shell construct
Synonymous with `source`. Used to execute commands in the current shell.

We can use the `$$` variable to see our shell's process ID:

~~~
[mterwilliger@Wayfarer /tmp]$ cat my_script.sh
#!/bin/bash

echo $$
[mterwilliger@Wayfarer /tmp]$ echo $$
3413
[mterwilliger@Wayfarer /tmp]$ ./my_script.sh
3503
[mterwilliger@Wayfarer /tmp]$ . ./my_script.sh
3413
~~~

Notice the first invocation (`./my_script.sh`) is spawned in a subshell with a
new PID, while the second (`. ./my_script.sh`) is run inline (same PID).

#### As a filesystem construct
`.` and `..` are special filesystem constructs that are [hard
links](https://en.wikipedia.org/wiki/Hard_link) to the current and parent
directories, respectively.

~~~
[mterwilliger@Wayfarer repo]$ pwd
/tmp/repo
[mterwilliger@Wayfarer repo]$ stat -f '%N %i' /tmp/
/tmp/ 99500509
[mterwilliger@Wayfarer repo]$ stat -f '%N %i' ..
.. 99500509
~~~

i.e. `/tmp/` and `..` are exactly the same
[inode](https://en.wikipedia.org/wiki/Inode) or entity on disk.

#### As a "dotfile"
There's a convention that filenames beginning with `.` are hidden by default.
(e.g. `.git`)

~~~
[mterwilliger@Wayfarer repo]$ ls
file1   file2   file3
[mterwilliger@Wayfarer repo]$ ls -a
.       ..      .git    file1   file2   file3
~~~

---

So, something like this is perfectly valid:

~~~
$ . ./.my_script.sh
~~~

1. Our filename is called `.my_script.sh`.
2. The reason we have to run `./.my_script.sh` is because `.`, or the current
   working directory, is not in `PATH`. This is _exactly_ the same as the full
   path, e.g. `/Users/mterwilliger/Desktop/.my_script.sh`, and has nothing to do
   with the shell. The reason our shell does not search our current directory
   for executable is security related: we don't want to automatically execute
   arbitrary programs that happen to be in the current (potentially untrusted)
   directory.
3. We then want to execute this inline, instead of in a subshell.

Also valid:

~~~
$ . ../...
~~~

Which says to `source` (`.`) the hidden file named `...` in the parent (`..`) directory.
