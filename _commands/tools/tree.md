---
---

tree
-------

Recursively generates a color-coded, indented list of files within a directory.
To print out your current directory, simply type:

~~~ bash
$ tree
~~~
~~~ bash
.
├── main.cpp
├── testFiles
│   ├── edgecase1.cpp
│   └── largemem.cpp
├── references
│   ├── project2Spec.pdf
│   ├── pseudocode.txt
│   └── README.txt
└── Makefile

2 directories, 7 files

~~~

Tree is an extension not initially built into your terminal, and must be installed.
To install on a linux machine, enter:

~~~ bash
$ sudo apt-get install tree
~~~

<!--more-->

### Useful Options / Examples

#### Example command

~~~ bash
$ tree -d
~~~
~~~ bash
.
├── testFiles
├── references

2 directories, 7 files
~~~

The -d flag lists directories only.

#### Example command

~~~ bash
$ tree -a
~~~
~~~ bash
.
├── main.cpp
├── testFiles
│   ├── edgecase1.cpp
│   ├── edgecase2.cpp
│   └── largemem.cpp
├── references
│   ├── project2Spec.pdf
│   ├── pseudocode.txt
│   └── README.txt
├── .git
└── Makefile
~~~
The -a flag will print out hidden files, such as those that begin with '.'. This is useful for git directories.

Look online for more useful flags, such as -s (prints the size of the files), -D (prints the most recent time the files were touched), or -p (prints the permissions and protections of each file).


