---
---

rmdir
--

`rmdir` is used to remove empty directories.

The format is

~~~ bash
$ rmdir [options] directories
~~~

<!--more-->

A basic example is

~~~ bash
$ rmdir dir1
~~~

This will remove folder dir1 in the current path if it is empty.

### Useful Options / Examples

#### `rmdir -p`

~~~ bash
$ rmdir -p dir2/dir3/dir4
~~~

##### Break it down
The `-p` or `--parents` flag will remove the parent directories of the specified directory, if they are empty. In this example, it means that the directories dir2, dir3, and dir4 will be removed.

#### `rmdir -v`

~~~ bash
$ rmdir -v dir5
rmdir: removing directory, 'dir5'
~~~

##### Break it down
The `-v` or `--verbose` flag will provied additional information about what is happening.

#### `rmdir --ignore-fail-on-non-empty`

~~~ bash
$ rmdir --ignore-fail-on-non-empty dir6
~~~

##### Break it down
If dir6 it not empty, adding the `--ignore-fail-on-non-empty` command will prevent an error message from being printed.
