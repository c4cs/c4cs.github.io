git-II autograder
=================

This is a bit messy, apologies to the future. A good chunk is hardcoded.
Highlights worth double-checking are the repository names; there's a pointer to
this script for people to look over if they have grading issues; the filename
and header written at the end; and probably other things.

In principle, you'd probably want to do something like:

  ./grade.py grade

Then look over /tmp/emails/{time}/... to make sure things look reasonable, then

  ./grade.py /tmp/emails/Mon\ Dec\ 12\ 10\:36\:48\ 2016/ rerun justsend

If you don't have email credentails, you can ask DCO.
