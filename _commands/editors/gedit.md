---
---

gedit
--

`gedit` is used to edit files in gedit.

~~~ bash
$ gedit filename
~~~

Then file specified by `filename` will be opened in gedit, and you can use gedit to edit it.

<!--more-->

### Useful Options / Examples

#### `gedit --list-encodings`

~~~ bash
$ gedit --list-encodings
~~~

Display list of possible values for the encoding instance of gedit.

#### `gedit --new-document`

~~~ bash
$ gedit --new-document
~~~

Create a new document in an existing instance of gedit.

#### `gedit --new-window`

~~~ bash
$ gedit --new-window
~~~

Create a new toplevel window in an existing instance of gedit.

#### `gedit -s`

~~~ bash
$ gedit -s
~~~

Run gedit in standalone mode.

#### `gedit -w`

~~~ bash
$ gedit -w
~~~

Open files and block the gedit process.
