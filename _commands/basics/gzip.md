---
---

gzip
-------

Gzip reduces the size of the name files by compressing ( or "packaging") a file into an "archive file". It will only attempt to compress regular files. Compressed files can be restored to their original form using gzip -d or gunzip or zcat.

~~~ bash
$ gzip archivefile.txt
~~~

<!--more-->

### Useful Options / Examples

#### Example command
$ gzip -r documets_folder
##### Break it down
 The "-r" option to recursively compress all the files under the specificed directory. 
#### Example command
$ gzip -c archivefile.txt > archivefile.txt.gz
##### Break it down
 If you want to keep an uncompressed version, you can use the -c option, which writes it to stanfard out, and then re-directs (">") the standard out to a file
