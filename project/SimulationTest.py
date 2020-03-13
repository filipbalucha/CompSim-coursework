from Simulation import Simulation

FILE_NAME = "body_data_backup.csv"
TIMESTEP = 1000
NUM_ITERATIONS = 5000


class SimulationTest:

    def __init__(self, file_name, timestep, num_iterations):
        self.simulation = Simulation(file_name, timestep, num_iterations)

    def run(self):
        self.simulation.run_simulation()
        pass


if __name__ == "__main__":
    test = SimulationTest(FILE_NAME, TIMESTEP, NUM_ITERATIONS)
    test.run()
