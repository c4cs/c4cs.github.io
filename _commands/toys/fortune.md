---
---

fortune
-------
`fortune` displays pseudorandom messages similar to those found in fortune cookies

To use `fortune`, type:

<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ sudo apt install fortune-mod
$ fortune
~~~

<!--more-->

### Useful Options
~~~ bash
 Usage: fortune -[aefilosw] [-m [pattern]] [-n [length]]
 -a: Use all databases, regardless of whether they may be "offensive"
 -e: Make the probability of choosing a fortune file equal for all files
 -f: Print list of all fortune files considered
 -i: When used with -m make the regex search case-insensitive
 -l: Use only quotations longer than length specified with -n, or 160 characters if -n is not used
 -m [pattern]: Print all fortunes matching the regex in [pattern]
 -n [length]: Override length used by -l and -s to determine long and short messages
 -o: Choose only from "offensive" databases
 -s: Use only quotations shorter than the length specified with -n or 160 characters if -n is not used
 -w: Wait for a period of time before terminating
~~~

#### Example command
~~~ bash
  $ fortune -l        // fortune longer than 160 characters
  $ fortune -s -n 100 // fortune shorter than 100 characters
  $ fortune -o        // offensive fortune
  $ fortune -f        // list of fortune files considered
~~~

#### Example output
~~~ bash
  $ fortune
  Familiarity breeds contempt -- and children
                    -- Mark Twain

  $ fortune
  Good news. Ten weeks from Friday will be a pretty good day

  $ fortune
  You will pioneer the first Martian colony

~~~
