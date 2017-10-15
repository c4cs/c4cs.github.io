---
---

asciiquarium
-------
`asciiquarium` is a script that doubles as a cool screensaver for the terminal.

To start `asciiquarium`, simply type the following:

~~~bash
$ asciiquarium
~~~

Using ascii art, `asciiquarium` gives the terminal the feel of being out at sea
with fish swimming around and the occasional fisherman. `asciiart`  is not built-in to your terminal. 

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

### Useful Commands
- `r` - redo the art
- `q` - quit the program
- `p` - pause the program
