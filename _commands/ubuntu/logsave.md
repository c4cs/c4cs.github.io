---
---

logsave
-------

logsave saves the output of a command into a logfile

~~~ bash
$logsave file.txt {linux command}
~~~

<!--more-->

### Useful Options / Examples
On top of the output, logsave will also add a timestamp and results of the command to standard output.  If the designated file does not appear, logsave will queue the data and write to the file upon its creation.

The logsave command also takes a few options:

-a
This appends output to the designated file, rather than replacing its current contents.
-s
This skips writing to the log file text which is bracketed with a control-A (ASCII 001 or Start of Header) and control-B (ASCII 002 or Start of Text), allowing progress bar information to be visible on the console, but not written to the file.  
-v
This displays verbose output.

#### Example command
$ logsave output.txt df -h  
##### Break it down
Here, logsave saves the output of df, a Linux command that shows free disk space, to var/output.txt, the designated file.
#### Example command
$ logsave -a output.log echo "hello world"
hello world

$ cat output.log
Log of echo Hello world
Wed Nov 24 16:51:24 2010

Hello world

Wed Nov 24 16:51:24 2010
----------------
##### Break it down
Here is another logsave command.  The results of the echo command are printed (note, appended) to output.log.  
