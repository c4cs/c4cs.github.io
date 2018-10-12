---
---

git
---
`git` is a version control tool allowing for easy collaboration on projects.

~~~ bash
$ git clone https://github.com/c4cs/c4cs.github.io.git
$ cd c4cs.github.io
$ echo "Modified File" >> README.md
$ git add README.md
$ git commit -m "Added to README.md"
$ git push origin master
~~~

<!--more-->

### Useful Options / Examples

### `git init`

Initializes the current directory as a git repository

~~~ bash
$ git init
~~~

### `git status`

`git status` shows the current state of your git repository. This lists the current branch, all the
changes that have been made, and which changes are being tracked.

~~~ bash
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   hello.cpp

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   bye.cpp

~~~


### `git log`

`git log` Will display a list of all commits made on this project. For each commit, it will contain
the SHA-1 hash of the commit (this is sort of like a commit ID), maybe some action done in that
commit (such as the merge below), the author of the commit (so you know who to blame when the
project breaks), the date of the commit, and the commit message.

~~~ bash
$ git log
commit 09f6ef6fe7b28a3c1a3a296eb6d29d2c41310c83
Merge: e71dec1 d9ea675
Author: Some User <suser@email.com>
Date:   Fri Oct 20 12:32:59 2017 -0400

    Merge branch 'other'

commit d9ea675b182da0f025695b4f311283f3b0d86a99
Author: Some User <suser@email.com>
Date:   Fri Oct 20 12:32:51 2017 -0400

    Add some files

commit e71dec129976601109ce805ed1d07cb684ae015f
Author: Some User <suser@email.com>
Date:   Fri Oct 20 12:31:47 2017 -0400

    Change some files

commit 54682b444b11f0e36f332679102a41329abe4a7f
Author: Some User <suser@email.com>
Date:   Fri Oct 20 12:06:04 2017 -0400

    Initial Commit
~~~


### `git branch`

`git branch` is used to make new branches or list local branches. A branch is like a different copy
of your repository. If you think of git as a tree (which you should), `git branch` branches off of
the current branch like so:

```
                   C other
                  /
    D---E---A'---F master
```

~~~ bash
$ git branch
* master
$ git branch other
$ git branch
* master
  other
~~~


### `git checkout`

`git checkout` allows you to switch to a different branch that you have already made.

~~~ bash
$ git branch other
$ git branch
* master
  other
$ git checkout other
$ git branch
  master
* other
~~~


### `.gitignore`

A `.gitignore` file in your git repository will allow you to exclude particular files from being
tracked by git. In this example, git will not track the compiled `.out` file. Notice how it is not
listed by `git status`. This is commonly used to ignore compiled binaries in git repos since git
does not (normally) do well with binary files.

~~~ bash
$ touch .gitignore
$ echo "*.out" >> .gitignore
$ # Make hello.cpp, a hello world program
$ git status
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	hello.cpp

no changes added to commit (use "git add" and/or "git commit -a")
$ g++ hello.cpp -o hello.out
$ ls
hello.cpp hello.out
$ git status
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	hello.cpp

no changes added to commit (use "git add" and/or "git commit -a")
~~~

### `.gitconfig`

This file is the global configuration file for all of your projects on this
machine. When you first ran git, it asked you to run `git config --global
user.name "Example Name"`. What that command was really doing was writing to
this file. Some other things that can be useful:

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
# The rest of the examples augment `git log` to include various summaries of
# changed files, including the last example `git graph` we showed in lecture.
# Try them out!
[alias]
	st = status
	ll = log --stat --abbrev-commit
	gr = log --graph --full-history --all --color
	graph = log --graph --full-history --all --color --pretty=tformat:"%C(red)%h%C(reset)%x09%C(green)%d%C(reset)%C(bold)%s%C(reset)%C(yellow)(%an)%C(reset)"
~~~

### `git add`

`git add` tells git to start tracking one or multiple files. Using the `-A` flag, you can tell git
to track all changes in the git respository. Tracked files go in the staging area.

~~~ bash
$ touch hello.cpp
$ touch goodbye.cpp
$ touch c4cs.hpp
$ touch c4cs.cpp
$ git add hello.cpp
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.cpp

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	c4cs.cpp
	c4cs.hpp
	goodbye.cpp

$ git add -A
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   c4cs.cpp
	new file:   c4cs.hpp
	new file:   goodbye.cpp
	new file:   hello.cpp

~~~


### `git commit`

`git commit` will save your added changes to the repository as a commit. The `-m` flag allows you to
add the commit comment inline. Otherwise, you would have to write the comment in a pop up text
editor (nano by default).

~~~ bash
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   c4cs.cpp
	new file:   c4cs.hpp
	new file:   goodbye.cpp
	new file:   hello.cpp

$ git commit -m "Initial commit"
 4 files changed, 0 insertions(+), 0 deletions(-)
~~~


### `git reset`

`git reset` is a command that undoes changes at several levels. You can un-add a tracked file by
using the `git reset` command. If you have already committed changes that you don't want to keep,
you can use `git reset --soft HEAD~1` which undoes the last commit, but keeps the changes in the
staging area. You undo the last n commits by changing `HEAD~1` to `HEAD~n` where n is the number of
commits you want to undo. If instead you don't want to keep any of the files in the commit, use `git
reset --hard HEAD~1`. This undoes a commit and removes the files that were committed.

~~~ bash
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   c4cs.cpp
	new file:   c4cs.hpp
	new file:   goodbye.cpp
	new file:   hello.cpp

$ git reset hello.cpp
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   c4cs.cpp
	new file:   c4cs.hpp
	new file:   goodbye.cpp

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	hello.cpp

$ git add hello.cpp
$ git commit -m "Commit all files"
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
$ git reset --soft HEAD~1
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   c4cs.cpp
	new file:   c4cs.hpp
	new file:   goodbye.cpp
	new file:   hello.cpp

$ git commit -m "Commit all files again"
$ git reset --hard HEAD~1
HEAD is not at 54682b4 Initial Commit
$ git status
On branch master
nothing to commit, working directory clean
$ ls
$
~~~


### `git push`

`git push` pushes the commited changes on your local repository to a remote repository. `remote` is
the url of the repository you are pushing to. `master` is the name of the branch you are pushing to
the repository.

~~~ bash
$ git push origin master
~~~


### `git fetch`, `git merge`, `git pull`

`git fetch` retreives the contents of the remote repository `origin` on branch `other` without
merging it with your current changes. You can checkout the fetched branch, but you will be in a
detached head which limits what you can do on the branch. You can merge your current branch with the
`other` branch by using `git merge other`. This will try to combine the commits in both branches in
chronological order. Issues will emerge if there are conflicting changes in the branches. These
issues must be resolved manually.
Alternatively you can do `git fetch origin other` to `fetch` then `merge` in one command.

~~~ bash
$ git fetch origin other
$ git merge other
~~~

OR

~~~ bash
$ git pull origin other
~~~


### `git rebase`

`git rebase` allows you to replay the changes made on one branch onto another branch. Think of git
as a tree. Initially you have this structure where each node is a commit:

```
          A---B---C other
         /
    D---E---A'---F master
```

Running `git rebase` will replay the changes you made on `other` onto `master` resulting in:

```
                   B'---C' other
                  /
    D---E---A'---F master
```

Notice here that A is skipped. This is because A and A' were both the same changes on both branches.
Rebasing instead of merging should be done when there are merge conflicts in order to maintain a
linear commit history.

During a rebase, conflicts may emerge. You have to resolve these manually. When you are done
resolving conflicts, execute `git rebase --continue` to continue with the rebase. If you do not wish
to resolve conflicts, execute `git rebase --skip`. If you want to abort the rebase process, execute
`git rebase --abort`.

~~~ bash
$ git rebase master other
First, rewinding head to replay your work on top of it...
Applying: change from branch other
Using index info to reconstruct a base tree...
M	hello.cpp
Falling back to patching base and 3-way merge...
Auto-merging hello.cpp
CONFLICT (content): Merge conglict in hello.cpp
Error: failed to merge in the changes.
$ # Fix merge conflicts manually
$ git rebase --continue
$ # Other merge conflict
$ git rebase --skip
$ # Other merge conflict
$ git rebase --abort
~~~


### `git blame`

`git blame` will provide a line by line break down of who made what change in which commit. This is
useful in not only blaming people when a project breaks, but also if you don't understand what a
line of code does, you know who to ask.

~~~ bash
$ git blame hello.cpp
~~~


### `git cherry-pick`

`git cherry-pick` allows you to choose particular commit(s) from one branch and apply them on another.
This will create new commits on the branch to which you are applying the commits. The command below
will apply the 13th to last and 4th to last commits from the branch `other` onto the branch
`master`.

~~~ bash
$ git checkout master
$ git cherry-pick other~12 other~3
~~~
