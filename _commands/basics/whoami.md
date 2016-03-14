---
---

whoami
--

`whoami` is used to print the current userid. Permissions for commands will be run with the 
level of permissions of userid.
 

~~~ bash
$ whoami
current_userid
~~~

<!--more-->

### Useful Options / Examples

#### `sudo whoami`
~~~ bash
$ sudo whoami
root
~~~

##### Break it down
 * `sudo` gives the user, root permission. `whoami` verifies this


#### `whoami` vs `id -un`
~~~ bash
$ whoami
uziemblo
$ id -un
uziemblo
~~~

##### Break it down
 * `whoami` and `id -un` give the same userid.
