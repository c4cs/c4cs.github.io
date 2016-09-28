---
---

fortune
-------

`fortune` prints a randomly-selected quip from its "cookie files".

~~~ bash
$ fortune
Good news, everyone!
~~~

<!--more-->

The cookie files are normally stored in `/usr/share/games/fortune/`. (Check `man fortune` on your system to be sure.)

The Ubuntu package repositories contain a variety of additional cookie files, including fortunes in other languages! Try `aptitude search fortunes`.

### Useful Options / Examples

#### Print a fortune from a particular file or directory

~~~ bash
$ sudo apt-get install fortunes-ubuntu-server
$ fortune ubuntu-server-tips
Did you know that releases of Ubuntu labeled LTS are maintained for 5 years
on servers? 'cat /etc/lsb-release' will tell you which release you are on.
~~~

You can specify the name of a cookie file to cause `fortune` to read from that file only. This also works for subdirectories of the cookie folder, like the ones used for different languages.

#### Show or hide offensive fortunes

~~~ bash
$ fortune -a
Handel's Proverb:
    You can't produce a baby in one month by impregnating 9 women!
~~~

Your system might have an `off/` directory in the cookie folder containing fortunes which could be offensive. By default, `fortune` will not read from this folder, but the `-a` option lets it choose from all fortunes (normal and offensive). Similarly, the `-o` option would make `fortune` *only* choose offensive fortunes.

#### List fortune files

~~~ bash
$ fortune -f
100.00% /usr/share/games/fortunes
    15.59% riddles
    31.91% literature
    52.50% fortunes
~~~

The `-f` command lists the cookie files that `fortune` will choose from. It takes into account the current options, meaning that the "offensive" files (see above) will not normally be listed - using `fortune -af` instead will include them.

It also shows the probability of picking each file. Instead of reading every cookie file every time you run `fortune`, it uses the file sizes to (fairly) choose a file to open before choosing a fortune from that file.

#### Print a short fortune

~~~ bash
$ fortune -s
Measure twice, cut once.
~~~

You can use `-s` or `-l` to print a short or a long fortune respectively. The `-n` option can then be used to specify the number of characters considered "short" - for instance, `fortune -s -n 40` prints a fortune no longer than 40 characters. This may be useful when pairing `fortune` with [`cowsay`](cowsay.html), if you want to prevent the speech bubble from getting too big.

#### Search for a fortune

~~~ bash
$ fortune -m Twain 2>/dev/null
Buy land.  They've stopped making it.
                -- Mark Twain
%
If you tell the truth you don't have to remember anything.
                -- Mark Twain
%
(...many more...)
~~~

The `-m` option prints all fortunes that match the given regex, much like how [`grep`](/commands/grep.html) works. You can generally just enter a word to search for (like in this example), even if you don't know how to use regex.

This option will also print to stderr the names of the cookie files that contain matching fortunes, so you may want to use `2>/dev/null` to hide them.
