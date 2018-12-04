---
---

vim
---
`vim` is a configerable text editor built to enable efficient text editing

~~~ bash
$ vim main.py
~~~

<!--more-->

### Useful Options / Examples

### `Exiting`

:qa       |      Close all files
:qa!       |     Close all files, abandon changes
:w         |     Save
:wq or :x     |        Save and close files
:q            |   Close file
:q!            |  Close file, abandon changes
ZZ         |     Save and quit
ZQ        |      Quit without checking changes
...................|...................

~~~ bash
$ vim main.py
if __name__ == '__main__':
print_welcome()
<<<<<<< HEAD
print('')
print('According to current estimates, the diag construction will be done:')
print('Never.')

:wq
~~~


### `Editing`

a        |      Append
i         |      Insert
o        |      Next line
0        |      Previous line
s        |      Delete char and insert
S       |       Deleete line and insert
C       |       Delete until end of line and insert
r        |       Replace one character
R       |       Enter Replace mode
..........|.............

we want to edit out "<<<<<<< HEAD" and save and close the file
~~~ bash
$ vim main.py
if __name__ == '__main__':
print_welcome()
<<<<<<< HEAD
print('')
print('According to current estimates, the diag construction will be done:')
print('Never.')

[a]

if __name__ == '__main__':
print_welcome()
print('')
print('According to current estimates, the diag construction will be done:')
print('Never.')

[esc]
:wq
~~~

### `Navigating`

h j k l                 |            Arrow keys
<C - U> / <C - D>   |      Page up/ page down
......................................|.................

Words               |
b / w                |              Previous/ next word
e / ge               |              Previous/next end of word
......................|.................

Line                |
0                      |              Start of Line
^                      |             Start of line (after whitespace)
$                      |              End of line
......................|.................

Character       |
fc                   |                Go forward to character c
Fc                  |                Go backward to character c
......................|.................

Document      |
gg                  |                First line
G                   |                 Last line
:n                   |                Go to line n
nG                 |                 Go to line n
......................|.................

Window          |
zz                  |                Center this line
H                   |                Move to top of screen
M                  |                 Move to middle of screen
L                   |                 Move to bottom of screen
......................|.................

~~~ bash
$ vim main.py
if __name__ == '__main__':
print_welcome()
<<<<<<< HEAD
print('')
print('According to current estimates, the diag construction will be done:')
print('Never.')

:2

if __name__ == '__main__':
print_welcome()                 <--- curser on this line now
<<<<<<< HEAD
print('')
print('According to current estimates, the diag construction will be done:')
print('Never.')

~~~

### `Clipboard`

x               |            Delete character
dd            |             Delete line (Cut)
yy            |             Yank line (Copy)
p             |              Paste
P              |             Paste before
.................|.................

### `Exiting Insert Mode`

Esc / <C - [>    |   Exit insert mode
<C - C>          |    Exit insert mode, and abort current command
..............................|.................

### `Visual Mode`

v              |          Enter visual mode
V             |           Enter visual line mode
<C - V>   |          Enter visual block mode
..............................|.................

In Visual Mode          |
d / x         |          Delete selection
s              |          Replace selection
y              |          yank selection (Copy)
.................|.................

### `Operators List`

d             |          Delete
y             |          Yank (copy)
c             |          Change (delete then insert)
'>            |          Indent right
'<            |          Indent left
g~           |          Swap case
gU          |           Uppercase
gu          |            Lowercase
!             |            Filter through external program
.................|.................

### `Text Objects`

p           |            Paragraph
w          |             Word
s           |             Sentence
[ ( { <      |           A [], (), or {} block
' " `         |           A quoted string
b            |           A block [(
B           |            A block in [{
t            |            A XML tag block
.......................|.................

### `Folds`

zo / zO      |       Open
zc / zC      |        Close
za / zA      |        Toggle
zv             |        Open folds for this line
zM           |         Close all
zR           |          Open all
zm          |          Fold more (foldlevel += 1)
zr            |          Fold less (foldlevel -= 1)
zx           |          update folds
.......................|.................

### `Navigation`

[(  [{  [<      |       Previous ( or { or <
] )             |        Next
[m            |        Previous method start
[M           |         Previous method end
.......................|.................

### `Jumping`

<C - O>    |      Go back to previous location
<C - I>      |      Go forward
gf             |       go to file in cursor
.......................|.................

### `Counters`

<C - A>     |       Increment number
<C - X>      |      Decrement
.......................|.................

### `Windows`

/{height}<Cr>     |      resize pane to {height} lines tall
.......................|.................

### `Tags`

: tag Classname     |    Jump to first definition of Classname
<C - ]>              |          Jump to definition
g]                      |          See all definitions
<C - T>              |         Go back to last tag
<C - O> <C - I>    |      Back / forward
:tselect Classname  |   Find definitions of Classname
:tjump Classname   |   Find definitions of Classname (auto-select 1st))
.................................|...........................

### `Case`

~          |      Toggle case (Case => cASE)
gU       |      Uppercase
gu       |       Lowercase
gUU     |      Upercase current line (also gUgU)
guu       |     Lowercase current line (also gugu))
.......................|.................
