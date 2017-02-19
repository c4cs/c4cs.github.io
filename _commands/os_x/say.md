---
---

Say
-------

The `say` command will speak whatever you type

~~~ bash
say "hello c4cs"
~~~

<!--more-->

### Useful Options / Examples

`-v` can change the voice and language

`-v` `?` will show all the voices and language they speak

`-f` can load a text file

`-i` can highlight where the computer is in the speech

`--interactive=<markup>` will change the preference of the highlighter

`-o` make an audiofile with what is said

#### Example commands

~~~ bash
say -v 'Tessa' "hello c4cs"

say -v ?

say -f sample.txt

say -i "Hello there, I have become self aware"

say --interactive=blue -v 'Alex' "What a nice day"

say -o words "Creating a file called words.aiff"
~~~


