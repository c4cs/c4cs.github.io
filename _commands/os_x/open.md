#Open (OSX)

`open` is used to open files, directories or URLs from the terminal. 

###Options

Here are some useful (but not all) options for `open` (Adapted from the `man` page):

|     Flag     |               Description                |
| :----------: | :--------------------------------------: |
|      -a      |  Opens item with a specific application  |
|      -e      |         Opens item with TextEdit         |
|      -t      |   Opens item with default text editor    |
|      -f      | Reads input from standard input and opens it with TextEdit |
| -R, --reveal | Selects in the Finder instead of opening |
|  -n, --new   | Opens a new instance of the application (even if it's already running) |
|  -j, --hide  |         Launches the app hidden          |

####Usage

~~~bash
#Opens google.com in your default browser
open http://www.google.com

#opens all Word documents in the directory
open *.doc

#Opens your current directory in the Finder
open .

#Opens google.com in Safari
open -a Safari http://www.google.com

#Opens specifed file location in Finder
open -R diary.txt
~~~

####Additional Notes

As we can see, open is fairly easy to use. For more flags, such as launching an application as hidden, please check out the man page.

~~~bash
man open
~~~

