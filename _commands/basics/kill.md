---
---

kill
--

`kill` is used to send a signal to a process.

~~~ bash
kill [-s] [-l] %pid
~~~

<!--more-->

### Useful Options / Examples


#### `kill -9 -1`

Kills all processes possible to be killed.

#### `kill -l 11`

Translates signal number 11 into its signal name.

#### `kill -L`

Lists the available signal choices in a tabular format.

#### `kill 123 543 2341 3453`

Sends the default signal (TERM) to the processes with IDs 123, 543, 2341, and 3453, terminating those processes.

