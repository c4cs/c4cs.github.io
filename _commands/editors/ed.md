---
---

ed
-------

`ed` is a standard, minimal and not a terribly intuitive text editor for Unix systems. 

To open `ed` simply type the following:

~~~ bash
$ed
~~~

<!--more-->
This will open an empty file in ed. 
Since ed is generally silent with feedback start by typing 'H' and pressing enter. This way `ed` will print error messages when you do something wrong.

Note: Most commands in the following list can be run with a line number before the command to perform that action on that line.

### Here are things you can do in the editor 
- `q` - exit if the buffer is empty
- `Q` - exit unconditionally 
- `w`filename - write/save (overrides file if it exists) 
- `W`filename - write/save (appends to the end of the file) 
- `a` - start writing into the buffer, when you are done put a period `.` by itself
- `p` - print line
- `n` - print line and line number
- `c` - replace line
- `d` - delete line
- `6d` - delete 6th line

### A short example 
~~~ bash
$ed
H
a
Hello
World
.
n
2     World
1n
1     Hello
1d
n
1     World
w world.txt
6
q
~~~

End result is a text file named world.txt in the current directory. 
