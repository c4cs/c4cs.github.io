---
---

set
--

`set` is a built in shell command. It essentially allows you to set and change shell options, variables and positional parameters. You can view all your shell settings with the following command: 

~~~ bash
$ set 
~~~

`set` has many options but does not have a `man` page. Instead, use `help` to view what the options are: 

~~~ bash
$ help set
~~~

As mentioned above, there are many options to use with `set`. Prepending a + infront of the option disables that option while -option enables the option. Here's an example: 

As you recall in the `history` page, that prints out the previous commands entered. If you wish to prevent recording history you can enter the following: 

~~~ bash 
$ set +o history
~~~

To again record the history of your commands: 

~~~ bash 
$ set -o history
~~~


