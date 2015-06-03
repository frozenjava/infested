#
# RatBrain.py
# Josh Artuso
# 06/03/16
#
# This is the AI that controls the Rat object
# I am not exactly sure how i want this to work yet...
# I am going to come back to it later and work on other things that need to be completed first.
#

import threading

import Rat


class RatBrain(threading.Thread):

    PLAYER = None
    RAT = None

    def __init__(self, rat, player):
        super(RatBrain, self).__init__()
        self.RAT = rat
        self.PLAYER = player

    def run(self):
        pass
