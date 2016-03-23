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
