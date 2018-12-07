---
permalink: /lectures/f18/python-twitter.html
---

class: center, middle

# Staff Lecture: Python + Twitter

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Slides by Stephanie Triesenberg **
]

---

# Announcements

## Fill out course evaluations!

  - we care a lot about what you think!

  - extra credit for posting screenshot of confirmation page to Canvas

## Today

- staff lectures

---

# Plan for Today

--

## Use Python to build a tree of Tweet replies

  - think "tree" in Linux

  - Python is cool

  - there's a library for (almost) everything

  - don't write code that you don't have to write!

---

# Requirements

--

### [twarc](https://github.com/docnow/twarc)

```
$ pip3 install twarc
```

  - created specifically to pull data from Twitter

  - handles authentication in one line

  - not very well-documented, but it has the reply-searching functionality we're looking for

--

### [anytree](https://anytree.readthedocs.io/en/latest/)

```
pip3 install anytree
```

  - simple and easy to use

  - gives node functionality to any user-defined class

  - builds AND renders trees

---

class: center, middle

# Let's get started!

---

# Step 1: Starter Code

## Go to [https://tinyurl.com/398-tweet](https://tinyurl.com/398-tweet)

--

### <code>bot.py</code> contains starter code for the Python program

### <code>secret.py</code> will hold your API keys and tokens

- you want to keep your API keys secret, which is why they are placed in a separate file from your program.

- if you choose to put your project on GitHub, do NOT commit <code>secret.py</code>!


---

# Step 2: Generate Twitter API Keys and Tokens

--

## Go to [developer.twitter.com](https://developer.twitter.com)

#### NOTE: You will need a Twitter developer account from this point on.

  - sign in then click "Create an app" in the upper right

  - fill out the name, description, website, and intent of your application

  - check the "Developer Agreement" box and finish creating your app


---

# Step 2: Generate Twitter API Keys and Tokens

--

## Consumer Keys

- located under App Details, Keys and Tokens

- copy and paste these keys into <code>secret.py</code>

## Access Tokens

- scroll down and click "Create"

- copy and paste these keys into <code>secret.py</code>

---

class: center, middle
# Let's code!

---

# Step 3: Import Libraries

--

### TODO: import libraries

  - <code>from twarc import Twarc</code>

  - <code>from anytree import NodeMixin, RenderTree</code>

  - <code>from secret import * </code>

---

# Step 4: Twitter

--

### TODO: create a new Twitter session

  - check out the twarc [documentation](https://github.com/DocNow/twarc)

  - use keys/tokens from <code>secret.py</code> to create the session

--

### TODO: user input

  - ask the user (you) what Tweet your app should build a tree for

  - user input is a Tweet ID, which can be found in a Tweet's URL

---

# Step 4: Twitter

--

### TODO: get the user's requested Tweet

  - make twarc do the work for us

  - returns a Python dictionary containing all the Tweet information


---

# Step 5: "Take the Recursive Leap of Faith!"

--

### TODO: implement <code>get_replies()</code>

--

## Getting Twitter replies is difficult...



--

## ...but twarc will do it for us!



--

## ...but twarc's documentation isn't great.


---
# Step 5: "Take the Recursive Leap of Faith!"

--

### TODO: implement <code>get_replies()</code>


  - check out <code>test_twarc.py</code> in the twarc GitHub repo for examples of how to use <code>replies()</code>

  - <code>get_replies()</code> should get the replies of replies of replies of replies, add them as nodes in our tree, and return the root

---
# Step 6: Display the Tree

--

### TODO: call <code>RenderTree()</code>

  - check out anytree's [documentation](https://anytree.readthedocs.io/en/latest/intro.html#basics) for examples of <code>RenderTree()</code>

  - call string function to print Tweet objects

---

class: center, middle
## Congratulations!
### You now know how to connect to the Twitter API with Python and display Tweets in a cool way.
