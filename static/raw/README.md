# Generate correct due dates and other general updates to the title pages
of the homework and advanced homework

This directory contains homework files to be used each semester. Every semester
specific due dates change (i.e. January dates generally become dates in
September for Winter to Fall semesters). The class semester also changes, maybe
specific due date times change, as well as other information that needs to be
added/removed from the title page of all the homework.


Instead of going through each file and making changes individually, a template
is kept here to insert into the files and then move them to the correct
directory to hopefully make maintaining homework from semester to semester
easier.

# ANY CHANGES TO HOMEWORK SHOULD BE MADE IN THIS DIRECTORY
After changes are made to a homework, the following should be run:
- `./seed_hw.py`
- `cd ../SEMESTER/hw && for file in *.tex; do pdflatex $file; pdflatex $file; rm *.out *.log *.aux; done`
- `cd ../SEMESTER/advanced && for file in *.tex; do pdflatex $file; pdflatex $file; rm *.out *.log *.aux; done`

# Images and file dependencies
Other files that are necessary for homework links or images for PDFs should be
placed in the `/src` directory either under `./hw/src` or `./advancded/src`.
Files in these locations will be moved to the destination and be available to be
compiled with the PDFs when necessary.
