---
---

passwd
-------

`passwd` is a command that is used to change the password of system users.

~~~ bash
$ passwd
Changing password for user [current user]
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
~~~

<!--more-->

### Useful Options / Examples

#### Usage
Unless logged in as `root`, this command will need to be used with `sudo` to get permission to modify other user's passwords.

~~~ bash
$ passwd [OPTION] [USER]
~~~

#### Example command

`sudo passwd` allows the current user to change other user's passwords if the current user has superuser permissions.  It requests the current user's password, then allows the current user to set the other user's new password.  This allows the current user to change the other user's current password without knowledge of the other user's password, which can come in handy if one ever forgets his or her own account password but has access to a user with superuser permissions.

~~~ bash
$ sudo passwd other_user
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
~~~

#### Example command
`-d`, `--delete`

This option makes a user's password empty.

~~~ bash
$ sudo passwd -d other_user
passwd: password expiry information changed.
$ sudo passwd -S other_user
other_user NP 01/01/1970 0 99999 7 -1
~~~

#### Example command
`-e`, `--expire`

Expires a user's password, forcing it to be re-set the next time the user logs in.  No change appears to occur to account status information.

~~~ bash
$ sudo passwd -e other_user
passwd: password expiry information changed.
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 7 -1
~~~

#### Example command
`-S`, `--status`

This option displays account status information in 7 fields:
<br>
1. User login name
<br>
2. *L* if locked password (seems to be if the user was created and no password was set), *P* if password exists, *NP* if no password
<br>
3. Date of last password change
<br>
4. Minimum password age (days)
<br>
5. Maximum password age (days)
<br>
6. Password warning period (days)
<br>
7. Password inactivity period(days)

~~~ bash
$ passwd -S
current_user P 01/01/1970 0 99999 7 -1
~~~

~~~ bash
$ sudo passwd -S other_user
other_user L 01/01/1970 0 99999 7 -1
~~~

#### Example command
`-a`, `--all`

This option displays account status information for all users.  The example shown below has removed out many default system users.
Note: this option won't work without -S

~~~ bash
$ sudo passwd -Sa
root P 01/01/1970 0 99999 7 -1
daemon L 01/01/1970 0 99999 7 -1
bin L 01/01/1970 0 99999 7 -1
sys L 01/01/1970 0 99999 7 -1
current_user P 01/01/1970 0 99999 7 -1
~~~

#### Example command
`-n num_days`, `--mindays num_days`

Sets the minimum number of days between password changes.  0 means the password can be changed at any time.

~~~ bash
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 7 -1
$ sudo passwd -n 30 other_user
passwd: password expiry information changed.
$ sudo passwd -S other_user
other_user P 01/01/1970 30 99999 7 -1
~~~

#### Example command
`-x num_days`, `--maxdays num_days`

Sets the minimum number of days a password is valid.  After num_days the password must be changed.

~~~ bash
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 7 -1
$ sudo passwd -x 55 other_user
passwd: password expiry information changed.
$ sudo passwd -S other_user
other_user P 01/01/1970 0 55 7 -1
~~~

#### Example command
`-w num_days`, `--warndays num_days`

Sets the number of days before password expiration that a warning will begin showing.  In other words, starting *num_days* before the password expires, warnings will begin to be shown.

~~~ bash
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 7 -1
$ sudo passwd -w 2 other_user
passwd: password expiry information changed.
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 2 -1
~~~

#### Example command
`-i num_days`, `--inactive num_days`

Sets the number of days an account's password can be expired until the account will be disabled.  The user may no longer sign on to the account after *num_days* days.

~~~ bash
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 7 -1
$ sudo passwd -i 4 other_user
passwd: password expiry information changed.
$ sudo passwd -S other_user
other_user P 01/01/1970 0 99999 7 4
~~~
