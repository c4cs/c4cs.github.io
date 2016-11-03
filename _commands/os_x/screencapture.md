---
---

screencapture
-------

`screencapture` is used to capture an image of the whole, or part of the screen.

~~~ bash
#Takes a screenshot of the entire screen and saves it to the file screencap.png in the cwd
screencapture screencap.png
~~~

<!--more-->

### Where to install

`screencapture` comes  built with OSX's command-line tools. If you don't have them, you can install them via:

~~~ bash
xcode-select --install
~~~

### Synopsis

~~~ bash
screencapture [options] [file] 
~~~ 

### Flags

Here are some cool flags that you could use within your program.

[-t format]


Example:


~~~ bash
#screencapture will save the file as a jpg instead of png (default)
screencapture -t jpg screencap.jpg
~~~


[-R x,y,w,h]


Example:


~~~ bash
#screencapture will capture a 500x500 rectange with (250,600) as the upper left hand corner
screencapture -R 250,600,500,500 screencap.jpg
~~~


[-T seconds]


Example:


~~~ bash
#Take the picture after a delay of 10 seconds
screencapture -T 10
~~~


Below are some other cool flags and their descriptions, try them out!


|     Flag     |               Description                |
| :----------: | :--------------------------------------: |
|      -c      | Force screen capture to go to the clipboard.|
|      -C      | Capture the cursor as well as the screen.  Only allowed in non-interactive modes.     |
|      -d      | Display errors to the user graphically. |
|      -i      | Capture screen interactively, by selection or window.|
|      -m      | Only capture the main monitor, undefined if -i is set. |
|      -M      | Open the taken picture in a new Mail message. |
|      -o      | In window capture mode, do not capture the shadow of the window. |
|      -P      | Open the taken picture in a Preview window. |
|      -s      | Open the taken picture in a new Mail message. |
|      -x      | Do not play sounds. |
|      -help   | Display help |



