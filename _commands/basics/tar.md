---
---

tar
-------
((t)ape (ar)chive) is a computer software utility for collecting many files into one archive file. tar is an useful tool to package files.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
tar -zcf eecs398.tar.gz homework1.txt homework2.pdf homework3.tex
~~~

<!--more-->

### Useful Options / Examples
~~~ bash     
       tar -c:	create a new file

       tar -x:	decompress a file 

       tar -t:	look up a tarfile

-------

       tar -z:	use gzip to compress the file

       tar -r:	use bzip2 to compress the file

       tar -v:	(verbose) show the compressing file names

       tar -f:	set the tarfile name  

~~~
#### `tar -czf`

this command is one of the most useful command in tar, it will make a tarfilename.tar.gz file for all the files

~~~bash
tar -zcf eecs398.tar.gz homework1.txt homework2.pdf homework3.tex
~~~

will create a eecs398.tar.gz file

the z in the -czf can be changed to -r or just use -cf

~~~bash
	tar -czf will create a file use gzip
	tar -crf will create a file use bzip2
	tar -cf  will create a file without compression
~~~

#### `tar -tzvf`

this command is used to look up the tarfile

~~~bash
	tar -tzvf name.tar.gz
	tar -trvf name.tar.bz2
~~~

#### `tar -xzvf`

this command is used to decompress a file, it can decompress a file into different path

~~~bash
	tar -xzvf file.tar.gz

	cd /tmp2/
	tar -xzf  /tmp/file.tar.gz
~~~