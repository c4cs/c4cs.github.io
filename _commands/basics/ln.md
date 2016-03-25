---
---

ln
--

`ln` is used to create a link (symbolic or hard) to a file on disk. Default creates hard links.

~~~ bash
$ ln file1.txt file2.txt
$ ln -s file1.txt file2.txt
~~~

<!--more-->

### What is Linking?

I'm glad you asked! When a file is created it is assigned both a filename and an _inode_ number. The _inode_ number is a unique identifier which points to where this file has been written onto the disk. In a normal _copy_ of a file, the disk literally writes the same data to a new location on the disk and, consequently, assigns a new filename and _inode_ number to this copied file.

A *hard* link allows multiple files to have the same _inode_ number. As a result, any modification made to any files *hard* linked will reflect in all files. If you delete any file of a set of hard linked files, the data stored on disk is *not* modified. The data at an _inode_ is not actually deleted until the count of linked filenames is 0.

A *symbolic* link one or more files to a _target_ file. All changes made in the linked files are reflected in the target file. However, if you delete the target file, the linked files are rendered useless. You can think of symbolic links as _shortcuts_ to a file.

### Useful Options / Examples

#### `ln [SOURCE] [TARGET]`
~~~ bash
$ echo hello > original.txt
$ ln original.txt linked.txt
$
$ ls
original.txt linked.txt
$ cat original.txt
hello
$ cat linked.txt
hello
$ echo world > linked.txt
$ cat original.txt
world
$ cat linked.txt
world
$ rm original.txt
$ ls
linked.txt
$ cat linked.txt
world
~~~

##### Break it down

 * We hard link a file, `linked.txt` to `original.txt`.
 * All changes we make to either are reflected in both
 * removing one does not affect the other

#### `ln -s [SOURCE] [TARGET]`
~~~ bash
$ echo hello > original.txt
$ ln -s original.txt linked.txt
$
$ ls
original.txt linked.txt
$ cat original.txt
hello
$ cat linked.txt
hello
$ echo world > linked.txt
$ cat original.txt
world
$ cat linked.txt
world
$ rm original.txt
$ ls
linked.txt
$ cat linked.txt
cat: linked.txt: No such file or directory
~~~

##### Break it down

 * We symbolic link a file, `linked.txt` to `original.txt`.
 * All changes we make to either are reflected in both
 * removing one leaves the other file on system, but its contents point to nothing valuable.

