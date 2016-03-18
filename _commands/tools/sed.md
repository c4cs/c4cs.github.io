---
---

sed
-------

`sed` is used to make replacements in text files using regular expressions. It searches for regex matches and executes the provided replacement at all instances.

~~~ bash
$ sed <options> string file
~~~

<!--more-->

### Useful Options / Examples

#### Example command

#### `sed 's/find/replace/' filename`

##### Break it down

* Replace the first occurence of the find string in filename with the replace string. 's/' is the substitution command, when at the front of the regex.


#### Example command

#### `sed '/line_pattern/s/find/replace/'`

##### Break it down

* First finds lines matching line_pattern, then does the 's/' substitution once using find and replace only on those matching lines.


#### Example command

#### `sed -i 's/find/replace/g' filename`

##### Break it down

* The -i flag does the substitution in-place.
* The /g regex ending says to do this substitution globally, not just once (ie replace ALL instances of find).


#### Example command

#### `sed -r 's/regex/replace/g' filename`

##### Break it down

* -r flag says to use extended regular expressions rather than basic regexes, ie those that egrep accepts.


#### Example command

#### `sed -e 's/find/replace/' -e 's/find/replace/' filename`

##### Break it down

* -e, when followed by an expression, adds the commands in that expression to the set to be run when the input is processed. This allows you to apply multiple find-replace expressions to a file in one go.


