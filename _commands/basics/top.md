---
---

top
--

`top` displays information on your Linux system, running processes, and system resources, including the CPU, RAM, swap usage, and total number of tasks being run:

~~~ bash
$ top
~~~

<!--more-->

~~~ bash
Processes: 255 total, 3 running, 6 stuck, 246 sleeping, 1066 threads   13:48:44
Load Avg: 1.79, 1.96, 1.66  CPU usage: 23.22% user, 4.64% sys, 72.12% idle
SharedLibs: 138M resident, 20M data, 21M linkedit.
MemRegions: 31043 total, 2250M resident, 129M private, 2114M shared.
PhysMem: 7842M used (1696M wired), 347M unused.
VM: 701G vsize, 533M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 17605/18M in, 14610/1889K out.
Disks: 123506/3994M read, 27200/553M written.

PID  COMMAND      %CPU  TIME     #TH   #WQ  #PORT MEM    PURG   CMPR PGRP PPID
581  mdworker     0.0   00:00.03 3     0    43    3136K  0B     0B   581  1
580  top          1.3   00:00.41 1/1   0    22    2144K  0B     0B   580  575
575  bash         0.0   00:00.01 1     0    17    760K   0B     0B   575  574
574  login        0.0   00:00.04 2     0    29    1136K  0B     0B   574  274
573  LookupViewSe 0.0   00:00.26 8     5    204   9860K  32K    0B   573  1
…(More info)

~~~


The `top` command is often used to display the processes that are using the most memory which can be viewed by typing `M`. The processes can also be sorted by CPU usage by typing `P`. A task can be killed using top by pressing `k` and then entering the process id.

### Useful Options / Examples

After running the `top` command:


#### `Q`



Exit the process list and go back to terminal



#### `M`



Sort the process list by memory usage with process using the most memory first



#### `P`



Sort the process list by cpu usage



#### `N`



Sort the process list by process id



#### `T`



Sort the process list by running time



#### `R`



Reverse the sorting order of the currently sorted column. By default, sorting is done in descending order



#### `U`



View only the processes of a specific user


#### `l`


Hide the load average information


#### `m`


Hide the memory information


#### `t`


Hide the task and cpu information

#### `h`
Opens a help menu
