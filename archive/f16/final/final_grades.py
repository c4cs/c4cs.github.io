#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.WARN)

import csv
import glob
import math
import multiprocessing
import os
import sys
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import git # pip install gitpython

# Get an updated version of sh with proper pushd support
sys.path.insert(0, '/Users/ppannuto/code/sh')
import sh
from sh import mkdir, rm

for a in sys.argv:
	if '/emails' in a:
		TIMEDIR = a
		if TIMEDIR[-1] != '/':
			TIMEDIR += '/'
		break
else:
	TIME = time.asctime()
	TIMEDIR = '/tmp/emails/'+TIME+'/'

mkdir('-p', TIMEDIR)

ACTUALLY_SEND = False

GRADES_PATH = '../../../../f16_grades/'

uniq_to_grade = {}
grades_lock = multiprocessing.Lock()


def uniqs_gen():
	with open(GRADES_PATH + 'gradebook.csv') as csvfile:
		r = csv.DictReader(csvfile)
		for row in r:
			if row['Student'] == '    Points Possible':
				continue
			if row['Student'] == 'Student, Test':
				continue
			yield row['SIS Login ID']


with open('email.cfg') as e:
	SMTP_HOST = e.readline().strip()
	SMTP_USER = e.readline().strip()
	SMTP_PASS = e.readline().strip()

sm = None

def send_email(uniqname, body):
	sys.exit()
	SUBJECT = "[C4CS] Final Grades"
	FROM = 'c4cs-staff@umich.edu'
	TO = uniqname + '@umich.edu'
	#TO = 'ppannuto' + '@umich.edu'
	encoding = 'html'

	msg = MIMEMultipart()
	msg['Subject'] = SUBJECT
	msg['From'] = FROM
	msg['To'] = TO
	#msg['CC'] = ','.join(CC)
	msg.attach(MIMEText(body, encoding))

	if not ACTUALLY_SEND:
		print(msg.as_string())

	if ACTUALLY_SEND:
		global sm
		if sm is None:
			sm = smtplib.SMTP(host=SMTP_HOST)
			sm.login(SMTP_USER, SMTP_PASS)

		#send_to = [TO,] + CC
		send_to = [TO,]
		sm.sendmail(FROM, send_to, msg.as_string())


uniqs = {}

def load_grades():
	# Student,ID,SIS User ID,SIS Login ID,Section,Homework Week 1
	for week in glob.glob(GRADES_PATH + 'hw/grades-hw*'):
		id = int(week.split('-')[-1].split('.')[0][2:])
		for row in csv.DictReader(open(week)):
			if row['Student'] == '    Points Possible':
				continue
			if row['Student'] == 'Student, Test':
				continue
			uniq = row['SIS Login ID']
			if uniq not in uniqs:
				uniqs[uniq] = {'hw': {}, 'adv': {}, 'attendance': {}}
			uniqs[uniq]['hw'][id] = int(row['Homework Week {}'.format(id)])

	for week in glob.glob(GRADES_PATH + 'attendance/grades-a*'):
		id = int(week.split('-')[-1].split('.')[0][1:])
		for row in csv.DictReader(open(week)):
			if row['Student'] == '    Points Possible':
				continue
			if row['Student'] == 'Student, Test':
				continue
			uniq = row['SIS Login ID']
			if uniq not in uniqs:
				uniqs[uniq] = {'hw': {}, 'adv': {}, 'attendance': {}}
			uniqs[uniq]['attendance'][id] = float(row['Attendance Week {:02}'.format(id)])

	for week in glob.glob(GRADES_PATH + 'advanced/grades-advanced*'):
		id = int(week.split('-')[-1].split('.')[0][8:])
		for row in csv.DictReader(open(week)):
			if row['Student'] == '    Points Possible':
				continue
			if row['Student'] == 'Student, Test':
				continue
			uniq = row['SIS Login ID']
			if uniq not in uniqs:
				uniqs[uniq] = {'hw': {}, 'adv': {}, 'attendance': {}}
			uniqs[uniq]['adv'][id] = float(row['Advanced Exercise Week {}'.format(id)])
			if uniqs[uniq]['adv'][id]:
				uniqs[uniq]['adv'][id] = 'Yes'
			else:
				uniqs[uniq]['adv'][id] = 'No'

	for line in open(GRADES_PATH + 'advanced/adv2_bonus.csv'):
		uniqs[line.split(',')[0]]['adv2bonus'] = 'Yes'

	for uniq in uniqs:
		hw_total = 0
		for wk in uniqs[uniq]['hw']:
			hw_total += uniqs[uniq]['hw'][wk]
		if hw_total > 40:
			hw_extra = (hw_total - 40) / 2
			hw_total = 40 + hw_extra
		uniqs[uniq]['hw_total'] = hw_total

		attn_total = 0
		for wk in uniqs[uniq]['attendance']:
			attn_total += uniqs[uniq]['attendance'][wk]
		if attn_total > 30:
			attn_extra = (attn_total - 30) / 2
			attn_total = 30 + attn_extra
		uniqs[uniq]['attn_total'] = attn_total

		adv_total = 0
		ADV1 = (2,3)
		ADV2 = (4,5,6)
		ADV3 = (7,8,9)
		ADV4 = (10,11,13)

		first = False
		for wk in ADV1:
			try:
				if uniqs[uniq]['adv'][wk] == 'Yes':
					if first:
						adv_total += 5
					else:
						adv_total += 10
						first = True
			except KeyError:
				pass

		first = False
		for wk in ADV2:
			try:
				if uniqs[uniq]['adv'][wk] == 'Yes':
					if first:
						adv_total += 5
					else:
						adv_total += 10
						first = True
			except KeyError:
				pass

		first = False
		for wk in ADV3:
			if uniqs[uniq]['adv'][wk] == 'Yes':
				if first:
					adv_total += 5
				else:
					adv_total += 10
					first = True

		first = False
		for wk in ADV4:
			try:
				if uniqs[uniq]['adv'][wk] == 'Yes':
					if first:
						adv_total += 5
					else:
						adv_total += 10
						first = True
			except KeyError:
				pass

		# Special case the adv2 bonus point
		if 'adv2bonus' in uniqs[uniq]:
			uniqs[uniq]['adv'][2] = 'Yes (+1)'
			adv_total += 1

		uniqs[uniq]['adv_total'] = adv_total

		uniqs[uniq]['final'] = hw_total + adv_total + attn_total
		uniqs[uniq]['letter'] = score_to_grade(uniqs[uniq]['final'])


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



def grade(uniqname):
	email = '''
<p>Hello {},</p>
<br />
<p>Your final course grade is {}/100, {}.</p>
'''.format(uniqname, uniqs[uniqname]['final'], uniqs[uniqname]['letter'])

	email += '''
<hr />
<p>It was wonderful having everyone in class this term. We hope that this
course will help you throughout the rest of your career in computer science, or
whatever career path you may pursue.
Materials from class will remain online on the course homepage and free for
anyone to access in perpetuity.</p>
<p>We would really appreciate if everyone could fill out
<a href="https://docs.google.com/a/umich.edu/forms/d/e/1FAIpQLScKpWL3RkzwXcQ6-i3fJh0Xwqg2kNTGNv44V20CaVOCy1tn9Q/viewform">this survey</a>
on how we can improve the course. The survey is completely anonymous.</p>
<p>One of the challenges we continually face is reaching out to incoming
computer science students. Many reviews "wish they had taken this before
280/281", but it is hard for us to reach students who have not yet declared CS
(and joined our e-mail lists) or found the
<a href="https://www.facebook.com/groups/343020979078852/">CSE Facebook group</a>.
If you found this course helpful, please help our outreach efforts by
encouraging new students in CS to consider C4CS. If there are ways in which you
think we could improve the class, please let us know in the
<a href="https://docs.google.com/a/umich.edu/forms/d/e/1FAIpQLScKpWL3RkzwXcQ6-i3fJh0Xwqg2kNTGNv44V20CaVOCy1tn9Q/viewform">exit survey</a>.
'''

	email += '''
<hr />
<h3>Detailed Grade Breakdown</h3>
<p>If you have any questions about how final grades were calculated,
<a href="https://c4cs.github.io/#grading">here</a> is the course rubric, and
<a href="https://github.com/c4cs/c4cs.github.io/blob/master/static/f16/final/final_grades.py">this script</a>
computed final grades.</p>
<table border="1">
  <tr>
'''
	HWS = (1,2,3,4,5,6,7,8,9,10,11,13)
	for wk in HWS:
		email += '    <th>HW {}</th>\n'.format(wk)
	email += '    <th>Total</th>\n'
	email += '  </tr><tr>\n'
	for wk in HWS:
		email += '    <td>{}</td>\n'.format(uniqs[uniqname]['hw'][wk])
	email += '    <td>{}</td>\n'.format(uniqs[uniqname]['hw_total'])
	email += '  </tr>\n'
	email += '</table>\n'

	ATTNS = (2,3,4,5,6,7,8,9,10,11,13,14)
	email += '<table border="1">\n'
	email += '  <tr>\n'
	for wk in ATTNS:
		email += '    <th>Attn {}</th>\n'.format(wk)
	email += '    <th>Total</th>\n'
	email += '  </tr><tr>\n'
	for wk in ATTNS:
		try:
			email += '    <td>{}</td>\n'.format(uniqs[uniqname]['attendance'][wk])
		except KeyError:
			email += '    <td>{}</td>\n'.format(0.0)
	email += '    <td>{}</td>\n'.format(uniqs[uniqname]['attn_total'])
	email += '  </tr>\n'
	email += '</table>\n'

	ADV1 = (2,3)
	ADV2 = (4,5,6)
	ADV3 = (7,8,9)
	ADV4 = (10,11,13)

	email += '<table border="1">\n'
	email += '  <tr>\n'
	for wk in ADV1+ADV2+ADV3+ADV4:
		email += '    <th>Adv {}</th>\n'.format(wk)
	email += '    <th>Total</th>\n'
	email += '  </tr><tr>\n'
	email += '    <td colspan="2">Intro and Basics</td>\n'
	email += '    <td colspan="3">Developing</td>\n'
	email += '    <td colspan="3">Being Efficient</td>\n'
	email += '    <td colspan="3">Shoulders of Giants</td>\n'
	email += '  </tr><tr>\n'

	for wk in ADV1+ADV2+ADV3+ADV4:
		email += '    <td>{}</td>\n'.format(uniqs[uniqname]['adv'][wk])
	email += '    <td>{}</td>\n'.format(uniqs[uniqname]['adv_total'])
	email += '  </tr>\n'
	email += '</table>\n'

	email += '''
<hr />
<p>Wishing you a happy holidays and a wonderful future in computer science!</p>
<p>The C4CS Staff</p>
'''

	#print(email)

	with open(TIMEDIR + uniqname, 'w') as w:
		w.write(email)


def theres_probably_a_better_way_to_do_this(args):
	try:
		grade(*args)
	except:
		print("EXCEPTION CAUSED BY {}".format(args))
		raise

def do_grading():
	load_grades()

	for uniqname in uniqs_gen():
		theres_probably_a_better_way_to_do_this((uniqname,))
	#with multiprocessing.Pool(10) as p:
	#	p.map(theres_probably_a_better_way_to_do_this, uniqs())

	write_wolv_grades()


# Generate canvas-friendly csv
def write_wolv_grades():
	enrolled = []
	for row in csv.DictReader(open(GRADES_PATH + 'gradebook.csv')):
		if row['Student'] == '    Points Possible':
			continue
		if row['Student'] == 'Student, Test':
			continue
		enrolled.append(row['SIS Login ID'])
	with open(GRADES_PATH + 'final_grades.csv', 'w') as out:
		for uniq in sorted(enrolled):
			out.write('{},{}\n'.format(uniq, uniqs[uniq]['letter']))

if __name__ == '__main__':
	if 'justsend' in sys.argv:
		ACTUALLY_SEND = True
		for path in glob.iglob(TIMEDIR + '*'):
			uniqname = path.split('/')[-1]
			send_email(uniqname, open(path).read())
			print('Sent {}'.format(uniqname))
			# Be kind to the smtp server
			time.sleep(.1)
		sys.exit()
	if 'email' in sys.argv:
		ACTUALLY_SEND = True

	os.environ['GIT_TERMINAL_PROMPT'] = "0"

	if 'grade' in sys.argv:
		do_grading()

