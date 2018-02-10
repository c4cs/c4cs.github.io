---
---

wget
-------
`wget` Allows you to pull files and directories straight from a web server.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ wget http://web.mst.edu/~price/cs53/code_example.html
~~~

<!--more-->

### Useful Options / Examples

#### wget --progress=type

`wget` Can be used with many different flags. One helpful flag is the `--progress` flag, which will change how download progress is shown. Accetable arguments are `dot` and `bar`.

~~~ bash
$ wget --progress=dot http://web.mst.edu/~price/cs53/code_example.html
$ wget --progress=bar http://web.mst.edu/~price/cs53/code_example.html
~~~

NOTE: `bar` is used by default when none are specified.

#### wget -c

`wget` Can also be included with the `-c` flag. This will continue a partially completed download that `wget` was used for in the past.

~~~ bash
$ wget -c http://web.mst.edu/~price/cs53/code_example.html
~~~
