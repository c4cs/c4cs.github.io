unit testing
============

You'll need a list of people and repositories:

```
$ head responses.csv
"Timestamp","Username","Give us a pointer to your dotfiles repository"
"2016/11/10 1:50:36 PM EST","ppannuto@umich.edu","https://gitlab.eecs.umich.edu/ppannuto/c4cs-dotfiles"
```

Run

    ./grade.py grade rerun

a few times until your happy with the output.


Things worth possibly looking into are the hacky way we accept various travis
configs (line 158) and finding the right test function (198, 201).


And then run

    ./grade.py justsend <path to emails>

when you're ready to send them out

