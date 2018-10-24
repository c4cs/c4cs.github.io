
---
---

ln
-------
`ln` is a unix command used for making hard links or symbolic links with files or directories.
Hard links actually link the files make it so one can access a file or directory using a different name.
Soft links create references using pointers, and can only be made on directories.
These functionalities are useful when one wants to have two directories that reflect eachothers changes. 

~~~ bash
$ tree
.
├── file1
└── temp
$ ls -l
total 8
-rw-r--r--  1 eleanorreich  staff   5 Oct 24 14:29 file1
drwxr-xr-x  2 eleanorreich  staff  64 Oct 24 14:32 temp
$ ln file1 temp/file2
$ ls -l
total 8
-rw-r--r--  2 eleanorreich  staff   5 Oct 24 14:29 file1
drwxr-xr-x  3 eleanorreich  staff  96 Oct 24 14:34 temp

~~~

<!--more-->

Note: if you have a symbolic link, it is an indirect reference. Therefore, if you remove the file being 
pointed to with out the -rf option, the link will exist but will be to an invalid file


#### ln <source_dir>/* <new_dir>

##### This will make all the files in source_dir available using the name new_dir.


-i : print an error if there is a duplicate pathname, and prompt users if they want to remove the
conflicting path
-f : ignore error of duplicate pathname
-v : shows filenames as they are linked
-r/R : link recursively
-q : warning messages suppressed
---
---

ln
-------
`ln` is a unix command used for making hard links or symbolic links with files or directories.
Hard links actually link the files make it so one can access a file or directory using a different name.
Soft links create references using pointers, and can only be made on directories.
These functionalities are useful when one wants to have two directories that reflect eachothers changes. 

~~~ bash
$ tree
.
├── file1
└── temp
$ ls -l
total 8
-rw-r--r--  1 eleanorreich  staff   5 Oct 24 14:29 file1
drwxr-xr-x  2 eleanorreich  staff  64 Oct 24 14:32 temp
$ ln file1 temp/file2
$ ls -l
total 8
-rw-r--r--  2 eleanorreich  staff   5 Oct 24 14:29 file1
drwxr-xr-x  3 eleanorreich  staff  96 Oct 24 14:34 temp

~~~

<!--more-->

Note: if you have a symbolic link, it is an indirect reference. Therefore, if you remove the file being 
pointed to with out the -rf option, the link will exist but will be to an invalid file


#### ln <source_dir>/* <new_dir>

##### This will make all the files in source_dir available using the name new_dir.


-i : print an error if there is a duplicate pathname, and prompt users if they want to remove the
conflicting path
-f : ignore error of duplicate pathname
-v : shows filenames as they are linked
-r/R : link recursively
-q : warning messages suppressed
