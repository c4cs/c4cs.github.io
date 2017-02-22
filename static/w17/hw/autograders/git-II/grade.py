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

from fuzzywuzzy import fuzz

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import git # pip install gitpython

# Get an updated version of sh with proper pushd support
# sys.path.insert(0, '/Users/ppannuto/code/sh')
import sh
from sh import mkdir, rm

GRADES_PATH = '/home/mterwilliger/Downloads/'

if 'rerun' not in sys.argv:
    if os.path.exists('/tmp/q1') or os.path.exists('/tmp/q2a') or os.path.exists('/tmp/q2b'):
        input('WARN: About to delete old runs. Use "rerun" to run again. Ctrl-C to quit, enter to continue')
    rm('-r', '-f', '/tmp/q1')
    rm('-r', '-f', '/tmp/q2a')
    rm('-r', '-f', '/tmp/q2b')

for a in sys.argv:
    if '/emails/' in a:
        TIMEDIR = a
        break
else:
    TIME = time.asctime()
    TIMEDIR = '/tmp/emails/'+TIME+'/'

mkdir('-p', TIMEDIR)

ACTUALLY_SEND = False


def uniqs():
    with open(GRADES_PATH + 'gradebook.csv') as csvfile:
        r = csv.DictReader(csvfile)
        for row in r:
            uniq = row['SIS Login ID']
            name = row['Student']
            if name == 'Student, Test':
                continue
            if name == '    Points Possible':
                continue
            print('------')
            print(uniq)
            print(name)
            print('------')
            name = ' '.join(reversed(list(map(str.strip, name.split(',')))))
            yield uniq, name

uniq_to_grade = {}

with open('email.cfg') as e:
    SMTP_HOST = e.readline().strip()
    SMTP_USER = e.readline().strip()
    SMTP_PASS = e.readline().strip()
    
sm = None

def send_email(uniqname, body):
    SUBJECT = "[C4CS] Homework 5 Graded"
    FROM = 'c4cs-staff@umich.edu'
    TO = uniqname + '@umich.edu'
    #TO = 'mterwil' + '@umich.edu'
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
            sm = smtplib.SMTP_SSL(host=SMTP_HOST)
            sm.login(SMTP_USER, SMTP_PASS)

        #send_to = [TO,] + CC
        send_to = [TO,]
        sm.sendmail(FROM, send_to, msg.as_string())

def clone(root, uniqname, project):
    into='/tmp/'+root
    mkdir('-p', into)
    url='git@gitlab.eecs.umich.edu:' + uniqname + '/' + project
    to_path=into + '/' + uniqname

    if 'rerun' in sys.argv:
        if os.path.exists(to_path):
            print('cached {}'.format(to_path))
            repo = git.Repo(to_path)
            return repo, to_path

    print('clone {}/{}'.format(uniqname, project))
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
            raise

        # Since we're hammering the gitlab server, rarely the first will
        # timeout, but this second chance will succeed. Create a repo object
        # from the path in that case.
        repo = git.Repo(to_path)
        return repo, to_path


TOTAL_COMMITS_THRESHOLD = 5

def grade_q1(uniqname):
    try:
        repo,path = clone('q1', uniqname, 'c4cs-w17-wk5')
    except sh.ErrorReturnCode as e:
        text = '''
<p><strong>Error! Failed to clone {}</strong></p>
<p>Ran command: <tt>{}</tt></p>
<p>stdout:</p>
<pre>
{}
</pre></p>
<p>stderr:</p>
<pre>
{}
</pre>
'''.format('c4cs-w17-wk5', e.full_cmd, e.stdout.decode('utf8'), e.stderr.decode('utf8'))
        return 0, text

    non_merge_count = 0
    non_single_line_count = 0
    TINY_SUMMARY_THRESHOLD = 12
    tiny_summary_line_count = 0
    LONG_SUMMARY_THRESHOLD = 72
    long_summary_line_count = 0
    non_blank_second_lines = None
    giant_body_lines = 0

    first_commit = True
    total_lines_changed = 0
    MINI_LINES_THRESHOLD = 4
    mini_lines_changed = 0
    MANY_LINES_THRESHOLD = 50
    many_lines_changed = 0

    try:
        next(repo.iter_commits('master'))
    except git.exc.GitCommandError:
        text = '''
    <dt>Question 1</dt>
    <dd>0.0/2.0</dd>
    <dl><dd>No master branch or no commits on master branch</dd></dl>
    '''
        return 0, text

    for commit in repo.iter_commits('master'):
        # Skip merge commits
        if len(commit.parents) > 1:
            if commit.message[:len('Merge')] == 'Merge':
                continue
            else:
                print(commit)
                print(commit.parents)
                print(commit.message)
                #raise NotImplementedError("Check me, multi-parents no merge string")
                continue
        non_merge_count += 1


        # Commit message quality
        lines = commit.message.strip().split('\n')

        if len(lines[0]) < TINY_SUMMARY_THRESHOLD:
            tiny_summary_line_count += 1

        if len(lines[0]) > LONG_SUMMARY_THRESHOLD:
            long_summary_line_count += 1

        if len(lines) > 1:
            non_single_line_count += 1
            if lines[1].strip() != '':
                non_blank_second_lines = commit

            for line in lines[2:]:
                if len(line) > 80:
                    if line[0:2] == '  ' or line[0] == '>':
                        # Ignore quoted stuff
                        continue

                    giant_body_lines += 1
                    # only count first instance
                    break


        # Commit content quality
        if first_commit:
            first_commit = False
            continue

        # commit.stats.total
        # {'deletions': 1, 'lines': 2, 'insertions': 1, 'files': 1}
        # commit.stats.files
        # {'filename': {'deletions': 1, 'lines': 2, 'insertions': 1}}
        total_lines_changed += commit.stats.total['lines']

        if commit.stats.total['lines'] < MINI_LINES_THRESHOLD:
            mini_lines_changed += 1
        if commit.stats.total['lines'] > MANY_LINES_THRESHOLD:
            many_lines_changed += 1

    text = ''
    grade = 0

    text += '<dt>Used git for an EECS project</dt>\n'
    if non_merge_count < TOTAL_COMMITS_THRESHOLD:
        text += '<dd>[0.0/2.0]. There is not enough history here to have realistically used git effectively (only {} non-merge commit{}).</dd>\n'.format(
                        non_merge_count, '' if non_merge_count==1 else 's')
    else:
        # Base points for using git at all: 0.2
        text += '<dd><strong>Used git [base 0.2]</strong></dd>\n'
        grade += 0.2

        # Summary quality: 0.6
        text += '<dd><strong>Summary Quality [base 0.6]</strong></dd>\n'
        grade += 0.6
        # -- No more than 25% tiny: 0.3
        if tiny_summary_line_count / non_merge_count > 0.25:
            text += '<dd>[-0.3]: Too many tiny summaries</dd>\n'
            grade -= 0.3
        # -- No more than 10% huge: 0.3
        if long_summary_line_count / non_merge_count > 0.10:
            text += '<dd>[-0.3]: Too many huge summaries</dd>\n'
            grade -= 0.3

        # Multi-line (explained) commits: 0.6
        # -- Base score:
        text += '<dd><strong>Complex commits [base 0.6]</strong></dd>\n'
        grade += 0.6
        #    0-none
        if non_single_line_count == 0:
            text += '<dd>[-0.6] All single line commits</dd>\n'
            grade -= 0.6
        #   Minus Commit Body Style
        else:
            # Base Score:
            # 0.4-any, 0.6-enough
            if non_single_line_count / non_merge_count < 0.1:
                text += '<dd>[-0.2] Too few detailed commits</dd>\n'
                text += '<ul><li>\
While short, single-line commit messages are good enough for most \
commits, sometimes the changes really do require a little more \
explanation. It is a good idea to get in the habit of jotting down \
even just an extra line or two as a quick note.\
</li></ul>\n'
                grade -= 0.2

            #   -- Non-blank second lines: -0.2
            if non_blank_second_lines is not None:
                text += '<dd>[-0.2] Commits ({}) with non-blank second lines</dd>\n'.format(non_blank_second_lines)
                grade -= 0.2

            #   -- Giant lines in commit body: -0.2
            if giant_body_lines > 0:
                text += '<dd>[-0.2] Commits with long lines (> 80 charcter) in body</dd>\n'
                grade -= 0.2

        # Commit content: 0.6
        text += '<dd><strong>Commit size [base 0.6]</strong></dd>\n'
        grade += 0.6
        # -- No more than 25% tiny: 0.3
        if mini_lines_changed / non_merge_count > 0.25:
            text += '<dd>[-0.3]: Too many tiny commits.</dd>\n'
            grade -= 0.3
        # -- No more than 25% huge: 0.3
        if many_lines_changed / non_merge_count > 0.25:
            text += '<dd>[-0.3]: Too many giant commits.</dd>\n'
            grade -= 0.3

    q1_entry = '''
<dt>Question 1</dt>
<dd>{:1.1f}/2.0</dd>
<dl>
{}</dl>
'''.format(grade, text)

    return grade, text



def grade_q2a(uniqname):
    try:
        repo,path = clone('q2a', uniqname, 'c4cs-w17-conflict1')
    except sh.ErrorReturnCode as e:
        text = '''
<p><strong>Error! Failed to clone {}</strong></p>
<p>Ran command: <tt>{}</tt></p>
<p>stdout:</p>
<pre>
{}
</pre></p>
<p>stderr:</p>
<pre>
{}
</pre>
'''.format('c4cs-w17-conflict1', e.full_cmd, e.stdout.decode('utf8'), e.stderr.decode('utf8'))
        return 0, text


    with sh.pushd(path):
        golden = '''\
Welcome to the simple test program

According to current estimates, the diag construction will be done:
Summer 2017.
'''
        test_golden = '''\
Success
'''
        text = ''
        grade = 0

        text += '<dd><strong>Merge content conflict [base 1.0]</strong></dd>\n'
        grade += 1.0


        if not os.path.exists('main.py'):
            text += '<dd>No <tt>main.py</tt> in repository [-1.0]</dd>'
            grade -= 1.0
        elif not os.path.exists('test.sh'):
            text += '<dd>No <tt>test.sh</tt> in repository [-1.0]</dd>'
            grade -= 1.0
        else:
            mainpy = open('main.py').read()
            testsh = open('test.sh').read()
            if ('>>>>' in mainpy) or ('<<<<' in mainpy):
                text += '<dd>Unresolved conflict in <tt>main.py</tt>.  Contents:<pre>{}</pre></dd>'.format(mainpy)
                grade -= 1.0
            elif ('>>>>' in testsh) or ('<<<<' in testsh):
                text += '<dd>Unresolved conflict in <tt>test.sh</tt>.  Contents:<pre>{}</pre></dd>'.format(testsh)
                grade -= 1.0
            else:
                try:
                    out = sh.python('main.py')
                    test_out = sh.bash('test.sh')

                    if ('diag construction' not in out) or ('Summer 2017' not in out):
                        text += '<dd><tt>main.py</tt> content not merged, missing diag construction or completion date [-1.0]. Output of main.py:<pre>{}</pre></dd>'.format(out)
                        grade -= 1.0
                    else:
                        # fuzz is a fuzzy string matching library that should
                        # allow for modest formatting or text differences
                        if fuzz.ratio(out, golden) < 75:
                            text += '<dd>Output of main.py seems to be a merge, but not quite correct [-0.4]. Expected <pre>{}</pre>, student main.py output <pre>{}</pre>'.format(golden, out)
                            grade -= 0.4

                        if fuzz.ratio(test_out, test_golden) < 75:
                            text += '<dd><tt>test.sh</tt> does not report success [-0.4].  Output of test.sh:<pre>{}</pre></dd>'.format(test_out)
                            grade -= 0.4

                except sh.ErrorReturnCode as e:
                    text += '<dd><tt>main.py</tt> or <tt>test.sh</tt> does not run [-1.0]. Output <pre>Ran {}\n\nStdout\n{}Stderr\n{}</pre></dd>'.format(e.full_cmd, e.stdout.decode('utf8'), e.stderr.decode('utf8'))
                    grade -= 1.0

            if grade == 1.0:
                text += '<dd>All correct!</dd>'

    q2a_entry = '''
<dt>Question 2a</dt>
<dd>{:1.1f}/1.0</dd>
<dl>
{}</dl>
'''.format(grade, text)

    return grade, text


def grade_q2b(uniqname):
    try:
        repo,path = clone('q2b', uniqname, 'c4cs-w17-conflict2')
    except sh.ErrorReturnCode as e:
        text = '''
<p><strong>Error! Failed to clone {}</strong></p>
<p>Ran command: <tt>{}</tt></p>
<p>stdout:</p>
<pre>
{}
</pre></p>
<p>stderr:</p>
<pre>
{}
</pre>
'''.format('c4cs-w17-conflict2', e.full_cmd, e.stdout.decode('utf8'), e.stderr.decode('utf8'))
        return 0, text

    with sh.pushd(path):
        golden = '''\
main.py
README.md
sales-2016-03-01
sales-2016-03-02
sales-2016-03-03
'''
        out = sh.ls('-1')

        text = ''
        grade = 0

        text += '<dd><strong>Merge path conflict [base 1.0]</strong></dd>\n'
        grade += 1.0

        if out == golden:
            text += '<dd>All correct!</dd>'
        else:
            text += '<dd>Incorrect files in directory after merge [-1.0]. Expected <pre>{}</pre>, but got <pre>{}</pre></dd>'.format(golden, out)
            grade -= 1.0

    q2b_entry = '''
<dt>Question 2b</dt>
<dd>{:1.1f}/1.0</dd>
<dl>
{}</dl>
'''.format(grade, text)

    return grade, text



def grade():
    for uniqname, name in uniqs():
        print("grading {}".format(uniqname))
        grade = 0;
        email = '''
<p>Hello {},</p>
<br />
<p>Your Homework&nbsp;5 has been graded.</p>
<p>Your raw score is {:1.1f}/4.0.</p>
<p>Your final score is {}/4.</p>
'''

        q1_grade, q1_text = grade_q1(uniqname)

        q2a_grade, q2a_text = grade_q2a(uniqname)
        q2b_grade, q2b_text = grade_q2b(uniqname)

        raw_grade = q1_grade + q2a_grade + q2b_grade
        if raw_grade <= 0.25:
            final_grade = 0
        elif raw_grade <= 2:
            final_grade = 2
        else:
            final_grade = 4

        assert final_grade in (0,2,4)

        email = email.format(name, raw_grade, final_grade)

        if final_grade != 4:
            email += '''
<hr />
<p>If you believe there to be an issue with the grading of your assignment
reply to this email before Monday, March&nbsp;13.</p>
<p>If you would like more information on how your assignment was graded, you can
look over the <a href="https://github.com/c4cs/c4cs.github.io/blob/master/static/w17/hw/autograders/git-II/grade.py">autograder script</a></p>.
'''

        email += '''
<hr />
<dl>
<dt>Question&nbsp;1 [{:1.1f}/2.0]</dt>
<dl>
{}</dl>
<dt>Question&nbsp;2a [{:1.1f}/1.0]</dt>
<dl>
{}</dl>
<dt>Question&nbsp;2b [{:1.1f}/1.0]</dt>
<dl>
{}</dl>
'''.format(q1_grade, q1_text, q2a_grade, q2a_text, q2b_grade, q2b_text)

        with open(TIMEDIR + uniqname, 'w') as w:
            w.write(email)

        uniq_to_grade[uniqname] = final_grade

        #break
        time.sleep(1)


def do_check_clone(uniqname, name):
    print(uniqname)
    email = '''
<p>Hello {},</p>
<br />
<p>This e-mail is a test run that verifies that the autograder can
access all of your repositories for this assignment.</p>
<p>This is the final test run before final grading Saturday night.</p>
<p><strong>NOTE:</strong> Repositories must be named exactly correctly!</p>
'''.format(name)
    for q, repo in (
            ('1', 'c4cs-w17-wk5'),
            ('2a', 'c4cs-w17-conflict1'),
            ('2b', 'c4cs-w17-conflict2'),
            ):
        try:
            email += '<hr /><h3>Question {} ({})</h3>'.format(q,repo)
            ref = clone('q' + q, uniqname, repo)[0]
            try:
                head = ref.head.reference.commit
                email += '''
<p>Cloned sucessfully.</p>
<p>The most recent commit is {}:</p>
<pre>{}</pre>
'''.format(head.hexsha[:6], head.message)
                if q == '1':
                    count = sum(1 for c in ref.iter_commits())
                    if count < TOTAL_COMMITS_THRESHOLD:
                        email += '''
<h3>Warning</h3>
<p>This repository only has {} commit{}, far too few to be a repository
that was actually used for a project. Are you sure you pushed the
correct repository?</p>
'''.format(count, '' if count == 1 else 's')
            except ValueError:
                email += '''
<p><strong>Error! This repository is empty (has no commits)</strong></p>
'''
        except sh.ErrorReturnCode as e:
            email += '''
<p><strong>Error! Failed to clone {}</strong></p>
<p>Ran command: <tt>{}</tt></p>
<p>stdout:</p>
<pre>
{}
</pre></p>
<p>stderr:</p>
<pre>
{}
</pre>
'''.format(repo, e.full_cmd, e.stdout.decode('utf8'), e.stderr.decode('utf8'))

    send_email(uniqname, email)

    with open(TIMEDIR + uniqname, 'w') as w:
        w.write(email)

def theres_probably_a_better_way_to_do_this(args):
    if 'rerun' in sys.argv:
        if os.path.exists(TIMEDIR + args[0]):
            return
    try:
        do_check_clone(*args)
    except:
        print("EXCEPTION CAUSED BY {}".format(args))
        raise

def check_clones():
    #for uniqname, name in uniqs():
    #    do_check_clone(uniqname, name)
    with multiprocessing.Pool(4) as p:
        p.map(theres_probably_a_better_way_to_do_this, uniqs())


# Generate canvas-friendly csv

def write_canvas_grades():
    week = 5
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
    if 'clone' in sys.argv:
        check_clones()
    if 'grade' in sys.argv:
        grade()
        write_canvas_grades()

