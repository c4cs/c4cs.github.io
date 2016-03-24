---
---
rmdir
--
`rmdir` is used to remove empty directories. `rmdir` will fail to remove directories that are non-empty.

~~~ bash
$ ls
myfolder/
$ rmdir myfolder
$ls

~~~

<!--more-->

### Useful Options / Examples

#### `rmdir -p`
~~~ bash
$ ls a/b/
c/
$ rmdir -p /a/b/c
$ ls

~~~

##### Break it down

* The `-p` option asks `rmdir` to remove explicit parent directories as long as they are emptied by removing the children directories.

#### `rmdir --ignore-fail-on-non-empty`
~~~ bash
$ ls myfolder/
somefile
$ rmdir --ignore-fail-on-non-empty myfolder
$ ls myfolder/
somefile
~~~

##### Break it down
* The `--ignore-fail-on-non-empty` option tells `rmdir` to ignore failures that occur due to non-empty directories being attempted to be removed. That is, no error output will be produced for non-empty directories.

#### `rmdir --verbose`
~~~ bash
$ rmdir --verbose tmp/
rmdir: removing directory, ‘tmp/’
~~~

##### Break it down
* The `--verbose` option asks `rmdir` to output a diagnostic for every directory removed.
