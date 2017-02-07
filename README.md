# Computing for Computer Scientists

[![Build Status](https://travis-ci.org/c4cs/c4cs.github.io.svg?branch=master)](https://travis-ci.org/c4cs/c4cs.github.io)

This repository holds the sources for the course homepage for Computing for Computer Scientists,
a course for early-career EECS students at the University of Michigan.

For more information, visit the course homepage: [https://c4cs.github.io]()

## Contributing

The site itself uses [GitHub Pages][] and [Jekyll][].

Before contributing, please check [open issues][] and create a [new issue][] if a one for your proposed contribution does not exist.

Content for the website is written in [Markdown][].
To contribute to the [reference page][], navigate to `_commands/` and then to the specific section and edit an existing `.md` file or create a new one.
For example, to edit the `cd` reference, edit `_commands/basics/cd.md`.

In order to build the site locally on your __Ubuntu__ computer, there are a
number of dependencies to resolve first:

```bash
$ sudo apt-get install ruby ruby-dev build-essential patch zlib1g-dev liblzma-dev nodejs
$ sudo gem install jekyll bundler
$ bundle install
$ bundle exec jekyll serve # serves site at http://127.0.0.1:4000
```

For more information on setting up, see [GitHub's guide][gh docs] or [Jekyll's documentation][jekyll docs].

After making a change and verifying that it works, please submit a [pull request][].

---------------------

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Computing for Computer Scientists</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://patpannuto.com" property="cc:attributionName" rel="cc:attributionURL">Pat Pannuto</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.


[GitHub Pages]: https://pages.github.com/
[Jekyll]: https://jekyllrb.com/
[open issues]: https://github.com/c4cs/c4cs.github.io/issues
[new issue]: https://github.com/c4cs/c4cs.github.io/issues/new
[Markdown]: http://daringfireball.net/projects/markdown/
[reference page]: https://c4cs.github.io/reference
[ruby]: https://www.ruby-lang.org/en/
[bundler]: https://bundler.io/
[gh docs]:https://help.github.com/articles/using-jekyll-with-pages/
[jekyll docs]: https://jekyllrb.com/docs/home/
[pull request]: https://github.com/c4cs/c4cs.github.io/pulls
[Homebrew]: https://c4cs.github.io/commands/brew
