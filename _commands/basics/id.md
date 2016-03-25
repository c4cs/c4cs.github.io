---
---

id
--

`id` id is used to get information about a user’s UID (user ID), the groups a user belongs to, groups associated with the user, and security context of the current user. The default id command shows the user and groups names and numeric ID’s. Use id with options to find more useful information.

~~~ bash
$ id -G username
203 403 94 32 93
~~~

<!--more-->

### Useful Options / Examples

#### Example command

to find a specific user's UID, add -u {username}. Moreover, id -G USERNAME will find all the groups a user belongs to. Force id to display the name of the UID or GID instead of ugly numbers by passing the -n options

~~~ bash
$id -ng username
staff eecsstudents club1 club2
~~~

#### Example command
To find all the groups associated with a user called exampleuser, enter:

~~~ bash
$ id exampleuser
~~~

sample output:

~~~ bash
uid = 0(exampleuser) gid=0(eecs) groups=1(computing), 1(hello),2(this), 3(is), 4(an), 5(example)
~~~

### Useful options:
<ul style = "list-style-type:disc">
<li>-g : Display only the effective group ID</li>
<li>-G : Display all group IDs</li>
<li>-u : Display only the effective user ID</li>
<li>-n : Display a name instead of a number, for -u or -g</li>
<li>-r : Display the real ID instead of the effective ID</li>
<li>-z : Show only the security context of the current user</li>
</ul>

