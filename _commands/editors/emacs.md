---
---

emacs
--

`emacs` is used to edit files in emacs

~~~ bash
$ emacs filename
~~~

Then file specified by `filename` will be opened in emacs, and you can use emacs to edit it.

<!--more-->

### Useful Options / Examples

#### `emacs -nw`

~~~ bash
$ emacs -nw
~~~

Open Emacs directly in terminal.

##### Break it down

 * `-nw` means new window.
 * You may occasionally want to run Emacs directly in the terminal window.  Use the -nw option for this.

#### `emacs -q`

~~~ bash
$ emacs -q
~~~

Open Emacs and do not load a init file.

##### Break it down

 * `-q` means do not load an init file.
 * When Emacs is started, it normally tries to load a Lisp program from an init file.
   This file, if it exists, specifies how to initialize Emacs for you. Emacs looks for
   your init file using the filenames ~/.emacs, ~/.emacs.el, or ~/.emacs.d/init.el. Here,
   ~/ stands for your home directory.

#### `emacs +number file`

~~~ bash
$ emacs +7 filename
~~~

Open Emacs and move the cursor to line 7.

##### Break it down
 * Go to the line specified by `number`.
 * Do not insert a space between the "+" sign and the `number`.

#### `emacs -font, -fn`

~~~ bash
$ emacs -font 12
~~~

~~~ bash
$ emacs -fn 12
~~~

Open Emacs with font size 12.

##### Break it down

 * Set the Emacs window’s font to that specified by font.
 * When you specify a font, be sure to put a space between the switch and the font name.

#### `emacs -geometry`

~~~ bash
$ emacs -geometry 70x24 filename
~~~

Open a frame with 70 chars wide and 24 chars high.

##### Break it down

 * Set the Emacs window’s width, height, and position as specified. The width and height are specified 
   in characters; the default is 80x24.

#### `emacs -fg`

~~~ bash
$ emacs -fg red filename
~~~

Open Emacs and set the color of the text red.

##### Break it down

 * On color displays, sets the color of the text.
   See the file /usr/lib/X11/rgb.txt for a list of valid color names.

