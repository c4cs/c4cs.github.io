----
----

zip
-------
`zip` is used to compress multiple files into a .zip file
or to compress a directory into a .zip file.

<!-- minimal example -->
~~~ bash
$ zip combined.zip file1 file2 file3
$ zip -r new.zip dir1
~~~


<!--more-->
### Useful Options / Examples

#### `zip`

~~~bash
$ zip [options] [archive] [inpath] [inpath] ...
$ zip [-aABcdDeEfFghjklLmoqrRSTuvVwXyz!@$][longoption ...][path][suffixes][date][date] [zipfile [file ...]] [list]
~~~

----

#### `zip -@ [archive] [inpath] [inpath] ...`

~~~bash
$ zip -@ foo
$ find . -name "*.[ch]" -print | zip source -@

~~~

##### Break it down

* If a file list is specified as -@, zip takes
the list of input files from standard input and not command line

----

#### `zip [options] [archive] [inpath] - ...`

~~~bash
$ zip -r - . | ....
$ tar cf - . | zip backup -
~~~

##### Break it down

* A single dash allows the zip to be written to standard
output, which allows for piping into other programs.

----

#### `zip -s [archive] [inpath] [inpath] ...`

~~~bash
$ zip -s 2g -r split.zip foo
$ zip -s 0 split.zip --out unsplit.zip
~~~

##### Break it down

* This allows for splitting the zip file into multiple
smaller archives. The size of each is defined by k (kB),
m (MB), g(GB), or t(TB)

----
