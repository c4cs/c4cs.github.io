---
---
curl
-------

`curl` is used to transfer data from one server to another using a supported protocol such as HTTP or HTTPS 

~~~ bash
$ curl google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
~~~

<!--more-->

### Useful Options / Examples
~~~ bash
$ curl -o output.txt google.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   219  100   219    0     0   3930      0 --:--:-- --:--:-- --:--:--  3981
~~~
##### Break it down
The `-o filename` option has the output written to a file instead of stdout. This is especially helpful when using test cases for projects. On piazza instructors will sometimes post large test cases that cannot be copy and pasted. This option allows for an easy download. A progress meter is shown during download.

~~~ bash
$ curl -m 10 google.com
~~~
##### Break it down
The `-m seconds` option is also useful. This sets an upper limit on how long the download can take place. This prevents the batch from stalling due to a poor network connection.

~~~ bash
$ curl -k shadywebsite.com
<html>
	<head>
		<title>This is a shady website. What are you even doing here?</title>
	</head>
	<body>
		<div style="
			text-align: center;
		"><img src="shady_pusheen.png" /></div>
	</body>
</html>

~~~
##### Break it down
The `-k` option allows the user curl to do SSL transfers. By default all SSL connections are attempted in a secure mode by with the `-k` option, any insecure transfer can be completed. 

