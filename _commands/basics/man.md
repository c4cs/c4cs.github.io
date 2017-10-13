---
---

man
--
`man` provides *manual pages* for terminal commands

<!-- minimal example -->
~~~ bash
$ man git
q // to quit
~~~

<!--more-->

### Useful Options / Examples

#### `man -f <command>` shows a list of related commands that match the <command> keyword
~~~ bash
$ man -f git
perlgit(1)               - Detailed information about git and the Perl repository
git(1)                   - the stupid content tracker
git-add(1)               - Add file contents to the index
git-am(1)                - Apply a series of patches from a mailbox
git-annotate(1)          - Annotate file lines with commit information
git-apply(1)             - Apply a patch to files and/or to the index
git-archimport(1)        - Import an Arch repository into Git
git-archive(1)           - Create an archive of files from a named tree
git-bisect(1)            - Use binary search to find the commit that introduced a bug
...
~~~

##### Break it down
