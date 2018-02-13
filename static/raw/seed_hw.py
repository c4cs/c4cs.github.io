#!/usr/bin/env python3


import arrow
import os
import re
import sys


# see https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.insert(0, '../../_syllabus')
# import the lectures from the other seed file for the syllabus so we don't have
# two copies of the lecture dates floating around
from seed import lectures

COURSE_SEMESTER = 'F' # Fall = 'F'; Winter = 'W'
COURSE_YEAR = '17' # 2017 = 17; 2017 = 18
GRADESCOPE_COURSE_NUMBER = '9999' # find this on gradescope.com

HW_TEMPLATE_HEADER = "\\\\\\fancyhead[C]{\\\\\\hl{Select the right page in Gradescope or we will not grade the question!}}\\\\\n" +\
"\\\\\\fancyhead[L]{}\\\\\n" +\
"\\\\\\fancyhead[R]{}\\\\\n" +\
"\\\\\n"

HW_TEMPLATE_BODY = "\\\\\\fancyfoot[L]{\\\\\\color{gray} C4CS -- %s}\\\\\n" +\
"\\\\\\fancyfoot[R]{\\\\\\color{gray} Revision %s}\\\\\n" +\
"\\\\\\fancyfoot[C]{\\\\\\color{gray} \\\\\\thepage\~\/\~\\\\\\pageref*{LastPage}}\\\\\n" +\
"\\\\\\pagestyle{fancyplain}\\\\\n" +\
"\\\\\n" +\
"\\\\\\title{\\\\\\textbf{%s %s\\\\\\\\\\\\\%s}}\\\\\n" +\
"\\\\\\author{\\\\\\textbf{\\\\\\color{red}{Due: %s (Hard Deadline)}}}\\\\\n" +\
"\\\\\\date{}\\\\\n" +\
"\\\\\\maketitle\\\\\n" +\
"\\\\\n" +\
"\\\\\n"

GRADESCOPE_SUBMISSION_INSTRUCTIONS = "\\\\\\section*{Submission Instructions}\\\\\n" +\
"Submit this assignment on \\\\\\\href{https:\/\/gradescope.com\/courses\/%s}{Gradescope}.\\\\\n" +\
"You may find the free online tool \\\\\\\href{https:\/\/www.pdfescape.com}{PDFescape}\\\\\n" +\
"helpful to edit and fill out this PDF.\\\\\n" +\
"You may also print, handwrite, and scan this assignment."

GITLAB_SUBMISSION_INSTRUCTIONS = "\\\\\\section*{Submission Instructions}\\\\\n" +\
"For this assignment, all of your submissions will be to GitLab."

GITHUB_SUBMISSION_INSTRUCTIONS = "\\\\\\section*{Submission Instructions}\\\\\n" +\
"When you are done, submit a link to your GitHub repository here: \\\\\\\\url{%s}"

SCREENSHOT_SUBMISSION_INSTRUCTIONS = "\\\\\\section*{Submission Instructions}\\\\\n" +\
"Submit screenshots with 1-3 descriptive paragraphs of what is shown, and how it\\\\\n" +\
"was a learning experience for you. Alternately, visit a TA during office hours\\\\\n" +\
"and have a show and tell about what you did and learned."

ADVANCED_HW_SUBMISSION_INSTRUCTIONS = "\\\\\\section*{Submission Instructions}\\\\\n" +\
"To receive credit for this assignment you will need to stop by someone's\\\\\n" +\
"office hours, demo your running code, and answer some questions. \\\\\\textbf{\\\\\\color{red}{Make sure\\\\\n" +\
"to check the office hour schedule as the real due date is at the last office\\\\\n" +\
"hours before the date listed above.}} This applies to assignments that need to be gone over with a TA only.\\\\\n" +\
"\\\\\\textbf{Extra credit is given for early turn-ins of advanced exercises. These details " +\
"can be found on the website under the advanced homework grading policy.}"


hw_info = [
    {
    'week': 1,
    'title': 'Welcome, Setup, and Some Light Reading',
    'revision': '1.0',
    'advanced': {}
    },
    {
    'week': 2,
    'title': 'Git',
    'revision': '1.0',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 3,
    'title': 'Shells, Environment, and Scripting',
    'revision': '1.0',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 4,
    'title': 'Editors',
    'revision': '1.0',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 5,
    'title': 'Git II',
    'revision': '1.0',
    'submission': GITLAB_SUBMISSION_INSTRUCTIONS,
    'advanced':
        {
        'revision':'1.0',
        'submission': ' ', # contribute to open source, no in person submission
        },
    },
    {
    'week': 6,
    'title': 'Practical Regexes and Synthesis of Rich Commands',
    'revision': '1.0',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 7,
    'title': 'Build Systems',
    'revision': '1.0',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 8,
    'title': 'Unit Testing and Python',
    'revision': '1.0',
    'submission': GITHUB_SUBMISSION_INSTRUCTIONS,
    'submission_link': 'https:\/\/docs.google.com\/forms\/d\/e\/1FAIpQLSezdSOWRusASNmkSQ458Alw1EjtqqvxVvT7eYfr04Rnb62F8g\/viewform?usp=sf_link',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 9,
    'title': 'Debugging',
    'revision': '1.1',
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 10,
    'title': 'Towards a Development Environment',
    'revision': '1.0',
    'submission': GITHUB_SUBMISSION_INSTRUCTIONS,
    'submission_link': 'https:\/\/docs.google.com\/forms\/d\/e\/1FAIpQLSf0-UO8GcD7vi3KT98Ss4aNt13ywu5vpKdLWhbYv0boV0xEKg\/viewform',
    'advanced':
        {
        'revision':'1.1',
        },
    },
    {
    'week': 11,
    'title': 'IDEs',
    'revision': '1.0',
    'submission': SCREENSHOT_SUBMISSION_INSTRUCTIONS,
    'advanced':
        {
        'revision':'1.0',
        },
    },
    {
    'week': 13,
    'title': 'Profiling, Linting, and Static Analysis',
    'revision': '1.0',
    'advanced':
        {
        'revision':'1.0',
        },
    },
]


_HEADER_INSERT_KEYWORDS = "%%% TITLE INFO INSERTED HERE AUTOMATICALLY"
def seed_all_hw(cur_sem_hw_dir):

    for abs_week_num, hw in enumerate(hw_info):
        abs_week_num += 1
        # do hw
        hw_template = get_header(hw) + get_body(hw, 'Homework') + get_submission(hw)
        filename = get_filename(hw['week'], 'homework')
        copy_file_to_dest(abs_week_num, hw, 'homework', 'hw', cur_sem_hw_dir)
        insert_header_into_tex_file(hw_template, cur_sem_hw_dir, 'hw', filename)

        # do adv hw
        if not hw.get('advanced'):
            # no advanced hw this week
            continue

        adv_hw_template = get_body_adv(hw) + get_adv_submission(hw['advanced'])
        filename = get_filename(hw['week'], 'advanced')
        copy_file_to_dest(abs_week_num, hw, 'advanced', 'advanced', cur_sem_hw_dir)
        insert_header_into_tex_file(adv_hw_template, cur_sem_hw_dir, 'advanced', filename)

def copy_src_files(cur_sem_hw_dir):
    """ Copy src files such as images and `.tar.gz`s to the destination directory"""
    for directory in ['./advanced/src', './hw/src']:
        for (dirpath, dirname, filenames) in os.walk(directory):
            if len(filenames) == 0:
                continue
            for filename in filenames:
                src_path = get_path(dirpath, filename)
                # cut off the '/src' part since that's not in the destination
                # directory
                dest_path = get_destination_path(cur_sem_hw_dir, dirpath[:-4], filename)
                copy_file(src_path, dest_path)


def insert_header_into_tex_file(template, cur_sem_hw_dir, hw_type, file_to_modify):
    dest_file = get_destination_path(cur_sem_hw_dir, hw_type, file_to_modify)
    os.system("sed -i '' -e \"s/{find}/{replace}/g\" {dest_file}".format(
        find=_HEADER_INSERT_KEYWORDS,
        replace=template,
        dest_file=dest_file
    ))

def copy_file_to_dest(abs_week_num, hw, file_type, hw_type, cur_sem_hw_dir):
    # source file is absolute week numbering, meaning there are no skips in weeks 1-12
    src_file = get_filename(abs_week_num, file_type)
    src_path = get_path(hw_type, src_file)
    # destination file will have relative week numbering, meaning there are
    # skips in weeks for holidays/breaks
    dest_file = get_filename(hw['week'], file_type)
    dest_path = get_destination_path(cur_sem_hw_dir, hw_type, dest_file)
    copy_file(src_path, dest_path)

def get_path(directory, filename):
    src_path = './{directory}/{filename}'.format(
        directory=directory,
        filename=filename
    )
    return src_path

def copy_file(src_path, dest_path):
    os.system("cp {src_path} {dest_path}".format(
        src_path=src_path,
        dest_path=dest_path
    ))

def get_destination_path(cur_sem_hw_dir, hw_type, dest_file):
    dest_path = '../{semester}/{hw_type}/{dest_filename}'.format(
        semester=cur_sem_hw_dir,
        hw_type=hw_type,
        dest_filename=dest_file
    )
    return dest_path

def get_cur_sem_dir(sem, year):
    return "{semester}{year}".format(semester=sem.lower(), year=year)

def get_filename(week, hw_type):
    return 'c4cs-wk{week}-{hw_type}.tex'.format(
        week=week,
        hw_type=hw_type
    )

def get_header(hw):
    if hw.get('submission_link'):
        return ''
    # don't need the header when they submit screenshots
    elif hw.get('submission') and 'screenshot' in hw.get('submission'):
        return ''
    return HW_TEMPLATE_HEADER

def get_body(hw, hw_type):
    FULL_COURSE_YEAR = COURSE_SEMESTER + '\'' + COURSE_YEAR
    # lookup the lecture date by the homework week number (-1 because of 0 indexing)
    release_date = arrow.get(lectures[hw['week']-1]['date'], 'MM/DD/YYYY')
    # calculate the submission date based on the release date
    due_date = release_date.replace(hours=11).shift(weeks=1, days=5,
            hours=12, minutes=59)
    # format the submission date as is custom for the homework
    due_date = due_date.format('dddd, MMMM Do, h:mmA')
    return HW_TEMPLATE_BODY % (FULL_COURSE_YEAR, hw['revision'], hw_type,
            hw['week'], hw['title'], due_date)

def get_body_adv(hw):
    hw['title'] = ''
    if hw.get('advanced'):
        hw['revision'] = hw['advanced'].get('revision')
    return get_body(hw, 'Advanced Homework')


def get_submission(hw):
    """Returns the correct submission directions based on what links are/aren't available"""
    if hw.get('submission'):
        if hw.get('submission_link'):
            return hw.get('submission') % hw.get('submission_link')
        return hw.get('submission')
    return GRADESCOPE_SUBMISSION_INSTRUCTIONS % GRADESCOPE_COURSE_NUMBER

def get_adv_submission(hw):
    if hw.get('submission') == '':
        return ''
    return ADVANCED_HW_SUBMISSION_INSTRUCTIONS



if __name__ == "__main__":
    print("!!! You must build the PDFs yourself after this process is done. !!!")
    print("Running the following in the ../semester/hw and " +\
          "../semester/advanced directories should create the pdfs:")
    print("`for file in *.tex; do pdflatex $file; pdflatex $file; rm *.out *.log *.aux; done`")
    cur_sem_hw_dir = get_cur_sem_dir(COURSE_SEMESTER, COURSE_YEAR)
    seed_all_hw(cur_sem_hw_dir)
    copy_src_files(cur_sem_hw_dir)
