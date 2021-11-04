#!/usr/bin/python
# scoreboard.py

'''class definition for score keeper'''

__author__ = "Melissa Jiang"
__version__ = "1.0"


class Score(object):
    score = 0

    def change_score(self):
        Score.score += int(self)
