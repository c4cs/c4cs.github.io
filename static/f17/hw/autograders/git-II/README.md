Things to do before running the script (may be incomplete):

1) Get a copy of the course gradebook and name it `gradebook.csv` in the local
directory. This can be done through Canvas in the "grades" section and clicking
"Export".

2) Open the `grade.py` file and change the dates that people are supposed to
respond by for re-grade requests. Also, for part `q2b` there is a diff check
against running `ls -1` in the student's repositories. Make sure your system
outputs these files in the same order that this grading script is expecting.

3) These environment variables are used in the script for sending emails
* `export SMTP_HOST=smtp.gmail.com`
* `export SMTP_USER=UNIQNAME@umich.edu`
* `export SMTP_PASS=PASSWORD`

4)

* To check access to repositories you can run:

> `./grade.py clone rerun`

* To grade (this doesn't email the results, just saves them locally):

> `./grade.py grade rerun`

* To email either the test access run or the final grading. I suggest sending a
few of the emails to yourself to make sure that they look correct and everything
is set up right:

> `./grade.py justsend "/tmp/emails/DATE_OF_RUN/"`

Look at the `/tmp/emails` path to see the available dates of when you ran the
program and pick the correct one as the argument to the grading script.


5) Finally, upload the output file to Canvas so the grades are there!
