---
permalink: /lectures/f16/week2.html
---

class: center, middle

# Git
## (and some other stuff)

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden **
]

---

# Recapping last week

## Any lingering administrative issues?

--

<hr />

## The readings

 - Biculturalism

 - Command-line "bullshittery"

???
 - Goal: Press insight that "neither is better"\
 - Goal: Failure / frustration in this class is not a reflection of you or your\
         abilities. Don't let frustration be an impediment to your CS career\

---

# What's version control?

--

## Why is it important?

## And how might we build a version control system?

--

## Why doesn't everyone use version control for everything?

???
  - Code is semi-independent lines of text, very easy to version

  - Other text?
    -- Many authors and editors too; many books written in latex
    -- What about Microsoft Word's track changes?
       --- Tie back to readings from week 1; easy to use, limited in power

  - Non-text?
    -- Hard, what's a "merge" of a picture, a CAD drawing?
    -- Many startups are trying to crack this nut

---

# Git-ing started (I'm so sorry)

 - first — `init`

 - making commits — `add`, `commit`

 - viewing work/history — `status`, `log`

--

## Let's peek under the hood

 - History is a linked list

 - What's `master`, `HEAD`?

 - Where's the old versions?

--

## I'm lazy, let's make `git st` == `git status`

 - `git config --global --edit`
.small-75[
- (Fancy way of saying `editor ~/.gitconfig`)

- (Fancy way of saying `editor /home/ppannuto/.gitconfig`)

- (Fancy way of saying `[nano/vim/emacs/...] /home/ppannuto/.gitconfig`)
]

```
[alias]
  st = status
```

???

master is a branch like any other, and just a name _nothing special to git_
                                                  _special to users by convention_

HEAD is an alias for what is currently "checked out", the files that you
see on disk at this moment

where are the others?
   - .git/objects

Check out .git/HEAD while we're here


---

# Using git locally

.center[
![Diagram of git operations](img/git_triangle-local.svg)
]

---

# Collaborating with git

## First, we have to talk just a little about branches

--

<hr />

![Diagram of git operations with remote server](img/git_triangle.svg)

---

# Why is git cool?

### Let's debug a real-world problem

[Phony](https://github.com/floere/phony) is a  `ruby` library for
pretty-printing phone numbers. It's used by a bunch of websites (AirBnB,
ZenDesk, etc)

1. `git clone https://github.com/floere/phony`

```bash
    # US phone number
    ruby -e 'require "./lib/phony"' -e 'puts Phony.format("17345551212")'
    + 1 (734) 555-1212
    # French phone number
    ruby -e 'require "./lib/phony"' -e 'puts Phony.format("33123456789")'
    +33 1 23 45 67 89
    # Emergency phone number in the UK
    ruby -e 'require "./lib/phony"' -e 'puts Phony.format("999")'
```

.footnote[
Example borrowed from http://www.paulboxley.com/blog/2015/01/a-simple-example-of-git-bisect-run-with-ruby
]

---

```bash
    ruby -e 'require "./lib/phony"' -e 'puts Phony.format("999")'
```

- Go back in time to when you know it worked

   - `git checkout v1.9.0`

--

- Search history for the problem

--

   - The `git bisect` command will help keep track of progress
   - `git bisect start`
   - `git bisect good`
   - `git checkout master`
   - `git describe`
   - `git bisect bad`
   - (magic)
   - `git describe`

--

- But I'm _still_ lazy

--

   - `git bisect run ruby -e 'require "./lib/phony"' -e 'puts Phony.normalize("+999")'`

--

- So what changed?

   - `git log -p` — or — <a href="https://github.com/floere/phony/commit/9b4234a5024780f3b781b9a68e9c12104dea9c94">github.com/floere/phony/commit/9b4234....</a>
   - https://github.com/floere/phony/issues/219

---

# Closing remarks

## **You must use git for something non-trivial this term**

 - You _should_ use version control for all your class projects

    - And I don't mean folder-copying

       - _(I'm looking at you, freshman-year Pat)_

 - Not in any programming classes?

    - Try using it for other homework

 - Deadline for this is Week 7 — Git II (Oct 19/21)

