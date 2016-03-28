---
---

id
--

`id`: `id` is used to get information about a user’s UID (user ID), the groups a user belongs to, groups associated with the user, and security context of the current user. The default id command shows the user and groups names and numeric ID’s. Use id with options to find more useful information.

~~~ bash
$ id -G username
203 403 94 32 93
~~~

<!--more-->

### Useful Options / Examples

#### Example command

to find a specific user's UID, add `-u {username}`. Moreover,`id -G USERNAME` will find all the groups a user belongs to. Force `id` to display the name of the UID or GID instead of ugly numbers by passing the `-n` options

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


### Break it down
When `id` is printed without options, it prints a whole lot of hard-to-read stuff. Of this hard-to-read stuff is the UID, a unique number assigned to each user on the machine. Moreover, `id` without options will also print the GID, or the group ID. A GID is a name that associates a user with other users sharing something in common. A user can be a member of more than one group and therefor have more than one GID. So, using `id` without options prints the UID, the GID, and a list of the groups the user is a member of along with their GIDs. ex:

~~~ bash
$ id
uid = 1000(mayden) uid=1000(mayden) gid=2000(mayden) groups=500(group1), 4(adm), 723(staff), 33(admin)
~~~

therefor, user mayden has UID number = 1000 and gid number = 2000. mayden is a member of the following groups: 
<ul>
<li> group1 with GID 500 </li>
<li> adm with GID 4 </li>
<li> staff with GID 723 </li>
<li> admin with GID 33 </li>
</ul>

