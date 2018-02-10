---
---

wget
-------
wget stands for "web get". It is a command-line utility which downloads files over a network.

The main advantages of wget are it is free for non-interactive download, meaning that it can work in the background and while the user is not logged on, and it supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies.
<!-- minimal example -->

~~~ bash
$ wget http://example.com/file.iso
~~~

<!--more-->

### Useful Options / Examples
\-\-mirror #turn on mirroring

\-\-adjust-extension #add proper extension to downloaded files

\-\-page-requisites #download css and other required files

\-\-execute robots=off #ignore robots.txt

\-\-wait=30 #wait between fetches and requests

\-\-convert-links #convert links for offline viewing

\-\-user-agent=C4CS #fake the User Agent

#### Example command

~~~ bash
$ wget ‐‐output-document=filename.html example.com
$ wget ‐‐directory-prefix=folder/subfolder example.com
~~~

Download a file but save it locally under a different name

Download a file and save it in a specific folder

#### Example command

~~~ bash
$ wget ‐‐recursive ‐‐no-clobber ‐‐no-parent ‐‐exclude-directories /forums,/support http://example.com
~~~

Download all files from a website but exclude a few directories.

