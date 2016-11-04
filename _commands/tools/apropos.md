---
---

apropos
---

`apropos` allows you to quickly figure which commands lead to the actions you want to perform

~~~ bash
$ apropos "list directory"
dir (1) - list directory contents
ls (1) - list directory contents
ntfsls (8) - list directory contents on an NTFS filesystem
vdir (1) - list directory contents
~~~

<!--more-->

### Useful Options / Examples

#### Simple Example

~~~ bash
$ apropos "copy" "directory"
Clone (3pm)          - recursively copy Perl datatypes
alphasort (3)        - scan a directory for matching entries
basename (1)         - strip directory and suffix from filenames
bcopy (3)            - copy byte sequence
bindtextdomain (3)   - set directory containing message catalogs
....
~~~

##### Break it down
`apropos` searches for all commands that contain at least one of the specified keywords in their man page files.

#### Options

`-r, --regex`

~~~ bash
$ apropos -r "[a-z]directory"
mmd (1)              - make an MSDOS subdirectory
mmove (1)            - move or rename an MSDOS file or subdirectory
mrd (1)              - remove an MSDOS subdirectory
~~~

##### Break it down
The `-r, --regex` option allows regex syntax to be used in keywords.

`-w, --wildcard`

~~~ bash
$ apropos -w "*directory"
alphasort (3)        - scan a directory for matching entries
basename (1)         - strip directory and suffix from filenames
bindtextdomain (3)   - set directory containing message catalogs
cups-files.conf (5)  - file and directory configuration file for cups
....
~~~

##### Break it down
The `-w, --wildcard` option allows wildcard characters to be used in keywords.

`-a, --and`

~~~ bash
$ apropos -a "list" "directory"
chacl (1)            - change the access control list of a file or directory
dir (1)              - list directory contents
File::Listing (3pm)  - parse directory listing
ls (1)               - list directory contents
ntfsls (8)           - list directory contents on an NTFS filesystem
vdir (1)             - list directory contents
~~~

##### Break it down
The `-a, --and` option requires commands to contain all the keywords.

`-e, --exact`

~~~ bash
$ apropos -ae "list" "directory"
chacl (1)            - change the access control list of a file or directory
dir (1)              - list directory contents
ls (1)               - list directory contents
ntfsls (8)           - list directory contents on an NTFS filesystem
vdir (1)             - list directory contents
~~~

##### Break it down
The `-e, --exact` option requires commands to match the keywords exactly.