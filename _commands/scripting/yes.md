---
---

yes
-------

`yes` outputs an affirmative response, or a user-defined string of text continuously until killed.

~~~ bash
$ yes [STRING]
$ yes option
$ yes | rm -i *.txt
$ yes n | rm -i *.txt
~~~

<!--more-->

### Useful Options / Examples

### `yes`

`yes` command by itself produces continuous output - 'y' by default, until killed.

~~~ bash
$ yes
y
y
y
y
y
y^C
$
~~~

### `yes [STRING]`

You can also provide a custom string for the yes command to use in output. For example:

~~~ bash
$ yes BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes
BeatState?yes^C
$
~~~


### `yes option`

`yes` can be useful for automating some mundane tasks, for example:

~~~ bash
$ rm -ri test
rm: remove directory 'test/test1'? y
rm: remove directory 'test/test1/test1'? y
rm: remove directory 'test/test3'? y
rm: remove directory 'test/test1/test4/test1'? y
~~~
You can see that user has to type 'y' for each query. It's in situation like these where yes can help. For the above scenario specifically, you can use yes in the following way:

~~~ bash
yes | rm -ri test
~~~

