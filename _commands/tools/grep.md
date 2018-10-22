---
---

grep
---
`grep`  is a linux command that processes text and prints any lines that match a specified pattern. `grep` stands for **G**lobal **R**egular **E**xpression **P**rint.

```bash
$grep [OPTIONS] PATTERN [FILE...]
```

<!--more-->
##Examples
Imagine a file called test.txt:
```
Linux is fun
C4CS is cool
CS is awesome
```
Running grep with the pattern "C4CS" will return the line all lines containg that pattern.
```bash
$grep C4CS test.txt
C4CS is cool
```

## Regular Expressions
The real power of grep comes from its ability to use regular expressions as a pattern. For the folowing examples consider a dictionary called dict.txt.
###Bracket Expressions
A bracket expression is a list of characters enclosed by [ and ]. A bracket expression will  match any single character in the list.
```bash
$grep c[aou]t dict.txt
cat
cot
cut
```
bracket expressions can also be used with a hypen to match a range. [a-e] is equivlent to [abcde]. And [0-9] is equivlent to [0123456789].
###Negating a Bracket Expression
A carat (^) at the begining of a bracketed expression will match characters not in the list.
```bash
$grep c[^u]t dict.txt
cat
cot
```
###Anchoring
The ^ symbol is used to match at the begining of the string. The $ symbol is used to match at the end of the string.
```bash
$grep t dict.txt
# returns all words containing an 't'
$grep ^t dict.txt
# returns all words begining with 't'
$grep t$ dict.txt
# returns all words ending in 't'
###Wildcard
The . symbol is used as a wildcard. It can match any single character.
```bash
$grep .oat dict.txt
boat
coat
goat
moat
```
###Repetition
The ?  symbol means the preceding item may be matched zero or one times. ab?c matches both "ac" and "abc".
The * symbol means the preceding item may be matched zero or more times. ab*c mathces "ac", "abc", "abbc", and so on.
The + symbol means the preceding item may be matched one or more times. ab+c matches "abc", "abbc", "abbbc", and so on.
{n} means the preceding item is matched exactly n times. a{5} matches "aaaaa".
{n,} means the preceding item is matched n or more times. a{3,} matches "aaa", "aaaa", and so on.
{,n} means the preceding item is matched at most n times. a{,3} matches "","a","aa","aaa".
{n,m} means the preceding item is matched at least n times and at most m times. a{1,3} matches "a","aa","aaa".

##grep Options

###-i, --ignore-case
Uses case insesitive matching for the PATTERN.
###-v, --invert-match
Prints lines that do not match the PATTERN.
###-c, --count
Does not print matching lines, instead prints the number of matching lines.
Can be used in combination with -v as -cv to print the number of non-matching lines.
###-q, --quiet, --silent
Do not print anything. Exit 0 if any match is found, even if there is an error.
###-H, --with-filename
Print the filename for eaach match. This option is default when provided with more than one file.
###-h, --no-filename
Suppress output of file names. This is default when provided with only one file to search
###-n, --line-number
Prefix each line of output with the 1-based line number within its file.
###-R, -r, --recursive
Read all files under a directory
