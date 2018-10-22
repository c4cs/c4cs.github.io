---
---

rm
-------

`rm` removes files or directories. An example is shown below:

~~~ bash
$ ls
file1.txt  file2.txt  file3.txt
$ rm file2.txt
$ ls
file1.txt  file3.txt
~~~

<!--more-->

### Useful Options / Examples

#### `rm <filename>`

###### Using just `rm` followed by a filename without any options removes the corresponding file.

#### `rm -r <directory-name>`

##### `-r` removes directories and their contents recursively.

~~~ bash
$ ls
Desktop  Documents  Downloads
$ mkdir testdir
$ ls
Desktop  Documents  Downloads  testdir
$ cd testdir
$ touch file1 file2 file3
$ ls
file1  file2  file3
$ cd ..
$ rm -r testdir
$ ls
Desktop  Documents  Downloads
~~~

#### `rm -f`

##### `-f` ignores nonexistent files while removing files and does not prompt.

~~~ bash
$ ls
file1 file2 file3
$ rm fileNotThere
rm: cannot remove 'fileNotThere': No such file or directory
$ rm -f fileNotThere
$
~~~

#### `rm --help`

##### `--help` displays the help message for the `rm` command.

~~~ bash
$ rm --help
Usage: rm [OPTION]... [FILE]...
Remove (unlink) the FILE(s).

  -f, --force           ignore nonexistent files and arguments, never prompt
  -i                    prompt before every removal
  -I                    prompt once before removing more than three files, or
                          when removing recursively; less intrusive than -i,
                          while still giving protection against most mistakes
      --interactive[=WHEN]  prompt according to WHEN: never, once (-I), or
                          always (-i); without WHEN, prompt always
      --one-file-system  when removing a hierarchy recursively, skip any
                          directory that is on a file system different from
                          that of the corresponding command line argument
      --no-preserve-root  do not treat '/' specially
      --preserve-root   do not remove '/' (default)
  -r, -R, --recursive   remove directories and their contents recursively
  -d, --dir             remove empty directories
  -v, --verbose         explain what is being done
      --help     display this help and exit
      --version  output version information and exit

By default, rm does not remove directories.  Use the --recursive (-r or -R)
option to remove each listed directory, too, along with all of its contents.

To remove a file whose name starts with a '-', for example '-foo',
use one of these commands:
  rm -- -foo

  rm ./-foo

Note that if you use rm to remove a file, it might be possible to recover
some of its contents, given sufficient expertise and/or time.  For greater
assurance that the contents are truly unrecoverable, consider using shred.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/rm>
or available locally via: info '(coreutils) rm invocation'
~~~

