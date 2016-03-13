---
---

find
--
`find` is used to _find_ items matching certain specified criteria in a given directory tree.

~~~ bash
$ find ~/ -name "foo" -print
~~~

<!--more-->

will search for files (including directories themselves) with the filename `foo`, starting in the current directory and then recursively through the subdirectories of the current directory, printing out the pathnames of the matching items.

More generally, `find` commands take the following pattern:

~~~ bash
$ find [path(s)] [expressions]
~~~

where the `paths` are the starting directories for `find` to traverse, and `expressions` are options, all of which return boolean values. `find` will "find" files for which all of the expressions return **true**. Note that `expressions` can also include options that take _action_ on the files that are found.

## Useful Options & Usage Examples

All of the following options are part of the `expressions` in the above formula.

### Situation
You want to free up some space and it would be helpful to see what the space hogs are on your computer.

### Solution
Here, we will use the `-size` option and `+` operator to find files.

~~~bash
$ find . -size +1000M
./VirtualBox VMs/398_Ubuntu/398_Ubuntu.vdi
~~~

Well isn't that ironic?

#### Break it down

`.` in the place of the directory name indicates to search starting from the current directory we are in (and then moving to its subdirectories).

The `-size [numM]` is true for files of size `num` megabytes (you can use `k` for kilobytes, `G` for gigabytes etc.).

The `+` indicates we want this to return true for files of size _greater_ than 1000 MB. (`-`, as expected, would match files _less_ than 1000 MB). You can use `+` and `-` in this way for any numerical arguments in the options of find.

### Situation

You want to clean up the files that LaTeX generates as part of the compilation process. These files have extensions `.aux`, `.log`, and `.out` (some compilers generate different files from these). You have several directories with several `.tex` files that you've been accumulating for some time.

### Solution

The general process is to craft a command that will find the files we want (this is recommended for any commands with `find [...] -delete`, to make sure you can review exactly what you're going to be deleting when you re-run with `-delete`).

~~~bash
$ find -E . -regex ".*\.(aux|log|out)" -type f
./eecs445/Project_2/writeup/project2.aux
./eecs445/Project_2/writeup/project2.log
./eecs445/Project_2/writeup/project2.out
$
~~~

Once we run this and verify the files that we wish to delete, we would then run the same command, with specifying `-delete`:

~~~bash
$ find -E . -regex ".*\.(aux|log|out)" -type f -delete
$ 
$ find -E . -regex ".*\.(aux|log|out)" -type f
$ 
~~~

#### Break it down

the `-delete` option (which always evaluates true) will delete files that `find` has found (i.e. that match the rest of the options given to `find`).

`-E` is an option placed at the beginning of the `find` command (even before the directories being searched), which allows us to use the `-regex` option to to find files matching a regular expression pattern.

The `-regex` command matches against _full_ filepaths. So, if we want to match anything of the form `.*aux`, `*.log`, or `*.out` we can use the regex pattern

`".*\.(aux|log|out)"`

where the first `.*` is because we want this to match any `*.aux` file in any directory in the file tree.

We also want to only match files, so we can specify the type of the items we match with `-type`, which takes in an argument (`f` for files, `d` for directory, etc.)
