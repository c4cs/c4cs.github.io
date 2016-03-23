---
---

tr
-------

`tr` is used to _translate_ the characters given as input into new characters based on flags and strings given as input.

~~~ bash
$ tr 'is' 'at'
this
that
~~~

<!--more-->

### Useful Options / Examples

#### `tr [:upper:] [:lower:]`
~~~ bash
$ tr [:upper:] [:lower:]
PLEASE TRANSLATE ME.
please translate me.
~~~ 

##### Break it down

 * The `[:upper:]` and `[:lower:]` options are called _sets_. These are very useful when trying to select entire sets of characters, such as digits `[:digit:]`, punctuation `[:punct:]`, or all letters and digits `[:alnum:]`. 
 * Subsets of the sets listed above can also be specified using similar notation. `[a-g]` selects all lower case letters between `a` and `g`, and `[3-7]` selects all numbers between `3` and `7`.
 * Different types of white space and also backslash characters can also be selected. For example, backspace `\b`, return `\r`, and backslash `\\`.

#### `tr -d '\ '`
~~~bash
$ tr -d '\ '
proper spacing is important
properspacingisimportant
~~~

##### Break it down

 * Flags can modify how `tr` treats each set. In this example, `-d` or `--delete` specifies that `tr` is to delete the characters given in the first set. 
 * Other flags include `-c` or `--complement`, which specifies the complement of the first set; `-s` or `--squeeze-repeats`, which replaces each repeated character in the first set with only one occurance of that character; and `-t` or `--truncate-set1`, which truncates the first set to be the size of the second set.

### `pwd | tr '/' '\n'`
~~~bash
$ pwd | tr '/' '\n' > WorkingDirectory.txt
~~~

### Break it down

 * Here, the output of the `pwd` command is piped into a `tr` command that replaces the `/` characters with `\n`, or newline characters. The output is then redirected into a file named WorkingDirectory.txt. 
 * The combination of piping, redirection, and optional flags make `tr` a good tool to use when modifying user input or poorly formatted / irregular text into something more managable.

