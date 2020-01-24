from Nucleus import Nucleus
from math import log as ln


class DecayArray(object):
    def __init__(self, length, timestep, decay_constant):
        self._time_elapsed = 0
        self._size = length**2
        self._timestep = timestep
        self._decay_constant = decay_constant
        prob_of_decay = timestep * decay_constant
        self._array = [[Nucleus(prob_of_decay)
                        for _ in range(length)] for _ in range(length)]

    def _count_decayed(self):
        """Calculates the number of nuclei that have decayed
        """
        return sum(sum(1 for nucleus in line if nucleus.decayed()) for line in self._array)

    def _half_decayed(self):
        """Determines if half of the nuclei have already decayed
        """
        return self._count_decayed()/self._size >= 0.5

    def simulate_decay(self):
        while(not self._half_decayed()):
            self._time_elapsed += self._timestep
            for line in self._array:
                for nucleus in line:
                    if not nucleus.decayed() and nucleus.should_decay():
                        nucleus.decay()
        self._present_results()

    def _present_results(self):
        """Prints out a readable summary of results
        """
        BORDER_LINE = "*" * (len(self._array)+4)
        EMPTY_LINE = f"*{' ' * (len(self._array)+2)}*"

        # output results
        measured_decay_constant = ln(2)/self._time_elapsed
        print(f"Initial  N: {self._size}")
        print(f"Final    N: {self._size - self._count_decayed()}")
        print(f"Measured λ: {measured_decay_constant:.5f}")
        print(f"Actual   λ: {self._decay_constant}")
        percentage_error = abs(measured_decay_constant -
                               self._decay_constant)/self._decay_constant * 100
        print(
            f"This is within: {percentage_error:.2f}% of the actual value.\n")

        # print grid of elements after one half-life
        print("o = undecayed")
        print(BORDER_LINE)
        print(EMPTY_LINE)
        for line in self._array:
            print(f"* {''.join(list(map(str, line)))} *")
        print(EMPTY_LINE)
        print(BORDER_LINE)
