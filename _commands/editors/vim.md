---
---

vim
--

`vim` is a screen-oriented text editor.

To open `vim` and use it to edit `example_file.txt`, type 

~~~ bash
$ vim example_file.txt
~~~

<!--more-->

### Modes
vim has two modes: normal mode and insert mode. By default, you are in normal mode after opening the editor. In normal mode, you can do tasks like moving the cursor around, save changes, and quit editor. You can only make change to the file in insert mode. You can press the `i` key to go from normal mode to insert mode. 
You can press the `esc` key to switch from insert mode to normal mode.  

### Moving around
`j`/`k`/`h`/`l` move up/down/left/right. 

`w` move to the beginning of next word. 

`b` move to the beginning of the previous word. 

`e` move to the end of the next word. 

### Editing
`i` insert at current location

`a` insert after current location (append)

`I` insert AT START of current line

`A` insert AFTER END of current line

`o` insert line below current line (open)

`O` insert line ABOVE current line

`s` delete character under cursor and start inserting in its place (substitute text)

`S` delete all text on line and start inserting in its place (substitute line)

### Saving and quiting 
`:w` save current changes 

`:q` quit editor 

`:wq` save and quit 
