---
---

yes
---

`yes` will continuosly output lines with `y`. Can be useful for automating
scripts.

~~~ bash
$ yes
y
y
~~~

### Useful Options / Examples

#### `yes | rm *.txt`

~~~ bash
$ yes | rm *.txt
~~~

##### Break it down

* The yes command will continuously pipe yes to the following command to automaticly make the following command  prove any raised question with form `[y/n]`

#### `yes [text] | head -1000 > [filename]`

~~~ bash
$ yes abcdefg | head -1000 > text.txt
~~~

##### Break it down

* The yes command is convenient to generate repeated text. This command will end up filling text.txt with 1000 lines of abcdefg
