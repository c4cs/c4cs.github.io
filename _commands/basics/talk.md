---
---

talk
--

`talk` allows you to chat with other logged in users from the terminal. It is a visual communication program which copies lines from your terminal and displays them on the terminal of another user. When first prompted, `talk` sends this message to the `talk` program on the other user's computer:

~~~bash
talk: connection requested by user_one@user_one's_machine
talk: respond with: talk your_name@your_machine
~~~

The second user would then reply by typing:

~~~ bash
talk your_name@your_machine
~~~

<!--more-->

### Useful Options / Information / Examples

It doesn't matter which machine someone replies from, as long as their login information is the same the two can type at the same time and the output will appear in separate windows.

When in talk:
`control-L(^L)` will reprint the screen.

`^H` will erase a character similar to backspace

`^U` will delete a whole line

`^W` will erase a word

`esc-p` and `esc-n` will scroll in your window

`ctrl-p` and `ctrl-n` will scroll the other user's text window

`^C` will exit the program and move the cursor to the bottom on the screen. The terminal will be restored to it's previous state before talk launched.\n\n

You can block talk requests by using the mesg command, but by default, talk requests are not blocked.


#### `talk` syntax
~~~bash
talk person [ttyname]
~~~

### Options
person:
If you want to `talk` to someone on your machine, person is just the person's login name. If you want to `talk` to a user on another host, put person in the format, "user@host'.

[ttyname]:
If you want to `talk` to a user who is logged in more than once, the optional `ttyname` argument can show the correct terminal name to contact them at.


