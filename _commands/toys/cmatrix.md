---
---

cmatrix
-------
 `cmatrix` is a program that simulate the cool scrolling lines from the movie 'The Matrix'.

To start `cmatrix`, simply type the following:

<!-- minimal example -->
~~~ bash
$ sudo apt install cmatrix
$ cmatrix 
~~~

<!--more-->

### Useful Options
~~~ bash
 Usage: cmatrix -[abBfhlsVx] [-u delay] [-C color]
 -a: Asynchronous scroll
 -b: Bold characters on
 -B: All bold characters (overrides -b)
 -f: Force the linux $TERM type to be on
 -l: Linux mode (uses matrix console font)
 -o: Use old-style scrolling
 -h: Print usage and exit
 -n: No bold characters (overrides -b and -B, default)
 -s: "Screensaver" mode, exits on first keystroke
 -x: X window mode, use if your xterm is using mtx.pcf
 -V: Print version information and exit
 -u delay (0 - 10, default 4): Screen update delay
 -C [color]: Use this color for matrix (default green)
 valid [color] options: green, red, blue, white, yellow, cyan, magenta and black.
~~~




#### Example command
~~~ bash
cmatrix -a     "the scroll will be Asynchronous
cmatrix -u 10  "set delay to 10 (slowest)
cmatrix -C red "set color to red
~~~
![cmatrix](http://www.asty.org/cmatrix/data/screen1.gif)

Visit [here](http://www.asty.org/cmatrix/) for more
