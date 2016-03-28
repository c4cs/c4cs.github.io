---
---

vi
----


`vi` is a text editor for programmers, designed to facilitate optimal efficiency when writing code. 

To open `vi`, simply type the following:

~~~ bash
$ vi [filename]
~~~


<!--more-->
This will open a file with the name specified. If there is an existing file with that name, it will open that file, however if no file is found with that name, a new, empty one will be created.

Since its creation, the developers have also released `vim (vi improved)`, an updated version with more features, such as support for more programming languages, compatibility with more OS's, and features like multilevel undo/redo. On some Linux distributions, the `vi` executable provided is actually `Vim`. 

Despite this, some programmers still prefer `vi` over `vim` for its simplicity and ease of access.


### Here are some useful things you can do in the editor:

- `esc` - enter command mode
- `h`, `j`, `k`, `l` - move cursor left, up, down, and right respectively.
- `i` - enter insert mode
- `s` -Delete character and enter insert mode
- `a` - insert after character
- `v + [direction]` - select text with cursor
- `:w` - write/save file
- `:q` - quit vim
- `dw` delete word
- `d$` delete to the end of the line
- `dd` delete entire line
- `y` - yank/copy selected text
- `p` - put/paste yanked text
- `r + [character]` - replace character at cursor with specified character
- `u` - undo action
- `ce` - replace text until end of word
- `/ + [search phrase]` - search file for specified phrase

And there are so many more! To learn more, type:
~~~~ bash
$ vimtutor
~~~~

