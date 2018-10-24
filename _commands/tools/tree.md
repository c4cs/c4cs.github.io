---
---

tree
-------

`tree` displays a directory structure in a tree-like visualization

~~~ bash
tree 

.
├── README.md
├── template.md
└── tools
    ├── git.md
    └── tree.md

1 directory, 4 files
~~~

<!--more-->

### Useful Options / Examples

#### `tree -L`
`tree`, by default, will recursively list all directories and files as far as it can go. For large directories, it may be best to limit how deep it lists.  
This can be done with the 'L' flag, used as `tree -L <number of levels>`  
Note: number must be greater than 0.  
1 will list the current director, 2 will list the current and the contents of directories within, and following on with higher levels.  

~~~ bash
tree -L 1

.
├── README.md
├── template.md
└── tools

1 directory, 2 files
~~~

#### `tree -d`

`tree -d` will cause `tree` to only list directories, omitting files within.

~~~ bash
tree -L 2 -d

.
└── tools

1 directory
~~~

#### `tree -s -h --du`

`tree -s -h` can be used to additionally list the size of files in a `h`uman-readable format.  
Adding `--du` additionally lists the size of directories.

~~~ bash
tree -L 2 -s -h --du

├── [ 827]  README.md
├── [ 248]  template.md
└── [ 15K]  tools
    ├── [ 10K]  git.md
    └── [1.1K]  tree.md

  21K used in 1 directory, 4 files
~~~

#### `tree -a`

Additionally lists hidden files, akin to `ls -a`.

### Extras

#### `tree -f`

Print the fullpath (relative to the current directory), generally combined with `-i`.

~~~ bash
`tree -f`

.
├── ./README.md
├── ./template.md
└── ./tools
    ├── ./tools/git.md
    └── ./tools/tree.md

1 directory, 4 files
~~~

#### `tree -i`

Print without the indentation lines, useful if combined with `-f`.

~~~ bash
`tree i`

.
README.md
template.md
tools
git.md
tree.md

1 directory, 4 files
 ~~~

#### `tree -D`

Additionally prints the last modified date of each listing.

~~~ bash
`tree -D`

.
├── [Oct 23 13:47]  README.md
├── [Oct 23 13:47]  template.md
└── [Oct 23 21:59]  tools
    ├── [Oct 23 13:47]  git.md
    └── [Oct 23 21:59]  tree.md

1 directory, 4 files
~~~

#### `tree -t`

Sort by last modified date, ascending (bottom will be latest modified)

#### `tree -r`

Sorts in reverse, such as descending with `-t` or reverse alphabetical by default.

#### `tree -p`

Prints the permissions of each file and directory.

~~~ bash
`tree -p`

.
├── [-rw-r--r--]  README.md
├── [-rw-r--r--]  template.md
└── [drwxr-xr-x]  tools
    ├── [-rw-r--r--]  git.md
    └── [-rw-r--r--]  tree.md

1 directory, 4 files
~~~
