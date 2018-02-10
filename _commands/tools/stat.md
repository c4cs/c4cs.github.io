---
---

stat
--
`stat` is used to display status information about a file or file system.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ stat test.txt
  File: 'test.txt'
  Size: 4096       Blocks: 8     IO Block: 4096 regular file
Device: 801h/2049d Inode:1319268 Links: 1
Access: (0664/-rw-rw-r--)  Uid: (1000/myname)   Gid: (1000/myname)
Access: YYYY-MM-DD HH:MM:SS -0500
Modify: YYYY-MM-DD HH:MM:SS -0500
Change: YYYY-MM-DD HH:MM:SS -0500
 Birth: -
~~~
<!--more-->

### Useful Options / Examples

#### File systems (`f`, `--filesystem`)

~~~ bash
$ stat -f directoryname
  File: "directoryname"
    ID: 294efda8470ab532 Namelen: 255     Type: ext2/ext3
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 6159711    Free: 3919892    Available: 3601236
Inodes: Total: 1572864    Free: 1271893
~~~

##### Break it down
The `-f`,`--filesystem` flag treats input as a file system.

#### Format and specifiers (`c`, `--format` and `%-`)

~~~ bash
$ stat -c %F foldername
directory
~~~

##### Break it down
* The `-c`, `--format` flag requires an operand (format specifier). Different format specifiers can be used to print specific information. Certain format specifiers will only return useful information if used for file systems (`-f`, `--filesystem` flag required).
* Useful format specifiers for files (without `-c`, `--filesystem`):
  * `%A` Access rights in human readable form
  * `%F` Filetype
  * `%s` Total size, in bytes
  * `%U` Username of owner
  * `%y` Time of last modification
* Useful format specifiers for file systems (with `-c`, `--filesystem`):
  * `%T` Type in human readable form

#### Example output:

~~~ bash
$ stat -f -c %T dirname # File system type
ext2/ext3
$ stat -f -c %T shareddirname
nfs
$ stat -c %A hw3.txt # Permissions
-rw-rw-r--
$ stat -f -c %A dirname # Some flags only work with files
?
~~~


