---
---

history
--

`history` is used to display the most recently used commands.

~~~ bash
$ history [options]
~~~

<!--more-->

### Useful Options / Examples

If a number is specified after `history`, up to this number of previous command will 
be printed. Otherwise, it will default to 500.

#### `history`

~~~ bash
$ history
  1  [500th most recently used command]
  .
  .
  500  history
~~~

##### **Break it down**
This displays up to the 500 most recently used commands. If fewer than 500 commands have 
been executed, it will display all of them. This example is in the case that exactly 
500 commands have been executed to this point; otherwise, the [1] and [500] would be 
shifted accordingly.

#### `history [n]`

~~~ bash
$ history 2
  500  history
  501  history 2
~~~

##### **Break it down**
This displays up to the 2 most recently used commands, as specified by the optional argument. 
If fewer than 2 commands have been executed, it will display all of them. This example is in 
the case that 501 commands have been executed to this point; otherwise, the [500] and [501] would be 
shifted accordingly.

#### `history -c`

~~~ bash
$ history -c
~~~

##### **Break it down**
This clears the history list. It produces no output.

#### `history -d [offset]`

~~~ bash
$ history -d 2
~~~

##### **Break it down**
This deletes the history entry at the specified offset from the beginning of the history. 
It produces no output.

#### `history -a [file]`

~~~ bash
$ history -a
~~~

##### **Break it down**
This adds the commands executed since the beginning of the current session to the history file. 
Unless a file is specified, the value of `$HISTFILE` is used as the history file.
It produces no output.

#### `history -n [file]`

~~~ bash
$ history -n
~~~

##### **Break it down**
This adds to the history list entries that have been added to the history file since the beginning of 
the current session. Unless a file is specified, the value of `$HISTFILE` is used as the history file. 
It produces no output.

#### `history -r [file]`

~~~ bash
$ history -r
~~~

##### **Break it down**
This adds all entries in the history file to the history list. 
Unless a file is specified, the value of `$HISTFILE` is used as the history file. It produces no output.

#### `history -w [file]`

~~~ bash
$ history -w
~~~

##### **Break it down**
This writes all entries in the history list to the history file. 
Unless a file is specified, the value of `$HISTFILE` is used as the history file. It produces no output.

#### `history -p [args]`

~~~ bash
$ history -p hi
  hi
~~~

##### **Break it down**
This performs a history substitution using the args provided and prints the result to standard output.

#### `history -s [args]`

~~~ bash
$ history
  1  ls
$ history -s hi
$ history
  1  ls
  2  hi
~~~

##### **Break it down**
This adds the specified args to the end of the history list. It produces no output.

