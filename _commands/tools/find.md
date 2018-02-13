---
---

find
---
`find` is used to search one or more directory trees of a file system, to locate files based on user-defined specifications and to apply a user-defined action on each matched target. 

<!-- minimal example -->
~~~ bash
$ find
.
./dir1
./dir1/fileInDir.txt
./file3.txt
./file2.txt
./file1.txt
~~~

<!--more-->

### Specifications

#### Basic Syntax

~~~ bash
$ find [-H] [-L] [-P] path... [expression]
~~~

`-P` flag explicitly instruct `find` not to follow symbolic links. This is the default behaviour.

`-L` flag causes the `find` command to follow symbolic links.

`-H` flag causes the `find` command to only follow symbolic links while processing the command line arguments.

#### Operators

Operators can be used to enhance the expressions of the find command. Operators are listed in order of decreasing precedence:

`( expr )` - forces precedence;

`! expr` - true if expr is false;

`expr1 expr2 (or expr1 -a expr2)` - AND. expr2 is not evaluated if expr1 is false;

`expr1 -o expr2` - OR. expr2 is not evaluated if expr1 is true.

#### Type filter

`find` supports several type filters. They can be configured using

~~~ bash
$ find -type x
~~~

where x may be any of:

`b` - block device (buffered)

`c` - character device (unbuffered)

`d` - **directory**

`f` - **regular file**

`l` - symbolic link. This is never true if the -L option or the -follow operator is in effect, unless the symbolic link is broken. If you want to search for symbolic links when -L is in effect, use -xtype (though that is a GNU extension)

`p` - named pipe

`s` - socket

`D` - door

Types listed in bold are most commonly used.

### Useful Options / Examples

All examples in this section are based on the following testing directory:

~~~ bash
$ tree
.
├── dir1
│   ├── file1.txt
│   └── fileInDir.txt
├── dir1_sln -> dir1/	# A symlink to dir1/
├── file1.txt
├── file1.txt.copy
├── file2.txt
└── file3.txt

2 directories, 6 files
~~~

#### `find`

~~~ bash
$ find
.
./dir1_sln
./dir1
./dir1/fileInDir.txt
./dir1/file1.txt
./file3.txt
./file2.txt
./file1.txt.copy
./file1.txt
~~~

##### Break it down

Equivalent to `find .` and `find . -print`. It simply lists out all the files in the current directory as well as the subdirectories in the current directory. Symlinks are included but not followed.

#### `find -L`

~~~ bash
$ find -L
.
./dir1_sln
./dir1_sln/fileInDir.txt
./dir1_sln/file1.txt
./dir1
./dir1/fileInDir.txt
./dir1/file1.txt
./file3.txt
./file2.txt
./file1.txt.copy
./file1.txt
~~~

##### Break it down

`-L` flag tells `find` to follow symlinks. Here `dir1_sln` is a symlink associated with `dir1/` and files under `dir1_sln` are also shown.

#### `find [path] -type [x] -name [name1] -a -name [name2] ...`

~~~ bash
$ find . -type f -name 'file*' -a -name '*copy'
./file1.txt.copy
~~~

##### Break it down

This command lists regular files with names starting with `file` and ending with `copy` in the current directory as well as its subdirectories. `-type f` adds a filter so that only regular files are listed. `-name 'file*'` matches any file starting with `file` and `-name '*copy'` matches those with trailing `copy` in their names. `-a` works as `AND` operator to apply both expressions to the search.

#### `find [path] -iname [name]`

~~~ bash
$ find . -type f -iname 'FiLe*' -a -iname '*cOpy'
./file1.txt.copy
~~~

##### Break it down

This command is identical with the previous one except that `-iname` is used to indicate an case-insensitive search.

#### `find [path] [expression] -exec [action] \;`

An additional file `file2.txt.copy` was added to the working directory only for this example.

~~~ bash
$ tree
.
├── dir1
│   ├── file1.txt
│   └── fileInDir.txt
├── dir1_sln -> dir1/
├── file1.txt
├── file1.txt.copy
├── file2.txt
├── file2.txt.copy
└── file3.txt

2 directories, 7 files
$ find . -type f \( -name 'file1*' -o -name 'file2*' \) -a \! -name '*.copy' -exec cp \{\} \{\}.copy2 \;
$ tree                                                                                                   
.
├── dir1
│   ├── file1.txt
│   ├── file1.txt.copy2
│   └── fileInDir.txt
├── dir1_sln -> dir1/
├── file1.txt
├── file1.txt.copy
├── file1.txt.copy2
├── file2.txt
├── file2.txt.copy
├── file2.txt.copy2
└── file3.txt

2 directories, 10 files
~~~

##### Break it down

This command finds files with names starting with `file1` or `file2` but not ending with `.copy`. Then it does a backup for these files with `.copy2` suffix. `-o` works as `OR` operator; `!` works as `NOT` operator; `( )` forces precedence; and `{ }` is used to indicate the search results. Note that these characters are escaped by `\` so that they are not interpreted as special shell characters.

### Reference: https://en.wikipedia.org/wiki/Find_(Unix)