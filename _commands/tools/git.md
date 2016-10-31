---
---

git
---

<em>TODO: Placeholder</em>

<!-- one-line explanation -->

<!-- minimal example -->

<!--more-->

<!--
### Useful Options / Examples


##### Break it down


##### Break it down

-->

----------------------

Git For Beginners
=================
This section of the Git page is for those of us that are actually in EECS 280/281, meaning you have little to no experience with Git and are more worried about figuring out the 
difference between staging and committing things than the neat little things 
you can do to make Git as personalized as possible.

What is Git? 
------------
Git is technology for version control. What is version control? Version control is a 
way to keep track of changes to a project so that while working, you don't change 
something and crash your program and have no way of getting back it back to a state 
when it was working. You have probably used some type of version control before, when I 
was in 280 I used to send emails to myself containing versions of my project 
just in case everything went to crap.

Step By Step
------------
If you want to use git for a project, you have to create a git repository in the 
folder that your project is either already stored or will be stored. You do that 
by opening a terminal, navigating to your project folder and typing:

~~~ bash
$ git init
~~~

Great, so you've created your git repository (or repo as the cool kids say). 
Now what? Before we do anything else, I should explain how git works.

Git is basically a bunch of snapshots of your project strung to together. As 
the programmer, it is your job to decide when to take the snapshots. Git is 
only as helpful as you make it. When you decide to take a snapshot of your work
git remembers everything that has changed to all the files in your working 
directory since the last time you took a snapshot. These snapshots are called 
commits. But before I show you how to make a commit, I need to show you what 
staging is.

Staging is picking which files you would like to take a snapshot of. As you 
work though your project, adding code and deleting code, git keeps track of
which files have changed since your last snapshot. To see the names of the 
files that have changed, we type:

~~~ bash
$ git status
~~~

It will show:

~~~ bash
	modified: file.cpp
~~~

However, we can't make a commit just yet. Currently, git doesn't know what 
files we want it to take a snapshot of. It just has a list of a bunch of files 
that have changed. To tell git which files to take a snapshot of, we type:

~~~ bash
$ git add file.cpp file2.cpp
~~~

Now if we type git status again, we will see

~~~ bash
Changes to be committed:
	(use git reset HEAD <filename>)
	modified: file.cpp
		  file2.cpp
~~~

If for whatever reason we don't want to commit one of the files we have staged (like if we 
discovered an error in file2.cpp), we can unstage that file by:

~~~ bash
$ git reset HEAD file2.cpp
~~~

So, now that we have all the files we want included in out snapshot staged, we can 
finally make the commit. Which we do by typing:

~~~ bash
$ git commit -m 'file1.cpp is being committed'
~~~

Where we put a descriptive sentence/message in the single quotes to remind 
ourselves and anyone else looking at our code why and what we committed.
If we run git status again, we see that file1.cpp is no longer "modified," in 
fact it's not listed at all.

Now, to see all the previous commits for a project, we type:

~~~ bash
$ git log
~~~

If we have more than 3 or 4 commits, our git log command is probably going to 
have more than one terminal's screen of output. Which if you are unfamiliar with
terminal navigation, like I was when I took this course, will leave you in kind of a 
funny spot. Your terminal screen is filled with a lines of commits with 
ungodly long strings of random numbers and letters, the author of 
the commit, the date of the commit, and the message attached to the 
commit. At the bottom of ther terminal  there will be a colon 
followed by your cursor. The first time I used git, I had no idea how to navigate or 
escape this screen. 

Luckily for you, I have since figured it out! You can navigate up 
a line up or down by using your arrow keys or by pressing the j key on your keyboard
to navigate up and the k key to navigate down (this is how you navigate using vim, 
a terminal-based text editor that while older than time itself, still has many users 
and isn't a bad thing to know how to use -> you can type really fast when your hands don't
leave the main keys). Once you have seen what you have needed to see, just press the q key 
and you will exit back to the terminal. You will probably come across a lot of terminal 
based applications in your time programming, and you can exit a lot of them just by pressing
q, which is something that took me an embarassingly long time to figure out. Now, back to git.

My Program Crashed, Now What?
-----------------------------



Git Niceties
============

This is a collection of tips and tricks that can make working with git more
pleasant. You may not like all of these or you may have other preferences, you
should explore!


~/.gitconfig
------------

This file is the global configuration file for your machine. When you first ran
git, it asked you to run `git config --global user.name "Example Name"`. What
that command was really doing was writing to this file. Some other things that
can be useful:

~~~ bash
$ cat ~/.gitconfig
[user]
	name = Pat Pannuto
	email = pat.pannuto@gmail.com

# This will automatically fix simple typos, e.g. `git psuh` will run `git push`
[help]
	autocorrect = 1

# Alias lets you create new git subcommands.
# The first example lets you type `git st` instead of `git status`.
# The second example augments `git log` to include a summary of changed files
# and to show only the commit titles.
# The last exaples are the `git graph` command we showed in lecture.
# Try them out!
[alias]
	st = status
	ll = log --stat --abbrev-commit
	graph1 = log --graph --full-history --all --color
--pretty=tformat:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s%x20%x1b[33m(%an)%x1b[0m"
	graph2 = log --graph --full-history --all --color --pretty=tformat:"%C(red)%h%C(reset)%x09%C(green)%d%C(reset)%C(bold)%s%C(reset)%C(yellow)(%an)%C(reset)"
~~~

You can see the full list of configuration options at
https://git-scm.com/docs/git-config


Git-Enabled PS1
---------------

PS1 is the prompt that bash will print before running a command. Git ships with
a helper function named `__git_ps1`. To enable this, we need to edit the `PS1`
environment variable, which can be a bit messy. `PS1` is set in `~/.bashrc`.
On my Ubuntu VM, this is the default:

~~~ bash
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\] \$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
~~~

To enable `__git_ps1`, we'll add this snippet to that line:

~~~ bash
$(declare -F __git_ps1 &> /dev/null && __git_ps1)
~~~

This first tests that a `__git_ps1` function exists and then calls that
function. Testing the function exists is generally a good habit as it will let
you reuse this `bashrc` file without worrying whether git is installed on every
machine.

The final result is then

~~~ bash
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(declare -F __git_ps1 &> /dev/null && __git_ps1) \$ '
~~~

You may also want to explore some settings, such as

~~~ bash
export GIT_PS1_SHOWDIRTYSTATE=true
export GIT_PS1_SHOWUNTRACKEDFILES=true
~~~

Check out `/usr/lib/git-core/git-sh-prompt`
(or `/usr/local/etc/bash_completion.d/git-prompt.sh` from OS X homebrew users)
for more options and settings.


### Third-Party PS1's

Beyond what git provides natively, many other people have written PS1's.
Here are some that may be worth trying out:

Git-focused:
   https://github.com/magicmonty/bash-git-prompt

General Prettiness:
   https://github.com/powerline/powerline
   https://github.com/milkbikis/powerline-shell

Or build your own:
   http://bashrcgenerator.com/


OS X Specific Things
--------------------

Sometimes, OS X will create `.DS_Store` files, which can be annoying to remember
to add to every `.gitignore`. You can automatically ignore them globally on your
machine by adding `.DS_Store` to `~/.gitexcludes`.


