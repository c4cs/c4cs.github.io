---
---

ls
--

`ls` is used to _list_ the contents of a directory. By default, `ls` will simply print file names.

~~~ bash
$ ls
directory file
~~~

<!--more-->

### Useful Options / Examples

#### `ls -a`
~~~ bash
$ ls -a
.            ..           .hidden_file directory    file
~~~

##### Break it down

 * The `-a` option asks `ls` to list _all_ files. By convention, files or
   directories whose name start with a leading `.` are considered to be
   hidden files. Many times a program's configuration file is a hidden file
   (such as `~/.bashrc`). Another common use is for psuedo-temporary files
   that are important to the program but not the user (such as caches).
 * The special directories `.` and `..` are created by the operating system.
   They refer to the current directory (`.`) and parent directory (`..`).
   It is this special directory that makes `./a.out` work, the leading `./`
   is just a convenient shortcut for specifying a complete path.

#### `ls -l`

~~~ bash
$ ls -l
total 8
-rwxr-xr-x  1 ppannuto  wheel   0 Mar  8 11:38 executable_file
-rw-r--r--  2 ppannuto  wheel   0 Mar  8 11:38 hard_linked_file_ref1
-rw-r--r--  2 ppannuto  wheel   0 Mar  8 11:38 hard_linked_file_ref2
-rw-r--r--  1 ppannuto  wheel   0 Mar  8 11:38 regular_file
lrwxr-xr-x  1 ppannuto  wheel  12 Mar  8 11:38 symlink_to_regular_file -> regular_file
~~~

##### Break it down
~~~
lrwxr-xr-x  1 ppannuto  wheel  12 Mar  8 11:38 symlink_to_regular_file -> regular_file
|---------  | |-------  |----  |-------------- |--------------------------------------
|           | |         |      |               |
|           | |         |      |               \- File Name: Normally just the name of
|           | |         |      |                             the file. For symlinks, it
|           | |         |      |                             will also print the target
|           | |         |      |                             of the link
|           | |         |      |
|           | |         |      \- Last Modified Time: When this file was last touched
|           | |         |
|           | |         \- Group: This is the group that owns this file
|           | |
|           | \- Owner: This is the user who owns this file
|           |
|           \- Reference Count: This is the number of directory entries that point to
|                               this file. Notice that it is 2 for the hard-linked files.
|
\- Permissions: 'l' means this file is a symbolic link, it is not actually a file, but
                a pointer to the real file

                Next are (r)ead, (w)rite, and e(x)ecute permissions. There are three
                sets of these. The first is for the user that owns the file (ppannuto),
                the next is for the group that owns the file (wheel), and the last is
                for others (any user who is not the owner and is not in the wheel group).

                The easiest way to change permissions is the chmod command. For example,
                chmod +x file_name will add execute permissions to a file.
~~~

#### `ls -lSh /var/log | head -5`

~~~ bash
$ ls -lSh | head -5
total 53872
-rw-r--r--@  1 root             admin              11M Mar  8 11:36 commerce.log
-rw-r--r--@  1 ppannuto         staff              11M Mar  8 11:36 install.log
-rw-r--r--   1 root             wheel             1.1M Mar  6 13:53 corecaptured.log
-rw-r-----@  1 root             admin             687K Mar  8 11:49 system.log
~~~

##### Break it down

 * The `-h` flag asks for "human readable" output. This is a common flag for
   many low-level tools. The effect is that the file size is printed as 11M
   instead of 11594838 bytes.
 * The `-S` flag asks `ls` to sort the output by file size. This can be useful
   for finding big files taking up lots of space that shouldn't be around.

