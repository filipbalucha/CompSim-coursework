from Nucleus import Nucleus
from math import log as ln

import numpy as np


class DecayArray(object):
    def __init__(self, length, timestep, decay_constant):
        self._time_elapsed = 0
        self._size = length**2
        self._num_decayed = 0

        self._length = length
        self._timestep = timestep
        self._decay_constant = decay_constant
        prob_of_decay = timestep * decay_constant
        self._array = np.array([Nucleus(prob_of_decay)
                                for _ in range(self._size)])
        self.function = np.vectorize(self.decay_nucleus)

    def _half_decayed(self):
        """Determines if half of the nuclei have already decayed
        """
        return self._num_decayed >= 0.5 * self._size

    def decay_nucleus(self, nucleus):
        if not nucleus.decayed() and nucleus.should_decay():
            nucleus.decay()
            self._num_decayed += 1

    def simulate_decay(self):
        print("Starting simulation...")
        while(not self._half_decayed()):
            self.function(self._array)
            self._time_elapsed += self._timestep
        self._present_results()

    def _present_results(self):
        """Prints out a readable summary of results
        """
        BORDER_LINE = "+" + "-" * (self._length+2) + "+"

        # output results
        measured_decay_constant = ln(2)/self._time_elapsed
        print(f"Initial  N: {self._size}")
        print(f"Final    N: {self._size - self._num_decayed}")
        print(f"Measured λ: {measured_decay_constant:.5f}")
        print(f"Actual   λ: {self._decay_constant}")
        percentage_error = abs(measured_decay_constant -
                               self._decay_constant)/self._decay_constant * 100
        print(
            f"This is within: {percentage_error:.2f}% of the actual value.\n")

        # print grid of elements after one half-life
        print("Legend:")
        print("+ = undecayed")
        print(BORDER_LINE)
        for line in self._array.reshape((self._length, self._length)):
            print(f"| {''.join(list(map(str, line)))} |")
        print(BORDER_LINE)
