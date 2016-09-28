---
---

t
-------

`t` lets you interface with Twitter from the command line.

~~~ bash
$ t update "tweet tweet"
$ t stream timeline -l
~~~

<!--more-->

t is a command line utility (CLI) for interacting with Twitter.
t is not typically bundled with an OS and thus requires installation. In order to install t you must already have Ruby installed. t requires a Twitter API token for each authorized user account.

t capitalises on the ability to string UNIX commands, vastly increasing its usefulness. (xargs may be required)

Full documentation on t is available on [the project's GitHub page.](https://github.com/sferik/t)

t is compatabile with Linux, OS X, and Windows

### Installation

#### Verify that Ruby is installed
t depends on Ruby. Check that its installed on your system.

~~~ bash
$ ruby -v
~~~

#### Install t
Run the following to install t.

~~~ bash
$ sudo gem install t
~~~

Note: this may take several minutes to finish and may provide no feedback.

#### Configure Twitter API Settings
In your terminal type the following, followed by 'enter'.

~~~ bash
$ t authorize
~~~

This will direct you to [apps.twitter.com](https://apps.twitter.com). Click "Create New App" and fill out the required fields. On the confirmation page click "modify app permissions". Change permissions to "Read, Write, and Access direct messages"

(Congratulations -- you're a Twitter Developer!)

#### Authorize t
Switch back to your terminal where t is waiting. Copy and paste your new API key and API secret from your web browser when prompted by t. Finish authorization with a tap of 'ye old 'enter'.

t will redirect you to the Twitter app authentication page. Input your credentials and click "Authorize App". Copy the resulting PIN number back into your terminal where t is prompting for it. You'll be greeted with an "Authorization successful" message.

### Using t

#### Help command

Information on t is available through its help command.

~~~ bash
$ t help
Commands:
  t accounts                          # List accounts
  t authorize                         # Allows an application to request user authorization
  t block USER [USER...]              # Block users.
  t delete SUBCOMMAND ...ARGS         # Delete Tweets, Direct Messages, etc.
  t direct_messages                   # Returns the 20 most recent Direct 
...

Options:
  -C, [--color=COLOR]   # Control how color is used in output
                        # Default: auto
                        # Possible values: icon, auto, never
  -P, [--profile=FILE]  # Path to RC file
                        # Default: /home/alexander/.trc
~~~

You can also get help for any specific t command.

~~~ bash
$ t help stream
Commands:
  t stream all                          # Stream a random sample of all Tweets (Control-C to stop)
  t stream help [COMMAND]               # Describe subcommands or one specific subcommand
  t stream list [USER/]LIST             # Stream a timeline for members of the specified list (Control-C...
...
~~~


#### Posting tweets and DMs
Post a tweet from the terminal.

~~~ bash
$ t update "Tweet tweet"
~~~

Tweet at a user.

~~~ bash
$ t update "@chezbetty When will Soylent be back in stock? Bundaberg?" 
~~~

Send an ROT13 encoded direct message.
Note: stringing commands together makes t *really powerful*. (And, in this case, *really confusing* to T Swizzle.)

~~~ bash
$ alias rot13="tr '[A-Za-z]' '[N-ZA-Mn-za-m]'"
$ echo "You belong with me" | rot13 | xargs -0 t dm @SwitfOnSecurity
~~~



#### See what's happening in your world
Print the 20 most recent tweets on your timeline.

~~~ bash
$ t timeline
~~~

Variation: Print a variable number of tweets from your timeline.

~~~ bash
$ t timeline -n 5
~~~

Stream your timeline in realtime. Type ^C to exit.

~~~ bash 
$ t stream timeline
~~~

Variation: Default streaming looks pretty but isn't very illuminating. Streaming in long mode shows much more info. Let's order it by the newest user to 

~~~ bash
$ t stream timeline -l
~~~

See what's trending in the Ann Arbor area. [(Uses the Ann Arbor WOEID)](http://woeid.rosselliot.co.nz/lookup/ann%20arbor)

~~~ bash
$ t trends 2354842
~~~

#### Random Power

Favorite the most recent tweet by What-If Numbers.

~~~ bash
$ t timeline @whatifnumbers -n 1 -l | awk '{print $1}' | xargs t favorite
~~~

Block a user.

~~~ bash
$ t block @JimmyFallon
~~~

Report a user for posting spam. (Yo Twitter, what is this 'Moments' thing and how do I get rid of it?)

~~~ bash
$ t report_spam @Twitter
~~~

Needs moar [`cowsay`](/commands/cowsay)

~~~ bash
$ t timeline @swiftonsecurity -n 1 | cowsay
 _______________________________________
/  @SwiftOnSecurity                     \
|                                       |
| Using Twitter has taught me to        |
| livetweet my problems over team email |
\ and my coworkers are getting mad      /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
~~~

### Appendix: Top-level t commands

~~~ bash
$ t accounts                          # List accounts
$ t authorize                         # Allows an application to request user authorization
$ t block USER [USER...]              # Block users.
$ t delete SUBCOMMAND ...ARGS         # Delete Tweets, Direct Messages, etc.
$ t direct_messages                   # Returns the 20 most recent Direct Messages sent to you.
$ t direct_messages_sent              # Returns the 20 most recent Direct Messages you've sent.
$ t dm USER MESSAGE                   # Sends that person a Direct Message.
$ t does_contain [USER/]LIST USER     # Find out whether a list contains a user.
$ t does_follow USER [USER]           # Find out whether one user follows another.
$ t favorite TWEET_ID [TWEET_ID...]   # Marks Tweets as favorites.
$ t favorites [USER]                  # Returns the 20 most recent Tweets you favorited.
$ t follow USER [USER...]             # Allows you to start following users.
$ t followers [USER]                  # Returns a list of the people who follow you on Twitter.
$ t followings [USER]                 # Returns a list of the people you follow on Twitter.
$ t followings_following USER [USER]  # Displays your friends who follow the specified user.
$ t friends [USER]                    # Returns the list of people who you follow and follow you back.
$ t groupies [USER]                   # Returns the list of people who follow you but you don't follow back.
$ t help [COMMAND]                    # Describe available commands or one specific command
$ t intersection USER [USER...]       # Displays the intersection of users followed by the specified users.
$ t leaders [USER]                    # Returns the list of people who you follow but don't follow you back.
$ t list SUBCOMMAND ...ARGS           # Do various things with lists.
$ t lists [USER]                      # Returns the lists created by a user.
$ t matrix                            # Unfortunately, no one can be told what the Matrix is. You have to see it for yourself.
$ t mentions                          # Returns the 20 most recent Tweets mentioning you.
$ t mute USER [USER...]               # Mute users.
$ t muted [USER]                      # Returns a list of the people you have muted on Twitter.
$ t open USER                         # Opens that user's profile in a web browser.
$ t reach TWEET_ID                    # Shows the maximum number of people who may have seen the specified tweet in their timeline.
$ t reply TWEET_ID [MESSAGE]          # Post your Tweet as a reply directed at another person.
$ t report_spam USER [USER...]        # Report users for spam.
$ t retweet TWEET_ID [TWEET_ID...]    # Sends Tweets to your followers.
$ t retweets [USER]                   # Returns the 20 most recent Retweets by a user.
$ t retweets_of_me                    # Returns the 20 most recent Tweets of the authenticated user that have been retweeted by others.
$ t ruler                             # Prints a 140-character ruler
$ t search SUBCOMMAND ...ARGS         # Search through Tweets.
$ t set SUBCOMMAND ...ARGS            # Change various account settings.
$ t status TWEET_ID                   # Retrieves detailed information about a Tweet.
$ t stream SUBCOMMAND ...ARGS         # Commands for streaming Tweets.
$ t timeline [USER]                   # Returns the 20 most recent Tweets posted by a user.
$ t trend_locations                   # Returns the locations for which Twitter has trending topic information.
$ t trends [WOEID]                    # Returns the top 10 trending topics.
$ t unfollow USER [USER...]           # Allows you to stop following users.
$ t update [MESSAGE]                  # Post a Tweet.
$ t users USER [USER...]              # Returns a list of users you specify.
$ t version                           # Show version.
$ t whoami                            # Retrieves profile information for the authenticated user.
$ t whois USER                        # Retrieves profile information for the user.
~~~
