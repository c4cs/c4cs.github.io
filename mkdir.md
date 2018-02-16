---
---

mkdir
--

`mkdir` is used to create directories (if they do not already exist) on a file system.

The general format is

~~~ bash
$ mkdir [options] directories
~~~

<!--more-->

A simple example is:

~~~ bash
$ mkdir dir1
~~~

This will create a folder named **dir1** under the current path.


### Useful Options / Examples

#### `mkdir -p,--parents`
Create parent directories as necessary. (If the sepcified parent directory already exist, no error is reported.)

This is helpful when we are creating nested directories. For example, when we do

~~~ bash
$ mkdir -p /home/a/b/c
~~~

if **/home/a/b/** does not exist, **mkdir** will first create it, and then create **/c** under it. But if we are not using the **-p** flag, it will report an error saying **/home/a/b/** does not exist.

Also, if we are creating a directory that is already exist, without the **-p** flag, there will be an error saying " File exists"; while adding the **-p** flag will not report an error. For example, 

~~~ bash
$ mkdir /a/d
$ mkdir /a/d
mkdir: cannot create directory ‘/a/d’: File exists
$ mkdir -p /a/d
~~~

#### `mkdir -m, --mode=`*`MODE`*

Set file access mode (as with the **chmod** command).

For example,

~~~ bash
$ mkdir -m 444 dir1
~~~

will create folder **dir1** which is read only for all users.

More usage about file access mode code can be found [here](https://help.ubuntu.com/community/FilePermissions#Changing_Permissions).

#### `mkdir -v, --verbose`

Verbose output; print a message for each created directory.

For example, if we do 

~~~ bash
$ mkdir -v -p -m 444 a/b/c
~~~

where **a** exists, but **a/b** does not, it will print

~~~ bash
mkdir: created directory `a/b'
mkdir: created directory `a/b/c'
~~~

(Yes, it will just print the directory name, but not the file access mode.)

#### Creating Multiple and Nested directories in one line
This is not done by **mkdir** itself. Instead, it can be done through making use of the Shell extension.

For example,

~~~ bash
$ mkdir -p a/{b1/c1/{d1,d2},b2,b3}
~~~

will create a tree like this

~~~ bash
a
│   b2
│   b3
└───b1
    └─── c1
         │   d1
         │   d2
~~~
