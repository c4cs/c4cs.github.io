---
---

pbpaste
-------

`pbpaste` is used to output the contents of a the previous [pbcopy](https://c4cs.github.io/commands/pbcopy) command.

~~~
$ echo "test" | pbcopy
$ pbpaste
test
~~~


### Usage
~~~ bash
# 1:
$ pbpaste # print the contents of the general (default) clipboard

# 2:
$ pbpaste -pboard general # equivalent to the above command

# 3:
$ pbpaste -pboard ruler > myfile.txt # Redirect the contents of the clipboard ruler to the file myfile.txt

# 4:
$ pbpaste -pboard font | grep copy # Searches the clipboard font for the keyword "copy" via grep

~~~
