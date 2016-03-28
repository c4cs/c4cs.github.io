---
---

tmux
--

`tmux` is a terminal multiplexer. It allows the user to access separate terminal sessions inside a single terminal window. `tmux` is especially useful in remote access.

~~~bash
$ tmux
~~~

<!--more--> 

### Getting Started
For Linux

~~~bash
$ sudo apt-get install tmux
~~~

For OS X

~~~
$ brew install tmux
~~~

To start tmux, simply type `tmux`. To quit, type `exit`.




### Key Binding
`tmux` can be controlled using a key combination as a prefix key, (which is <kbd>Ctrl</kbd>+<kbd>b</kbd> by default), followed by a command. The following are the most frequently used commands.


~~~
%			split horizontally into two panes
"			split vertically into two panes
!			break the current pane out of the window
x			kill the current pane
c			create a new window
&			kill the current window
n			switch to the next window
p			switch to the previous window
f			promt a search in the current window
,			rename the current window
Left/Right/Up/Down	switch to the pane in the specified direction
~~~

### Session
* `tmux new -s session_name` create a new tmux session
* `tmux attach -t session_name` or `tmux at -t session_name` attache to the session named session_name
* `tmux switch -t session_name` switche to the session named session_name
* `tmux list-sessions` or `tmux ls` list all existing tmux sessions
* `tmux detach` detach the currently attached session

### Window
* `tmux new-window` create a new window
* `tmux select-window -t :0-9` move to the window based on index
* `tmux rename-window` rename the current window

### Pane
* `tmux split-window` split vertically into two panes
* `tmux split-window -h` split horizontally into two panes
* `tmux select-pane -[UDLR]` switch to the pane in the specified direction
* `tmux select-pane -t :.+` switch to the next pane in numerical order



### Configuration
The configuration of tmux is stored in `~/tmux.conf`.

Here are some examples how people change their tmux configurations.

<br>
Change prefix from <kbd>Ctrl</kbd> + <kbd>b</kbd> (which is used by vim!) to <kbd>Ctrl</kbd> + <kbd>a</kbd>.

~~~
unbind C-b
set -g prefix C-a
bind C-a send-prefix
~~~

<br>
Change pane splitting key-binding into a more intuitive way (<kbd>~</kbd> for splitting vertically and <kbd>|</kbd> for splitting horizontally)

~~~
bind ~ split-window
bind | split-window -h
unbind '"'
unbind %'"'
~~~

<br>
You can map vim movement key as tmux movement key

~~~
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
~~~

<br>
Use prefix + <kbd>r</kbd> to reload configuration.

~~~
bind r source-file ~/.tmux.conf \; display-message "Config reloaded..."
~~~


