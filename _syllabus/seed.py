#!/usr/bin/env python3

import arrow

template = """---
sectionHeader:{sectionHeader}
week: {week}
dates: {lecDate}
lecturer: mmdarden
slidesName: {lecSlide}
homeworkRelease: {hwDate}
lectureRelease: {lecReleaseDate}
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
    'date': '09/07/2018',
    'title': 'Introduction, Virtual Machines, & Command Line Primer',
    'adv': 'false'
    }, {
    'date': '09/14/2018',
    'title': 'Basic Git'
    }, {
    'date': '09/21/2018',
    'title': 'Shells, Environment, Scripting, and Bash'
    }, {
    'sectionHeader': 'Being Efficient',
    'date': '09/28/2018',
    'title': 'Editors'
    }, {
    'date': '10/05/2018',
    'title': 'Git II'
    }, {
    'date': '10/12/2018',
    'title': 'Unix II'
    }, {
    'sectionHeader': 'Developing',
    'date': '10/19/2018',
    'title': 'Build Systems'
    }, {
    'date': '10/26/2018',
    'title': 'Unit Testing and Python'
    }, {
    'date': '11/02/2018',
    'title': 'Debuggers'
    }, {
    'sectionHeader': 'Standing on the Shoulders of Giants',
    'date': '11/09/2018',
    'title': 'Package Managers & Development Environment'
    }, {
    'date': '11/16/2018',
    'title': 'IDEs'
    }, {
    'date': '11/23/2018',
    'title': 'No lecture, Thanksgiving break',
    'adv': 'false'
    }, {
    'date': '11/30/2018',
    'title': 'A Sampling of Other Things'
    }, {
    'date': '12/07/2018',
    'title': 'TBA - Staff'
    }
]

if __name__ == '__main__':
    for idx, lecture in enumerate(lectures):
        syllabusInfo = 'f18/week{0:02d}.md'.format(idx + 1)
        lecSlide = 'f18/week{0:01d}'.format(idx + 1)
        with open(syllabusInfo, 'w') as f:
            secHeader = lecture.get('sectionHeader', '')
            lecDate = arrow.get(lecture['date'], 'MM/DD/YYYY')
            # homework out at 11am (start of first lecture) each week
            hwDate = lecDate.replace(hours=11)
            hwFormatted = hwDate.format('YYYY-MM-DD HH:mm:ss')
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
                lecSlide= lecSlide,
                lecReleaseDate= hwFormatted,
                hwDate= hwFormatted,
                advThisWeek= weekHasAdv,
                solDate= solDate.format('YYYY-MM-DD HH:mm:ss'),
                title= lecture['title'],
                week= idx + 1,
            )

            f.write(weekData)
