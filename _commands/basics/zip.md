---
---

zip
---

'zip' is used to compress multiple files* into a .zip file
or to compress a directory^ into a .zip file.

~~~ bash
*zip combined.zip file1 file2 file3
^zip -r new.zip dir1
~~~

'@' (Not on MacOS): If a file list is specified as -@, zip takes
the list of input files from standard input and not command line

ex: zip -@ foo

'-': A single dash allows the zip to be written to standard
output, which allows for piping into other programs.

ex: zip -r - . | ....

's': This allows for splitting the zip file into multiple
smaller archives. The size of each is defined by k (kB),
m (MB), g(GB), or t(TB)

ex: zip -s 2g -r split.zip foo

SEE ALSO:
To uncompress, use 'unzip':
unzip file.zip
To extract to a dir:
unzip file.zip -d somedir
