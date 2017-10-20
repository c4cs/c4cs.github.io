---
---

asciiquarium
-------
`asciiquarium` is a script that doubles as a cool screensaver for the terminal.

To start `asciiquarium`, simply type the following:

<!-- minimal example -->
~~~bash
$ asciiquarium
~~~

<!--more-->

### Examples of `asciiquarium`

Using ascii art, `asciiquarium` gives the terminal the feel of being out at sea
with fish swimming around and the occasional fisherman.

![asciiquarium](http://www.robobunny.com/projects/asciiquarium/screenshot.png)

`asciiquarium`  is not built-in to your terminal and in order to use it, you have to install it to your machine. 

If you are using a linux machine, do the following steps:

~~~bash
$ wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
$ tar -zxvf asciiquarium.tar.gz
$ cd asciiquarium_1.1/
$ chmod +x asciiquarium
$ sudo cp asciiquarium /usr/local/bin/asciiquarium
$ sudo cpan Term::Animation
$ asciiquarium
~~~

For Mac users, there's a nice [packaged
version](https://habilis.net/macasciiquarium/MacAsciiquarium_1.1.0.dmg) that will run out of the box,
courtesy of Chuck Houpt:

~~~bash
https://habilis.net/macasciiquarium/
~~~

#### Useful Commands
- `r` - redo the art
- `q` - quit the program
- `p` - pause the program
