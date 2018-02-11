---
---

apropos
---
`apropos` searches the man database for entry that contains the string passed in as argument. 
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ apropos whoami
whoami (1)           - print effective userid
~~~

<!--more-->

### Useful Options / Examples

#### `apropos STRING_ARGUMENT`

Outputs a list of entrys in the what is data base that contain the the string argument

~~~ bash
$ apropos whoami
whoami (1)           - print effective userid
~~~

* The string argument is not case sensitive.

~~~ bash
$ apropos wHOaMi
whoami (1)           - print effective userid
~~~

* Press 'q' to quit the apropos display.

#### `apropos STRING_ARGUMENT | less`

For string aruments that return a large list of entries such as "cat" it may be helpful to pipe in the less command which allows you to browse through the results page by page.

~~~ bash
$ apropos cat | less
~~~
