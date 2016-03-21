---
---

t
-------

`t` lets you interface with Twitter from the command line.

~~~ bash
$ t update "tweet tweet"
$ t stream timeline -l
~~~

<!--more-->

t is a command line utility (CLI) for interacting with Twitter.
t is not typically bundled with an OS and requires installation. In order to install t you must already have Ruby installed. t requires a Twitter API token for each authorized user account.

Full documentation on t is available on the project's GitHub page: <a href="https://github.com/sferik/t">https://github.com/sferik/t</a>

t is compatabile with Linux, OS X, and Windows

### Installation

#### Verify that Ruby is installed
t depends on Ruby. Check that its installed on your system.

~~~ bash
$ ruby -v
~~~

#### Install t
Run the following to install t.

~~~ bash
$ sudo gem install t
~~~

Note: this may take several minutes to finish and may provide no feedback.

#### Configure Twitter API Settings
In your terminal type the following, followed by 'enter'.

~~~ bash
$ t authorize
~~~

This will direct you to <a href="https://apps.twitter.com">apps.twitter.com</a>. Click "Create New App" and fill out the required fields. On the confirmation page click "modify app permissions". Change permissions to "Read, Write, and Access direct messages"

(Congratulations -- you're a Twitter Developer!)

#### Authorize t
Switch back to your terminal where t is waiting. Copy and paste your new API key and API secret from your web browser when prompted by t. Finish authorization with a tap of 'ye old 'enter'.

t will redirect you to the Twitter app authentication page. Input your credentials and click "Authorize App". Copy the resulting PIN number back into your terminal where t is prompted for it. You'll be greeted with an "Authorization successful" message.

### Using t





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

The `-m` option prints all fortunes that match the given regex, much like how [`grep`](../tools/grep.html) works. You can generally just enter a word to search for (like in this example), even if you don't know how to use regex.

This option will also print to stderr the names of the cookie files that contain matching fortunes, so you may want to use `2>/dev/null` to hide them.
