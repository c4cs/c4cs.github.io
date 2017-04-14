---
permalink: /lectures/w17/week15a.html
---

class: center, middle

# Understanding VPS Security via SSH

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden / [Cameron Gagnon](https://github.com/cameron-gagnon) (for today!)**
]


---

# Today's Definitions

### - VPS

---

# Today's Definitions

### - VPS

### - PAM

---

# Today's Definitions

### - VPS

### - PAM

### - SPAM

---

# Today's Definitions

### - VPS

### - PAM

### - SSH

---

# Really Today's Definitions

### - Virtual Private Servers (VPS)
### - Pluggable Authentication Modules (PAM)
### - Secure SHell (SSH)

---

# Really Today's Definitions

### - Virtual Private Servers (VPS)
- [Homework 1!](https://c4cs.github.io/static/w17/hw/c4cs-wk1-homework.pdf)

### - Pluggable Authentication Modules (PAM)
### - Secure SHell (SSH)

---

# Really Today's Definitions

### - Virtual Private Servers (VPS)
- [Homework 1!](https://c4cs.github.io/static/w17/hw/c4cs-wk1-homework.pdf)

### - Pluggable Authentication Modules (PAM)
### - Secure SHell (SSH)
- [Matt's post on Piazza!](https://piazza.com/class/ixgsfwif4f35is?cid=79)

---

# Now You Know

.center[
![:scale_img 60%](https://i.imgur.com/GaPPuyT.jpg)
]

---

# Project's Goal

### - Show us the passwords of people (or programs) trying to authenticate to the Virtual Private Server

---

# Project's Goal

### - Show us the passwords of people (or programs) trying to authenticate to the Virtual Private Server


# Lecture's Goal

### - Show how knowledge from this class can be applied

---

# Setting up a Virtual Private Server

### - What do you do when you first set up a new computer, phone, or personal device?

---

# Setting up a Virtual Private Server

### - What do you do when you first set up a new computer, phone, or personal device?


## Dotfiles
- [Homework 12!](http://c4cs.github.io/static/w17/hw/c4cs-wk12-homework.pdf)

---

# Setting up a Virtual Private Server

### - What do you do when you first set up a new computer, phone, or personal device?


## Dotfiles
- [Homework 12!](http://c4cs.github.io/static/w17/hw/c4cs-wk12-homework.pdf)


## `~/.ssh/config`
```bash
Host c4cs-lecture
    Hostname 138.236.11.81
    User root
    IdentityFile ~/.ssh/id_rsa_do_pnu
```
- Regular and Advanced Homework 12

---

# Let's dive in

- https://github.com/cameron-gagnon/ssh_pass_logging

---

# Make and `Makefile`s

- [Homework 7!](https://c4cs.github.io/static/w17/hw/c4cs-wk7-homework.pdf)

---

# Installing the PAM module

### Where did we learn how programs get configuration information?

---

# Installing the PAM module

### Where did we learn how programs get configuration information?
 - [Lecture 3!](http://leccap.engin.umich.edu/leccap/viewer/r/gWkG4c)

---

# Installing the PAM module

### Where did we learn how programs get configuration information?
 - [Lecture 3!](http://leccap.engin.umich.edu/leccap/viewer/r/gWkG4c)

## Alternatives to a PAM module
 - Install and compile OpenSSH from source while adding [this patch](https://gist.github.com/sjmurdoch/1572229).
 - Would get to tie in package managers (Week 12!)

---

# Scripting

```bash
# from create_initial_users.sh

# list of some default usernames to add
while IFS='' read -r user || [[ -n "$user" ]];
do
    ./honeypot_user.sh "$user"
done < "usernames.txt"
```

- [Regular and Advanced Homework 3](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
- [Advanced Homework 6](https://c4cs.github.io/static/w17/advanced/c4cs-wk6-advanced.pdf)

---

# Piping commands
- From [Lecture 6](http://leccap.engin.umich.edu/leccap/viewer/r/qlB5Sh)
 - `ifconfig enp0s3 | grep 'inet ' | tr -s "[:space:]" ":" | cut -d ":" -f 4`

- From the `Makefile`
 - `cat /var/log/passwords | cut -d';' -f3 | grep -vE '^[[:cntrl:]]|^[[:space:]]*$$' | cut -d= -f2 | tr -d ' ' | sort | uniq | tee -a usernames.txt`


---

# Security

## What to do about all these attempts?
 - Configure settings in `/etc/ssh/sshd_config` to prevent password based authentication
 - [fail2ban](https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-14-04)

---

# Attendance

.center[
![:scale_img 80%](https://hikaruzone.files.wordpress.com/2015/10/in-case-of-fire-1-git-commit-2-git-push-3-leave-building2.png?w=800&h=559)
]

---

class: center, middle

# Questions?
