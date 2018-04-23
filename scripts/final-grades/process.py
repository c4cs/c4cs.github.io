#!/usr/bin/env python3

import csv
import sys
import numpy

def score_to_grade(score):
    if score > 100:
        return 'A+'
    if score >= 93:
        return 'A'
    if score >= 90:
        return 'A-'
    if score >= 86.7:
        return 'B+'
    if score >= 83.3:
        return 'B'
    if score >= 80:
        return 'B-'
    if score >= 76.7:
        return 'C+'
    if score >= 73.3:
        return 'C'
    if score >= 70:
        return 'C-'
    if score >= 66.7:
        return 'D+'
    if score >= 63.3:
        return 'D'
    if score >= 60:
        return 'D-'
    return 'F'

def ceil_plus_half(raw, max_val):
    raw = float(raw)
    max_val = float(max_val)

    if raw > max_val:
        extra = raw - max_val
        return max_val + extra / 2.
    else:
        return raw

if len(sys.argv) != 2:
    print('Usage: ./process.py canvas_gradebook.csv')
    exit(0)

raw = {}
with open(sys.argv[1]) as csvf:
    reader = csv.DictReader(csvf)

    for row in reader:
        if 'Points Possible' in row['Student']:
            continue

        raw[row['SIS Login ID']] = row

raw_grades = {}
for uniq, data in raw.items():
    raw_grades[uniq] = {
        'homework': {},
        'advanced': {},
        'attendance': {},
        'extra': {},
    }

    for k, v in data.items():
        # treat empty as zero
        if v == '': v = 0.

        if 'Attendance' in k:
            # Attendance Week 02 (261199)
            k = int(k.split()[2])
            raw_grades[uniq]['attendance'][k] = float(v)
        elif 'Homework' in k:
            # Homework 01 (260019)
            k = int(k.split()[1])
            raw_grades[uniq]['homework'][k] = float(v)
        elif 'Advanced' in k:
            # Advanced Exercise 02 (262450)
            k = int(k.split()[2])
            raw_grades[uniq]['advanced'][k] = float(v)
        elif 'Extra Credit' in k:
            raw_grades[uniq]['extra'] = float(v)

final_grades = {}
for uniq, grades in raw_grades.items():
    final_grade = 0.

    # Homework
    # Any points over 40 points are worth half their value.
    final_grade += ceil_plus_half(sum(grades['homework'].values()), 40)

    # Attendance
    # Any points over 30 points are worth half their value.
    final_grade += ceil_plus_half(sum(grades['attendance'].values()), 30)

    final_grade += grades['extra']

    # Advanced
    advanced_raw = [
        sum([grades['advanced'][i] for i in [2,3]]),            # Introduction and Basics
        sum([grades['advanced'][i] for i in [4,5,6]]),          # Being Efficient
        sum([grades['advanced'][i] for i in [7,8,9,10,11]]),    # Developing
        sum([grades['advanced'][i] for i in [12,13,14,15]]),    # Standing on the Shoulders of Giants
    ]

    # Advanced grading script takes care of the weighted adv-hw points
    for score in advanced_raw:
        final_grade += float(score)

    final_grades[uniq] = final_grade

final_letter_grades = {}
for uniq, grade in final_grades.items():
    final_letter_grades[uniq] = score_to_grade(grade)

with open('mailmerge_database.csv', 'w') as outf:
    writer = csv.DictWriter(outf, fieldnames=['email', 'name', 'number', 'letter'])
    writer.writeheader()

    for uniq in final_grades.keys():
        writer.writerow({
            'email': '{}@umich.edu'.format(uniq),
            'name': uniq,
            'number': '{:.2f}'.format(final_grades[uniq]),
            'letter': final_letter_grades[uniq],
        })
