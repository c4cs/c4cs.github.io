---
---

sl
-------

Prints a steam locomotive that drives across the window.

~~~ bash
$ sl
~~~
<!--more-->

The ASCII train depicted below will travel horizontally across the terminal window.

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
 __/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__|__________________________|_
  |/-=|___|=   O=====O=====O=====O|_____/~\___/          |_D__D__D_|  |_D__D__D_|
   \_/      \__/  \__/  \__/  \__/      \_/               \_/   \_/    \_/   \_/

~~~

### How to install sl
Steam locomotive can be installed on Unix systems with apt-get or with [Homebrew on OSX](https://brew.sh/) with either

~~~ bash
$ sudo apt-get install sl
~~~

or

~~~ bash
$ brew install sl
~~~

respectively
### Special flags
* `-a` an accident has occurred on board, and passengers cry out for help as the train passes by
* `-l` a significantly smaller train runs instead
* `-F` the train flies diagonally upward
* `-c` a different type of train renders; a C51 instead of a D51. Note that using the `c` flag with the `l` flag unfortunately will not render a mini version of the C51 train
