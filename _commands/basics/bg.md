---
---

bg
---

`bg` resumes a stopped job in the background, so the terminal remains usable.

~~~ bash
$ gedit file.txt
^Z
$ bg 'gedit file.txt'
$ jobs
[1]+ Running    gedit file.txt
$
~~~

<!--more-->

### Useful Options / Examples

`bg` can be passed job numbers as well as job names

~~~ bash
$ jobs
$ sleep 100
^Z
$ gedit file.txt
^Z
$ jobs
[1]+ Stopped    sleep 100
[2]+ Stopped    gedit file.txt
$ bg 2
$ jobs
[1]+ Stopped    sleep 100
[2]+ Running    gedit file.txt
$ bg 'sleep 100'
$ jobs
[1]+ Running    sleep 100
[2]+ Running    gedit file.txt
$
~~~

### Related Commands
[fg](../commands/fg), [jobs](../commands/jobs), [kill](../commands/kill)

