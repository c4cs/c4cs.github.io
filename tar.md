COMMAND
-------

Package files into a compressed archive file

~~~ bash
tar -czf archive.tar.gz main.cpp lib.h lib2.h
# archive.tar.gz is created in the current dir with the target files
~~~

<!--more-->

### Useful Options / Examples
Useful Flags:
- x = extract specified file
- c = create a new archive (tar thing) containing the specified items
- t = list contents of archive to stdout
- f = first argument after this flag is the name of the tar file
- v = verbose output
- z = (use only with c-mode) compress the archive with gzip

Useful Examples:
##### Package up your test cases:
	tar -vczf test-cases.tar.gz test-1.txt test-2.txt test-3.txt <...>
##### Unpackaging someone else's test cases:
	tar -xvf test-cases.tar
##### Extact a single file (main.cpp) from a tarball
	tar --extract --file=tarball.tar.gz main.cpp
##### or multiple files (main.cpp, main.h):
	tar --extract --file=tarball.bz2 "main.cpp" "main.h"
##### or with wildcards:
	tar -xvf archive.tar --wildcards "*.cpp"
	tar -zxvf archive.tar.gz --wildcards "*.cpp"
	tar -jxvf archive.tar.bz2 -- wildcards "*.cpp"

#### Example command
	tar -vcjf test-cases.tar.bz2 test*.txt

output (al of the files added to the archive):
    a test-1.txt
    a test-2.txt
    a test-3.txt
    <output will continue with same pattern>

##### Break it down
1. "tar"
    invoke the tar command
2.  "-vcjf"
    these are the flags that are passed to the tar command
    v means verbose output: tar will print a list of all the files it adds to the archive as it compresses them
    c (create) specifies that we want to create a tarball
    j speifies that we want the encoding of the tar ball to be ".tar.gz" (bzip)
    f tells tar that the next argument immediately after this will be the name of where to write the archive
3. "test-cases.tar.bz2 test\*.txt"
    "test-cases.tar.bz2" is the name of where the archive will be written
    test\*.txt is a regular expression intrepreted by bash/zsh/fsh/etc. that selects all of the files in the directory that start with "test" and end with ".txt"

#### Example command
    tar -xzvf archive.tar.gz

output (all of the files extracted from the archive):
    x file1.cpp
    x file2.h
    x file3.txt
    x ...
##### Break it down
1.  tar:
    invoke the "tar" command
2. "-xzvf"
    x tells tar that we want to extract files from an archive
    z tells tar that the type of the archive is tar.gz
    v (verbose) tells tar that we want it to print a list of files that it extracts after it extracts each one
    f specifies that the following argument will be the name of the archive to extract from
