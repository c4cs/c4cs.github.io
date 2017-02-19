---
---

Asciiquarium
-------

The command `asciiquarium` fills your terminal with a lively aquarium in all ascii text


<!--more-->

You first need to install a perl package called Term-Animation

~~~ bash
$ sudo apt-get install libcurses-perl
$ cd /tmp
$ wget http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/Term-Animation-2.4.tar.gz
$ tar -zxvf Term-Animation-2.4.tar.gz
$ cd Term-Animation-2.4/
$ perl Makefile.PL && make && make test
$ sudo make install
~~~

Next you need to download and install asciiquarium

~~~ bash
$ cd /tmp
$ wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
$ tar -zxvf asciiquarium.tar.gz
$ cd asciiquarium_1.1/
$ sudo cp asciiquarium /usr/local/bin
$ sudo chmod 0755 /usr/local/bin/asciiquarium
~~~

To view the your virtual fish bowl:

~~~ bash
$ asciiquarium
~~~

#### COMMANDS

While running:

Press ‘q’ to quit

Press ‘r’ to redraw

Press ‘p’ to pause





