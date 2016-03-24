---
---

file
--

`file` is used to find out the _type_ of a file

~~~ bash
$ file file.md
file.md: ASCII text
~~~

<!--more-->

### How `file` Works

#### Magic Headers
The `file` command works by interpreting the "magic" header of a file, if it exists (many files, including basic text files do not have this type of header). The first few bytes of a file make up the header, which the file command can interpret. 

A good example is `#!`. These bytes are used at the beginning of bash and other script files. They allow the operating system to correctly run the script and also allow the `file` command to tell the user that it is a script file. 

Magic headers are a bit confusing, but the main idea is that they are a series of bytes at the beginning of a file that can be interpreted by various different operations including the operating system and the `file` command. To find out more about magic headings, check out `man 5 magic`. 

#### Files Without Magic Headers 
If a file does not have a magic header, the `file` command scans the document and makes an educated guess based on a few factors, one of which is the range of bytes in the document. For instance, it can guess that a file is just ASCII text if it doesn't inlcude any bytes in the range 0x00-0x20. 

Because of the way that the `file` command works, it can make mistakes. For example, the `file` command is not always accurate with movie files, primarily because of the large variety of different types of files and versions of video file types. But, for many files it can help identify the type either by interpreting its magic header or making an educated guess. 


### Useful Options/Examples

### `file -F separator`

~~~ bash
$ file -F :: file.md
file.md:: ASCII text
~~~

~~~ bash
$ file -F " :: " file.md
file.md ::  ASCII text
~~~

#### Break it down

* `-F` flag is the short version of `--separator`
* `-F` flag allows you to provide a custom delimter between the file name and type in output. This is especially useful when trying to format output specifically when piping into an output file. 
* `separator` is the command argument - it will be used as the delimiter. The default is ":"
* You can use quotes around the string if you want spaces included in the output - this is seen in the second example above

### `file -i`

~~~ bash
$ file -i file.md
file.md: text/plain; charset=us-ascii
~~~

#### Break it down

* `-i` flag is the short version of `--mime`
* `-i` flag changes the way that the command interprets file types, giving more information about the file
* This option is very useful when you're unsure about what the type that is output actually is
