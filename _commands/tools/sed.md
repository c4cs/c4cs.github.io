---
---

sed
-------
`sed` is a _stream editor_ utility which supports insertion, deletion, and search and replace of streams then prints the edited stream to standard output.  

~~~ bash
$ sed OPTIONS... [SCRIPT] [INPUTFILE...]
~~~

<!--more-->

### Useful Options / Examples

#### `sed 's/FindWord/ReplaceWord/' filename > outfile`
~~~ bash
$ sed 's/Nick/Josh/' names.txt > out.txt
~~~
Changes first instances of 'Nick' in names.txt to 'Josh' and prints output to out.txt

#### `sed 's/FindWord/ReplaceWord/g' filename > outfile`
~~~ bash
$ sed 's/Nick/Josh/g' names.txt > out.txt
~~~
Changes all instances of 'Nick' in names.txt to 'Josh' and prints output to out.txt

#### `sed 'nd' filename`
~~~ bash
$ sed '5d' filename.txt
~~~
Deletes the 5th line from filename.txt

### Options

| Option | Description |
| --- | --- |
| --help | Display a help message and exit. |
| --version | Output version information and exit. |
| -n --quiet --silent | Disables automatic printing. |
| -e _script_ --expression=_script_ | Add commands in _script_ to set of commands to be run when processing input. |
| -f _script-file_ --file=_script-file_ | Add commands in _script-file_ to set of commands to be run when processing input. |
| -i[_SUFFIX_] --in-place[=_SUFFIX_] | Specifies editing files in place. |
| -l _N_ --line-length=_N_ | Specifies line-wrap length (default = 70). |
| -posix | |
| -b --binary | Opens files in binary mode. |
| --follow-symlinks | Specifies that file passed in is a symbolic link. |
| -E -r --regexp-extended | Use extended regular expressions. |
| -s --separate | Consider files as separate streams. |
| --sandbox | Specifies that `sed` does not run any external programs. |
| -u --unbuffered | Buffer both input and output as minimally as practical. |
| -z --null-data --zero-terminated | Treat each line as null-terminated instead of newline-terminated. |
