---
---

logsave
-------

logsave saves the output of a command into a logfile

~~~ bash
$logsave file.txt {Linux command}
~~~

<!--more-->

### Useful Options / Examples
On top of the output, logsave will also add a timestamp and results of the command to standard output.  If the designated file does not appear, logsave will queue the data and write to the file upon its creation. 
#### Example command
$logsave /var/output.txt df -h 
##### Break it down
Here, logsave saves the output of df, a Linux command, to var/output.txt, the designated file. 
#### Example command

##### Break it down