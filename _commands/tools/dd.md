---
---

dd
--

`dd` is a utility that can be used to convert and copy files in a number of ways. This can be used for backing up/restoring entire hard drives or partions, converting data formats, converting the case of a file, and more.

<div class="alert alert-warning">
Warning: dd is often referred to by many as 'disk destroyer' or 'data deleter' due to its potential to erase large chunks of data when used improperly. If you plan on testing any of these commands exercise extreme caution to avoid losing any significant data.
</div>

~~~ bash
$ dd if=[inputFile] of=[outputFile] [options]
0+1 records in
0+1 records out
6 bytes copied, 0.000101046 s, 59.4 kB/s
~~~

<!--more-->

### Useful Options / Examples


#### `dd if=[inputFile] of=[outputFile]`

Without any arguments, this functions similairly to the `cp` command.

`if` stands for input file

`of` stands for output file

One noteable difference however is that `dd` can be used on entire drives in addition to files and folders. For example the following command creates an image of a disk.

~~~ bash
$ dd if=/dev/sda of=/tmp/sdadisk.img
~~~

This disk image can then be restored by simply reversing the parameters.

~~~ bash
$ dd if=/tmp/sdadisk.img of=/dev/sda
~~~

#### `dd if=[inputFile] of=[outputFile] bs=4096 conv=noerror,sync`

While working between different drives it is often useful to use these additional options to ensure accuracy.

`bs=4096` specifies the block size or number of bytes to read/write at a time

`conv=noerror` tells the tool to continue even if it encounters an error

`conv=sync` allows the tool to use synchronized I/O

One example of when this should be used is when you are backing up an entire hard drive to another hard drive or clone one partition to another

~~~ bash
$ dd if=/dev/sda of=/dev/sdb bs=4096 conv=noerror,sync
~~~


#### `dd if=[inputFile] of=[outputFile] conv=[conversionOptions]`

The utility can also convert the data being copied in a number of useful ways. 

`conv=ucase` will result in the new file being generated with lowercase letters converted to uppercase ones.

`conv=lcase` will result in the new file being generated with uppercase letters converted to lowercase ones.

~~~ bash
$ cat hello.txt
Hello World!
$ dd if=hello.txt of=out.txt conv=ucase
0+1 records in
0+1 records out
13 bytes copied, 0.00280173 s, 4.6 kB/s
$ cat out.txt
HELLO WORLD!
$ dd if=hello.txt of=out.txt conv=lcase
0+1 records in
0+1 records out
13 bytes copied, 0.00282392 s, 4.6 kB/s
$ cat out.txt
hello world!
~~~

`conv=ebcdic` will convert the data format of a file from ASCII to EBCDIC

`conv=ascii` will convert the data format of a file from EBCDIC to ASCII
