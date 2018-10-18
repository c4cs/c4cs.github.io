---
---

gedit
---
`gedit` is a general purpose text editor with an emphasis on simplicity and usability.

~~~ bash
$ gedit [OPTION...] [FILE...] [+LINE[:COLUMN]]
~~~

This will open file specified by the `FILE` if one is specified with the specified `OPTION`s if any are specified at the spefied line and column numbers (which will default to 0 if left out).

<!--more-->

### Useful Options / Examples

### `gedit`

Opens a blank, untitled file in gedit.

~~~ bash
$ gedit
~~~

### `gedit <filename>`

Opens the file named `filename` in gedit. If no file named `filename` exists, gedit will create one. If multiple files are listed, then all of them will be opened in gedit.

~~~ bash
$ gedit test.txt
~~~

### `gedit <filename> +line:col`

Opens the file named `filename` if it exists. The cursor will start on line `line`, column `col`. If there are less than `col` columns, it will go to the end of the line. If there are less than `line` lines, it will go to the last line in `filename`.

~~~ bash
$ gedit test.txt +10:5
~~~

### `gedit <filename> -w`

Opens `filename` and blocks the gedit process until files are closed.

~~~ bash
$ gedit test.txt -w
^c
$ # ^c would normally kill gedit but with the -w flag, it will remain running.
~~~

### `gedit --help`

Displays the help message for `gedit`.

~~~ bash
$ gedit --help 
Usage:
  gedit [OPTION…] [FILE…] [+LINE[:COLUMN]]

Help Options:
  -h, --help                      Show help options
  --help-all                      Show all help options
  --help-gapplication             Show GApplication options
  --help-gtk                      Show GTK+ Options

Application Options:
  -V, --version                   Show the application’s version
  --list-encodings                Display the list of possible values for the encoding option
  --encoding=ENCODING             Set the character encoding to be used to open the files listed on the command line
  --new-window                    Create a new top-level window in an existing instance of gedit
  --new-document                  Create a new document in an existing instance of gedit
  -w, --wait                      Open files and block process until files are closed
  -s, --standalone                Run gedit in standalone mode
  --display=DISPLAY               X display to use
~~~

