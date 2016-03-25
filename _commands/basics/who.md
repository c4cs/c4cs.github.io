---
---

who
-------

`who` is a command that shows which users are currently logged on the machine.

~~~ bash
$ who
alice    pts/0        2016-03-19 20:52 (:0)
bob      pts/1        2016-03-18 09:00 (:0)
mallory  pts/4        2016-03-19 22:48 (10.1.1.3)
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
alice    + :0           2016-03-19 22:38   .          2715 (:0)
bob      + pts/2        2016-03-19 22:39  old         5239 (:0)
mallory  - pts/3        2016-03-19 22:40   .         10892 (10.1.1.3)
~~~

##### Break it down
`who` with the `-H` flag prints out a line of headings for each column of information.
The `-a` or the `-all` option prints all the data the `who` command allows.
This includes the boot time, login processes, current runlevel, dead processes and logged on users.
The boot time is displayed on as the first entry of our example:

~~~ bash
           system boot  2016-03-18 13:04
~~~

The second line displays the [runlevel](https://en.wikipedia.org/wiki/Runlevel#Linux_Standard_Base_specification) of the machine.
`who` with the `-r` flag also displays the runlevel.
The runlevel is the current state of the machine; runlevel = 6 means the machine is rebooting and 5 means the system started normally.

~~~ bash
           run-level 5  2016-03-18 13:04
~~~

On the last three lines of the example, the users are displayed (the column headers are included for reference):

~~~
NAME       LINE         TIME             IDLE          PID COMMENT  EXIT
                                                                             <<<
alice    + :0           2016-03-19 22:38   .          2715 (:0)
bob      + pts/2        2016-03-19 22:39  old         5239 (:0)
mallory  - pts/3        2016-03-19 22:40   .         10892 (10.1.1.3)
|------    |----        |---------------  |---       |---- |---------
|          |            |                 |          |     |
|          |            |                 |          |     \- Shows the
|          |            |                 |          |        user's address
|          |            |                 |          |        :0 is shown for
|          |            |                 |          |        local users
|          |            |                 |          | 
|          |            |                 |          \- The process ID
|          |            |                 |             of the user's
|          |            |                 |             shell
|          |            |                 | 
|          |            |                 \- Shows the idle time of session
|          |            | 
|          |            \- Time the user logged in
|          | 
|          \- Shows where the shell is located. :0 means the user
|             on a local X Windows display session. pts stands for
|             "pseudo-terminal session" and created by remote sessions
|             and terminal emulator programs. In most cases, this means
|             the user is on a remote session like SSH.
|
\- The username of the owner of the session
~~~

-------

#### `who mom likes`
~~~ bash
$ who mom likes
alice    pts/0        2016-03-19 20:52 (:0)
$ who am i
alice    pts/0        2016-03-19 20:52 (:0)
$ who -m
alice    pts/0        2016-03-19 20:52 (:0)
~~~

##### Break it down
This only shows information associated with the user who called the command. It is equivalent to `who am i` and `who -m`.
Note that `who am i` is not the same command was `whoami`. See the [`whoami` page](whoami.html) for more information.
