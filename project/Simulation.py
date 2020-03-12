from Body import Body
from pandas import read_csv
import numpy as np


class Simulation:
    def __init__(self, file_name, timestep, num_iterations):
        self.file_name = file_name
        self.timestep = timestep
        self.num_iterations = num_iterations
        self.body_list = []
        self.patch_list = []
        self.read_input_data()

    def read_input_data(self):
        with open(self.file_name) as csv_file:
            df = read_csv(csv_file)
            for row in df.itertuples():
                print(*row[1:])
                self.body_list.append(Body(*row[1:], self))
            for body in self.body_list:
                print(body)
                body.update_velocity(self.timestep)

    def run_simulation(self):
        pass

    def step_forward(self):
        pass

    def calc_acceleration(self, body):
        pass

    def update_display(self):
        pass

    def calc_total_energy(self):
        pass
