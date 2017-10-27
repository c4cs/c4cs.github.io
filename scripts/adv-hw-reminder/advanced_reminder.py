#!/usr/bin/env python3

import csv
from collections import Counter

UNIQ_KEY = 'SIS Login ID'

num_adv_completed = Counter() # dictionary of uniq's to # adv hw's completed

with open('gradebook.csv', 'r') as csvfile:
    cgb = csv.DictReader(csvfile)

    for row in cgb:
        uniq = row[UNIQ_KEY]
        print(uniq)
        for assignment in row.keys():
            if "Advanced" in assignment:
                if (row['Student'] == "Student, Test" or
                    row['Student'] == "    Points Possible"):
                    continue
                num_adv_completed[uniq] += 1 if row.get(assignment, 0) else 0

    print(num_adv_completed)

uniqs_to_email = [ (uniq, num_done) for uniq, num_done in num_adv_completed.items() if num_done <= 1 ]

with open('mailmerge_database.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['email', 'num_complete', 'uniq'])

    for uniq, num_complete in uniqs_to_email:
        writer.writerow([uniq + '@umich.edu', num_complete, uniq])
