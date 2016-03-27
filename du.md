---
---

du
--

The du (disk usage) command shows you the sizes of directory trees including all of their contents and sizes of individual files.
This makes it usefull for taking down particular directories that are hogging disk space. 

~~~ bash
$ mkdir test
$ yes > test/bigfile.txt
$ du -h
51M    ./test
51M    .
~~~

<!--more-->

### Useful Options / Examples

#### `du -h`
~~~ bash
$ du -h
92K	.
~~~

##### Break it down

* The -h option asks for 'human readable' output. This can be very usefull for people who are not as experienced programmers. The       effect is that it more clearly states what these numbers such as '92' mean in the output (KB).

#### `du -a`

~~~ bash
$ du -a
4	./sudo.md
4	./cd.md
4	./sort.md
4	./which.md
4	./echo.md
4	./ls.md
4	./whoami.md
8	./man.md
4	./pwd.md
4	./true.md
4	./cp.md
4	./kill.md
4	./head.md
4	./chown_chgrp.md
4	./cat.md
4	./mkdir.md
4	./chmod.md
4	./mv.md
4	./tar.md
4	./id.md
4	./wc.md
92	.
~~~

##### Break it down

* The -a option asks for not just all of the disk usage for each directory at every level in the directory tree, but also to show
  the space consumption for each individual file anywhere within the tree.
