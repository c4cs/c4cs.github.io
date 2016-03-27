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

#### useradd -d

~~~bash
$ useradd -d /projects/users username
~~~

##### Break it down
 * The `-d` flag option allows you to choose the location of the new home directory
 * By default the 'useradd' command creates the home directory under /home directory with username

 
#### useradd -u

~~~bash
$ useradd -u 750 newUser
~~~

##### Break it down
 * Every user has its own unique identification numer (UID). By default, new user accounts are assigned UID 500, 501, 502, and so on
 * The `-u` flag option allows you to choose a specific UID


#### useradd -e

~~~bash
$ useradd -e 2016-10-10 username
~~~

##### Break it down
 * By default, 'useradd' creates accounts that never expire
 * The `-e` flag option allows you to create temporary accounts 
 * Use the date in YYYY-MM-DD format for desired date


#### useradd -f

~~~bash
$ useradd -f 20 username		
#password of "username" account expires in 20 days
~~~

##### Break it down
 * By default, a user's password will never expire
 * The `-f` option will set a password expiry date (in days)
 

### Final details
After adding a new user with `useradd`, the new account will be locked.
To unlock the user account, you'll need to set a password with the 'passwd' command.

~~~bash
$ useradd newperson
$ passwd newperson
Changing password for user newperson
New password:
Retype new password:
passwd: all authentication tokens updated successfully
~~~
