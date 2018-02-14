---
---

kill
--
The kill command is used on Linux systems to terminate process by its process id without having to reboot the system.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
The syntax is kill [signal or option] PID(s)
$kill 27410         Means killing a current running process with process id 27410
~~~

<!--more-->

### Useful Options / Examples

#### Example command

##### kill -9 PID
Actually, kill is a command to send signals to the specified process, each process has a set of standard handlers by the operating systems, and signal 9 called SIGKILL can almost guarantee to kill a process if the default signal 15 can't kill it.

#### Example command

##### kill -l 
Although kill -9 PID is the most common kill commands and you probably don't need to know more, but if you really need to know the full list of about 60 different signals, type kill -l

#### Example command

##### ps -aux | less 
Yes, you want to kill a process, but you first need to know the process id of that process. By the command above you can see brief information of current running processes including its PID, thus you can kill that process by its process id
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~                                                                                                                                                            
~     

