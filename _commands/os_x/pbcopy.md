---
---

pbcopy
-------

`pbcopy` is used to copy text from the terminal into the clipboard.
The linux equivalent of `pbcopy` is `xclip`.

~~~ bash
# Copies the contents of a file into the clipboard
$ pbcopy < example.txt
~~~

<!--more-->

### Useful Options / Examples

#### `<command> | pbcopy`
~~~ bash
# 1:
$ cat example.txt | pbcopy

# 2:
$ echo 'Hello World!' | pbcopy

# 3:
$ grep hello helloworld.txt | pbcopy

# 4:
$ ps aux | pbcopy
~~~

##### Break it down

* All of the above examples direct the output of various commands into the clipboard
with the combination of the pipe ( `|` ) and pbcopy
* 1: Demonstrates another way to copy the contents of the file, example.txt, into the clipboard
* 2: Copies 'Hello World!' into your clipboard buffer
* 3: Pipes the grep results into the clipboard
* 4: Pipes the `ps aux` results into the clipboard


#### `pbcopy -pboard {general | ruler | find | font}`

~~~ bash
# 1:
$ pbcopy -pboard general < example.txt

# 2:
$ pbcopy -pboard ruler < ruler.txt

# 3:
$ echo 'hello' | pbcopy -pboard find

# 4:
$ pbcopy -pboard font < text.txt
~~~

##### Break it down

* The `-pboard` flag is used to specity which pasteboard to copy to (the default being general)
* 1: The `general` option signals to the `-pboard` flag to copy to the standard clipboard.  In this case, the contents of example.txt are copied into the standard clipboard. Pressing cmd+v after this command will paste your copied text from example.txt.
* 2: The `ruler` option signals to the `-pboard` flag to copy to the ruler clipboard.  In this command, the contents of ruler.txt are piped into the ruler clipboard.
* 3: The `find` option signals to the `-pboard` flag to copy into find clipboard. Running cmd+f after this command will pre-populate the search bar with 'hello'.
* 4: The `font` option signals to the `-pboard` flag to copy to the font clipboard. This command specifically, pipes the contents of test.txt into the font clipboard.  The font clipboard allows you to copy the font from a selection (in this case, test.txt),
 and paste it onto some other text.

