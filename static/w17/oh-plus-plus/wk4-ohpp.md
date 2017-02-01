`OH++` Editors
==============

## vim vs. emacs vs. everything else

We don't advocate for one editor over another. That may sound contradictory,
given Darden's consistent shoutouts to "Team Vim", but trust me when I say this
is merely tribal, red team / blue team ridiculousness. None of us seriously
believe one editor is strictly better than the other. Everyone thinks
differently. Everyone works differently. Everyone has preferences which
differentiate them from their peers, but it's frequently difficult to argue
that one set of preferences is strictly better than the other. Whatever helps
you think clearly and efficiently puts bytes into files will be the editor you
use.

That said, we _will_ recommend that everyone know how to use at least one
command line editor. It will make your life easier when you find yourself on
a command line without access to a graphical editor. This happens more often
than you might think.

Regretably, I don't have the time (tonight) to write a guide to emacs. That
said, if you come to my office hours wanting to know how to customize emacs,
I will gleefully learn along with you.

[Here's a good post on the vim/emacs
debate](http://stackoverflow.com/a/1433315/3681820)

## On customization

When you install your first plugin, there can be an urge to go crazy and
immediately install ten more. You may even feel tempted to use a pre-configured
version of vim or emacs, like `spf-13 vim` and `spacemacs`. In general, it's
better to start small and build up your own configuration. The reasoning is
3-fold ...

1. These editors are already confusing enough. Most of the time, these
   'all-in-one' starter packages usually don't make the learning curve any
   easier. These editors already have a ton of features. Double check that you
   can't already do what you want with stock features.
1. By writing your own configuration file and selecting your own plugins,
   you'll be much more familiar with what you've actually installed. It'll be
   much easier to remember the any new commands, features, or hotkeys because
   you'll be setting them up.
1. Part of the advantage to using a [close to] stock editor is being
   comfortable when you don't have access to your own configuration.

That said, plugins can be really helpful, and get you more invested in
professional development leading you to more interesting corners of computing.

> _"Okay, whatever. Can we do something already?"_

___Yes.___

### `vim`

Key points:
* Vim is "Modal" -- it has modes. Insert, Visual, Normal, Replace -- etc.
  - Key combinations can change based on which mode you're in.
* Vim is pretty quick to open.
  - This allows you to open and close files quite quickly to bounce back to the
      command line.
* You may never learn all of the vim hotkeys.
  - And that's totally fine. I just learned how markers work. That's
      not even a vim feature -- it's been around since vi (thirty years?).


#### Installing a plugin

We recommend that you use a plugin manager, but it is important to have an idea
of what's going on. [This brief
post](https://howchoo.com/g/ztmyntqzntm/how-to-install-vim-plugins-without-a-plugin-manager)
gives some intuition for what is happening behind the scenes.

For now, knowing how to use a plugin manager is good enough. Personally,
I use `vim-plug`, but there's `Vundle`, `neobundle`, and `pathogen` which come
to mind as well. There's not a huge difference between them, but I find that
`vim-plug` is the most straightforward.

[Go ahead and install `vim-plug` here](https://github.com/junegunn/vim-plug).
The guide for installing plugins is pretty comprehensive. Come to office hours
if you still need help.

#### Changing the colorscheme

Vim actually comes with a bunch of colorschemes built in. Go ahead and try
this. After opening vim, type `:colorscheme <tab>`. Go ahead and cycle through.
If you want the change to be permanent , add the command `colorscheme
<colorscheme name>` to your `.vimrc` file and it will be invoked everytime you
start vim.

To install another colorscheme, add the `<colorscheme name>.vim` file to
`~/.vim/colors` folder. Some may require additional setup, like special
terminal integration. Hopefully, we've prepared you well for this. When
installed with a plugin manager, the colorscheme should be accessible as long
as you set it after the section of your `.vimrc` file where the plugins are
declared. This is because custom colorschemes from plugins are not "on the
path" for vim until the plugin manager adds them.

#### Creating a new keybinding

> _"This keybinding makes no sense. How do I change it?"_
> _- everyone at some point_

When writing markdown files, much like this one, I like to be able to use spell
check. Most of the time though, I'll want it off. I always forget the command,
`:setlocal spell!<CR>`, so I set it to `<leader>ss`. Now, when I press `,ss` in
normal mode, spell check underlines incorrectly spelled words.

I enabled this by adding `nmap <leader>ss :setlocal spell!<CR>` to my `.vimrc`
file. Let's break this down.

```
nmap <leader>ss :setlocal spell!<CR>
|    |          \
|    \           This is where you'll put the sequence of keys for the command.
\     The leader key begins many commands. The default is backslash \
 'map' means "Map this key combination to a command", the 'n' in 'nmap' means
 it only applies to normal mode.
```

Whenever you want to change your `.vimrc` file, you've got to open it in some
text editor to make changes. You don't need to leave vim to do this, as you can
always just open the file from within vim, by this will likely require you to
type the full file path. And, once you've finished editing and saved your
`.vimrc`, you'll have to reload the file for any changes to take effect. This
is all super lame, so I've rebound the sequences for these two actions to two,
easy to remember key combinations.

```
" reload vimrc (reload RC)
nmap <leader>rc :so ~/.config/nvim/init.vim<CR>

" Edit ~/.vimrc (Edit Vim Rc)
nmap <leader>erc :e ~/.config/nvim/init.vim<CR>
```

* [Some great tips for using vim](http://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim)
* [A laundry list of interesting
configurations](https://sheerun.net/2014/03/21/how-to-boost-your-vim-productivity/)


