import Simulation

FILE_NAME = "body_data.csv"
TIMESTEP = 0.01
NUM_ITERATIONS = 500


class SimulationTest(object):

    def __init__(self, file_name, timestep, num_iterations):
        self.simulation = Simulation(file_name, timestep, num_iterations)

    def run(self):
        # self.simulation().animate()
        pass


if __name__ == "__main__":
    test = SimulationTest(FILE_NAME, TIMESTEP, NUM_ITERATIONS)
    test.run()
