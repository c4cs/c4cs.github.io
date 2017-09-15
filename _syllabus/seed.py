#!/usr/bin/env python3

import arrow

template = """---
sectionHeader:{sectionHeader}
week: {week}
dates: {lecDate}
lecturer: mmdarden
homeworkRelease: {hwDate}
advancedThisWeek: {advThisWeek}
solutionRelease: {solDate}
title: "{title}"
# lectureTopics:
#   - TBD
# homeworkTopics:
#   - TBD
# advancedTopics:
#   - TBD
lectureSummary:
leccapFri:
---
"""

lectures = [
    {
    'sectionHeader': 'Introduction and Basics',
    'date': '09/08/2017',
    'title': 'Introduction, Virtual Machines, & Command Line Primer',
    'adv': 'false'
    }, {
    'date': '09/15/2017',
    'title': 'Basic Git'
    }, {
    'date': '09/22/2017',
    'title': 'Shells, Environment, Scripting, and Bash'
    }, {
    'sectionHeader': 'Being Efficient',
    'date': '09/29/2017',
    'title': 'Editors'
    }, {
    'date': '10/06/2017',
    'title': 'Git II'
    }, {
    'date': '10/13/2017',
    'title': 'Unix II'
    }, {
    'sectionHeader': 'Developing',
    'date': '10/20/2017',
    'title': 'Build Systems'
    }, {
    'date': '10/27/2017',
    'title': 'Unit Testing and Python'
    }, {
    'date': '11/03/2017',
    'title': 'Debuggers'
    }, {
    'sectionHeader': 'Standing on the Shoulders of Giants',
    'date': '11/10/2017',
    'title': 'Package Managers & Development Environment'
    }, {
    'date': '11/17/2017',
    'title': 'IDEs'
    }, {
    'date': '11/24/2017',
    'title': 'No lecture, Thanksgiving break',
    'adv': 'false',
    }, {
    'date': '12/01/2017',
    'title': 'A Sampling of Other Things'
    }, {
    'date': '12/08/2017',
    'title': 'TBA - Staff'
    }
]

if __name__ == '__main__':
    for idx, lecture in enumerate(lectures):
        with open('f17/week{0:02d}.md'.format(idx + 1), 'w') as f:
            secHeader = lecture.get('sectionHeader', '')
            lecDate = arrow.get(lecture['date'], 'MM/DD/YYYY')
            # homework out at 11am (start of first lecture) each week
            hwDate  = lecDate.replace(hours=11)
            # homework due/solution released 1.5 weeks after released (due on
            # Wednesday night at midnight)
            solDate = hwDate.shift(weeks=1, days=5, hours=13)

            if secHeader != '':
                secHeader = " '{}'".format(secHeader)

            weekHasAdv = 'true'
            if lecture.get('adv'):
                weekHasAdv = lecture.get('adv')

            weekData = template.format(
                sectionHeader= secHeader,
                lecDate= lecDate.format('MM/DD/YYYY'),
                hwDate= hwDate.format('YYYY-MM-DD HH:mm:ss'),
                advThisWeek= weekHasAdv,
                solDate= solDate.format('YYYY-MM-DD HH:mm:ss'),
                title= lecture['title'],
                week= idx + 1,
            )

            f.write(weekData)
