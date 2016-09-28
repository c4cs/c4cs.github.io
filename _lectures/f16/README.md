Lecture Slides
==============

These slides use [remark](https://github.com/gnab/remark) to render markdown
into slides. Jekyll takes care of the plumbing, so here you only need to author
the markdown content for the slides.


Creating PDF versions
---------------------

1. Host a copy of the site that's accessible to external machines, i.e. `bundle exec jekyll serve -H 0.0.0.0`

2. Grab a copy of your machine's IP address

3. Run this beautiful magic: `docker run --rm --net=host -v `pwd`:/slides astefanutti/decktape http://<--YOUR IP HERE-->:4000/lectures/f16/week4 slides.pdf`

