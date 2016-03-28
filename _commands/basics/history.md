---
---

history
--

`history` is used to list command history. By default, `history` will print the last 500 commands typed into the terminal.

~~~ bash
$ history
  ...
  498  third_most_recent_command
  499  second_most_recent_command
  500  most_recent_command
  501  history
~~~

<!--more-->

### Useful Options

#### `history | grep <search_string>`
This option allows you to search for most recent commands containing the search string

~~~ bash
$ history | grep cd
    9  cd /home/name/secrets
   11  cd topSecrets
   14  history | grep cd
~~~

#### `!<#>`
This shortcut runs the #th command from your history.

~~~ bash
$ !11
cd topSecrets
~~~

#### `!<string>`
This option will execute the last command starting with <string>.
My favorite use for this is the following:

~~~ bash
$ !.
./lastExecutable with lots of command line options
~~~

Executing `!m` (to run the makefile) followed by `!.` saves me lots of typing time.

#### `history -c`
This options clears your history - this is for when you don't want anyone to know that you accessed your `secrets/topSecrets` directory
