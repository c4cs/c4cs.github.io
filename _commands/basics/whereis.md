---
---

whereis
--

`whereis` is used to locate source/binary and manuals sections for specified files. The supplied names are first stripped of leading pathname components and any (single) trailing extension of the form `.ext`.

~~~ bash
$ whereis [options] filename
~~~

<!--more-->

### Useful Options / Examples

#### `whereis`

~~~ bash
$ whereis gcc
gcc: /usr/bin/gcc /usr/lib/gcc /usr/share/man/man1/gcc.1.gz /usr/share/info/gcc.info.gz
~~~

##### Break it down

* This returns a list of source, binary and documentation files for gcc.

#### `whereis -b`

~~~ bash
$ whereis -b gcc
gcc: /usr/bin/gcc /usr/lib/gcc
$ whereis -m gcc
gcc: /usr/share/man/man1/gcc.1.gz /usr/share/info/gcc.info.gz
$ whereis -s gcc
gcc:
~~~

##### Break it down

* The `-b` option tells `whereis` to return a list of only binary files for gcc.
* Similarly `-m` can be used for documentation files and `-s` can be used for source files.

#### `whereis -B`

~~~ bash
$ whereis -B /usr/bin -f -b gcc
gcc: /usr/bin/gcc
~~~

##### Break it down

* The `-B` option limits the places where `whereis` searches for binaries
* The `-f` is used to terminate the last directory list and signals the start of filenames.
* Similarly `-M` can be used to limit the places for documentation files and `-S` can be used to limit the places for source files.

#### `whereis` vs `which`

~~~ bash
$ whereis gcc
gcc: /usr/bin/gcc /usr/lib/gcc /usr/share/man/man1/gcc.1.gz /usr/share/info/gcc.info.gz
$ which gcc
/usr/bin/gcc
~~~

##### Break it down
* `which` command is used to find the location of an executable which is in the user's path.
* `whereis` command doesn't only return the location of an executable but also of source files and documentations. `whereis` also doesn't search for configured path but searches through an internal list of common Unix paths.
* There are executables which will be found by `which` but not by `whereis` because they are in a non-standard directory which is in the path.
* There are also some executables which will be found by `whereis` but not by `which` because they are in some of the standard directories that are not in the path.
* If you could not find an executable with one of the two commands, give the other one a try.
