from DecayArray import DecayArray


class RadioactiveDecayChainTest(object):
    def run(self):
        # [(element_name,half_life)]
        length = 50
        timestep = 0.01
        decay_chain = [("Lead-211", 36), ("Bismuth-211", 2.1),
                       ("Thallium-207", 4.08), ("Lead", None)]
        decay_array = DecayArray(length, timestep, decay_chain)
        print("Starting simulation...")
        decay_array.simulate_decay()


if __name__ == "__main__":
    radioactiveDecayChainTest = RadioactiveDecayChainTest()
    radioactiveDecayChainTest.run()
