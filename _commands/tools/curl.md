---
---
curl
-------
`curl` transfers data to/from a server, using one of the supported protocols. The supported protocols include DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
$ curl http://www.google.com
~~~

<!--more-->

### Useful Options / Examples

#### `curl -o filename url`

Saves the curl command to the given filename

~~~ bash
$ curl -o test.html http://www.google.com
~~~
This saves the content to test.html


#### `curl -O url1 -O url2 -O url3`

Saves the curl commands for all three urls in their respective files

~~~ bash
$ curl -O http://fakeurl.ca -O http://fakeurl1.ca
~~~
