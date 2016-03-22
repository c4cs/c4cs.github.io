---
---

wget
-------

`wget` is a tool for downloading files using HTTP, HTTPS, or FTP using the command line.

~~~ bash
$ wget https://c4cs.github.io/hw/c4cs-wk9-advanced.pdf
~~~

<!--more-->

### Useful Options / Examples

#### `wget -O`

The `-O` flag gives the downloaded file the filename specified after the flag.

~~~ bash
$ wget https://c4cs.github.io/hw/c4cs-wk9-advanced.pdf -O adv_hw9.pdf
--2016-03-16 23:49:01--  https://c4cs.github.io/hw/c4cs-wk9-advanced.pdf
Resolving c4cs.github.io (c4cs.github.io)... 23.235.40.133
Connecting to c4cs.github.io (c4cs.github.io)|23.235.40.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 147386 (144K) [application/pdf]
Saving to: ‘adv_hw9.pdf’

100%[=============================================================================================================>] 147,386     --.-K/s   in 0.06s   

2016-03-16 23:49:01 (2.33 MB/s) - ‘adv_hw9.pdf’ saved [147386/147386]


$ ls
adv_hw9.pdf
~~~



#### `wget` a webpage with all content necessary to view it offline

~~~ bash
$ wget --page-requisites --span-hosts --convert-links https://c4cs.github.io/index.html
~~~

#### Break it down

The `--page-requisites` option tells `wget` to fetch all the files necessary to display the webpage offline such as inlined images, stylesheets, and sounds.

Some of the content used on the webpage could be served from a different host. By default, `wget` will not fetch content from hosts other than the one specified in the url. The `--span-hosts` option tells `wget` to fetch the content necessary to view the page even if it is from another host.

The `--convert-links` option helps make local browsing of the webpage reliable, i.e., if the file was not downloaded the link is changed to include the hostname and absolute path to the content and if the file was downloaded the link is converted to a relative link on the local machine. This applies to hyperlinks as well as links to contents such as images.
