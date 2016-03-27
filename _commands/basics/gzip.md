---
---

gzip
-------

Gzip reduces the size of the name files by compressing a file. It will only attempt to compress regular files. Compressed files can be restored to their original form using gzip -d or gunzip or zcat.

~~~ bash
$ gzip archivefile.txt
~~~

<!--more-->

### Useful Options / Examples

### Example Command
$ apt-get install gzip gunzip
####
$ ls
####
folder file1 file2 file3 file4
####
$ gzip file1 file2 file3
####
folder file1.gz file2.gz file3.gz file4
####

#### Example Command
To keep the original files after individual file compressions, use -k
####
$ gzip -k file1 file2
####
folder file1 file1.gz file2 file2.gz file3 file4
####

#### Example Command
To know the compressions ratio, use -l
####
$ gzip -l all.gz
####
    compressed           uncompressed         ratio    uncompressed_name
####
           294                   628          46.8%    all
####

#### Example Command
To unzip the gzip file, use gunzip
####
$ ls
####
cool all.gz fun.doc not.sh
####
$ gunzip all.gz
####
cool all gun.doc not.sh
####
#### Example command
$ gzip -r documets_folder
##### Break it down
 The "-r" option to recursively compress all the files under the specificed directory. 
#### Example command
$ gzip -c archivefile.txt > archivefile.txt.gz
##### Break it down
 If you want to keep an uncompressed version, you can use the -c option, which writes it to stanfard out, and then re-directs (">") the standard out to a file
