from Nucleus import Nucleus
from math import log as ln


class DecayArray(object):
    def __init__(self, length, timestep, decay_chain):
        self._time_elapsed = 0
        self._size = length**2
        self._timestep = timestep
        self._array = [[Nucleus(timestep, decay_chain)
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
        print("Starting simulation...")
        while(not self._half_decayed()):
            self._time_elapsed += self._timestep
            for line in self._array:
                for nucleus in line:
                    if not nucleus.decayed() and nucleus.should_decay():
                        nucleus.decay()
        self._present_results()

    def _nucleus_dict(self):
        """Returns a dictionary of each nucleus type and its concentration in the sample
        """
        d = {}
        for line in self._array:
            for nucleus in line:
                if nucleus._name in d:
                    d[nucleus._name] += 1
                else:
                    d[nucleus._name] = 1
        return d

    def _present_results(self):
        """Prints out a readable summary of results
        """
        BORDER_LINE = "+"+"-" * (len(self._array)+2)+"+"

        # output half-life
        print(f"\nMeasured half-life: {self._time_elapsed:.2f}min\n")

        # summarise concentration for each type of nucleus
        print("Conc.  Element")
        for (nucleus_name, nucleus_count) in self._nucleus_dict().items():
            concentration = (nucleus_count/self._size)*100
            print(f"{concentration:5.2f}% {nucleus_name}")
        print()
        # print grid of nuclei
        print(BORDER_LINE)
        for line in self._array:
            print(f"| {''.join(list(map(str, line)))} |")
        print(BORDER_LINE)
