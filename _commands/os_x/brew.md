---
---

brew
--

`brew`, or known by its longer name as Homebrew, bills itself as the "missing package manager for OS X".

~~~
$ brew install rsync
==> Installing rsync from homebrew/dupes
==> Downloading https://homebrew.bintray.com/bottles-dupes/rsync-3.1.2.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring rsync-3.1.2.el_capitan.bottle.tar.gz
🍺  /usr/local/Cellar/rsync/3.1.2: 8 files, 748.2K
~~~

<!--more--> 

That's right - `brew` uses emojis as part of its standard output 🙌 

Various Linux distributions include package managers for installing software out of the box (e.g. `apt-get` for Ubuntu), and `brew` is a third-party effort to replicate the same for OS X. As an example of `brew` usage, above is an example of installing [rsync](https://en.wikipedia.org/wiki/Rsync). 

To install `brew`, the [official Homebrew website](https://brew.sh) directs you to run this command, which incidentally explains itself as it runs:

~~~
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
~~~

### Useful Options / Examples

#### `brew install [package-name]`
~~~
$ brew install rsync
==> Installing rsync from homebrew/dupes
==> Downloading https://homebrew.bintray.com/bottles-dupes/rsync-3.1.2.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring rsync-3.1.2.el_capitan.bottle.tar.gz
🍺  /usr/local/Cellar/rsync/3.1.2: 8 files, 748.2K
~~~

##### Break it down

* The `brew install [package-name]` command is the command for installing various `brew` packages. 
* There is a [public list](https://github.com/Homebrew/homebrew-core/tree/master/Formula) of available packages that `brew` pulls from. Each package has a "formula", or package definition, that `brew` can parse. 
* Upon picking a formula, like `node`, `wget`, or `cowsay`, `brew` retrieves the formula and follows the instructions (e.g. downloading the appropriate files) to install that package.

#### `brew remove [package-name]`
~~~
$ brew remove rsync
Uninstalling /usr/local/Cellar/rsync/3.1.2... (8 files, 748.2K)
~~~

##### Break it down

* The `brew remove` command is the command for uninstalling various `brew` packages, given the name of a package, using the package's formula.

#### `brew update`
~~~
$ brew update
Updated Homebrew from 86fc508 to 5531fd9.
Updated 1 tap (homebrew/dupes).
==> New Formulae
...
==> Updated Formulae
...
==> Deleted Formulae
...
~~~

##### Break it down

* `brew update` updates `brew` to the latest version, directly from `brew`'s [GitHub repository](https://github.com/Homebrew/homebrew). 
* This includes refreshing `brew`'s "taps", which are essentially lists of formulae that your installation of `brew` can see. Above, you can see that I have one tap - `homebrew/dupes`, which has duplicates of useful Linux-y tools like `rsync`, `screen`, and `less`.

#### `brew upgrade`

~~~
$ brew upgrade
==> Upgrading 2 outdated packages, with result:
boost 1.60.0_1, coreutils 8.25
==> Upgrading boost
==> Downloading https://homebrew.bintray.com/bottles/boost-1.60.0_1.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring boost-1.60.0_1.el_capitan.bottle.tar.gz
🍺  /usr/local/Cellar/boost/1.60.0_1: 11,139 files, 436.0M
==> Upgrading coreutils
==> Downloading https://homebrew.bintray.com/bottles/coreutils-8.25.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring coreutils-8.25.el_capitan.bottle.tar.gz
==> Summary
🍺  /usr/local/Cellar/coreutils/8.25: 216 files, 8.3M
~~~

##### Break it down
* `brew upgrade` upgrades all of ones' packages to the latest releases.

#### `brew list`
~~~
$ brew list
autoconf	cowsay		gdbm		libtool		openssl		rbenv		sqlite
automake	dfu-util	gettext		libusb		pkg-config	readline	tmux
boost		fortune		gnu-getopt	mongodb		postgresql	ruby-build	valgrind
coreutils	gdb			libevent	node		python		scons		xz

~~~

##### Break it down

* `brew list` lists all of the `brew` packages that one has installed. For instance, you can see that I've installed `mongodb`, `node`, and `python`, among others.

#### `brew search [text]`
~~~
$ brew search wget
wget						wgetpaste                                                 
~~~

~~~
$ brew search /*get*/
gengetopt        gnu-getopt ✔     languagetool     libgetdata       vegeta           wgetpaste        wxwidgets      
Caskroom/cask/igetter                   Caskroom/cask/join-together             Caskroom/cask/pwnagetool              
~~~

##### Break it down

* `brew search [text]` or `brew search [/text/]` takes the input `text`, and tries to match it against all the packages it can find, including looking other popular taps.
*  It also accepts regular expressions wrapped in `/`, like the second example `/*get*/` above.
