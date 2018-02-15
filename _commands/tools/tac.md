---
---

tac
---
`tac` is used to concatenate files in reverse, line by line.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ tac numberedlines.txt
Line number five
Line number four
Line number three
Line number two
Line number one
~~~

<!--more-->

### Useful Options / Examples

#### `-s`, `--separator`

~~~ bash
$ cat numberedlines.txt

START1
Line number one
Line number two
END2

START3
Line number three
Line number four
END4

START5
Line number five
Line number six
END6

START7
Line number seven
Line number eight
END8

START8
Line number nine
Line number ten
END9

$ tac -s "START" numberedlines.txt
8
Line number nine
Line number ten
END9

7
Line number seven
Line number eight
END8

START5
Line number five
Line number six
END6

START3
Line number three
Line number four
END4

START1
Line number one
Line number two
END2

START
START$
~~~

##### Break it down

The `-s`, `--separator` flag uses the string to demarcate a "line". So it detects the last instance and prints everything following it until the end of the line. Then it detects the second to last instance and prints lines after it until the next instance of the string including the line separating string, and so on. Output has weird behavior at the edges of the file, use `-b`, `--before`.

#### `-b`, `--before`

Using same file as before

~~~ bash
$ tac -b -s "START" numberedlines.txt 
START8
Line number nine
Line number ten
END9

START7
Line number seven
Line number eight
END8

START5
Line number five
Line number six
END6

START3
Line number three
Line number four
END4

START1
Line number one
Line number two
END2
~~~

##### Break it down

The `-b`, `--before` flag attaches the line separating string before each line of output instead of after.
