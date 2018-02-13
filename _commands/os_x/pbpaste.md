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
#### `pbpaste -pboard {general | ruler | find | font}`
~~~ bash
# 1:
$ pbpaste # print the contents of the general (default) clipboard

# 2:
$ pbpaste -pboard general # equivalent to the above command

# 3:
$ pbpaste -pboard ruler > myfile.txt # Redirect the contents of the clipboard ruler to the file myfile.txt

# 4:
$ pbpaste -pboard font | grep copy # Searches the clipboard font for the keyword "copy" via grep

# 5:
$ pbpaste -pboard find > pbcopy

~~~

##### Break it down
* All of the commands above are followed by a previous pbcopy command.
* 1: Demonstrates how default pbpaste behavior.
* 2: Demonstrates another from of pasting the general form.
* 3: Demonstrates how to paste from the `ruler` clipboard into `myfile.txt` via input redirection
* 4: Demonstrates how to search the output of the `font` clipboard for the keyword `copy` via grep.
* 5: Redirects the find clipboard into the general clipboard

### Advanced Flags
#### `pbpaste -Prefer {txt | rtf | ps}`
Tells  pbpaste  what  type of data to look for in the pasteboard first. Default behavior is `-Prefer txt`. Using `-Prefer ps` tells pbpaste to look first for Encapsulated  PostScript. Finally, `-Prefer rtf` looks first for Rich Text format.
