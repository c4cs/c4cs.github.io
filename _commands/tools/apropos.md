---
---

apropos
---
`apropos`  is a tool that allows users to search manual page name and descriptions. It displays all the list of topics in the man pages that are related to the subject of a query. If you do not specify command will output entries that contain at least one keyword.

~~~ bash
$ apropos mkdir
$ apropos move -e

~~~

<!--more-->

### Useful Options / Examples

### `apropos --exact`

You can use `apropos --exact` or `apropos <keyword> -e` to specify you want results that match your keywords exactly. This prevents results that contain partial matches to your keywords.

~~~ bash
$ apropos --exact who
bsd-from (1)        - print names of those who have sent mail
from (1)            - print names of those who have sent mail
w (1)               - Show who is logged on and what they are doing.
w.procps (1)        - Show who is logged on and what they are doing.
who (1)             - show who is logged on
~~~




### `apropos --and`
This command allows you to find queries that contain all of the keywords listed, not just one.

~~~ bash
$ apropos --and move files
aa-remove-unknown (8) - remove unknown AppArmor profiles
cut (1)              - remove sections from each line of files
fanotify_mark (2)    - add, remove, or modify an fanotify mark on a filesyste...
git-clean (1)        - Remove untracked files from the working tree
git-prune-packed (1) - Remove extra objects that are already in pack files
git-rm (1)           - Remove files from the working tree and from the index
mv (1)               - move (rename) files
py3clean (1)         - removes .pyc and .pyo files
pyclean (1)          - removes .pyc and .pyo files
rm (1)               - remove files or directories
~~~
