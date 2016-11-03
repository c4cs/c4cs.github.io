---
---

bg
--

`bg` is used to continue a stopped job by running it in the background. By default, `bg` will simply resume the most recently suspended job. `bg` will commonly be used with the [`fg`](/commands/fg) and [`jobs`](/commands/jobs) commands.

~~~ bash
$ bg
$ bg [%jobID]
~~~

<!--more-->

### Useful Options / Examples

#### `bg [%jobID]`
~~~ bash
$ jobs
[1]- Running    bash download-file.sh
[2]+ Stopped    cp /usr/LargeDir /usr/SomewhereElse
$ bg %2
$ echo "Run more jobs while cp /usr/LargeDir /usr/SomewhereElse runs in background"
~~~

##### Break it down

 * The `%2` brings job number 2 to the background. Alternatively `%cp` would bring the same job to the background.
 * Bringing multiple jobs is possible by using the syntax:

~~~ bash
$ bg [%jobID1] [%jobID2] [%jobID3] ... [%jobIDN]
~~~





