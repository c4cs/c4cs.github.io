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
import traceback
import yaml

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import git # pip install gitpython

import sh # pip install sh
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

GRADES_PATH = '../../../../../../f16_grades/'
WEEK=5

uniq_to_grade = {}
grades_lock = multiprocessing.Lock()


def uniqs():
	with open('responses.csv') as csvfile:
		r = csv.reader(csvfile)
		for row in r:
			if row[1] == 'Username':
				continue
			uniq = row[1].split('@')[0]
			repo = row[2]
			yield uniq, repo


with open('email.cfg') as e:
	SMTP_HOST = e.readline().strip()
	SMTP_USER = e.readline().strip()
	SMTP_PASS = e.readline().strip()

sm = None

def send_email(uniqname, body):
	SUBJECT = "[C4CS] Homework 5 Graded"
	FROM = 'c4cs-staff@umich.edu'
	TO = uniqname + '@umich.edu'
	#TO = 'ppannuto' + '@umich.edu'
	#CC = ['ppannuto@umich.edu',]
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

class CloneError(Exception):
	pass

def clone(root, uniqname, url):
	# Work around gitlab weirdness that's a bit subtle
	if 'gitlab' in url:
		if url[-4:] != '.git':
			url += '.git'

	into='/tmp/'+root
	mkdir('-p', into)
	to_path=into + '/' + uniqname

	if os.path.exists(to_path):
		if 'rerun' in sys.argv:
			print('cached {}'.format(to_path))
			repo = git.Repo(to_path)
			return repo, to_path
		else:
			print('warn {} already exists'.format(to_path))
			input('enter to continue and delete, ctrl-c to quit; run with "rerun" to use cache')
			rm('-r', '-r', to_path)

	print('clone {}'.format(to_path))

	try:
		repo = git.Repo.clone_from(
				url=url,
				to_path=to_path,
				)
		return repo, to_path
	except:
		# Fall back to sh path to grab the error
		try:
			sh.git('clone', url, to_path)
		except sh.ErrorReturnCode as e:
			if 'Connection closed by remote host' in e.stderr.decode('utf8'):
				# gitlab rate-limited us
				time.sleep(3)
				return clone(root, uniqname, project)
			if 'terminal prompts disabled' in e.stderr.decode('utf8'):
				raise CloneError("No permission")
			raise

		# Since we're hammering the gitlab server, rarely the first will
		# timeout, but this second chance will succeed. Create a repo object
		# from the path in that case.
		repo = git.Repo(to_path)
		return repo, to_path


def grade_q1(uniqname, repo):
	repo, path = clone('wk5-unit-testing', uniqname, repo)

	text = ''
	grade = 0

	with sh.pushd(path):

		# Test Travis stuff [1 pt]
		if not os.path.exists('.travis.yml'):
			text += '<dd><strong>No .travis.yml file [travis: 0.0/1.0]</strong></dd>'
		else:
			try:
				travis = yaml.load(open('.travis.yml'))

				# There's probably something better to do here
				if 'test_rpn.py' in travis['script'] \
						or 'python -m unittest' in travis['script'] \
						or 'python3 -m unittest' in travis['script'] \
						or 'python test_rpn.py' in travis['script'] \
						or 'coverage run test_rpn.py' in travis['script'] \
						or 'coverage run -m unittest' in travis['script'] \
						or 'coverage run -m  unittest' in travis['script'] \
						or 'coverage run python3 -m unittest' in travis['script'] \
						or 'make' in travis['script'] \
						or 'make test' in travis['script'] \
						or 'nosetests' in travis['script'] \
						or 'nosetests --with-coverage --cover-erase --cover-package=rpn --cover-tests' in travis['script'] \
						or 'nosetests --with-coverage' in travis['script']:
					text += '<dd><strong>Travis set up to run tests [travis: 1.0/1.0]</strong></dd>'
					grade += 1.0
				else:
					print(travis['script'])
					allow = input("Look at travis for {}. Give credit? [y/N] ".format(uniqname)).strip().upper()
					if len(allow) and allow[0] == 'Y':
						text += '<dd><strong>Travis set up to run tests [travis: 1.0/1.0]</strong></dd>'
						grade += 1.0
					else:
						text += '<dd><strong>Travis does not appear to run tests [travis: 0.0/1.0]</strong></dd>'

			except yaml.YAMLError as exc:
				text += '<dd><strong>Failed to parse .travis.yml as valid YAML [travis: 0.0/1.0]</strong></dd>\n'
				text += '<dd>Error from YAML parser:</dd>\n'
				text += '<dd><pre>{}</pre></dd>\n'.format(exc)


		# Test exponentiation ourselves, then monkey patch to break calculate
		# function and verify that exponentiation test works
		ugly_one_liner = '''
import inspect
import traceback
import rpn
import test_rpn
c = rpn.calculate
T = test_rpn.TestBasics()
fns = inspect.getmembers(T, predicate=lambda x: inspect.ismethod(x) and 'test_' in x.__name__ and 'test_add' not in x.__name__ and 'test_subtract' not in x.__name__ and 'test_multiply' not in x.__name__ and 'test_divide' not in x.__name__ and 'test_badstring' not in x.__name__)
if len(fns) > 1:
	for f in fns:
		if f[0] == 'test_carat' or f[0] == 'test_exp' or f[0] == 'test_exponent' or f[0] == 'test_power3' or f[0] == 'test_exponentiation' or f[0] == 'test_power' or f[0] == 'test_expo' or f[0] == 'test_exponentiate' or f[0] == 'test_exponant':
			test_fn = f[1]
			break
	else:
		print(fns)
		assert(len(fns) == 1)
elif len(fns) == 0:
	test_fn = None
else:
	test_fn = fns[0][1]
try:
	print(">>> {}".format(rpn.calculate("2 3 ^")))
except Exception as e:
	print(">>> Fail our ^ test. " + traceback.format_exc().replace("\\n", "ç"))
try:
	if test_fn:
		print(">>> {}".format(test_fn()))
	else:
		print(">>> !! NO TEST FN")
except Exception as e:
	print(">>> Fail to pass student ^ test function. " + traceback.format_exc().replace("\\n", "ç"))
test_rpn.rpn.calculate = lambda x: -1 if "^" in x else c(x)
try:
	print(">>> {}".format(rpn.calculate("2 3 ^")))
except Exception as e:
	print(">>> Fail ^ after monkey patch. " + traceback.format_exc().replace("\\n", "ç"))
try:
	if test_fn:
		print(">>> {}".format(test_fn()))
	else:
		print(">>> !! NO TEST FN")
except T.failureException:
	print(">>> GoodFail")
except Exception as e:
	print(">>> Fail ^ (bad) test function threw an unknown exception. " + traceback.format_exc().replace("\\n", "ç"))
'''

		try:
			a = sh.python3('-c', ugly_one_liner)
			lines = [x for x in a.stdout.decode('utf-8').split('\n') if '>>>' in x]
		except Exception as e:
			print("Need to revisit nested python code")
			raise

		# golden lines should be
		# ['>>> 8', '>>> None', '>>> -1', '>>> GoodFail']

		if lines[1] == '>>> None':
			text += '<dd><strong>Test case passes valid exponentiation function [test_good: 1.0/1.0]</strong></dd>'
			grade += 1.0
		elif lines[1] == '>>> !! NO TEST FN':
			text += '<dd><strong>Could not find test case for exponentiation [test_good: 0.0/1.0]</strong></dd>'
		else:
			text += '<dd><strong>Testing for valid exponentiation function failed [test_good: 0.0/1.0]</strong></dd>'
			text += '<dd><pre>{}</pre></dd>'.format(lines[1].replace('ç', '\n'))

		if lines[3] == '>>> GoodFail':
			text += '<dd><strong>Test case catches bad exponentiation implmentation [test_bad: 1.0/1.0]</strong></dd>'
			grade += 1.0
		elif lines[3] == '>>> !! NO TEST FN':
			text += '<dd><strong>Could not find test case for exponentiation [test_bad: 0.0/1.0]</strong></dd>'
		else:
			text += '<dd><strong>Testing that bad exponentiation function fails [test_bad: 0.0/1.0]</strong></dd>'
			text += '<dd><pre>{}</pre></dd>'.format(lines[3].replace('ç', '\n'))

		if lines[0] == '>>> 8' or lines[0] == '>>> 8.0':
			text += '<dd><strong>Exponentiation implementation correct [exp: 1.0/1.0]</strong></dd>'
			grade += 1.0
		else:
			text += '<dd><strong>Testing student exponentiation function [exp: 0.0/1.0]</strong></dd>'
			text += '<dd><pre>{}</pre></dd>'.format(lines[0].replace('ç', '\n'))

	q1_entry = '''
<dt>Week 5</dt>
<dd>{:1.1f}/4.0</dd>
<dl>
{}</dl>
'''.format(grade, text)

	return grade, text



def grade(uniqname, repo):
	grade = 0;
	email = '''
<p>Hello {},</p>
<br />
<p>Your Homework&nbsp;5 has been graded.</p>
<p>Your final score is {}/4</p>
'''

	try:
		q1_grade, q1_text = grade_q1(uniqname, repo)
	except CloneError:
		print("Clone error for\n\t{} -- {}".format(uniqname, repo))
		q1_grade = 0
		q1_text = """
<p><strong>Error cloning repository.</strong> The repository given ({}) was not
public and could not be accessed.</p>""".format(repo)

	raw_grade = q1_grade

	if raw_grade <= 0.25:
		final_grade = 0
	elif raw_grade <= 2:
		final_grade = 2
	else:
		final_grade = 4

	assert final_grade in (0,2,4)

	email = email.format(uniqname, final_grade)

	if final_grade != 4:
		email += '''
<hr />
<p>If you belive there to be an issue with the grading of your assignment
reply to this email before Monday, December&nbsp;19.</p>
'''

	email += '''
<hr />
<dl>
<dt>Question&nbsp;1 [{:1.1f}/4.0]</dt>
<dl>
{}</dl>
'''.format(q1_grade, q1_text)

	#print(email)

	with open(TIMEDIR + uniqname, 'w') as w:
		w.write(email)

	with grades_lock:
		uniq_to_grade[uniqname] = final_grade


def theres_probably_a_better_way_to_do_this(args):
	try:
		grade(*args)
	except:
		print("EXCEPTION CAUSED BY {}".format(args))
		raise

def do_grading():
	for uniqname, repo in uniqs():
		theres_probably_a_better_way_to_do_this((uniqname, repo))
	#with multiprocessing.Pool(10) as p:
	#	p.map(theres_probably_a_better_way_to_do_this, uniqs())

	write_canvas_grades()

# Generate canvas-friendly csv
def write_canvas_grades():
	week = WEEK
	with open(GRADES_PATH + 'hw/grades-hw{}.csv'.format(week), 'w') as out:
		with open(GRADES_PATH + 'gradebook.csv') as csvfile:
			cgb = csv.DictReader(csvfile)

			fieldnames = (
					'Student',
					'ID',
					'SIS User ID',
					'SIS Login ID',
					'Section',
					'Homework Week {}'.format(week),
					)
			writer = csv.DictWriter(out, fieldnames=fieldnames)
			writer.writerow({
				'Student': 'Student',
				'ID': 'ID',
				'SIS User ID': 'SIS User ID',
				'SIS Login ID': 'SIS Login ID',
				'Section': 'Section',
				'Homework Week {}'.format(week): 'Homework Week {}'.format(week),
				})

			for row in cgb:
				if row['Student'] == "Student, Test":
					continue
				if row['Student'] == "    Points Possible":
					continue
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
						'Homework Week {}'.format(week): score,
						}
				writer.writerow(to_write)

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

