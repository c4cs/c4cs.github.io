---
---

xclip
-------

`xclip` can put the output of a command into the X-clipborad if we pipe the command into xclip.

~~~ bash
ls -la | xclip
~~~

`xclip` can also directly copy the content of the following file:

~~~ bash
xclip SomeOtherFile.txt
~~~

`xclip -o` can print the stuff in X-clipboard.

~~~ bash 
xclip -o > output.txt
~~~

If you're on a Mac the equivalent command is `pbcopy`.
<!--more-->

### Useful Options / Examples

#### -selection

~~~ bash
ls -la | xclip -selection clipboard
~~~

##### Break it down

We can specify which X selection to use. The default is "primary". Other options are "secondary" and "clipboard". "clipboard" means the system clipboard. Thus, in the upper example, we can use <kbd>Ctrl+Shift+v</kbd> to paste the result later. 

##### To make life easier

As mentioned, `-selection clipboard` is more convenient than default setting, making an alias can make the life much easier:

~~~ bash
alias xclip='xclip -selction clipboard'
~~~


#### -loops, -l

~~~ bash
who | xclip -loops 3 -verbose
~~~

##### Break it down
With `-loops`, xclip will wait until it receives certain number of X-selection requests. In the example, `-verbose` makes xclip provide a running commentary of what it is doing. 

