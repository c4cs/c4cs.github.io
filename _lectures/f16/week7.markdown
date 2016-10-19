---
permalink: /lectures/f16/week7.html
---

class: center, middle

# Git II

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Marcus Darden **
]


---


# Goin' Old School

Lecture this week will use the whiteboard during class.

These slides capture the lecture notes / plan.

We will also post some supplemental material on the [course homepage](https://c4cs.github.io/#schedule)


---

# Create repo

```
            -> 5  with_five
           /
1 -> 2 -> 3       master
 \         \
  \         -> 4  with_four
   \
    \-> 3 -> 4    no_two
```

---

## Branches

1. Create empty repo, add commits 1, 2, 3 and record hashes

2. Check out .git/HEAD
  - What is "HEAD"?

3. `git branch with_four`

4. `git checkout with_four`, add commit 4

5. Explore .git/refs/heads/...
  - What is a branch?


---


## Merging

1. `git checkout master`

2. `git checkout -b with_five`, add commit 5
  - look around

3. `git branch master with_six`, add commit 6
  - look around

4. `git checkout master`

5. `git merge with_four`
  - 'merge' means 'merge into'
  - What does 'fast forward' mean?
  - look around

6. `git merge with_five with_six`
  - Can merge multiple
  - Creates a 'merge commit', why?


---


## Remotes

1. Show how the graph varies based on machine
  - Sync'ing is all about syncing graph objects

2. Open GitLab, explain what it is

3. Push demo to GitLab

4. Pull down a clone

5. Make changes

6. Push up

7. Fetch, then merge

8. Repeat with pull

9. Pushing, pulling, and _tracking_ branches

---


## Rewriting History: Squashing, Rebasing

0. Commit everything. Branch often.

1. Create a feature branch, several commits, squash

2. `git rebase one`, will linearize the 5,6 merge


