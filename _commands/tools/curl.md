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
This will output the content of of the url to the command line

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

#### `curl protocol:url`

Will force curl to use the desired protocol

~~~bash
$ curl dict://dict.org/m:hello
~~~

Will get the definition of hello from a dictionary

#### `curl -u username url`

This will specify username for the proxy authentication

~~~bash
$ curl -u jsmith sftp://random.com
~~~

Uses sftp to get a file from an SSH server

#### `curl -# url`

Will display a more simple progress bar then the default one

~~~bash
$ curl -# testurl.com
~~~


