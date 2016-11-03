---
---

jobs
--

`jobs` is used to _list_ all active or suspended jobs. `jobs` will commonly be used with the [`fg`](/commands/fg) and [`bg`](/commands/bg) commands.

~~~ bash
$ jobs
list of jobs in form
[jobID]		status		jobs
~~~

<!--more-->

### Useful Options / Examples

#### `jobs -l`
~~~ bash
$ jobs -l
[1]		14891	Running		firefox &
[2]+	14900	Stopped		sleep 10s
[3]-	14912	Running		sleep 20s &
~~~

##### Description
~~~ bash
$ jobs -l
[1]		14891	Running		firefox &
[2]+	14900	Stopped		sleep 10s
[3]-	14912	Running		sleep 20s &
 |        |        |            |
 \- jobID |        |            |
          \- PID   |            |
                   \- status    |
                                \-job
~~~

### `jobs -r`
~~~ bash
$ jobs -l
[1]		Running		firefox &
[3]-	Running		sleep 20s &
~~~

##### Description
 * the `-r` flag tells `jobs` to limit the list to running jobs

#### `jobs -s`
~~~ bash
$ jobs -s
[2]+	14900	Stopped		sleep 10s
~~~

##### Description
 * the `-s` flag tells `jobs` to limit the list to stopped jobs
