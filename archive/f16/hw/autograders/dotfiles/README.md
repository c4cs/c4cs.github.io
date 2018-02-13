dotfiles
========

Less hardcoded stuff here, but still not great. Big one is probably which week
the homework belongs to which creeps in a few places.

You'll need a list of people and repositories:

```
$ head responses.csv
"Timestamp","Username","Give us a pointer to your dotfiles repository"
"2016/11/10 1:50:36 PM EST","ppannuto@umich.edu","https://gitlab.eecs.umich.edu/ppannuto/c4cs-dotfiles"
```

Run

    ./grade.py grade rerun

a few times until your happy with the output.

And then run

    ./grade.py justsend <path to emails>

when you're ready to send them out

