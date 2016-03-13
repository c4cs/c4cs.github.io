---
---

mv
--

`mv` is used to move a source file or directory into a destination directory. It is also commonly used to rename files. 

~~~ bash
$ mv source desination
~~~

<!--more-->

### Useful Options / Examples

#### `mv source destination`
~~~ bash
$ ls 
file1 file2 file3 directory1
$ mv file1 directory1 
$ ls 
file2 file3 directory1 
$ ls ../directory1
file1
~~~

##### Break it down

 * mv source destination simply moves the source file to the destination directory.   In this case, we moved file1 into directory1. 

#### `mv -r source destination`

~~~ bash
$ ls 
file1 file2 file3 directory1 directory2 
$ mv -r directory2 directory1
$ ls 
file1 file2 file3 directory1 
$ ls ../directory1
directory2
~~~

##### Break it down

 * mv -r source destination recursively moves source into destination. This is necssary when moving directories. 

#### `mv -t destination source1 source2 source3..`

~~~ bash
$ ls 
file1 file2 file3 directory1 
$ mv -t directory1 file1 file2 
$ ls 
file3 directory1 
$ ls ../directory1
file1 file2 
~~~

##### Break it down

 * mv -t destination source1 source2.. moves multiple sources into the desination directory specified after -t 
 * Note: this commmand doesn't work on OSX




