---
---
gzip
-------
gzip is a tool to compress and decompress files. It operates using  Lempel-Ziv coding (LZ77).
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
gzip [ -acdfhklLnNrtvV19 ] [--rsyncable] [-S suffix] [ name ... ]
~~~

<!--more-->

### Useful Options / Examples

#### gzip filename

##### Compresses filename and deletes original file

#### gzip -k filename

##### Compresses filename and does NOT delete original file

#### gzip -d filename

##### Uncompresses filename

#### gzip -l filename

##### Lists details concerning the compressed file filename

#### gzip -4 filename

##### This flag allows us to regulate the speed of compression. Any number between 1 and 9 may be chosen, 1 being the fastest compression and 9 being the slowest.
