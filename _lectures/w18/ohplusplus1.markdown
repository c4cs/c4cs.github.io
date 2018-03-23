---
permalink: /lectures/w18/ohplusplus1.html
---

class: center, middle

# Office Hours ++ (Git II)

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Slides by Tarun Khubchandani **
]


---

# Open Source Projects

--

## Examples?

--

### Programming Languages/Frameworks
  - [Rust](https://github.com/rust-lang/rust)
  - [Swift](https://github.com/apple/swift)
  - [React Native](https://github.com/facebook/react-native)

--

### Package Managers
  - [Homebrew](https://github.com/Homebrew/legacy-homebrew)

--

### Utilities
  - [Tensorflow](https://github.com/tensorflow/tensorflow)

--

### Websites
  - [C4CS](https://github.com/c4cs/c4cs.github.io)

---

class: center, middle

# Think Bigger...

--

# [Linux](https://github.com/torvalds/linux)

![LinuxGithub](img/LinuxGithub.png)

---

# Okay... but really, what is it?

--

## Software with source code made available to public
  - Generally with a specific license

--

## Commonly associated with community driven development (enter Git)

- Git allows for easy collaboration
- Version control and release handling

--

## Allows customization of applications for wider usage

---

# Cool. Why should I contribute?

--

## Community Driven Development helps everyone using a piece of software
  - Build something that's useful to others
  - Suggest ideas for useful features

--

## Personal Benefits

  - Learn new skills
  - Community recognition
  - (Looks great on your resume!)

--

## It's Fun!
### There's a project for pretty much [everything](https://github.com/NARKOZ/hacker-scripts)

---

class: center, middle
# Enough talking.
# Let's do something cool.

---

# How to contribute

### 1.  [Fork](https://help.github.com/articles/fork-a-repo/) the repository you want to contribute to
<img alt="fork" width="600" src="https://github-images.s3.amazonaws.com/help/bootcamp/Bootcamp-Fork.png" />

---

# How to contribute

### 1.  [Fork](https://help.github.com/articles/fork-a-repo/) the repository you want to contribute to

### 2. [Clone](https://help.github.com/articles/cloning-a-repository/) your forked repository
 Use either HTTPS or SSH [remote URL](https://help.github.com/articles/which-remote-url-should-i-use/)
<img alt="clone" width="600" src="https://help.github.com/assets/images/help/repository/remotes-url.png" />

---

# How to contribute

### 1.  [Fork](https://help.github.com/articles/fork-a-repo/) the repository you want to contribute to

### 2. [Clone](https://help.github.com/articles/cloning-a-repository/) your forked repository

### 3. [Create an issue](https://help.github.com/articles/creating-an-issue/)/take ownership of an existing issue
Do this in the parent repository, not your fork
<img alt="issue" width="600" src="https://help.github.com/assets/images/help/repository/repo-tabs-issues.png" />

---

# How to contribute

### 1.  [Fork](https://help.github.com/articles/fork-a-repo/) the repository you want to contribute to

### 2. [Clone](https://help.github.com/articles/cloning-a-repository/) your forked repository

### 3. [Create an issue](https://help.github.com/articles/creating-an-issue/)/take ownership of an existing issue

### 4. Create a branch locally and setup environment
In the directory of your local repository:
```sh
$ git checkout -b <feature-name>
```
Then follow setup instructions in the `README.md`

---

# How to contribute

### 1.  [Fork](https://help.github.com/articles/fork-a-repo/) the repository you want to contribute to

### 2. [Clone](https://help.github.com/articles/cloning-a-repository/) your forked repository

### 3. [Create an issue](https://help.github.com/articles/creating-an-issue/)/take ownership of an existing issue

### 4. Create a branch locally and setup environment

### 5. Do cool stuff. Make some commits.

--

### 6. Push your changes to your remote
```sh
$ git status
$ git add <files>
$ git commit -m "<Descriptive commit message>"
$ git push --set-upstream origin <feature-name>
```

---

# How to contribute

### 1.  [Fork](https://help.github.com/articles/fork-a-repo/) the repository you want to contribute to

### 2. [Clone](https://help.github.com/articles/cloning-a-repository/) your forked repository

### 3. [Create an issue](https://help.github.com/articles/creating-an-issue/)/take ownership of an existing issue

### 4. Create a branch locally and setup environment

### 5. Do cool stuff. Make some commits.

### 6. Push your changes to your remote

### 7. Create a [Pull Request](https://help.github.com/articles/creating-a-pull-request/) from your [fork](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)

(We'll walk through this one)

---

class: center, middle
## Congratulations!
###You've just joined the open source community
<img alt="congratulations" src="http://m.memegen.com/12vgnp.jpg" />

---

# I'm lost, what just happened?

## What We Did:
  - Built a new feature on a software shipped to hundreds of people
  - Worked collaboratively on an international project
  - (Hopefully) Learned something new

--

## Stop Speaking Greek to me
Don't worry, most Git users don't really know what's going on when they're using Git. If you're looking to brush up, the following resources may be helpful:
- [Understanding the Github Flow](https://guides.github.com/introduction/flow/)
- [Learn Enough Git to Be Dangerous](https://www.learnenough.com/git-tutorial)
