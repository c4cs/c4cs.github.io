---
---

du
-------

`du`, or disk usage, displays amount of disk space used by directory or word. 
displayed in kilobytes by default.


~~~ bash
$ du filename1.txt
kilobytes   filename1.txt
~~~

<!--more-->

### Useful Options / Examples

### `du`
Displays space use of all folders in cwd including itself.

~~~ bash
$ du
4       ./basics
12      ./tools
20      .
~~~

### `du -a`
Displays all files in cwd and files in folders of cwd with amount of space used in kilobytes.

~~~ bash
$ du -a
4       ./basics/du.md
4       ./basics
4       ./README.md
0       ./template.md
12      ./tools/git.md
12      ./tools
20      .
~~~

### `du -c`
Includes a count of the total amount of memory at the bottom.

~~~ bash
$ du -c
4       ./basics
12      ./tools
20      .
20      total
~~~

### `du -h`
Displays files in 'human' readable form.

~~~ bash
$ du -h
1K      filename.txt
2.4M    song.mp3
753M    movie.mp4
~~~