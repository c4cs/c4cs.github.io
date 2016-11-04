---
---

fg
--

`fg` is used to continue a stopped job by running it in the foreground. By default, `fg` will simply resume the most recently suspended backgrounded job. `fg` will commonly be used with the [`bg`](/commands/bg) and [`jobs`](/commands/jobs) commands.

~~~ bash
$ fg
$ fg [%jobID]
~~~

<!--more-->

### Useful Options / Examples

#### `fg [%jobID]`
~~~ bash
$ jobs
[1]- Running 		bash download-file.sh
[2]+ Stopped		cp /usr/LargeDir /usr/SomewhereElse
$ fg %2
~~~

##### Break it down

 * The `%2` brings job number 2 to the foreground. Alternatively `%cp` would bring the same job to the foreground.
 * Bringing multiple jobs is possible by using the syntax:

~~~ bash
$ fg [%jobID1] [%jobID2] [%jobID3] ... [%jobIDN]
~~~





