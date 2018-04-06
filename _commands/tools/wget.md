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
* \-\-mirror
	<br/> #Turns on mirroring, i.e. it makes the download recursive to get a mirror of the desired web page.

* \-\-adjust-extension 
	<br/> #Adds proper extensions to downloaded files (such as html or css) depending on their content type.

* \-\-page-requisites 
	<br/> #Downloads css style sheet, images and other required files to properly display the page offline.

* \-\-execute robots=off 
	<br/>  #Ignores robots.txt.

* \-\-convert-links 
	<br/>  #Converts all the links to relative for offline viewing.

#### Example command 1

~~~ bash
$ wget ‐‐output-document=filename.html example.com
~~~

The command above downloads a file and saves it locally under a different name.

#### Example command 2

~~~ bash
$ wget ‐‐directory-prefix=folder/subfolder example.com
~~~

The command above downloads a file and saves it in a specific folder.

#### Example command 3

~~~ bash
$ wget ‐‐recursive ‐‐no-clobber ‐‐no-parent ‐‐exclude-directories /forums,/support http://example.com
~~~

The command above downloads all files from a website but excludes a few directories. Note that \-\-no-clobber suppresses wget from redownloading the same files and \-\-no-parent guarantees that wget never leaves the exisiting hierarchy.

#### Example command 4

~~~ bash
$ wget ‐‐input list-of-file-urls.txt
~~~

The command above downloads files from multiple URLs with wget. The user only needs to put the list of URLs in another text file on separate lines and pass it to wget.

#### Example command 5

~~~ bash
$ wget --mirror --convert-links --adjust-extension --page-requisites http://example.org
~~~

The command above creates an offline copy of a site that you can take and view without internet access utilizing the command flags in the useful option section above.
