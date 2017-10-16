---
---

man
--
`man` provides *manual pages* for terminal commands

<!-- minimal example -->
~~~ bash
$ man git
# displays git man page
q # to quit
~~~

<!--more-->

### Useful Options / Examples

`man -f <command>` shows a list of related commands that match the <command> keyword

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

#### Manual sections

The numbers in parentheses next to the commands correspond to the manual section they are in:

The standard sections of the manual include:

    1      User Commands
    2      System Calls
    3      C Library Functions
    4      Devices and Special Files
    5      File Formats and Conventions
    6      Games et. al.
    7      Miscellanea
    8      System Administration tools and Daemons

e.g. `man -f printf` lists `printf(1)`, and `printf(3)`:

~~~ bash
$ man 1 printf
# displays printf (as a command) man page
q
$ man 3 printf
# displays printf (as a stdlib fn) man page
q
~~~

#### Sections within a manual page:
    NAME             Name of manual page
    SYNOPSIS         A brief summary of the command or function's interface
    CONFIGURATION    Configuration details for a device [Normally only in Section 4]
    DESCRIPTION      An explanation of what the program, function, or format does
    OPTIONS          [Normally only in Sections 1, 8]
    EXIT STATUS      [Normally only in Sections 1, 8]
    RETURN VALUE     [Normally only in Sections 2, 3]
    ERRORS           [Typically only in Sections 2, 3]
    ENVIRONMENT
    FILES
    VERSIONS         [Normally only in Sections 2, 3]
    ATTRIBUTES       [Normally only in Sections 2, 3]
    CONFORMING TO
    NOTES
    BUGS
    EXAMPLE
    SEE ALSO

#### Man pages reference

~~~ bash
$ man man
# displays the man pages for man
q
$ man man-pages
# displays information of manual sections and descriptions
q
~~~
