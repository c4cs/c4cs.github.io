---
---

who
-------

`who` is a command that shows which users are currently logged on the machine.

~~~ bash
$ who
alice    pts/0        2016-03-19 20:52 (:1)
bob      pts/1        2016-03-18 09:00 (:1)
mallory  pts/4        2016-03-19 22:48 (0587396660.track.nsa.gov)
~~~

<!--more-->

### Useful Options / Examples
-------
#### `who -q`
~~~ bash
$ who -q
alice bob mallory
# users=3
~~~
##### Break it down
`who` with the `-q` flag prints out all the logged on usernames on a single line, and then the total number of logged on users on second line.

-------

#### `who -b`
~~~ bash
$ who -b
         system boot  2016-02-26 08:43
~~~
##### Break it down
`who` with the `-b` flag displays the time of the last system boot.

-------

#### `who -Ha`
~~~ bash
NAME       LINE         TIME             IDLE          PID COMMENT  EXIT
           system boot  2016-03-18 13:04
           run-level 5  2016-03-18 13:04
LOGIN      tty1         2016-03-18 13:04              1594 id=tty1
           pts/0        2016-03-19 01:59             12031 id=ts/0  term=0 exit=0
alice    + pts/1        2016-03-19 22:38   .          2715 (:1)
bob      + pts/2        2016-03-19 22:39  old         5239 (:1)
mallory  - pts/3        2016-03-19 22:40   .         10892 (0587396660.track.nsa.gov)
~~~
##### Break it down
`who` with the `-h` flag prints out a line of headings for each column of information. The `-a` or the `-all` option prints all the data the `who` command allows. This includes the boot time, login processes, current runlevel, dead processes, and other user & processes data. 

-------

#### `who mom likes`
~~~ bash
$ who mom likes
alice    pts/0        2016-03-19 20:52 (:1)
$ who am i
alice    pts/0        2016-03-19 20:52 (:1)
$ who -m
alice    pts/0        2016-03-19 20:52 (:1)
~~~
##### Break it down
This only shows information associated with the user who called the command. It is equivalent to to `who am i` and `who -m`
