---
---

tar
-------
`tar` is a command that is used to store and extract files from a tape or disk archive.
The _tar_ command which stands for _tape_ _archive_ simply archives a collection of files into one single file usually refered to as the `tarball`.

~~~ bash
$ tar -cf tarball.tar file1 file2
~~~

<!--more-->

### Useful Information / Options / Examples

#### Information
_tar_ can be used in tandem with the _gzip_ program to create a compressed tarball or _.tar.gz_ or _.tgz_ file as we will see later in the examples. Note that although the Gzip program is the most popular mode of compression of tarballs, there are many other compression programs. For instance, Bzip2 is a program that can compress harder than Gzip, but it is slower.

#### Example command
The following bash session shows how to create a tarball containing the files file1, file2, file3 and target.

~~~ bash
$ tar -cvf Archive.tar file1 file2 file3
file1
file2
file3
target
~~~

let's break down the above command:

* `tar` is obviously the name of the program.
* The `c` flag creates a new tarball. Use the `x` flag to <span style="color:red;">untar</span> or extract a tar achive.
* The `v` is the usual verbose option.
* The `f` option specifies the archive file or device. In this case _Archive.tar_.

#### Example command
the following bash session shows how to add a file or a directory to a tar achive using the `r` flag.

~~~ bash
$ tar -rvf Archive.tar added.txt
added.txt
~~~

#### Example command
You can also look inside a tarball to see its content without extracting anything before hand by using the `t` flag. This comes very handy especially when the tarball has a large number of files, but you are only interested in one or a couple of them. In that case you can pipe the output of the tar listing to `grep` for a more targeted search. 

~~~ bash
$ tar -tvf Archive.tar | grep target
-rw-rw-r-- user/group	0 2016-03-22 21:41 target
~~~

Notice how tar printed out the file attributes namely the user/group name and permission, the access/modification date etc. This is an important feature of the Tar program. It was designed to handle archiving while preserving the file system attributes even when the tarballs are bounced around from one device/platform to another.

#### Options
 Use the options <span style="color:red;">z</span> and <span style="color:red;">j</span> to handle _compressed_ tarballs <span style="color:blue;">.tar.gz</span> and <span style="color:blue;">.tar.bz2</span> respectively.
