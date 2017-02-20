---
---

nano
----


`nano` is a simple text editor for unix systems, with a much smaller learning curve than vi and emacs. It is great for people who are new to the command line, and need to quickly make small changes to files.

~~~ bash
$ nano filename
~~~


<!--more-->

`nano` comes pre-installed on most linux distributions. If your distribution does not contain `nano`, you can easily install it with `apt`.

~~~ bash
$ apt-get install nano
~~~

### Why nano?

`nano` is perfect for people who need to change files on the command line, but don't have the time (or patience) to learn the ins and outs of vim/emacs. If you often use an external editor for programming but occasionally need to make changes to config files on a remote server, `nano` is your best friend.

![example image of nano editor layout](https://www.nano-editor.org/multibuffer.png)

In `nano`, common keyboard shortcuts are displayed at the bottom of the screen. No more forgetting how to save and close, or googling how to search for a keyword - `nano` has your back!

### Command Reference

`nano` has the benefit of being very beginner-friendly as well as maintaining some powerful features from other editors. Here are some useful commands that are not listed on the main screen.

- `Ctrl+^` aka `Ctrl+6` - Set mark for cut/copy (use arrow keys to extend/retract mark)
- `Alt+^` aka `Alt+6` - Copy text
- `Alt+U` - Undo
- `Alt+E` - Redo
- `Alt+\` - Go to beginning of file
- `Alt+/` - Go to end of file
- `Alt+(` aka `Alt+9` - Go to beginning of paragraph
- `Alt+)` aka `Alt+0` - Go to end of paragraph
- `Alt+-` - Scroll up one line without moving cursor
- `Alt+=` - Scroll down one line without moving cursor
- `Alt+$` - Enable/disable soft wrapping for long lines

### External References

* [Official GNU nano Homepage](https://www.nano-editor.org/)
