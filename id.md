---
---

id
--
`id` is a command that prints out the effective and real user and group ids.
<!-- one line explanation would go here -->

<!-- minimal example -->

The syntax for the command is:

~~~ bash
id [option(s)]
~~~

<!--more-->

### Useful Options / Examples

#### `id`

~~~ bash
id [option(s)]
id [option(s)] [USERNAME]
~~~

 * The `id` command prints out information for the current user. However, it is possible to specify a different user by appending their name to the end of the command.

Simply entering `id` prints out all the information about the current user.

~~~bash
$ id
uid=1000(biswash) gid=1000(biswash) groups=1000(biswash),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare),999(vboxsf)
~~~

#### `id -u`
The `-u` flag prints out the current user ID

~~~bash
$ id -u
1000
~~~

#### `id -g` && `id -G`
The `-g` flag prints out the current group id, whereas the `-G` flag prints out the id of all groups.

~~~bash
$ id -g
1000
$ id -G
1000 4 24 27 30 46 113 128 999
~~~

#### `id -n`
The `-n` flag is used in conjuction with the `-u` and the `-g` flags to find the name of the user or group rather than their id.

~~~bash
$ id -un
biswash
$ id -gn
biswash
$ id -Gn
biswash adm cdrom sudo dip plugdev lpadmin sambashare vboxsf
~~~

 * The main reason to use the id command is to find to which group an user belongs to. This is helpful when switching between users with different permissions and settings.

