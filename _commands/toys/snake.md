---
---

snake
-------
`snake` is a program that simulates a snake growing up by eating dollars.

To use `snake`, simply type:

~~~ bash
$ snake
~~~

<!--more-->
`snake` is a display-based game which must be played on a CRT terminal. The object of the game is to make as much money as possible without getting eaten by the snake.

`snake`  is not built-in to your terminal and in order to use it, you have to install it to your machine. 

If you are using a linux machine, do the following steps:

~~~bash
$ sudo apt install bsdgames
~~~


### Useful Options / Examples
- `-l` allows you to specify the length of the field. By default the entire screen length is used.
- `-w` allows you to specify the width of the field. By default the entire screen width is used.
- `-t` makes the game assume you are on a slow terminal.
- Type the following in the bash to see your highest score in game:

~~~bash
$ snscore
~~~

#### Example command

~~~bash
$ snake -l 5 -w 6
~~~