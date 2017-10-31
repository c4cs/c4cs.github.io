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

<!--more-->

### Useful Options / Examples

Typing `/` within `less` allows you to forward search using regex
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


# Options:

~~~
| Options |                         Description                        |
|---------|:----------------------------------------------------------:|
| -?      |                       Displays help.                       |
| -I      |               Makes search case insensitive.               |
| -M      |                    More detailed prompt.                   |
| -S      | Long lines are chopped, and can be seen by side scrolling. |
| -X      |      Contents of file remain on screen after exiting.      |
~~~

# Commands:

~~~
| Command     |                              Description                             |
|-------------|:--------------------------------------------------------------------:|
| Space bar   |                               Next Page                              |
| b           |                             Previous Page                            |
| v           |                             Edit Content                             |
| j           |                         or ↵ Enter  Next Line                        |
| k           |                             Previous Line                            |
| F           |              Follow Mode (for logs). Interrupt to abort.             |
| g or <      |                              First Line                              |
| G or >      |                               Last Line                              |
| <n>G        |                               Line <n>                               |
| /<text>     |      Forward Search for <text>. Text is interpreted as a regex.      |
| ?<text>     |                        Backward Search like /                        |
| n           |                           Next Search Match                          |
| N           |                         Previous Search Match                        |
| Esc u       |       Turn off Match Highlighting (see -g command line option)       |
| -<c>        | Toggle option <c>, e.g., -i toggles option to match case in searches |
| m<c>        |                             Set Mark <c>                             |
| '<c>        |                            Go to Mark <c>                            |
| = or Ctrl+G |                           File information                           |
| :n          |                               Next file                              |
| :p          |                             Previous file                            |
| h           |             Help. This is presented with less, q to quit.            |
| q           |                                 Quit                                 |
~~~

[Reference](https://en.wikipedia.org/wiki/Less_(Unix))
