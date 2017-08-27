---
---
locate
-------

`locate` finds the locations of directories and files on Linux as well as other Unix-like OS.

~~~ bash
$ locate hello.cpp
~~~

<!--more-->

### Useful Options / Examples

#### `locate filename`

This would list the absolute paths for all files with "filename" in the name.

~~~ bash
$ locate hello.cpp
/home/user/Desktop/Folder/hello.cpp
~~~

Note: The `locate` command does not work for macOS unless you create a locate database. You can create one by running the following command:

~~~ bash
$ sudo launchtl load -w /System/Library/LaunchDaemons/com.apple.locate.plist
~~~

Another alternative is to use the `find` command using the following syntax:

~~~ bash
$ find . -name "hello.cpp"
/home/user/Desktop/Folder/hello.cpp
~~~
