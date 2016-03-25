---
---

emacs
--

`emacs` is used to open a file in emacs
~~~ bash
$ emacs filename
~~~
Then file specified by `filename` will be opened in emacs, and you can use emacs to edit it.

<!--more-->

### Useful Options / Examples

#### `emacs -q`

~~~ bash
$ emacs -q
~~~

##### Break it down

 * `-q` means do not load an init file.
 * `-q` will be ignored if it is followed by a `filename`.

#### `emacs +number file`

~~~ bash
$ emacs +7 filename
~~~

##### Break it down
 * Go to the line specified by `number`.
 * Do not insert a space between the "+" sign and the `number`.

#### `emacs -font, -fn`

~~~ bash
$ emacs -font 12 filename
~~~

~~~ bash
$ emacs -fn 12 filename
~~~

##### Break it down

 * Set the Emacs window’s font to that specified by font. You will find the various X fonts
   in the /usr/lib/X11/fonts directory. Note that Emacs will only accept fixed width fonts. 
   Under the X11 Release 4 font-naming conventions, any font with the value "m" or "c" in the 
   eleventh field of the font name is a fixed width font. Furthermore, fonts whose name are of
   the form widthxheight are generally fixed width, as is the font fixed. See **xlsfonts**(1) for 
   more information.
 * When you specify a font, be sure to put a space between the switch and the font name.

#### `emacs -geometry`

~~~ bash
$ emacs -geometry 70 filename
~~~

##### Break it down

 * Set the Emacs window’s width, height, and position as specified. The geometry specification
   is in the standard X format; see X(1) for more information. The width and height are specified 
   in characters; the default is 80 by 24.

#### `emacs -fg`

~~~ bash
$ emacs -fg red
~~~

##### Break it down

 * On color displays, sets the color of the text.
   See the file /usr/lib/X11/rgb.txt for a list of valid color names.

