---
---

file
--

`file` is used to find out the _type_ of a file

~~~ bash
$ file file.md
file.md: ASCII text
~~~

<!--more-->

### Useful Options/Examples

### `file -F _separator_`
### `file --separator _separator_`

~~~ bash
$ file -F :: file.md
file.md:: ASCII text
~~~

~~~ bash
$ file -F " :: " file.md
file.md ::  ASCII text
~~~

#### Break it down

* `-F` flag allows you to provide a custom delimter between the file name and type in output. This is especially useful when trying to format output specifically when piping into an output file. 
* `_separator_` is the command argument - it will be used as the delimiter. The default is ":"
* You can use quotes around the string if you want spaces included in the output - this is seen in the second example above

### `file -i`
### `file --mime`

~~~ bash
$ file -i file.md
file.md: text/plain; charset=us-ascii
~~~

#### Break it down

* `-i` flag changes the way that the command interprets file types, giving more information about the file
* This option is very useful when you're unsure about what the type that is output actually is
