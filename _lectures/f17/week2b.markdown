---
permalink: /lectures/f17/week2b.html
---

class: center, middle

# Crashing into EECS like a wrecking ball

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Cameron Gagnon**
]

---

class: center, middle

<a href="http://www.youtube.com/watch?feature=player_embedded&v=I7Tps0M-l64"
target="_blank"><img src="http://img.youtube.com/vi/I7Tps0M-l64/0.jpg"
alt="Cool dude Coach" width="533" height="400" border="10" /></a>

---

# Quick Poll

--

<hr />

## Mac -- Windows -- Linux

--

## Terminal/command line

--

## SSHed into CAEN

--

## Git

--

## Vi/Vim or Emacs


---

# Linux/Unix: What is it?

--

## Unix
  - Proprietary (think: costs money, closed source)
  - Kernel + GUI pieces + everything else that comprises an OS
  - Comes from specific vendors
  - Ex. Solaris

--

## Linux
  - Open sauce kernel developed by Linus Torvalds and fam (not actually family)
  - Technically just kernel (no GUI or commands)
  - GNU (GNU's not Unix) + Linux == OS
  - Ex. Ubuntu is built on top of Debian which is built on top of Linux

--

## EECS 482 for more background on what a kernel and OS is

---

class: center, middle


<a rel="history" href="http://futurist.se/gldt/">If you are ever wondering what
to do with those extra engineering prints</a>


---

# Enough talk, let's play

## Fire up a terminal

--

  - What is this?

--

  - Not magic

--

## Two images of the same directory structure

Finder | Terminal
--- | ---
![Finder "terminal"](img/finder_tree.png) | ![Terminal "Finder"](img/terminal_tree.png)


--

## We'll hit up our friend `tree` later, he/she/it/tree is pretty cool

---

# Let's play around a bit:

  - `cd` `c`hange `d`irectory
  - `pwd` `p`rint `w`orking `d`irectory
  - `ls` list files
  - `mkdir` make directory
  - `touch FILENAME` create an empty file if it doesn't yet exist
  - `mv SRC_FILE DESTINATION` move file(s) around
  - `rm FILENAME` remove files
  - `rm -r DIRECTORY` remove directories

---

# Still no clue...
<hr/>

--

  - What do you do when you have a question?

--

  - Ask for...

--

# `help`!

---

# Several ways of getting help

<hr />

## - `help CMD`

## - `man CMD`

## - `info CMD`

## - `CMD --help` or `CMD -h` sometimes works


.footer[Knowing a bit about what's on this slide should help with a future
homework...]

---


# But one towers over the rest...

--

#### ...not really, but it's the most commonly used

--

## `Man`ual

### Opens a document with another command called `less`

  - `q`(uit)
  - `j` down one line at a time
  - `k` up one line at a time
  - `d`(own) half a page at a time
  - `u`(p) half a page at a time
  - `/searchPattern` ex. `/output`
  - `n`(ext) occurrence of search
  - `g`(o to) top of page
  - `Shift` + `G` jumps to bottom of page

#### Still more commands, but not as commonly used

---

# Let's explore a bit with `man`

### - Might as well bring back our friend `tree`


--

# What if `man` pages didn't suck so much?

---

class: center, middle

# WARNING: TOO COOL COMMAND AHEAD!!!!

--

## You've been warned. Proceed with caution

---

# `tldr`

### Too long; didn't read

  - Use it the same way as `man`

### To install

  - Mac: `brew install tldr`
  - Ubuntu: multiple methods
    - One option: `sudo apt install python-pip && pip install tldr`
    - Another: `sudo apt install npm && npm install -g tldr`
    - Otherwise refer to: https://github.com/tldr-pages/tldr

### Take a minute and install it

--

### Try it out on a few commands. `tree`, `man`, even `tldr` itself

---

# You've earned it

![Coach](img/coach_1.png)

---

# SSH and CAEN

### Start out with a `man ssh` to feel our way around. Or better yet, try out `tldr ssh`

--

  - `ssh uniqname@login.engin.umich.edu`

--

### Cool! What's actually happening?

--

## Let's make it easier

Add:
```
Host caen
    HostName login.engin.umich.edu
    User uniqname
```
to `~/.ssh/config`


--

Now you can type `ssh caen` and give your password to login

---

# `git`

<hr/>

### Let's set up ssh keys with GitHub

  - `ssh-keygen -t rsa -b 4096 -C your_email@example.com`
    - On Mac: `cat ~/.ssh/id_rsa_github.pub | pbcopy` (install `pbcopy`)
    - On Ubuntu: `cat ~/.ssh/id_rsa_github.pub` and then copy it to your clipboard
  - Go to https://github.com/settings/keys
  - Do *NOT* copy the `~/.ssh/id_rsa_github` key. That one is *private*

--

### Add this to your `~/.ssh/config` file:
```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_github
```

--

## What if working with `git` didn't have to suck so much?

---

class: center, middle

# WARNING: TOO COOL COMMAND AHEAD!!!!

--

## You've been warned. Proceed with caution

---

# `scm_breeze` makes `git` life easier

## - Check it out: `https://github.com/scmbreeze/scm_breeze`

## - Install it:
```
git clone git://github.com/scmbreeze/scm_breeze.git ~/.scm_breeze
~/.scm_breeze/install.sh
source ~/.bashrc   # or source ~/.zshrc
```

## Let's mess around

---

# You've earned it


![Coach](img/coach_2.png)

---

# Getting repos on CAEN

  - Create a local repo `git init`
  - Create a repo on GitHub https://github.com/new (give it whatever name you like)
  - Follow the steps on GitHub for creating a new repo

--

  - `ssh uniqname@login.course.engin.umich.edu`

--

### Also check out https://c4cs.github.io/commands/Caen-Connect-Tutorial

--

## For more cool ideas
  -  https://dotfiles.github.io/

---

# Vim

## Three main modes
 - Insert (regular typing)
 - Normal (issue commands to do things)
 - Visual (highlight and select text)

## Normal mode commands
 - `:q`(uit)
 - `:w`(rite)
 - `j` down
 - `k` up
 - `gg` (go to top of file)
 - `Shift` + `G` (go to bottom of file)
 - `dd` delete line
 - `yy` yank (copy) line

---

class: center, middle

# WARNING: TOO COOL COMMAND AHEAD!!!!

--

## You've been warned. Proceed with caution

---

# Another awesome trick

## `z` - jump around

## https://github.com/rupa/z


### After you `cd` around a bit, `z` builds up a database that lets you quickly jump to where you need to go

  - ex. `z 398` takes you to your `398` folder

--

## How to install
  - On Mac with `brew`:
    - `brew install z`
  - On Ubuntu:
    - `git clone https://github.com/rupa/z ~/z`
    - `echo ". ~/z/z.sh" >> ~/.bashrc`

---

# You made it!

![Coach](img/coach_3.png)
