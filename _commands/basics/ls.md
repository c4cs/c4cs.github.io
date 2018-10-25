---
---

ls
-------

`ls`  ls command lists the contents of, and optional information about, directories and files. 
With no options, ls lists the files contained in the current directory, sorting them
alphabetically.

~~~ bash
$ ls [option ...] [file]...
ls [option ...] [file]...
~~~
 
 <!--more-->
 
### Useful Options / Examples
 
### `ls -a`
 
Shows the hidden files in the directory as well.
 
~~~ bash
 $ ls -a
 a.txt b.txt c.txt
~~~
 
### `ls -l`
 
 Shows file or directory, size, modified date and time,  
 file or folder name and owner of file and its permission.

~~~ bash
 $ ls - l
 $ -rw-r--r--. 1 <directory>   683 Aug 19 09:59 a.txt
 $ -rw-------. 1 <directory>   1586 Jul 31 02:17 b.txt
~~~
