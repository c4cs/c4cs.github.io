---
---

pbcopy
-------

`pbcopy` is used to copy text from the terminal into the clipboard.

~~~ bash
#Copies the contents of a file into the clipboard
$ pbcopy < example.txt
~~~

<!--more-->

### Useful Options / Examples

#### `<command> | pbcopy`
~~~ bash
#Directs the output of commands into the clipboard

#Another way to copy the contents of a file into the clipboard
$ cat example.txt | pbcopy

#Copies 'Hello World!' into your clipboard buffer
$ echo 'Hello World!' | pbcopy

#Pipes the grep results into the clipboard
$ grep hello helloworld.txt | pbcopy

#Pipes the 'ps aux' results into the clipboard
$ ps aux | pbcopy
~~~

##### Break it down

* The output of the commands run is being redirected into the clipboard
with the combination of the pipe ( | ) and pbcopy

#### `pbcopy -pboard {general | ruler | find | font}`

~~~ bash
#Copies the contents of example.txt into the clipboard
$ pbcopy -pboard general < example.txt

#Pipes the contents of the echo command into the search clipboard
#Running cmd+f after this command will pre-populate the search bar with 'hello'
$ echo 'hello' | pbcopy -pboard find
~~~

##### Break it down
~~~
* pboard specifies which pasteboard to copy from (the default being general)
~~~

