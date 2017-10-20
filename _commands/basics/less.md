---
---

less
--
`less` is a tool to view a text file one screen at a time. You can navigate through the file with `j` or `RETURN`, and backwards with `k`

<!-- minimal example -->
~~~ bash
$ less hello.txt
# displays hello.txt
q # to quit
~~~

<!--less-->

### Useful Options / Examples

typing `/` within `less` allows you to forward search using regex
and `?` allows you to backward search
pressing `n` goes to the next item
~~~ bash
$ less hello.txt
........
........
........
..git...
.....git

:/git
# git will be highlighted
n
# the next git is highlighted
~~~ 

| Options |                           Description                          |
|---------|:--------------------------------------------------------------:|
|    **-?**   | Displays help.                                             |
|    **-I**   | Makes search case insensitive.                             |
|    **-M**   | More detailed prompt.                                      |
|    **-S**   | Long lines are chopped, and can be seen by side scrolling. |
|    **-X**   | Contents of file remain on screen after exiting.           |
