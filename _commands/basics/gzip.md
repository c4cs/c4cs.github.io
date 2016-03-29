---
---
gzip
-------

`gzip` reduces the size of the name files by compressing a file. It will only attempt to compress regular files. Compressed files can be restored to their original form using gzip `-d` or gunzip or zcat.

~~~ bash
$ gzip archivefile.txt
~~~

<!--more-->

### Useful Options / Example

~~~ bash
$ apt-get install gzip gunzip
$ ls
folder file1 file2 file3 file4
$ gzip file1 file2 file3
folder file1.gz file2.gz file3.gz file4
~~~

#### Example command

To keep the original files after individual file compressions, use `-k`.

~~~ bash
$ gzip -k file1 file2
folder file1 file1.gz file2 file2.gz file3 file4
~~~

#### Example command

To keep the original files after individual file compressions, use `-k`.

~~~ bash
$ gzip -k file1 file2
folder file1 file1.gz file2 file2.gz file3 file4
~~~

#### Example command

To know the compressions ratio, use `-l`.

~~~ bash 
$ gzip -l all.gz
	    compressed           uncompressed         ratio    uncompressed_name
	           294                   628          46.8%    all
~~~

#### Example

To unzip the gzip file, use gunzip

~~~ bash 
$ ls
cool all.gz fun.doc not.sh
$ gunzip all.gz
cool all gun.doc not.sh
~~~

#### Example command

Use the `-r` option to recursively compress all the files under the specified directory.

~~~ bash
$ gzip -r documets_folder
~~~

#### Example command

If you want to keep an uncompressed version, you can use the `-c` option, which writes to standard out, and then re-direct (">") standard out to a file. 

~~~ bash
$ gzip -c archivefile.txt > archivefile.txt.gz
~~~

