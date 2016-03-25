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