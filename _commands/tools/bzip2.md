---
---

bzip2
-------
<!--TODO: Add documentation for this command by submitting a pull request.-->
<!-- one line explanation would go here -->
`bzip2` is the command used for compressing and decompressing files.

<!-- minimal example -->
~~~ bash
$ bzip2 filename
~~~


<!--more-->

### Useful Options / Examples

#### `bzip2`

~~~bash
$ bzip2 [Option(s)] filename(s)
~~~

Options include:

1. `-v` for verbose: provide confirmation and degree to which the data is compressed
2. `-s` for small: reduce the memory usage for compression
3. `-d` for decompress: decompress the specified file
4. `-c` for stdout: compress or decompress to standard output
5. `-z` for compress: the complement to -d: forces compression, regardless of the invokation name
6. `-t` for test: check integrity of the specified file(s), but don't decompress them, really performs a trial decompression and throws away the result
7. `-f` for force: force overwrite of output files (normally, bzip2 will not overwrite existing output file), also forces bzip2 to break hard links to files, which it otherwise wouldn't do
8. `-k` for keep: keep (don't delete) input files during compression or decompression
9. `-q` for quiet: suppress non-essential warning messages. Messages pertaining to I/O errors and other critical events will not be suppressed
10. `-L` for license: display the software version, license terms and conditions
11. `-V` for version: the same as license, display the software version, license terms and conditions

----

#### `bzip2 file1 file2 file3`

~~~bash
$ bzip2 file1 file2 file3
~~~

Compress multiple files (file1 file2 and file3, in this case) in the "zip" format at the same time. Each file is replaced by a compressed version of itself, with the extension .bz2 appended to its name. Thus, in the case of the above example, the three input files would be replaced by files named file1.bz2, file2.bz2 and file3.bz2. This can be easily confirmed with the ls (i.e., list) command, and the sizes of the new files can be viewed by using ls together with its -s (i.e., size) option. The original files can be retained by using the -k (i.e., keep) option.

----
