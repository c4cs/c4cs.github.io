---
---

mpage
---

`mpage` is used to print pages to a postcript printer. It is useful at condensing output, and can condense up to 8 pages onto a single piece of paper.

~~~ bash
$ mpage [options] <files...>
~~~

<!--more-->

###Useful Options / Examples

#### `mpage -8 test.txt`
~~~ bash
$ls
test.txt
$mpage -8 test.txt
~~~

##### Break it down
 * The '-8' option sets the condensing from every 8 pages of normal text, to one page printed out. 
 * Other similar flags are '-4' (which is the default behaviour) which prints four pages to a piece of paper, '-2' which prints two pages to a piece of paper, and '-1' which prints one page per piece of paper, this allows for symmetry.

#### `mpage -O test.txt`
~~~ bash
$ls
test.txt
$mpage -O test.txt
~~~

##### Break it down
 * The '-O' flag prints 2 normal pages to one piece of paper. However it only prints every first and fourth page, leaving out the second and third.
 * Similarly, the '-E' option prints every second and third page per four pages to a single sheet of paper.
 * This is useful if you need to get a sample of a large text file, but don't need the entire thing.

#### `mpage -F<fontname> text.txt`
~~~ bash
$ ls
text.txt
$ mpage -F DejaVuSerif-Bold
~~~

##### Break it down
 * The '-F' flag sets the font type to be printed in. Courier is the default font.

#### `mpage -t text.txt`
~~~ bash
$mpage -t test.txt
~~~

##### Break it down
 * The '-t' flag toggles duplex printing, or double sided printing. The default is off.
 * This can further save paper by printing both more normal pages per piece of paper, and also by printing on both sides of the sheet.


