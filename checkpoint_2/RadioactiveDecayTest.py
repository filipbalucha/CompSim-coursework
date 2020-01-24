from DecayArray import DecayArray
from collections import OrderedDict


class RadioactiveDecayTest(object):
    def _user_input(self):
        """Obtains user input that conforms to the expected types
        """
        while(True):
            try:
                decay_constant = float(input("Decay constant: "))
                if decay_constant <= 0:
                    raise ValueError
                break
            except ValueError:
                print("\nPlease enter a positive number!\n")
        while(True):
            try:
                length = int(input("Length of array: "))
                if length > 0:
                    break
            except ValueError:
                print("\nPlease enter a positive integer!\n")
        while(True):
            try:
                timestep = float(input("Timestep (in minutes): "))
                if timestep <= 0:
                    raise ValueError
                break
            except ValueError:
                print("\nPlease enter a positive number!\n")
        return (length, timestep, decay_constant)

    def run(self):
        # Test values
        # (length, timestep, decay_constant) = (50, 0.01, 0.02775)
        (length, timestep, decay_constant) = self._user_input()
        decay_array = DecayArray(length, timestep, decay_constant)
        print("Starting simulation...")
        decay_array.simulate_decay()


if __name__ == "__main__":
    radioactiveDecayTest = RadioactiveDecayTest()
    radioactiveDecayTest.run()
