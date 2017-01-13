Lecture Slides
==============

These slides use [remark](https://github.com/gnab/remark) to render markdown
into slides. Jekyll takes care of the plumbing, so here you only need to author
the markdown content for the slides.


Creating PDF versions
---------------------

1. Host a copy of the site that's accessible to external machines, i.e. `bundle exec jekyll serve -H 0.0.0.0`
1. Pick a week + run this beautiful magic:

```
WEEK=7
IP=$(ifconfig en0 | grep inet | grep -v inet6 | cut -d ' ' -f2)
docker run --rm --net=host -v `pwd`:/slides astefanutti/decktape http://$IP:4000/lectures/w17/week$WEEK week$WEEK.pdf
```
