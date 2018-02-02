# While you were away, I...

* updated my Guest Additions to 5.2.6
  - Host: Devices -> Insert Guest Additions CD Image...
* attached a shared folder from my host
  - Check the VirtualBox host app GUI
  - Added myself to the guest vboxsf user group by editing `/etc/group`
* installed the full vim and GUI vim
  - `% sudo apt-get remove -y vim-tiny`
  - `% sudo apt-get install -y vim vim-gnome`
* made vim my default editor
  - `% echo "export EDITOR='vi'" >> .bashrc`
  - `% echo "export VISUAL='vi'" >> .bashrc`
* installed [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt.git)
  - `% git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-prompt --depth=1`
  - `% echo "GIT_PROMPT_ONLY_IN_REPO=1" >> .bashrc`
  - `% echo ". ~/.bash-git-prompt/gitprompt.sh" >> .bashrc`
* installed curl
  - `% sudo apt-get install -y curl`
* installed Brave (web browser)
  - Got it from [brave.com](https://brave.com)
  - Made it my default browser
* added keyboard shortcuts
  - to open a File Browser
  - to open a Web Browser (Brave)
* cleaned up my desktop launchers
  - unlocked some, locked some, reordered things
* installed Asciinema (for terminal recordings)`
  - `% sudo apt-add-repository ppa:zanchey/asciinema`
  - `% sudo apt-get update`
  - `% sudo apt-get install asciinema`
  - then I edited its config file a bit (~/.config/asciinema/config)
```
[record]
command = /bin/bash -l
maxwait = 2
yes = true
quiet = true

[play]
maxwait = 1
```
