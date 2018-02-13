---
---

alias
--

`alias` instructs the shell to replace one string with another when executing commands.

~~~ bash
$ alias rm='rm -i'
$ rm sample.txt
rm: remove regular empty file 'sample.txt'? Y
$ 
~~~

<!--more-->
 
 The advantages of using alias include:

1. Time Saving: can shorten the length of commands so we do not need to type out all the characters
2. No longer need to remember long command names
3. Can run multiple commands (using command chaining) with a single alias
4. Correct common misspellings of commands (`alias pdw='pwd'`)
5. Can help standardize the names of commands across multiple operating systems (`alias dir='ls'`)

### Description
Aliases are used to customize the shell session interface.  Using alias, frequently-used commands can be invoked
using a different, preferred term; and complex or commonly used options can be used as the defaults for a given command.

Aliases only persist for the **current** session, however, they can be loaded at login time by modifying the shell's
**.rc** file.  To add them permanently, we have to edit our shell profile files (**~/.bashrc**) and enter the alias into the file.

### Syntax
~~~ bash
alias [name=['command']]
~~~

*name* is the name of the new alias.

*command* is the command(s) which it initiates.

The alias name and replacement text can contain any valid shell input expect for *=*.

The commands, including any options, arguments and redirection operators, are all enclosed within a pair of
single or double quotes.

### Options/Examples

#### `alias`/`alias -p`/`compgen -a`


Invoking `alias` with no arguments will display all currently aliased commands.

~~~ bash
cjlebioda@cjlebioda-VirtualBox:~$ alias
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
~~~

So the command `ls` is actually an alias such that using `ls` will always display color output.


#### Removing Aliases


`unalias` removes aliases created during the current session **and** permanent aliases that are listed in system 
configuration files.  The option *-a* tells `unalias` to remove all aliases for the current user for the current 
shell.

Another way to remove an alias is by using the `alias` command to create a new alias with the same name to 
overwrite the existing alias with that name.

~~~ bash
cjlebioda@cjlebioda-VirtualBox:~$ unalias ll
cjlebioda@cjlebioda-VirtualBox:~$ ll
-bash:ll: command not found
~~~

#### Example Command

This alias will make our process table searchable with an argument we will pass in:

~~~ bash
$ alias psg='ps aux | grep -i -e'
$ psg bash
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
cjlebio+  2093  0.0  0.0  29764   356 pts/4    Ss   21:54   0:00 bash
cjlebio+  2151  0.0  0.1  29780  3404 pts/17   Ss+  21:57   0:00 bash
cjlebio+ 18476  0.0  0.2  29704  5220 pts/18   Ss   22:18   0:00 bash
$ 
~~~
