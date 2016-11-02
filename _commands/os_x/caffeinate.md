---
---

caffeinate
-------

`caffeinate` is used to caffeinate your computer, i.e. prevent it from automatically going to sleep when idle, it is primarily used by processes, applications like 'Caffeine' and 'Amphetamine' are wrappers to this command.

~~~ bash
#Prevents your computer from going to sleep
caffeinate
~~~

<!--more-->

### Where to install

'caffeinate' usually comes in built with OSX's command-line tools. If you don't have them, you can install them via:

~~~ bash
xcode-select --install
~~~

### Synopsis

~~~ bash
caffeinate [-disu] [-t timeout] [-w pid] [utility arguments...]
~~~ 

### Flags

Here are some cool flags that you could use within your program.

[-w pid]


Each running process has a unique pid. A good way to see what the pid for a particular process is:


~~~ bash
pgrep <process_name>
~~~


Example:


~~~ bash
#caffeinate till process with pid 4565 exits
caffeine -w 4565
~~~


[-t time]


Example:


~~~ bash
#caffeinate for time seconds
caffeinate -t 5000
~~~


Below are some other flags and their descriptions, try them out!


|     Flag     |               Description                |
| :----------: | :--------------------------------------: |
|      -d      |  create an assertion to prevent the display from sleeping |
|      -i      |  create an assertion to prevent the system from idle sleeping     |
|      -t      |   specifies the timeout value for which this assertion is valid |
|      -m      | create an assertion to prevent disk from idle sleeping |
|      -s      | create an assertion to prevent the system from sleeping, only available when connected to charger |
|      -u      | creates an assertion to declare that the user is active. if no timeout value is specified, it defaults to 5 seconds |
|      -w      | waits for process with specified pid to exit |

