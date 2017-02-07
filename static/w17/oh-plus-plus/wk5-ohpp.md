`OH++` Git
==============

## reviewing the basics
`git` has __branches__. `master` is the default by convention. Branches are
great to work on a new feature/idea/implementation without worrying about
screwing up your existing code. It allows multiple users (or one user!) to work
on different features all at once, completely independent of one another.

This gets super powerful when working with __remotes__ and __merging__
branches. If you work on, test, and are satisfied with a feature, you can `git
merge` your changes into the `master` branch and remove your feature branch
(`git branch -d feature_branch`).

A "feature branch" is simply a branch created (usually off of `master` i.e.
using `master` as a starting point) for the purpose of developing a specific
feature. Once that feature has been deemed complete, it's usually merged into
`master`, and the feature branch deleted. You might hear of "short lived" and
"long lived" branches. `master` is typically a long-lived branch. That's where
commits go to stay. Feature branches, on the other hand, usually churn quite a
bit as the project gets developed. There's no technical distinction between the
two; they are exactly the same in `git`'s view of the world.

`git` is a __distributed version control system__. What this means is that
everyone who has a copy of the code also has a copy of the repository and state
changes needed to get to that code. No network connection required. That means
your computer, your partner's computer, GitHub (see below), etc. all have
duplicate metadata (`.git` folder).

So, all you're doing when you say `git push` is syncing `.git` folders. Remember
that `git` does not know/care about other people or other repositories _unless
you tell it to_. That means `git push` and `git pull` are your friends.

```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

__Q__: Does this necessarily mean we are up to date with `origin/master`? Nope!
Just up to date relative to the last time we `git fetch`'d.

__Q__: What is this `origin` business? Just like `master`, `origin` is simply a
convention for the first remote in a repository. `git remote --help` will tell
you more.

__Q__: What's the difference between `master` and `origin/master`? `master` is
your local branch `master`. `origin/master` is our local computer's knowledge of
the remote's branch `master`. They don't have to be the same -- you might be
ahead of or behind `origin`.

## `git` vs Git[Hub|Lab]
`git` as a version control system is a subset of the functionality provided by
software companies GitHub and GitLab. GitHub, as one of the largest users of
`git`, has made their own modifications to the software you install on your
machine, and also pushes contributions upstream.

GitHub/GitLab provide (near) feature parity, adding several collaboration
niceties not built into `git` (not a comprehensive list):

- __Forks__ are copies of the main repository. They contain the same data,
  only in a different location (usually your account as opposed to the project
  maintainer's) with different permissions. Why? The project maintainer doesn't
  want everyone to have push access to their repository - that would be quite
  dangerous. So instead, a user can _fork_ their repository, and create a _pull
  request_ upstream.
- __Pull requests__ are requests to merge in a patch (code change) from a user.
  They're wrapped in a nice interface that allows everyone to centrally comment
  and easily collaborate.
- __Issues__ are another way to collaborate on a project
- __Web interface__
- __Desktop apps__ e.g. GitHub Desktop

__Note__: An _upstream_ repository is considered the "main" repository.

## global `.gitignore`
Pesky `.DS_Store` files? `Thumbs.db`? `.swp`? Some of this crap you never want
to commit, regardless of the project. Git provides per-user (as opposed to
per-repository) settings for ignoring files too:

```bash
$ touch ~/.gitignore_global # put things to ignore in here
$ git config --global core.excludesfile ~/.gitignore_global # tell git to ignore them
````

GitHub has a [nice list](https://gist.github.com/octocat/9257657) for your
consideration.

__Note__: I call mine `.gitignore_global` and put it in my home folder. The
second command tells git where to look, put yours wherever is most convenient
for you.

## stash
Git's `stash` is a double edged sword. It can be super useful, but quickly turn
into neverland when you don't `pop` quickly. If you need to save some changes
real fast that you're not quite ready to commit, `git stash` will do the trick
(or maybe `git add . && git stash` if some of those files are untracked. 

Why would you ever need to do this? Maybe to pull in a change from your project
partner without committing nor losing your place. Maybe you want to quickly test
the behavior _without_ the new code you've been writing. There are a number of
everyday use cases.

__TL;DR__ `git stash` is a _stack_ of changesets you can push/pop from distinct
from your staging area, repository, and working directory.

Basic usage:

```bash
$ git status
$ git add . # add any untracked files
$ git status
$ git stash # push onto the stack
$ git status
$ git stash list
$ # do whatever you've gotta do
$ git stash pop # pop off the stack
$ git status
```

Lots of `git status`? Yep. Always `git status`, `git status`, `git status`.

## rebase

### interactive

### non-interactive

## More resources

