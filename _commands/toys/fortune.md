---
---

fortune
-------

`fortune` prints a random saying to standard output

~~~ bash
$ fortune
"Confound these ancestors.... They've stolen our best ideas!"
                -- Ben Jonson
$ fortune -m "you will be happy"
(fortunes)
%
There will be big changes for you but you will be happy.
%
(kids)
%
Remember that as a teenager you are in the last stage of your life when
you will be happy to hear that the phone is for you.
                -- Fran Lebowitz, "Social Studies"
%
~~~

<!--more-->

### Setup

Install the package named fortune or fortune-mod.

Run the command `apt-cache search "^fortunes"` to see what databses you can have and install any that catch your eye. 

### Useful Options / Examples

#### fortune [file] [directory] [all]

The user may specify alternate sayings. You can specify a specific file, a directory which contains one or more files, or the special word all which says to use all the standard databases. The probability of selecting from one of them will be based on their relative sizes in fortunes not raw file size.

As an example, given two databases science and riddles

~~~ bash
$ fortune science riddles
Logic is a systematic method of coming to the wrong conclusion with confidence.
~~~

#### fortune -a, fortune -o
 
The -a flag lets you choose from all lists of maxims, both offensive and not.

The -o flag lets you choose only from potentially offensive aphorisms.  The -o option is ignored if a fortune directory is specified.

Use at your own risk!

No potentially offensive examples here!

#### fortune -c

The -c flag shows the cookie file from which the fortune came.

~~~ bash
$ fortune -c
(kids)%
Anyone who uses the phrase "easy as taking candy from a baby" has never
tried taking candy from a baby.
                -- Robin Hood
~~~

#### fortune -f

The -f flag prints out the list of files which would be searched, but doesn't print a fortune.

~~~ bash
$ fortune -f science riddles
83.00% /usr/share/games/fortunes/science
17.00% /usr/share/games/fortunes/riddles
$ fortune -f
100.00% /usr/share/games/fortunes
     3.06% art
     0.07% ascii-art
     6.91% computers
     7.45% cookie
     0.56% debian
     7.91% definitions
     1.87% disclaimer
     1.37% drugs
     1.33% education
     1.06% ethnic
     1.30% food
     2.83% fortunes
     0.35% goedel
     1.29% humorists
     0.99% kids
     3.55% knghtbrd
     1.35% law
     2.21% linux
     0.68% linuxcookie
     1.72% literature
     0.99% love
     0.20% magic
     0.49% medicine
     3.82% men-women
     4.28% miscellaneous
     0.35% news
     0.47% paradoxum
     8.22% people
     1.79% perl
     0.34% pets
     3.29% platitudes
     4.62% politics
     0.01% pratchett
     0.84% riddles
     4.11% science
     4.73% songs-poems
     0.97% sports
     1.49% startrek
     0.54% tao
     0.08% translate-me
     2.79% wisdom
     4.14% work
     3.60% zippy
~~~

#### fortune -m [pattern], fortune -im [pattern]
The flag -m followed by a pattern prints out all fortunes which match the basic regular expression pattern.  The syntax of these expressions depends on how your system defines re_comp(3) or regcomp(3), but it should nevertheless be similar to the syntax used in grep(1).

The  fortunes  are  output  to standard output, while the names of the file from which each fortune comes are printed to standard error. Either or both can be redirected; if standard output is redirected to a file, the result is a valid  fortunes database file. If standard error is also redirected to this file, the result is still valid, but there will be ``bogus'' fortunes, i.e. the filenames themselves, in parentheses. This can be useful if you wish to remove the gathered matches from their original files, since each filename-record will precede the records from the file it names.

The flag -i when added onto the -m flag tells the -m flag to ignore case for the pattern

~~~ bash
$ fortune -m Macbeth
(definitions)
%
transparent, adj.:
        Being or pertaining to an existing, nontangible object.
        "It's there, but you can't see it"
                -- IBM System/360 announcement, 1964.

virtual, adj.:
        Being or pertaining to a tangible, nonexistent object.
        "I can see it, but it's not there."
                -- Lady Macbeth.
%
fortune -m MacBeth
(songs-poems)
%
Come, you spirits
That tend on mortal thoughts, unsex me here,
And fill me, from the crown to the toe, top-full
Of direst cruelty! make thick my blood,
Stop up the access and passage to remorse
That no compunctious visiting of nature
Shake my fell purpose, not keep peace between
The effect and it! Come to my woman's breasts,
And take my milk for gall, you murdering ministers,
Wherever in your sightless substances
You wait on nature's mischief! Come, thick night,
And pall the in the dunnest smoke of hell,
That my keen knife see not the wound it makes,
Nor heaven peep through the blanket of the dark,
To cry 'Hold, hold!'
                -- Lady MacBeth
%
fortune -im macbeth
(definitions)
%
transparent, adj.:
        Being or pertaining to an existing, nontangible object.
        "It's there, but you can't see it"
                -- IBM System/360 announcement, 1964.

virtual, adj.:
        Being or pertaining to a tangible, nonexistent object.
        "I can see it, but it's not there."
                -- Lady Macbeth.
%
(songs-poems)
%
Come, you spirits
That tend on mortal thoughts, unsex me here,
And fill me, from the crown to the toe, top-full
Of direst cruelty! make thick my blood,
Stop up the access and passage to remorse
That no compunctious visiting of nature
Shake my fell purpose, not keep peace between
The effect and it! Come to my woman's breasts,
And take my milk for gall, you murdering ministers,
Wherever in your sightless substances
You wait on nature's mischief! Come, thick night,
And pall the in the dunnest smoke of hell,
That my keen knife see not the wound it makes,
Nor heaven peep through the blanket of the dark,
To cry 'Hold, hold!'
                -- Lady MacBeth
%
~~~

As you can see without the -i the Macbeth and MacBeth patterns return two differnt fortunes whereas with the -i both are accepted with macbeth

### Extras

#### With Cowsay

A popular method of recieving your fortunes is from a cow by using cowsay.

~~~ bash
$ fortune | cowsay
 ________________________________________
/ If computers take over (which seems to \
| be their natural tendency), it will    |
| serve us right.                        |
|                                        |
\ -- Alistair Cooke                      /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
~~~

#### With Every Time New Terminal Window

To get a fortune with every new terminal window add a fortune command (fortune, fortune -o, etc) to your bash rc file:

go to ~/.bashrc and add the fortune command or even the cowsay fortune combination as a line in the file. 

