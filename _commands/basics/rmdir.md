---
---

rmdir
-------

__rmdir__: Removes empty directories

### Usage
~~~ bash
rmdir [OPTION] DIRECTORY
~~~

This removes the directory `DIRECTORY` if it is empty. `OPTION` can be specified to modify command execution. If `DIRECTORY` is not empty, no directories will be deleted and an error message similar to the following will show up:

> rmdir: Failed to remove 'DIRECTORY': Directory not empty

#### Example Usage
~~~ bash
rmdir directory_to_delete
~~~
Removes `directory_to_delete`  if it is empty

#### Example Usage with option
~~~ bash
rmdir -p parent/child
~~~
Removes both `parent` and `parent/child` if each is empty

<!--more-->

### Available Options
`--ignore-fail-on-non-empty`

Ignore failures that occur because a directory is non-empty

`-p, --parents`

remove DIRECTORY and its parents; for example, the result of `rmdir --parents a/b/c` (removes directories `a`, `a/b`, and `a/b/c`) is the same as the following sequence:
~~~
rmdir a/b/c
rmdir a/b
rmdir a
~~~

`-v, --verbose`

Output diagnostic information that logs every step taken by the `rmdir` command

`--help`

Displays help message. A more condensed, less nicely formatted version of `man rmdir`

`--version`

Output version information for `rmdir` on your machine