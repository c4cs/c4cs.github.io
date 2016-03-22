---
---

id
--

Helps you to find username and group information

~~~ bash
$ id
uid=1000(username) gid=1000(username) groups=1000(username),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
~~~

<!--more-->

### Useful Options / Examples
$ id<br> 
gives you username info about yourself

$ id HarryPotter<br>
gives you information about the given username - in this case HarryPotter 

### Flags
-u username <br>
gives you the effective userid of username (replace username with the actual username you want to find the id for)

-g username <br>
same as the -u flag but it gives you the GID

-G username <br>
 all of the groups a user belongs to

-n username <br>
 display the name rather than the number of the user for -u or -g

### Set Variables
$UID <br>
 your user id

$EID <br>
 your eid

