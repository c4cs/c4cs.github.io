#!/usr/bin/env python3

import argparse
import configparser
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math
import os
import pprint
import smtplib
import string
import sys

import markdown
import numpy as np


config = configparser.ConfigParser()
config.read('config.ini')

parser = argparse.ArgumentParser('Convert raw scores, format for canvas, and e-mail results')
parser.add_argument('week', type=int, help="which week?")
parser.add_argument('-E', '--no-email', action='store_true',
		help="Do not send emails")
args = parser.parse_args()

scores = []

seen_scores = set()

uniq_to_raw = dict()
uniq_to_grade = dict()

infile = os.path.join(
		os.path.expanduser(config['grades']['hw.path']),
		config['grades']['hw.input_format'].format(args.week),
		)
gradebook = os.path.join(
		os.path.expanduser(config['grades']['hw.path']),
		config['grades']['hw.gradebook'],
		)
outfile = os.path.join(
		os.path.expanduser(config['grades']['hw.path']),
		config['grades']['hw.output_format'].format(args.week),
		)

with open(infile) as csvfile:
	ggb = csv.DictReader(csvfile)

	for row in ggb:
		uniq = row['Email'].strip().split('@')[0]
		if row['Total Score'] == '':
			score = 0
		else:
			score = float(row['Total Score'])
		seen_scores.add(score)

		uniq_to_raw[uniq] = score

		if score <= 0.25:
			score = 0
		elif score <= 2:
			score = 2
		else:
			score = 4

		scores.append(score)

		if score not in (0,2,4):
			print("Bad score?")
			print(score)
			raise NotImplementedError

		uniq_to_grade[uniq] = score


# Generate canvas-friendly csv

with open(outfile.format(args.week), 'w') as out:
	with open(gradebook) as csvfile:
		cgb = csv.DictReader(csvfile)

		fieldnames = (
				'Student',
				'ID',
				'SIS User ID',
				'SIS Login ID',
				'Section',
				'Homework Week {}'.format(args.week),
				)
		writer = csv.DictWriter(out, fieldnames=fieldnames)
		writer.writerow({
			'Student': 'Student',
			'ID': 'ID',
			'SIS User ID': 'SIS User ID',
			'SIS Login ID': 'SIS Login ID',
			'Section': 'Section',
			'Homework Week {}'.format(args.week): 'Homework Week {}'.format(args.week),
			})

		for row in cgb:
			try:
				score = uniq_to_grade[row['SIS Login ID']]
			except KeyError:
				print("Warn: No grade for " + row['SIS Login ID'])
				score = 0
			to_write = {
					'Student': row['Student'],
					'ID': row['ID'],
					'SIS User ID': row['SIS User ID'],
					'SIS Login ID': row['SIS Login ID'],
					'Section': row['Section'],
					'Homework Week {}'.format(args.week): score,
					}
			writer.writerow(to_write)

print("All seen scores")
print(sorted(seen_scores))
print('')

scores = np.array(scores)
print("Min {}, Max {}, Mean {:.2f}, Med {}, Std {:.2f}".format(
	np.min(scores),
	np.max(scores),
	np.mean(scores),
	np.median(scores),
	np.std(scores),
	))
print('')

input("Grades written. Press enter to send e-mails or Ctrl-C to quit. ")

email_subject = "[{}] Homework {} Graded".format(
		config['term']['class_name'], args.week)
email_body = string.Template("""
Hi $name,

Your Homework {week} for {klass} {term} has been graded!

---

A reminder on Homework scoring: https://c4cs.github.io/#syllabus-homework

We will give each homework a "raw" grade in Gradescope, which will then convert to a final score using the following conversion:

    [0,0.25] → 0 points No / very little effort
    (0.25,2] → 2 points Some effort, but not quite there
    (2,4] → 4 points Solid effort, completed successfully

The idea here is that homework does not have to 100% perfect to receive full credit. In addition, course staff can be a little "nit-picky", taking of tenths of points to draw your attention to corrections and suggestions without actually penalizing your grade.

---

Your raw grade on this assignment is: **$raw_grade**

Your final grade on this assignment is: **$final_grade**

Any issues or regrade requests should go through [Gradescope](https://gradescope.com)

Some class statistics:

    Minimum: {min:0.2f}
    Maximum: {max:0.2f}
    Mean: {mean:0.2f}
    Median: {median:0.2f}
    Standard Deviation: {std:0.2f}

---

Your {klass} {term} instructors,

{instructors}
""".format(
	week=args.week,
	klass=config['term']['class_name'],
	term=config['term']['term_name'],
	instructors=config['term']['instructors'],
	min=np.min(scores),
	max=np.max(scores),
	mean=np.mean(scores),
	median=np.median(scores),
	std=np.std(scores),
	)
)

if 'host' in config['smtp']:
	sm = smtplib.SMTP(host=config['smtp']['host'])
else:
	sm = smtplib.SMTP()
	sm.connect()
if 'username' in config['smtp']:
	sm.login(config['smtp']['username'], config['smtp']['password'])

with open(gradebook) as csvfile:
	cbg = csv.DictReader(csvfile)

	msg = MIMEMultipart('alternative')
	msg['Subject'] = email_subject
	msg['From'] = config['email']['from']

	for row in cbg:
		uniqname = row['SIS Login ID']
		raw = uniq_to_raw.get(uniqname, 0)
		score = uniq_to_grade.get(uniqname, 0)
		name = row['Student']
		name = ' '.join(name.split(',')[::-1]).strip()
		md = email_body.substitute({
				'name': name,
				'raw_grade': raw,
				'final_grade': score,
				})
		html = markdown.markdown(md)

		msg['To'] = uniqname + config['email']['suffix']
		#msg['To'] = 'ppannuto@umich.edu'

		text_part = MIMEText(md, 'plain')
		html_part = MIMEText(html, 'html')

		msg.attach(text_part)
		msg.attach(html_part)

		#print(msg.as_string())
		sm.sendmail(msg['From'], msg['To'], msg.as_string())

		#break
