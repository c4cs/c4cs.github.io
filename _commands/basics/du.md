---
---

du
---
`du`, or _disk usage_, reports the sizes of directories, including of all of their contents and the sizes of individual files, and the sizes of each directory in the directory tree.

<!-- minimal example -->
~~~ bash
$ du [options] [directories and/or files]
~~~

<!--more-->

### Useful Options / Examples

#### `du`
~~~ bash
$ du
236 ./hw1
375 ./hw2
1794 .
~~~

##### Break it down

  * This is the simplest usage of `du`. It prints out the size of your current working directory and the size of all the directories inside of your current directory in KB. This example assumes you're in your `home/eecs398` directory, which contains the subdirectories `hw1/` and `hw2/`, both of which only contain files.

#### `du [directory or file]`
~~~ bash
$ du home/eecs398/hw1
236 ./_hw1
~~~

##### Break it down

  * This prints out the size of your `home/eecs398/hw1` directory. If this directory contained any subdirectories, it would print out the size of those subdirectories as well.

#### `du -h`
~~~ bash
$ du -h
236K ./hw1
375K ./hw2
1.7M .
~~~

##### Break it down

  * This prints out directory sizes in human-readable form, so instead of printing out only KB for each directory, it prints out the number of B, MB, KB, or GB depending on the size of each directory.

#### `du -sh`
~~~ bash
$ du -sh
1.7M .
~~~

##### Break it down

  * This tells du to _only_ print out the size of your current working directory (instead of printing out the size of all of your current working directories _and_ the sizes of all of its subdirectories).

#### `du -a`
~~~ bash
$ du -a
106K ./hw1/hw1.tex
130K ./hw1/hw1.pdf
236K ./hw1
75K  ./hw2/hw2.tex
300K ./hw2/hw2.pdf
375K ./hw2
400K ./README.pdf
1.7M .
~~~

##### Break it down

  * This tells du to also print out the sizes of every individual file in your current working directory and all of its subdirectories.
