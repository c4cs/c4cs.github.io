---
---

jobs
--

`jobs` is used to list the jobs running in the background of the current shell session.

The general format is

<!-- minimal example -->
~~~ bash
$ jobs [options] [jobID]
~~~

<!--more-->

A simple example is:

~~~ bash
$ gnome-calculator &
[1] 14616
$ xeyes &
[2] 14624
$ jobs
[1]-  Running                 gnome-calculator &
[2]+  Running                 xeyes &
~~~

This will display the status of every job in the current shell. Status is displayed by job number, status, and job. Jobs running in the background have an `&` after them. `+` refers to the job that was sent to the background least recently and `-` refers to the second least recent job sent to the background.

### Useful Options / Examples

#### jobs 1
~~~ bash
$ jobs 1
[1]-  Running                 gnome-calculator &
~~~

##### Break it down

 * Display the status of the job with jobID 1.

#### jobs -p
~~~ bash
$ jobs -p
14616
14624
~~~

##### Break it down

 * Display only the process ids of every job in the current shell.

#### jobs -l
~~~ bash
$ jobs -l
[1]- 14616 Running                 gnome-calculator &
[2]+ 14624 Running                 xeyes &
~~~

##### Break it down

 * Display the process ids as well as the normal information for every job in the current shell.

#### jobs -n
~~~ bash
$ sleep 100 &
[3] 14707
$ jobs -n
[3]+  Running                 sleep 100 &
~~~

##### Break it down

 * Display the jobs in the current shell that have changed status since last notified. For example, if you start a new job or a job finishes since you last called jobs, `jobs -n` will display that job.

#### jobs -r
~~~ bash
$ jobs -r
[1]   Running                 gnome-calculator &
[2]-  Running                 xeyes &
[3]+  Running                 sleep 100 &
~~~

##### Break it down

 * Display only the running jobs in the current shell.

#### jobs -s
~~~ bash
$ xeyes
^Z
[1]+  Stopped                 xeyes
$ jobs -p
[1]+  Stopped                 xeyes
~~~

##### Break it down

 * Display only the stopped jobs in the current shell. You can stop a job by doing ctrl + z in the terminal.
