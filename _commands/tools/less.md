---
---

less
-------

`less` is used to display contents of a file, as well as allow navigation. Its name is derived from being the _opposite of_ `more`.

~~~ bash
$ less file.txt

These are the contents of "file.txt".

The output will actually take up the entire screen, and you can navigate using Vim-like commands.
~~~

<!--more-->

### Useful Options / Examples

##### Navigation/ General Commands
`less` can be navigated using Vim-like commands.

* `j`/ `k`: move to the next/ previous line of the file
* `spacebar`/ `b`: move to the next/ previous page of the file
* `h`: displays a help screen with a summary of `less` commands
* `q`: quits `less`

For more commands, use `man less` or visit [this](http://www.tutorialspoint.com/unix_commands/less.htm) tutorial page.

##### Search
`/def`, `?def` ("**" represents highlighted text)

~~~
**def** foo():
        print "foo"

**def** bar():
        print "bar"

**def** main():
        foo()
        bar()

~~~

When inside `less`, you can type `/<regex>` to search _forward_ for a regular expression. You can use `n` to find the next occurrence, or `N` to find the previous occurrence. `?<regex>` is the same, but searches _backwards_ and inverts `n` and `N`.

##### Marks
`m <lowercase letter>`, `' <lowercase letter>`

The `m` command inside `less` allows you to "mark" the current line at the top of your screen with that letter. Later, you can use the `'` command with that same letter to jump back to that position.

##### Line Numbers

`less -N huge_file.txt`, `less --LINE-NUMBERS huge_file.txt`

~~~
      1 These are the contents of "huge_file.txt".
      2
      3 You can't really tell from here, but this file goes on and on and on and      3  on...
      4
      5 You can navigate this huge file using Vim-like commands!
      6
      7 If it's hard to keep track of where you are in the file though...
      8
      9 Use -N or --LINE-NUMBERS to help you out!
~~~
The `-N` and `--LINE-NUMBERS` flags turn on line numbers on the side. You can also use `-n` or `--line-numbers` to suppress line numbers.

##### Follow Mode
`less +F log.txt`

`echo "hello world!" >> log.txt`

~~~
...
Line 41
Line 42
Line 43
Line 44
Line 45
Line 46
Line 47
Line 48
Line 49
Waiting for data... (interrupt to abort)
~~~
The `+F` flag sets `less` to work in "follow mode", which tracks additions to a file. For example, when you use the `>>` operator to append to a file, `less` will automatically track it and display what you appended. This is especially useful for error logs on a server, for example. You can press `Ctrl-c` at any time to stop following and navigate normally, and then `F` to continue following the file.

