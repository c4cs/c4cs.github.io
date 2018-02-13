---
layout: default
---

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

