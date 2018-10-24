---
---

man
---
`man` displays user manual pages that is by default built into Linux. Displays information about specified commands

~~~ bash
$ man git
$ man grep
$ man ls
~~~

<!--more-->

### Useful Options / Examples

### `man man`

Displays information about how to use the `man` command as well as the options that can be used with it

~~~ bash
$ man man
man(1)                                                                  
NAME
man - format and display the on-line manual pages
SYNOPSIS
man  [-acdfFhkKtwW]  [--path]  [-m system] [-p string] [-C config_file]
[-M pathlist] [-P pager] [-B browser] [-H htmlpager] [-S  section_list]
[section] name ...
~~~


### `man -k [keyword]`

 `man -k [keyword]` searches all descriptions in manual pages for keyword and display any matches found.

~~~ bash
$ man -k grep
git-grep(1)              - Print lines matching a pattern
pcre2grep(1)             - a grep with Perl-compatible regular expressions
pcregrep(1)              - a grep with Perl-compatible regular expressions
xzgrep(1)                - search compressed files for a regular expression
Tcl_NewObj(3tcl), Tcl_DuplicateObj(3tcl), Tcl_IncrRefCount(3tcl), Tcl_DecrRefCount(3tcl), Tcl_IsShared(3tcl), Tcl_InvalidateStringRep(3tcl) - manipulate Tcl objects
grep(1), egrep(1), fgrep(1), zgrep(1), zegrep(1), zfgrep(1) - file pattern searcher
pgrep(1), pkill(1)       - find or signal processes by name
ptargrep(1)              - Apply pattern matching to the contents of files in a tar archive
zipgrep(1)               - search files in a ZIP archive for lines matching a pattern
~~~

### `man -f [keyword]`

`man -f [keyword]` is equivalent to the `whatis` command and if commands contain the keyword, it displays them as well as their short manual page descriptions.

~~~ bash
$ man -f grep
git-grep(1)              - Print lines matching a pattern
pcre2grep(1)             - a grep with Perl-compatible regular expressions
pcregrep(1)              - a grep with Perl-compatible regular expressions
grep(1), egrep(1), fgrep(1), zgrep(1), zegrep(1), zfgrep(1) - file pattern searcher
~~~

