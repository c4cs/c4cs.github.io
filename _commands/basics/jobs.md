---
---

jobs
-------

`jobs` is a command to view processes running in the background of the shell

~~~ bash
$ gedit jobs.md &
$ gedit example.txt
$ jobs
[1]-  Running        gedit jobs.md &
[2]+  Done           gedit example.txt
~~~

<!--more-->

### Useful Options / Examples

### `jobs %string`

List only jobs that start with `string`. Useful if you have lots of jobs running

### `jobs -l`

List process ids of running jobs. Use `jobs -p` to list *only* the process ids

~~~bash
$ jobs -l
[1]- 18511 Running   gedit jobs.md &
[2]+ 18519 Done      gedit example.txt &
~~~

### `jobs -n`

List only the jobs that have finished since you were last notified

### `jobs -r` 

List only jobs that are still running

### `jobs -s`

List only jobs that have stopped


#### Example command

~~~bash 
$ jobs -lr
[1]+ 18511 Running   gedit jobs.md &
~~~
The -r flag means that jobs ignores the finished gedit process created by
`gedit example.txt&`
The -l flag means that jobs adds the `18511`, which is the process id of `gedit jobs.md&`

#### Example command

~~~bash
$ jobs
[1]   Running        sudo bundle exec jekyll serve &
[2]-  Running        gedit jobs.md &
[3]+  Running        nautilus . &
$ jobs %ged
[2]-  Running        gedit jobs.md &
~~~

The second command prints only the gedit proces, since it is the only process starting with `ged`
