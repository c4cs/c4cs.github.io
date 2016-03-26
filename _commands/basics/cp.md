---
---

cp
--

`cp` is used to _copy_ files or directories.

~~~ bash
$ cp source destination
$ cp file1.txt file2.txt
$ cp -b file1.txt file2.txt
$ cp -v file1.txt file2.txt
$ cp * ~/Desktop
~~~

<!--more-->

### Useful Options / Examples

#### `cp`
~~~ bash
$ cp file1.txt file2.txt
~~~

##### Break it down

 * This is the simplest use of `cp`. It copies the contents of `file1.txt` and puts
   it into `file2.txt`. If `file2.txt` does not exist, it creates it and puts the
   contents of `file1.txt` into it. If `file2.txt` does exist, it overwrites it.

#### `cp -b`
~~~ bash
$ cp -b file1.txt file2.txt
~~~

##### Break it down

 * This flag makes a backup of the destination (if it exists) before overwriting it.
   The backup file will be called `file2.txt~`. If the destination does not exist, the
   flag doesn't do anything.


#### `cp -r`
~~~ bash
$ cp -r eecs280-w15 eecs280-w15-copy
~~~

##### Break it down

 * The `-r` option will copy directories recursively. That means that if you want to
   make a copy of a folder, including its sub-folders, you must include the `-r` flag.
   In the example above, the command will copy over all of the contents of `eecs280-w15`
   into another folder called `eecs280-w15-copy`.


#### `cp -u`
~~~ bash
$ cp -u file1.txt file2.txt
~~~

##### Break it down

 * This option ensures that the copy only occurs when the source file is newer than the
   destination file or when the destination file is missing. If `file2.txt` is updated 
   after `file1.txt`, the `file1.txt` will not be copied over to `file2.txt`. If `file2.txt`
   does not exist, it is created and will contain the contents of `file1.txt`.


#### `cp -v`
~~~ bash
$ cp -v file1.txt file2.txt
'file1.txt' -> 'file2.txt'
~~~

##### Break it down

 * This option explains what is being done during the copy process. It can be combined with
   other flags (like `-u`) so that it can be determined whether the copy occurred or
   not. If the copy did not occur, there will be no output.

#### `cp file1.txt ~/Desktop/HW4`
~~~ bash
$ cp file1.txt ~/Desktop/HW4
~~~

##### Break it down

 * This usage of cp is very useful. Instead of copying directly to another file, a directory
   can be specified. `file1.txt` will be copied over to a newly created file in the specified
   directory.

#### `cp * ~/Desktop/HW4`
~~~ bash
$ cp * ~/Desktop/HW4
~~~

##### Break it down

 * This usage of cp is similar to the example above. This time, all the files of the current
   folder will be copied to the specified directory. It is particularly useful if you wish
   to copy all files in one directory into another.
