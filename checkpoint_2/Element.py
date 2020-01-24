from random import random


class Nucleus(object):
    def __init__(self, prob_of_decay):
        self._decayed = False
        self._prob_of_decay = prob_of_decay

    def decayed(self):
        """Tells whether the current nucleus has decayed
        """
        return self._decayed

    def should_decay(self):
        """Determines whether a given nucleus should decay
        """
        return self._prob_of_decay >= random()  # the nucleus should decay iff the probability of its decay is greater than the pseudorandomly generated number

    def decay(self):
        """Decays the current nucleus
        """
        self._decayed = True

    def __str__(self):
        """Returns a sensible representation of the nucleus based on its state
        """
        return "0" if self._decayed else "1"
