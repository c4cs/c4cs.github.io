---
---

git
---

<!-- one-line explanation -->
Git is a version control system that can be used for collaboration
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
something and crash your program and have no way of getting it back to a state 
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

So, now that we have all the files we want included in our snapshot staged, we can
finally make the commit. Note that commits should be
[atomic](https://www.freshconsulting.com/atomic-commits/); they should contain exactly one
discrete change or fix.
We commit by typing:

~~~ bash
$ git commit -m 'Add file1.cpp'
~~~

We put a descriptive sentence/message in the single quotes to remind
ourselves and anyone else looking at our code why and what we committed.
Commit messages have a particular style: they should be written in the imperative
mood, without ending punctuation. Certain verbs, like "Add", "Implement", and
"Remove", are good first words in a commit message. Read [Chris Beams' "How to Write
a Git Commit Message"](https://chris.beams.io/posts/git-commit/) to learn the best
practices.

If we run git status again, we see that file1.cpp is no longer "modified," in 
fact it's not listed at all. Word to the wise: always run git status right before
you commit to make sure everything is the way it is supposed to be. It 
is very easy to shoot yourself in the foot with git, so be careful.

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
commit. At the bottom of the terminal  there will be a colon 
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

So, you told me that if I ruined my program and I had been using git correctly, I could 
get back to the old state of my project where everything still worked. How do 
you do it?

First, you need to identify which commit you need to get back to. You can do this
using git log to look at all the past commits. When you have decided which commit
you want to look at you just need to remember the first couple characters of the commit 
number (the big ugly one with all the numbers and letters). If the commit I wanted to 
look at was numbered 2adfs34231dg8d8... then I would:

~~~ bash
$ git checkout 2adfs3
~~~

Now, all the files in your working directory are in the state they were when when you made 
commit 2adfs34... You just need to open one a file and see that your code looks the 
way it did when you made the commit. You can re-test, compile files, and even edit files, 
but I wouldn't recommend doing that unless you create a new branch, which is something
I'll discuss later. When you want to get back to the state of your project before you 
checked out the old commits, you type:

~~~ bash
$ git checkout master
~~~

However, if you really screw up on your project, you have no interest in getting back 
to your current state. You just want to make your current state the working state that was 
2 or 3 commits ago. Do this by:

~~~ bash
git revert 2adfs3
~~~

This would get rid of all the changes I've made/committed since commit 2adfs3 and make a 
new commit signifying those removals. So now my project would have the exact same 
state it did when I made commit 2adfs3, but I would still have my commit history of 
all those changes I made previously. This revert command is useful because 
it still maintains your history, so if you reverted to a commit that was more 
than 1 commit ago you still have a record of those "bad" commits in between. Which would 
be useful if say you had implemented some code in one of those commits that actually wasn't 
bad and you decided you still needed it.


If you notice bugs in your project and aren't sure which commit introduced them, git help you
find the commit quickly!

~~~ bash
git bisect start
~~~

This will start the bisection of your project to find where the errors were introduced. git-bisect
uses binary search to pick commits to review and asks you if the commit under review is `good` or `bad`.
Upon finding the bad commit, revert it!

Creating New Features in A Sandbox (Sort Of)
--------------------------------------------

One of the many advantages of git is that you can work on a new feature or implementation 
without messing up your current working code. We do this in git with branches. 
Branches are a parallel series of snapshots to what is going on in our 
main series of snapshots (master). You can think of a branch as a side character 
that gets his own movie (which is in all likelihood far insuperior to the orginal movie) 
and backstory that eventually ties back into the main series of movies. If you are 
still confused, just do a Google Images search on git branches. I find that visuals help 
a lot with this stuff. So, say I decide I want to re-write one of 
my functions so that it is tail-recursive instead of just recursive. I would create a new 
branch with the name of tail at my current commit by typing:

~~~ bash
$ git branch tail
~~~

To add commits to this branch while working on my wicked awesome 
tail recursive implementation, I would have to check this branch out. Branches in git 
are basically just pointers (yeah, I know, those nasty 280 topics, gotta know 'em), so 
you need to tell git which pointer will point to your next commit, tail or master 
(which is the "main" git pointer). I would do this by typing:

~~~ bash
$ git checkout tail
~~~

To see all the branches I have created:

~~~ bash 
$ git branch
~~~

So, I am doing fine and dandy while working in my tail branch when I realize I need 
to change something in my master branch. What to do?! Well, you just use that handy 
checkout command again. To get back to the master branch, I would just:

~~~ bash
$ git checkout master
~~~
 
I could then make commits on my master branch for my new changes. 

Now that my changes are done, I want to navigate back to where I was working on 
my tail recursion, so I must checkout the tail branch.

~~~ bash 
$ git checkout tail
~~~

When I have finished my tail recursion function, I'm going to want to put it back 
with the rest of my finished project in the master branch. To do this we are going 
to use the git command merge. When you use git merge, it merges the branch you include
in the command with the branch you are currently on. So, if we want to merge our tail 
branch with master we must first navigate to our master branch and then merge.

~~~ bash
$ git checkout master
$ git merge tail
~~~

If both master and tail have had commits since we created a seperate branch, we will 
be responsible for making a merge commit that lets everyone looking at our log 
know that we merged two branches. However, if both the commits attached to tail and 
master chenged the same files in the same places, git gets confused and doesn't 
know what to keep. This is called a merge conflict, or a massive pain in the butt. Git 
won't let you merge the two branches until you have resolved the conflicts. Thankfully,
git makes your life easier by telling you which files are effected. To fix these merge 
conflicts you must open the listed file and determine what to keep and what to delete.
Git actually writes in the effected files what one branch says and what the other says, 
so you just have to delete one, save, git add the changed files and commit. 

The Power of Collaboration
--------------------------

Another reason people use git is because it allows us to easily (relatively) collaborate 
on projects. Lots of people use GitHub (although for class you should use GitLab because 
having a public repo on GitHub for EECS classes is an honor code violation) to store and 
share their projects in the cloud. To access and change code in the cloud you need to 
first have the online repo as a remote in git. But to do that we need to setup 
our repo in the cloud, whereupon, we will be given a url associated with our 
repo. Let's say we want to create a new remote named new and we have a git 
repo with a url of https://gitlab.com:

~~~ bash
$ git remote add new https://gitlab.com
~~~

To add new code or updated code to this repo we must push it (to the limit! Sorry). When 
pushing code to our git repo of choice, we only push the master branch. We can push to 
our git remote of new by:

~~~ bash
$ git push new
~~~

When we want to grab code from the cloud, we use git pull.

~~~ bash
$ git pull new
~~~

Pushing and pulling when working on a group project often results in numerous 
merge conflicts. Unfortunately, this is just something that you have to work through.

Conculsion of Git for Beginners
-------------------------------

I did my best to include a general overview of what first time Gitters would need to 
know. I obviously missed a lot of things, but luckily for you there are a ton of 
great Git resources on the web. I would recommend looking more into what the 
HEAD is and what it does. I would also recommend reading more into and practicing with 
pull and push. Your upper level EECS classmates are going to hate you if you 
continually mess up the shared repo or don't know how to use git properly. With that
said, most of your peers won't see Git until they absolutely need to, which gives you 
a huge advantage as you will have learned and mastered Git by that time, right :)? 
Hopefully this helps. There are some other neat Git tricks farther down the page. 


Git Niceties
============

This is a collection of tips and tricks that can make working with git more
pleasant. You may not like all of these or you may have other preferences, you
should explore!


Git Stash
---------

When working on a large project, you may find yourself in a position where you're halfway through implementing one feature, but then somebody asks you to switch to a different feature. What do you do with the progress that you've made on the first feature? One option would be to commit the work you've done so far, but if it's a work-in-progress, it might not even compile! Another option would be to make a temporary directory and put the work in there, but now you'd have two directories to manage and it could become a version control nightmare. Fortunately, git provides an easy way to handle this situation: the stash.

The stash is a hidden data structure that you can use to store changes to the working directory that have not yet been committed. These changes can then be loaded out of the stash at a later time when you want to resume working on that part of the project.

To store a set of changes in the stash, first modify the files in your working directory (and `git add` any untracked files), and then type `git stash save`. Git will then store away those modifications and restore your working directory to a clean slate matching the most recent commit. When you want to bring the changes back, type `git stash apply` and your most recently stashed work will be loaded into the working directory. (Note that if the repository has changed in the meantime, you may have to resolve merge conflicts upon loading from the stash.)

Saving and applying are the most fundamental commands for working with the stash, but there are a few other helpful commands as well:

  * `git stash list` will show a list of all of the work that's been stored in the stash, ordered from newest to oldest.
  * `git stash save "<message>"` will give the entry in the stash list a custom message so that you'll know later what the stashed work was doing.
  * `git stash drop stash@{<number>}` will remove an entry from the stash, where `<number>` is the index of the entry in the stash list.
  * `git stash pop` will `apply` the most recent stash entry and then `drop` it, essentially treating the stash as a stack data structure.
  * `git stash clear` will empty the entire stash.

The full `git stash` documentation can be found [here](https://git-scm.com/docs/git-stash).

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


