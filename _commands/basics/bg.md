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

#### `bg` can be passed job numbers as well as job names
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

#### Background multiple jobs at once by passing multiple arguments
~~~ bash
$ jobs
$ sleep 15
^Z
$ sleep 20
^Z
$ sleep 25
^Z
$ sleep 30
^Z 
$ sleep 35
^Z
$ jobs
[1]  Stopped    sleep 15
[2]  Stopped    sleep 20
[3]  Stopped    sleep 25
[4]- Stopped    sleep 30
[5]+ Stopped    sleep 35
$ bg 1 2
$ jobs
[1]  Running    sleep 15
[2]  Running    sleep 20
[3]  Stopped    sleep 25
[4]- Stopped    sleep 30
[5]+ Stopped    sleep 35
$ bg 3 'sleep 30' 5
$ jobs
[1]  Running    sleep 15
[2]  Running    sleep 20
[3]  Running    sleep 25
[4]- Running    sleep 30
[5]+ Running    sleep 35
$
~~~

### Related Commands
[fg](../commands/fg), [jobs](../commands/jobs), [kill](../commands/kill)

