---
---

diff
--

`diff` is used to check for the differences between two files line by line. This is very useful for checking a programs output against a file containing its expected output.

~~~ bash
$ printf "this\ndifference\n" > first.txt
$ printf "this\nsimilarity\n" > second.txt
$ diff first.txt second.txt
2c2
< difference
---
> similarity
~~~

<!--more-->

### Useful Options / Examples

When the files completely match, there is no output from `diff`.

~~~ bash
$ printf "same" > first.txt
$ printf "same" > second.txt
$ diff first.txt second.txt
$
~~~


#### `diff -y`

Fully outputs both files in 2 columns with a '\|' marking lines with differences, similar to the standard output of `sdiff`.

~~~ bash
$ printf "working with github\nlets you share your work\ncollaboration" > haiku1.txt
$ printf "working with github\nlets you backup your data\nrefrigerator" > haiku2.txt
$ diff -y haiku1.txt haiku2.txt
working with github			working with github
lets you share your work	      | lets you backup your data
collaboration			      | refrigerator
~~~

