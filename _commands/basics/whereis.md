---
---

whereis
--

`whereis` is used to locate source/binary and manuals sections for specified files. The supplied names are first stripped of leading pathname components and any (single) trailing extension of the form `.ext`.

~~~ bash
$ whereis [options] filename
~~~

<!--more-->

### Useful Options

#### The search restrictions (-b, -m, -s) are cumulative and apply to the subsequent filename patterns on the command line. Any new search restrictions would reset the search mask.

~~~ bash
$ whereis [options] filename
~~~

#### `-b`

Search only for binaries.

#### `-m`

Search only for manual sections.

#### `-s`

Search only for sources.

#### `-u`

Search for unusual entries. A file is said to be unusual if it does not have one entry of each requested type.

~~~ bash
$ whereis -m -u *
~~~

This example will return all files in the current directory that have no documentation.

#### `-f`

Terminate the last directory list and signals the start of filenames. This must be used when any of the directory options (-B, -M, -S) options are used.

#### The options -B, -M and -S reset the search paths for the subsequent filename patterns.

~~~ bash
$ whereis [directory options] directories -f filename
~~~

#### `-B`

Change or otherwise limit the places where whereis searches for binaries, by a whitespace-separated list of directories.

#### `-M`

Change or otherwise limit the places where whereis searches for manual sections, by a whitespace-separated list of directories.

#### `-S`

Change or otherwise limit the places where whereis searches for sources, by a whitespace-separated list of dierctories.

### Examples

~~~ bash
$ whereis perl
~~~

List the directories where `perl` source files, documentations and binaries are stored.

~~~ bash
$ whereis -u -ms -M /usr/man/man1 -S /usr/src -f *
~~~

Find all files in the current directory which are not documented in `/usr/man/man1` or have no source in `/usr/src`.
