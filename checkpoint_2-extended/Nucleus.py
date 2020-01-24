from random import random
from math import log as ln


class Nucleus(object):
    def __init__(self, timestep, decay_chain):
        self._decayed = False
        self._timestep = timestep
        self._next = list(decay_chain)
        self._name, self._half_life = self._next.pop(0)
        self._prob_of_decay = self._decay_constant()

    def decayed(self):
        """Tells whether the current nucleus has decayed
        """
        return self._decayed

    def _decay_constant(self):
        """Calculates the decay constant, i.e. the probability that a nucleus should decay
        """
        decay_constant = ln(2)/self._half_life
        return decay_constant * self._timestep

    def should_decay(self):
        """Determines whether a given nucleus should decay
        """
        return self._prob_of_decay >= random()  # the nucleus should decay iff the probability of its decay is greater than the pseudorandomly generated number

    def decay(self):
        """Decays the current nucleus
        """
        if not self._next:
            self._decayed = True
        elif len(self._next) == 1:
            self._name, _ = self._next.pop(0)
            self._decayed = True  # the last element is stable
        else:
            self._name, self._half_life = self._next.pop(0)
            self._prob_of_decay = self._decay_constant()

    def __str__(self):
        """Returns a sensible representation of the nucleus based on its state
        """
        # we uniquely identify each nucleus using the number of nuclei left in the decay chain
        return str(len(self._next))
