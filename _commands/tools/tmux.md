---
---

tmux
--

'tmux' allows a user to use 1 terminal window to access multiple separate terminal sessions. It lets you keep running them in the background by detaching them and then reattach them to a different terminal.

~~~ bash
$ tmux
$ tmux new -s myname
$ tmux a -t myname
$ tmux ls
$ tmux kill-session -t myname
~~~

<!--more-->

### Useful Options / Examples


#### `CTRL-B + % or CTRL-B + "`

`%` represents a vertical split, while " represents a horizontal split. This will split the terminal window into multiple terminal sessions. Use `CTRL-B + arrow keys` to navigate.

#### `tmux new -s foo`

New creates a session with the name foo and attaches it to the terminal. Adding `-d` to the end will create a detached session named foo. To list sessions, use the command `tmux ls`.

#### `tmux attach -t foo`

Attaches the session to the existing tmux session named foo.

#### `CTRL-B + d`

Detaches from session.

#### `tmux kill-session -t foo`

Kills session named foo. To kill all sessions except for the current one, use `tmux kill-session -a`. To kill all sessions except for the session named foo, use `tmux kill-session -a -t foo`.

#### `tmux list-commands`

Lists out every tmux command and its respective arguments.
