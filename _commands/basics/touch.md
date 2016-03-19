---
---

touch
--

`touch` is used to create new, empty files or update the timestamp of an existing file.

~~~ bash
$ touch newFile.txt
~~~

<!--more-->

will create a new, empty file named `newFile.txt` in the current directory.  The other main use for `touch`, updating timestamps, can be achieved by:

~~~ bash
$ touch existingFile.txt
~~~

As `touch` does not overwrite an existing file, `touch` here only updates the timestamp of a file.  This is useful
when trying to do something such as rerunning a makefile after having updated the makefile, but none of the files it operates on.

Generally, use:

~~~ bash
$ touch [option(s)] [path(s)]
~~~

### Useful Options / Examples

There are a number of useful options.  For instance, `-a` changes only the access time 
while using `-m` changes only the file's modification time.  You can combine these options
to get back to `touch`'s default behavior!

You can use the `-r` flag to reference another file's access time and update another file
to have those values.

The `-B` option rewinds a file's timestamp a specified number of seconds.  The `-d` flag
sets the timestamp equal to a relatively free form string (E.g. `Sun, 29 Feb 2016 13:24:31` or 
something like `next Thursday`) while the `-t` flag accepts a more rigid time format.

#### Situation

You want to update a file's timestamp to rerun make after having edited the makefile,
but don't want to change any of the files the makefile executes on.

##### Solution

Simply run 

~~~~bash
touch [pathToMakefileDependency]
~~~~

to update the timestamp of the file and then run the makefile again. It's that easy!

##### Break it down

`pathToMakefileDepenency` is the path to one of the dependencies of the makefile.  After
running this command, the timestamp of the specified path will be updated to the current
system time.  As `touch` does not overwrite previously existing files, only the timestamp is 
updated here.

#### Situation

You want to change the timestamp of a file `bestFile.txt` (for some reason) to next Saturday.

##### Solution

Use `touch` with its `-d` flag!!

~~~~bash
$ touch -d 'Next Saturday' bestFile.txt
~~~~

Catchy.

##### Break it down

The -d flag stands for date.  This accepts a freeform string specifying the date
to which the timestamp should be changed.  

`Next Saturday` is the date string which is passed to `touch` via `-d`.

`bestFile.txt` is the file whose timestamp will be changed.

Running this entire command sets the timestamp of `bestFile.txt` to the date of next
Saturday.

#### Situation

You want to create a number of new, empty files to upload to some web app which will
then manipulate those files.

##### Solution

Use `touch` to create new, empty files!

~~~~bash
$ touch newFile1.txt newFile2.txt newFile3.txt
~~~~

##### Break it down

As these new files don't yet exist in the current directory (assuming they don't), 
`touch` simply creates new empty versions of them in the directory.  It will create
an empty `newFile1.txt`, `newFile2.txt`, and `newFile3.txt`.
