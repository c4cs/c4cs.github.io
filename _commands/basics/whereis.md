---
---

whereis
--
Locates the binary, source, and manual page for a command.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$whereis ls

ls: /bin/ls /usr/share/man/man1/ls.1.gz


$whereis vim

vim: /usr/bin/vim.tiny /usr/bin/vim /usr/bin/vim.basic /etc/vim /usr/share/vim /usr/share/man/man1/vim.1.gz
<!--more-->

~~~
### Useful Options / Examples

#### Example command
There is an option to list all the paths whereis uses to search for commands:

whereis -l

For my system this is the output:

~~~ bash
$whereis -l

bin: /usr/bin
bin: /usr/sbin
bin: /usr/lib
bin: /bin
bin: /sbin
bin: /etc
bin: /lib
bin: /lib64
bin: /usr/games
bin: /usr/local/bin
bin: /usr/local/sbin
bin: /usr/local/etc
bin: /usr/local/lib
bin: /usr/local/games
bin: /usr/include
bin: /usr/local
bin: /usr/share
bin: /opt/VBoxGuestAdditions-5.2.4/bin
man: /usr/share/man/ru
man: /usr/share/man/gd
man: /usr/share/man/man7
man: /usr/share/man/ms
man: /usr/share/man/da
man: /usr/share/man/fa
man: /usr/share/man/el
man: /usr/share/man/ku
man: /usr/share/man/ta
man: /usr/share/man/en_GB
man: /usr/share/man/bs
man: /usr/share/man/shn
man: /usr/share/man/ko
man: /usr/share/man/zh_TW
man: /usr/share/man/en_CA
man: /usr/share/man/kk
man: /usr/share/man/man8
man: /usr/share/man/sq
man: /usr/share/man/he
man: /usr/share/man/man3
man: /usr/share/man/uz
man: /usr/share/man/man1
man: /usr/share/man/sl
man: /usr/share/man/hu
man: /usr/share/man/zh_HK
man: /usr/share/man/fi
man: /usr/share/man/gl
man: /usr/share/man/lt
man: /usr/share/man/ug
man: /usr/share/man/cy
man: /usr/share/man/km
man: /usr/share/man/ce
man: /usr/share/man/ast
man: /usr/share/man/sv
man: /usr/share/man/fr.ISO8859-1
man: /usr/share/man/ca@valencia
man: /usr/share/man/pl
man: /usr/share/man/it
man: /usr/share/man/th
man: /usr/share/man/nn
man: /usr/share/man/sk
man: /usr/share/man/ja
man: /usr/share/man/cs
man: /usr/share/man/my
man: /usr/share/man/fr
man: /usr/share/man/ne
man: /usr/share/man/nb
man: /usr/share/man/man2
man: /usr/share/man/pt_BR
man: /usr/share/man/en_AU
man: /usr/share/man/id
man: /usr/share/man/ml
man: /usr/share/man/hi
man: /usr/share/man/uk
man: /usr/share/man/be
man: /usr/share/man/io
man: /usr/share/man/vi
man: /usr/share/man/oc
man: /usr/share/man/ca
man: /usr/share/man/fy
man: /usr/share/man/se
man: /usr/share/man/de
man: /usr/share/man/man6
man: /usr/share/man/ar
man: /usr/share/man/bn
man: /usr/share/man/ro
man: /usr/share/man/zh_CN
man: /usr/share/man/ps
man: /usr/share/man/lv
man: /usr/share/man/bg
man: /usr/share/man/eo
man: /usr/share/man/fr_CA
man: /usr/share/man/az
man: /usr/share/man/nl
man: /usr/share/man/si
man: /usr/share/man/tr
man: /usr/share/man/et
man: /usr/share/man/mhr
man: /usr/share/man/fo
man: /usr/share/man/man4
man: /usr/share/man/pt
man: /usr/share/man/es
man: /usr/share/man/man5
man: /usr/share/man/hy
man: /usr/share/man/bo
man: /usr/share/man/pa
man: /usr/share/man/sr
man: /usr/share/man/fr.UTF-8
man: /usr/share/man/hr
man: /usr/share/man/te
man: /usr/share/man/eu
man: /usr/share/info
src: /usr/src/linux-headers-4.10.0-28-generic
src: /usr/src/linux-headers-4.10.0-28
src: /opt/VBoxGuestAdditions-5.2.4/src/vboxguest-5.2.4
src: /usr/src/linux-headers-4.4.0-104
src: /usr/src/virtualbox-guest-5.0.40
src: /usr/src/linux-headers-4.4.0-104-generic

~~~

#### Example command
Sometimes the command whereis is looking for is unusual(empty documentation or documentation with multiple places).
Thus, we need some flags for this scenario:

$whereis -m -u *
 
The -u flag allows for whereis to show the command names that have unusual entries

Here we also use the -m flag to only look for manuals, we can also use -b for binary files.

~~~bash
$whereis -m -u *

chmod: /usr/share/man/man1/chmod.1.gz /usr/share/man/man2/chmod.2.gz
gzip: /usr/share/man/man1/gzip.1.gz /usr/share/info/gzip.info.gz
kill: /usr/share/man/man1/kill.1.gz /usr/share/man/man2/kill.2.gz
man: /usr/share/man/man7/man.7.gz /usr/share/man/man1/man.1.gz
mkdir: /usr/share/man/man1/mkdir.1.gz /usr/share/man/man2/mkdir.2.gz
passwd: /usr/share/man/man1/passwd.1ssl.gz /usr/share/man/man1/passwd.1.gz /usr/share/man/man5/passwd.5.gz
printf: /usr/share/man/man3/printf.3.gz /usr/share/man/man1/printf.1.gz
rmdir: /usr/share/man/man1/rmdir.1.gz /usr/share/man/man2/rmdir.2.gz
sleep: /usr/share/man/man3/sleep.3.gz /usr/share/man/man1/sleep.1.gz
~~~
