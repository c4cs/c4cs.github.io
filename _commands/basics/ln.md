---
---

ln
--

'ln' creates a link to another file or directory

~~~ bash
$ ln /dir1/file1 /dir2/file2
~~~

<!--more-->

#The default is creating a hard link, if you want to create a symbolic link, you#should use the '-s' option:
~~~bash
$ ln -s /dir1/file1 /dir2/file2
~~~
#Then the path of /dir1/file1 will be saved in /dir2/file2

###### other options
~~~bash
 -b --backup #delete the previous backup
 -d --directory #To create a link to directories
 -f --force #Force to create a link even if the dir or file does not exist
 -i --interface #ask the user's permission before cover the original file
 -s --symbolic #create symbolic link instead of hard link
--help #show help information
--version #show version informationi
~~~
