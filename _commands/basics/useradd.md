---
---

useradd
--------

`useradd` is used to create a new user or update default new user information 

On Debian, `adduser` should be used instead.  


~~~ bash
$ useradd [options] username
~~~

<!--more-->

### Details
`useradd` edits /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow files for new user account.

`useradd` creates and populates a home director for new user

`useradd` sets permissions and ownerships to home directory

### Useful Options
~~~bash
# by default the 'useradd' command creates the home directory under /home directory with username
# the '-d' option allos you to choose the location of the new home directory.
$ useradd -d /projects/users username
~~~



~~~bash
# every user has its own unique identification number (UID)
# by default, new user accounts are assigned uid 500, 501, 502, and so on
# with the '-u' option we can choose a specific uid
$ useradd -u 750 newUser
~~~


~~~bash
# by default, 'useradd' creates accounts that never expire
# using 'e' with the date in YYYY-MM-DD format, we can create temporary accounts
$ useradd -e 2016-10-10 username
~~~


~~~bash
# by default, a user's password will never expire
# using the 'f' option will set a password expiry date in days
$ useradd -f 20 username		
#password of "username" account expires in 20 days
~~~





