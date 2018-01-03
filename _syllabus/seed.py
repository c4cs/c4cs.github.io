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
    'date': '01/05/2018',
    'title': 'Introduction, Virtual Machines, & Command Line Primer',
    'adv': 'false'
    }, {
    'date': '01/12/2018',
    'title': 'Basic Git'
    }, {
    'date': '01/19/2018',
    'title': 'Shells, Environment, Scripting, and Bash'
    }, {
    'sectionHeader': 'Being Efficient',
    'date': '01/26/2018',
    'title': 'Editors'
    }, {
    'date': '02/02/2018',
    'title': 'Git II'
    }, {
    'date': '02/09/2018',
    'title': 'Unix II'
    }, {
    'sectionHeader': 'Developing',
    'date': '02/16/2018',
    'title': 'Build Systems'
    }, {
    'date': '02/23/2018',
    'title': 'Unit Testing and Python'
    }, {
    'date': '03/02/2018',
    'title': 'No lecture, Spring break'
    }, {
    'date': '03/09/2018',
    'title': 'Debuggers'
    }, {
    'sectionHeader': 'Standing on the Shoulders of Giants',
    'date': '03/16/2018',
    'title': 'Package Managers & Development Environment'
    }, {
    'date': '03/23/2018',
    'title': 'IDEs'
    }, {
    'date': '03/30/2018',
    'title': 'No lecture, Thanksgiving break',
    'adv': 'false',
    }, {
    'date': '04/06/2018',
    'title': 'A Sampling of Other Things'
    }, {
    'date': '04/13/2018',
    'title': 'TBA - Staff'
    }
]

if __name__ == '__main__':
    for idx, lecture in enumerate(lectures):
        syllabusInfo = 'w18/week{0:02d}.md'.format(idx + 1)
        lecSlide = 'w18/week{0:01d}'.format(idx + 1)
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
