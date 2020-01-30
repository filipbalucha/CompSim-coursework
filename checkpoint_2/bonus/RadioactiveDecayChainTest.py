from DecayArray import DecayArray


class RadioactiveDecayChainTest(object):
    def run(self):

        length = 50
        timestep = 0.01
        # FORMAT: [(element_name,half_life)]
        decay_chain = [("Lead-211", 36), ("Bismuth-211", 2.1),
                       ("Thallium-207", 4.08), ("Lead-207", None)]

        # test exercise from main part:
        # decay_chain = [("Iodine-128", 24.98), ("Xenon-128", None)]
        decay_array = DecayArray(length, timestep, decay_chain)
        decay_array.simulate_decay()


if __name__ == "__main__":
    radioactiveDecayChainTest = RadioactiveDecayChainTest()
    radioactiveDecayChainTest.run()
