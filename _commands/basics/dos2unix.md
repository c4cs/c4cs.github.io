---
---

dos2unix
-------

'dos2unix' In DOS/Windows text files, a newline is a combination of a Carriage Return (CR) and a Line Feed (LF). In Unix text files, a newline is just a LF. 'dos2unix' converts
the DOS file into a Unix file. This could be useful for when someone makes a test file in windows, move it over to a Unix environment, but then needs the file to be in Unix
format.

~~~ bash
$ dos2unix test.txt
~~~

<!--more-->

### Useful Options / Examples

#### 'dos2unix -k a.txt b.txt ...'

Convert and replace a.txt while keeping original date stamp. Convert and replace b.txt while keeping original date stamp. Etc.

~~~ bash
$ dos2unix -k test1.txt test2.txt
~~~
This command is converting and replacing test1.txt and test2.txt while keeping both original date stamps.

#### 'dos2unix -n a.txt b.txt'

Converts and writes a.txt to b.txt

~~~ bash
$ dos2unix -n test1.txt outTest.txt
~~~
This command converts test1.txt to Unix and then writes it to outTest.txt

#### 'dos2unix a.txt -n b.txt c.txt'

Converts and replaces a.txt. Converts b.txt and writes to c.txt.

~~~ bash
$ dos2unix test1.txt -n test2.txt outTest.txt
~~~
This command converts/replaces test1.txt to Unix. Then converts test2.txt and writes it into outTest.txt.


