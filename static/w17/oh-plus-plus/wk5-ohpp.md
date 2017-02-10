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

`git rebase` is a very powerful, and sometimes a very confusing tool. However,
understanding this built in command can lead to very clean git histories as
well as easily revertible commits. As we saw in the examples above, usually
when you're done working on a branch, you will `git merge` it back into
`master`. This results in a "merge commit". This workflow is very common, and
not necessarily a bad idea, however if there are many times that feature
branches are being merged into a master branch, the git history can look a bit
hectic. Many open-source projects have contributor notes specifying what the
requirements are when adding code to the main repository, and rebasing will
likely be a part of that workflow.

A small side note, yet something that has a lot of bang for your buck, is
understanding what `git pull` does. What happens under the hood is that git runs
 `git fetch` and then `git merge FETCH_HEAD`. Sometimes, as a result of this, we
 can get merge commits. This can further clutter the git history. If you want
 `git pull` to default to performing a rebase, you can type `git pull --rebase`.
 Or if you wish to set that as your default, you can run `git config --global
 pull.rebase true`.

### Example workflow using `git merge` vs. `git rebase`

When working on a project and using `git merge` you may have a history such as:

```
Most recent in time

 H   <--- This is the merge commit which comes from running 'git merge feature'
 |\
 E G  <-- Add some commits that aren't on master
 | |
 D F  <-- First commit on a branch named 'feature'
 |/
 C
 |
 B
 |
 A

Oldest in time
```


If you want to see what this looks like happening tens of times in a short
amount of time, clone the websites' repository and look through the history
using this git command:

`git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset
 %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit`


__Protip__: alias the above command to `gl` to be able to use that to quickly get a
sense of a project's history.

`alias gl='git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset
%s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit'`


Now what would the history look like if we rebase instead of merging? This is
what the history will look like just before we run `git rebase master` when
we're on the feature branch.

```
Most recent

 E G  <-- Add some commits that aren't on master
 | |
 D F  <-- First commit on a branch named 'feature'
 |/
 C
 |
 B
 |
 A

Oldest
```

After running `git rebase master` when we're on the feature branch,
we will end up with this:

```
Most recent

   G'
   |
   F' <-- Our first commit on the feature branch
  /
 E    <-- Last commit on master
 |
 D
 |
 C
 |
 B
 |
 A

Oldest
```

What rebasing does is re-apply any commits you made in your feature branch, on top of the `HEAD` of
master. It also generates new commit hashes for them, but otherwise the commits
are nearly identical (this is why there is a quote next to the F and G commits,
since they are technically different to git, but really the same to you).
When you run this command you will still get merge __conflicts__, but not merge
__commits__.

At this point, you may be saying, "Well, our work still isn't in the master
branch, so what do we do?" Well, we can `git merge feature` when we're on
the master branch. This will now perform what is called a 'fast-forward' merge,
because all of the history on master is already accounted for in the feature
branch, so no merge commit will be created.

Our history now looks like this:

```
Most recent

 G' <-- Master and feature branch are both here now
 |
 F'
 |
 E
 |
 D
 |
 C
 |
 B
 |
 A

Oldest
```

What a beautiful, linear history! Now if you're done developing on the feature
branch, you can delete it with `git branch -D feature`, and be on your way.


### interactive

Looking at the last example, we see that both the commits `F` and `G` were
re-applied onto `master` from our `feature` branch. However, what if everyone
else who saw our feature didn't need to know about both `F` and `G` commits, but
maybe just one commit saying the entire feature was done? This is where
interactive rebasing comes in!


Interactive rebasing can help you do several things, however, the one we will be
talking about here is what is referred to as "squashing commits" together to
make one commit.

Interactive rebasing is invoked with `git rebase --interactive <commit>` or `git rebase
-i <commit>` on the command line. The point in time that running `git rebase -i` takes
place is just before we want to merge our feature branch into master. Because
this involves opening a text editor to modify the commits, it is difficult to
show exactly how to do this through here. However, a good example can be found
[here](https://robots.thoughtbot.com/git-interactive-rebase-squash-amend-rewriting-history#squash-commits-together).


## More resources

To learn about the power of rebasing in general, I do suggest reading [this
article](https://robots.thoughtbot.com/git-interactive-rebase-squash-amend-rewriting-history#squash-commits-together).
It highlight several of the common use cases and goes through each one with an
example.


