---
---

pstree
-------

pstree is a command the prints the entire process
heirarchy as a tree

~~~ bash
pstree

example output:
init--parent_ps -- running_ps
   |-- dif_prnt -- another_run_ps
~~~

<!--more-->

### Useful Options / Examples
You can also specify a process id to see all of its children
or you an specify a user to see all of the processes of that user

#### Example command
pstree pid

#### Example Output
ps--children--children

#### Example command
pstree username

#### Example Output
prsA -- subprocess -- etc

prsB -- subprocess

prsC -- subprocess
     |- another one

etc
