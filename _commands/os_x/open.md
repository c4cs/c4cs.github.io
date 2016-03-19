---
---

open
-------

`open` is used to open files, directories or URLs from the terminal. 

~~~ bash
#Opens google.com in your default browser
open http://www.google.com
~~~

<!--more-->

### Useful Options / Examples
Besides the one example up top, there's many other ways to use `open`:

~~~ bash
#opens all Word documents in the directory
open *.doc

#Opens your current directory in the Finder
open .

#Opens google.com in Safari
open -a Safari http://www.google.com

#Opens specified file location in Finder
open -R diary.txt
~~~

|     Flag     |               Description                |
| :----------: | :--------------------------------------: |
|      -a      |  Opens item with a specific application  |
|      -e      |         Opens item with TextEdit         |
|      -t      |   Opens item with default text editor    |
|      -f      | Reads input from standard input and opens it with TextEdit |
| -R, --reveal | Selects in the Finder instead of opening |
|  -n, --new   | Opens a new instance of the application (even if it's already running) |
|  -j, --hide  |         Launches the app hidden          |


#### `open -a Safari --hide http://www.google.com`
Opens google.com in Safari minimized by default

##### Break it down
* The `-a` flag lets you choose an application to open your item with. Without it, the item would open up with the default handler. For example, if you remove `-a Safari` and your default browser is Chrome then google.com will open in Chrome.

* `--hide` won't display the application immediately. In this case it will open up google.com but you would need to click on the Safari icon in the dock to actually see the window.

#### `ls | open -f`
Outputs the contents of the `ls` command and displays it in TextEdit, after saving the file in `/tmp/`

##### Break it down
* As we know ls displays all the files and directories in the current directory. Rather than redirecting the output to our own temporary file and then opening that, we can do everything in one go by just piping it to `open -f`.

~~~bash
python main.py > /tmp/python_example.txt 
open /tmp/python_example.txt
~~~

becomes 

~~~bash
python main.py | open -f
~~~

