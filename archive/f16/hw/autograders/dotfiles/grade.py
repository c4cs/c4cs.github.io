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

GRADES_PATH = '../../../../../../f16_grades/'
WEEK=10

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
	SUBJECT = "[C4CS] Homework 10 Graded"
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
				raise NotImplementedError("No permission")
			raise

		# Since we're hammering the gitlab server, rarely the first will
		# timeout, but this second chance will succeed. Create a repo object
		# from the path in that case.
		repo = git.Repo(to_path)
		return repo, to_path


TOTAL_COMMITS_THRESHOLD = 5

other_dotfiles = set()
no_bash = set()
no_dotfiles = set()

def grade_q1(uniqname, repo):
	repo, path = clone('wk10-dotfiles', uniqname, repo)

	with sh.pushd(path):
		# Handle cases where people put stuff in a folder:
		if os.path.exists(os.path.join(path, 'configs')):
			files = set(sh.ls('-a', 'configs').split())
		elif os.path.exists(os.path.join(path, 'bash')):
			files = set(sh.ls('-a', 'bash').split())
		elif os.path.exists(os.path.join(path, 'dotfiles')):
			files = set(sh.ls('-a', 'dotfiles').split())
		elif os.path.exists(os.path.join(path, 'shell')):
			files = set(sh.ls('-a', 'shell').split())
		elif os.path.exists(os.path.join(path, 'ssh_configs')):
			files = set(sh.ls('-a', 'ssh_configs').split())
		else:
			# Common case
			files = set(sh.ls('-a').split())
		files.discard('.')
		files.discard('..')
		files.discard('.git')
		text = ''
		grade = 0

		# Viable .bashrc targets we've seen or are in the spirit of the Q
		bashrc = set((
			'.bashrc',
			'bashrc',
			'bash.bashrc',
			'.bash_profile',
			'bash_profile',
			'.zshrc',
			'zshrc',
			'mybashrc',
			'bashrc1',
			))

		if len(files.intersection(bashrc)):
			# Bashrc file
			text += '<dd><strong>.bashrc [2.0/2.0]</strong></dd>\n'
			grade += 2.0
		else:
			text += '<dd><strong>.bashrc [0.0/2.0]</strong></dd>\n'
			text += '<dd>Output of <tt>find .</tt></dd>\n'
			text += '<dd><pre>{}</pre></dd>\n'.format(sh.find('.'))
			with grades_lock:
				no_bash.add(uniqname)
			grade += 0.0

		others = files - bashrc
		nonfiles = set((
			'3',
			'__pycache__',
			'.DS_Store',
			'.bashrc.swp',
			'.make.sh',
			'.ssh-config.swp',
			'a',
			'a.h',
			'a.cpp',
			'autoload',
			'backup.sh',
			'bin'
			'bootstrap.sh',
			'clean.sh',
			'copy.sh',
			'dotfiles_old',
			'file1.txt',
			'file2.txt',
			'file3.txt',
			'games',
			'hello.sh',
			'init',
			'init.sh',
			'install.sh',
			'install-list.txt',
			'ls',
			'LICENSE',
			'LICENSE.txt',
			'LICENSE-MIT.txt',
			'link.sh',
			'link_files.sh',
			'make_symlink.sh',
			'make_symlinks.sh',
			'makesymlinks.sh',
			'main.py',
			'main.pyc',
			'make.sh',
			'os',
			'pro.py',
			'prog.cpp',
			'q2.py',
			'q3.py',
			'README',
			'README.md',
			'readme.md',
			'README.txt',
			'scripts',
			'set_up.sh',
			'setup_dotfiles.sh',
			'setupDotfiles.sh',
			'shell',
			'something.txt',
			'source.sh',
			'status_repos.py',
			'system_spec',
			'test',
			'test1',
			'test1.cpp',
			'test2.cpp',
			'test3.cpp',
			'trial.py',
			'update.sh',
			'update_repos.py',
			'updateall.sh',
			'updatebashrc.sh',
			'updatesymlinks.sh',
			'x',
			))

		others = others - nonfiles

		with grades_lock:
			for o in others:
				other_dotfiles.add(o)

		if len(others):
			# Any other dotfile
			text += '<dd><strong>Any other dotfile ({}) [2.0/2.0]</strong></dd>\n'.format(others.pop())
			grade += 2.0
		else:
			text += '<dd><strong>Any other dotfile [0.0/2.0]</strong></dd>\n'
			text += '<dd>Output of <tt>find .</tt></dd>\n'
			text += '<dd><pre>{}</pre></dd>\n'.format(sh.find('.'))
			grade += 0.0
			no_dotfiles.add(uniqname)

	q1_entry = '''
<dt>Week 10</dt>
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
<p>Your Homework&nbsp;10 has been graded.</p>
<p>Your final score is {}/4</p>
'''

	try:
		q1_grade, q1_text = grade_q1(uniqname, repo)
	except NotImplementedError:
		print("Clone error for\n\t{} -- {}".format(uniqname, repo))
		q1_grade = 0
		q1_text = """
<p><strong>Error cloning repository.</strong> The repository given ({}) was not
public and could not be accessed.</p>""".format(repo)

	raw_grade = q1_grade
	final_grade = math.ceil(raw_grade)

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

	print("NO BASH -- These submissions lost points for missing a .bashrc:")
	print(no_bash)
	print('')
	print("OTHER DOTFILES -- These files were considered valid dotfiles, may want")
	print("                  to add specious entries to the nonfiles set")
	print(other_dotfiles)
	print('')
	print("NO DOTFILES -- These submissions lost points for not having any dotfiles:")
	print(no_dotfiles)

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

