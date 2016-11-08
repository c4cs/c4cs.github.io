---
---

Cmatrix
-------

The command `cmatrix` draws a Neo style matrix on your terminal and makes you feel a little more geekier.

~~~ bash
$ sudo apt-get install cmatrix
~~~

After install cmatrix, just type in the command in command line window. Like

~~~ bash
$ cmatrix -option 
~~~
<!--more-->

#### OPTIONS

`-a`: Asynchronour scroll

`-b`: Bold characters on

`-B`: All bold characters(overrides -b)

`-f`: Force the Linux $TERM type to be on

`-l`: Linux mode (sets "matrix.fnt" font in console)

`-o`: Use old-style scrolling

`-h`: Print usage and exit

`-n`: No bold characters (overrides -b and -B)

`-s`: "Screensaver" mode, exits on first keystroke

`-u delay`: Screen update delay 0 - 9, default 4

`-C color`: Use this color for matrix (default green). Valid colors are green, red, blue, white, yellow, cyan, magenta, and black. 

#### And BOOM! 

Magic happens. Hold `Ctrl` + `z` to exit.

#### BUGS
This program is very CPU intensive. Don't be surprised if it eats up over 40% ofCPU at times.
