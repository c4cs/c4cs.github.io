---
---

id
--

`id` is used to get information about a user's UID (user ID), the groups a user belongs to, groups associated with the user, and security context of the current user. The default `id` command shows the user and groups names and numeric ID's. Use id with options to find more useful (i.e. readable) information. Example1: to find a specific user's UID, add -u {username}. Moreover, id -G USERNAME will find all the groups a user belongs to. Force id to display the name of the UID or GID instead of ugly numbers by passing the -n option.
~~~ bash

$ id -u username
302
id -G username
203 403 94 32 94
$ id -ng username
staff eecsstudents club1 club 2
~~~




~

<!--more-->

### Useful Options / Examples

#### Example command

##### Break it down

#### Example command

##### Break it down


