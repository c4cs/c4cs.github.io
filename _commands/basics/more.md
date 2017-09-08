---
---

more
--

The `more` command displays the file called name in the screen. The RETURN key displays the next line of the file. The spacebar displays the next screen of the file.

The syntax is:

~~~ bash 
$ more [options] [files]
~~~

<!--more-->

A simple example is:

~~~ bash
$ more text.txt
~~~

It will display the content of **text.txt** file on the screen
It is similar with `cat` command, but using `cat` command is annoyed if the text file is long, all the output scrolls off the top of the screen. 
`more` command fixes that problem by letting the user scroll the output one screenful of data at a time.

### Useful Options / Examples

#### `more -d [files]`
It will display "Press space to continue, 'q' to quit

For example, when we do:

~~~ bash
$ more -d foo.sh
~~~

It will show an intruction message **"Press space to continue, 'q' to quit"** at the bottom of the screen 

#### `more +[number] [files]`

It wil count logical lines rather than screen lines

For example:

~~~ bash
$ more +10 foo.sh
~~~

It will display the file starting at number **10**

#### `more +/[pattern] [files]`

It will display the file, beginning at the first line containing the [pattern]

For example:

~~~ bash
$ more +/'Hello' hello.c
~~~ 

It will display the first line containing **'Hello'** string of the **'hello.c' file

There are other useful options as the table below:

| Options |                           Descitption                          |
|---------|:--------------------------------------------------------------:|
|    **-c**   | Page through the file by clearing the window. (not scrolling). |
|    **-f**   | Count logical lines rather than screen lines (wrapping text)   |
|    **-l**   | Ignores form feed (^L) characters.                             |
|    **-s**   | Displays multiple blank lines as one blank line.               |
|    **-u**   | Does not display underline characters and backspace (^H).      |
|    **-w**   | Waits for a user to press a key before exiting.                |
|         |                                                                |
|         |                                                                |
|         |                                                                |
|         |                                                                |


