advanced-hw-reminder
-----------------------

It's helpful to send out a reminder to students who haven't completed an
advanced homework late into the semester.

Make sure the advanced homework grades are up to date in the Canvas
gradebook. Whoever is running the advanced homework script should run it
manually before pulling the Canvas gradebook. Then grab a copy of the gradebook
from Canvas and save it in the local directory as `gradebook.csv`. Then run
`./advanced_reminder.py` and it should output the `mailmerge_database.csv` file
needed for mailmerge. It's recommended to add yourself as the first line in the
database file to test the emails work properly. By default the script looks for
students with <= 1 advanced homework submits. Edit the script to change this.

Use [awdeorio/mailmerge](https://github.com/awdeorio/mailmerge) to send
out the emails and you're done.

