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
$ tree
.
├── directory1
│   └── file1
├── file2
└── file3

1 directory, 3 files
~~~

##### Break it down

 * mv source destination simply moves the source file to the destination directory. In this case, we moved file1 into directory1. 
 * note: tree will list the file heirarchy of the current directory. If you don't have it installed, you can use homebrew ( brew install tree).

#### `mv oldfilename newfilename`

~~~ bash
$ ls 
file1
$ mv file1 file1newname
$ ls 
file1newname
~~~

##### Break it down

 * mv is commonly used to change the name of files. Simply replace 'source' and 'destination' with the old and the new names of the file respectively. 

#### `mv -i -v source destination` 

~~~ bash
$ ls 
file1 directory1 
$ touch directory1/file2
$ mv directory1/file2 .
overwrite ./file2? (y/n [n]) y
directory1/file2 -> ./file2
~~~

##### Break it down

 * `-i` will run the mv command in 'interactive mode', meaning that it will prompt the user for confirmation whenever they are about to override a file
 * `-v` runs mv in 'verbose mode' where what is being moved and where it is being moved to is depicted in the terminal 
 * Many people alias mv to mv -iv by adding `alias mv='mv -iv'` to their `.bashrc`.


