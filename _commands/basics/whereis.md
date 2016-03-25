---
---

WHEREIS
-------

`whereis` is used to locate binary, source, and manual pages for specified files. Supplied filenames 
are stripped of pathname and file extensions. `whereis` attempts to locate the file in a list of standard
Linux places.

~~~ bash
$ whereis [-options] filename ...
~~~


### Useful Options / Examples

`-b` - Search only for binaries

`-m` - Search only for manual sections

`-s` - Search only for sources.

~~~ bash
$ whereis perl
perl: /usr/bin/perl /etc/perl /usr/share/perl /usr/share/man/man1/perl.1.gz
~~~
