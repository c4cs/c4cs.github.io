advanced-hw-reminder
-----------------------

It's helpful to send out a reminder to students who haven't completed an
advanced homework late into the semester.

I didn't go as far to actually put getting the students' uniqnames into a
script, but this directory contains the email from W17.

To grab the uniqnames, I just loaded up the advanced homework spreadsheet,
did a `collections.Counter` on that data, then

```python
>>> [ uniq for uniq, num_done in adv_hw_counter if num_done == 1 ]
```

Also you'll have to grab a copy of the Canvas gradebook for enrollment to get
people that have turned in 0 advanced homeworks.

```python
>>> all_students = set(canvas_uniqs)
>>> students_w_submissions = set(adv_hw_counter.keys())
>>> no_submissions = all_students.difference(students_w_submissions)
```

(disclaimer: I think this code should work, but wrote it off the cuff)

Use [awdeorio/mailmerge](https://github.com/awdeorio/mailmerge) to send
out the emails.
