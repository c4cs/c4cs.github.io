---
permalink: /lectures/w18/python-twitter.html
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

- due Wednesday, 4/18

## Today

- staff lectures

---

# Plan for Today

--

## Use Python to grab and analyze data on a specific hashtag from Twitter

--

### [tweepy](http://www.tweepy.org)

```
$ pip3 install tweepy
```
--

- created specifically to pull data from Twitter

--

- no need to index into large dictionaries or format request URLs

--

### [matplotlib](https://matplotlib.org/2.2.2/index.html)

```
pip3 install matplotlib
```
--

- good for plotting data

--

- "not the best out there, but easy to use" - Amrit

---

class: center, middle

# Let's get started!

---

# Step 1: Starter Code

--

## Have the slides?  Great!  Starter code is [here](https://github.com/stevietriesenberg/eecs398-python-twitter).

## Don't have the slides?  No problem! Go to [https://tinyurl.com/398-pyt](https://tinyurl.com/398-pyt)

--

### `bot.py` contains starter code for the Python program

--

### `secret.py` will hold your API keys and tokens

- you want to keep your API keys secret, which is why they are placed in a separate file from your program.

- if you choose to put your project on GitHub, DO NOT commit `secret.py`

---

# Step 2: Generate Twitter API Keys and Tokens

--

## Go to [https://apps.twitter.com](https://apps.twitter.com)

--

#### NOTE: You will need a Twitter account from this point on.

--

- sign into Twitter, then click "Create New App" in the upper right

--

- fill out the name, description, and website for your applicaiton.  Check the "Developer Agreement" box and finish creating your app!

--

- under the name of your application, find and click the "Keys and Access Tokens" tab

---

# Step 2: Generate Twitter API Keys and Tokens

--

## Consumer Keys

- located under Applicaiton Settings

- copy and paste these keys into `secret.py`

--

## Access Tokens

- scroll down and click "Authorize my Application"

- located under "Your Access Token"

- copy and paste these keys into `secret.py`

---


# Why?

--

class: center, middle
## Verification!

---

# Step 3: Let's get coding!

--

### TODO: import libraries

- `import tweepy`

- `import matplotlib`

- `from secret import *`

---

# Step 4: Twitter

--

### TODO: create a new Twitter session

- check out the tweepy documentation on [getting started](http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html)

- use keys/tokens from `secret.py` to create the session

--

### TODO: user input

- ask the user (you) what hashtag to search

---

# Step 4: Twitter

--

### TODO: search for hashtag

- create new Tweet objects for each result

- we only need the time each tweet was posted, but other data may be useful for debugging or other data analysis

---

# Step 5: Let's graph it!

--

### TODO: graph timestamps from tweets in a histogram

- check out the matplotlib documentation on [histograms](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist) and [subplots](https://matplotlib.org/examples/pylab_examples/subplots_demo.html)

- this is just one analysis you could do on Twitter data

- try something on your own!

---

class: center, middle
## Congratulations!
### You now know how to grab data from Twitter and display it in a meaningful way.

.center[
![:scale_img 30%](https://i.imgur.com/DAAN8yB.jpg)
]
