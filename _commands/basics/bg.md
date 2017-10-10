---
---

bg
---

'bg' resumes a stopped job in the background, so the terminal remains usable.

~~~ bash
$ gedit file.txt
^Z
$ bg 'gedit file.txt'
$ jobs
[1]+ Running    gedit file.txt
~~~

<!--more-->

### Useful Options / Examples

#### Example command
'bg' can be passed job numbers as well as job names

~~~ bash
$ jobs
[1]+ Stopped    gedit file.txt
$ bg 1
$
~~~

### Related Commands


