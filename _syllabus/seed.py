#!/usr/bin/env python3

import arrow

template = """---
week: {week}
dates: {lecDate}
lecturer: mmdarden
homeworkRelease: {hwDate}
solutionRelease: {solDate}
title: "{title}"
# lectureTopics:
#   - TBD
# homeworkTopics:
#   - TBD
# advancedTopics:
#   - TBD
lectureSummary:
leccapWed:
leccapFri:
---
"""

lectures = [
    {
    'date': '01/06/2017',
    'title': 'Introduction, Virtual Machines, & Command Line Primer'
    }, {
    'date': '01/13/2017',
    'title': 'Basic Git'
    }, {
    'date': '01/20/2017',
    'title': 'Shells, Environment, Scripting, and Bash'
    }, {
    'date': '01/27/2017',
    'title': 'Editors'
    }, {
    'date': '02/03/2017',
    'title': 'Git II'
    }, {
    'date': '02/10/2017',
    'title': 'Unix II'
    }, {
    'date': '02/17/2017',
    'title': 'Build Systems'
    }, {
    'date': '02/24/2017',
    'title': 'Optional Lecture: TBD'
    }, {
    'date': '03/03/2017',
    'title': 'Spring break no lecture'
    }, {
    'date': '03/10/2017',
    'title': 'Unit Testing and Python'
    }, {
    'date': '03/17/2017',
    'title': 'Debuggers'
    }, {
    'date': '03/24/2017',
    'title': 'Package Managers & Development Environment'
    }, {
    'date': '03/31/2017',
    'title': 'IDEs'
    }, {
    'date': '04/07/2017',
    'title': 'A Sampling of Other Things'
    }, {
    'date': '04/14/2017',
    'title': 'TBA - Staff'
    }
]

for idx, lecture in enumerate(lectures):
    with open('w17/week{0:02d}.md'.format(idx + 1), 'w') as f:
        lecDate = arrow.get(lecture['date'], 'MM/DD/YYYY')
        hwDate  = lecDate.replace(hours=15)
        solDate = hwDate.shift(weeks=1)

        weekData = template.format(
            lecDate= lecDate.format('MM/DD/YYYY'),
            hwDate= hwDate.format('YYYY-MM-DD HH:mm:ss'),
            solDate= solDate.format('YYYY-MM-DD HH:mm:ss'),
            title= lecture['title'],
            week= idx + 1,
        )

        f.write(weekData)
