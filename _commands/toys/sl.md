---
---

sl
---
`sl` is a useful tool which shows a **s**team **l**ocomotive animation in your terminal when you mistype `ls`.

~~~ bash
					(@@) (  ) (@)  ( )  @@    ()    @     O     @     O      @
					(   )
				(@@@@)
			(    )

		(@@@)
		====        ________                ___________
	_D _|  |_______/        \__I_I_____===__|_________|
	|(_)---  |   H\________/ |   |        =|___ ___|      _________________
	/     |  |   H  |  |     |   |         ||_| |_||     _|                \_____A
	|      |  |   H  |__--------------------| [___] |   =|                        |
	| ________|___H__/__|_____/[][]~\_______|       |   -|                        |
	|/ |   |-----------I_____I [][] []  D   |=======|____|________________________|_
__/ =| o |=-O=====O=====O=====O \ ____Y___________|__|__________________________|_
|/-=|___|=    ||    ||    ||    |_____/~\___/          |_D__D__D_|  |_D__D__D_|
	\_/      \__/  \__/  \__/  \__/      \_/               \_/   \_/    \_/   \_/
~~~

<!--more-->

### About

`sl` is a tool developed by Toyoda Masashi which claims to cure bad typing habits (the one of mistyping the common `ls` command). I just think it's a fun tool to print a steam train.

The tool is open source, and you can view the source/contribute at the [repository on GitHub here](https://github.com/mtoyoda/sl).

### Getting `sl`

Most systems shouldn't come with `sl` installed, but it is available on most major package managers for unix/unix-like systems. 

To install on macOS:

~~~ bash
$ brew install sl
~~~

To install on Debian based GNU/Linux distributions:

~~~ bash
$ sudo apt install sl
~~~




### Usage and Options

### `sl`

Displays an animation of an ascii steam locomotive.

~~~ bash
$ sl
~~~

Output:

~~~ bash
						(@@) (  ) (@)  ( )  @@    ()    @     O     @     O      @
					(   )
				(@@@@)
			(    )

		(@@@)
		====        ________                ___________
	_D _|  |_______/        \__I_I_____===__|_________|
	|(_)---  |   H\________/ |   |        =|___ ___|      _________________
	/     |  |   H  |  |     |   |         ||_| |_||     _|                \_____A
	|      |  |   H  |__--------------------| [___] |   =|                        |
	| ________|___H__/__|_____/[][]~\_______|       |   -|                        |
	|/ |   |-----------I_____I [][] []  D   |=======|____|________________________|_
__/ =| o |=-O=====O=====O=====O \ ____Y___________|__|__________________________|_
|/-=|___|=    ||    ||    ||    |_____/~\___/          |_D__D__D_|  |_D__D__D_|
	\_/      \__/  \__/  \__/  \__/      \_/               \_/   \_/    \_/   \_/
~~~

### `sl -a`

Displays an animation of an ascii steam locomotive where an **a**ccident is occuring on board and the passengers are calling for help.

~~~ bash
$ sl -a
~~~

Output:

~~~ bash
						(@@) (  ) (@)  ( )  @@    ()    @     O     @     O      @
					(   )
				(@@@@)
			(    )

		(@@@)
		====        ________                ___________
	_D _|  |_______/        \__I_I_____===__|_________|
	|(_)---  |   H\________/ |   |        =|HelpHelp!     _________________
	/     |  |   H  |  |     |   |         |\O/ \O/|     _|                \_____A
	|      |  |   H  |__--------------------| [___] |   =|                        |
	| ________|___H__/__|_____/[][]~\_______|       |   -|                        |
	|/ |   |-----------I_____I [][] []  D   |=======|____|________________________|_
__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__|__________________________|_
	|/-=|___|=O=====O=====O=====O   |_____/~\___/          |_D__D__D_|  |_D__D__D_|
	\_/      \__/  \__/  \__/  \__/      \_/               \_/   \_/    \_/   \_/
~~~

### `sl -l`

Displays an animation of a **l**ittle ascii steam locomotive.

~~~ bash
$ sl -l
~~~

~~~ bash
						(@@) (  ) (@)  ( )  @@    ()    @     O     @     O      @
					(   )
				(@@@@)
			(    )
		(@@@)
		++      +------ ____                 ____________________ ____________________
	    ||      |+-+ |  |   \@@@@@@@@@@@     |  ___ ___ ___ ___ | |  ___ ___ ___ ___ |
	  /---------|| | |  |    \@@@@@@@@@@@@@_ |  |_| |_| |_| |_| | |  |_| |_| |_| |_| |
	 + ========  +-+ |  |                  | |__________________| |__________________|
	_|--/~O========O-+  |__________________| |__________________| |__________________|
	//// \_/      \_/       (O)       (O)        (O)        (O)       (O)        (O)
~~~

### `sl -F`

Displays an animation of a **F**lying ascii steam locomotive (like the galaxy express 999).

~~~ bash
$ sl -f
~~~

### `sl -c`

Displays an animation of a **c**51 ascii steam locomotive instead of a D51. Essentially a different style of train.

~~~ bash
$ sl -c
~~~





~~~ bash
						(  ) (@@) ( )  (@)  ()    @@    O     @     O     @      O
					(@@@)
				(    )
			(@@@@)

		(   )
		___
		_|_|_  _     __       __             ___________
	D__/   \_(_)___|  |__H__|  |_____I_Ii_()|_________|
	| `---'   |:: `--'  H  `--'         |  |___ ___|      _________________
	+|~~~~~~~~++::~~~~~~~H~~+=====+~~~~~~|~~||_| |_||     _|                \_____A
	||        | ::       H  +=====+      |  |::  ...|   =|                        |
|    | _______|_::-----------------[][]-----|       |   -|                        |
| /~~ ||   |-----/~~~~\  /[I_____I][][] --|||_______|____|________________________|_
------'|oOo|==[]=- O=======O=======O   |  ||=======_|__|__________________________|_
/~\____|___|/~\_|      ||      ||      |__|+-/~\_|        |_D__D__D_|  |_D__D__D_|
\_/         \_/  \____/  \____/  \____/      \_/           \_/   \_/    \_/   \_/
~~~

### Other information

Any of these flags can be combined, so you could get a **l**ittle **F**lying **c**51 train with the passengers calling for **h**elp. 

The basic way this program works is it has some arrays of c-style strings (otherwise known as an array of arrays of `chars`). The different arrays are different components of the animation (i.e. an array for the steam) and the c-style strings within the arrays can be thought of as "frames" in the animation. The program cycles through these frames by using the unix function `usleep`, which suspends operation for a specified number of microseconds. So, it shows a frame, suspends operation and then shows another frame until the train is across the screen.
 





















