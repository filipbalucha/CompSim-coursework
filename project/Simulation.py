import csv
from Body import Body


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
            csv_reader = csv.reader(csv_file, delimiter=',')
            # skip header
            next(csv_reader)
            for row in csv_reader:
                # name, mass, velocity, orbital_radius = row
                self.body_list.append(Body(*row, self))
                # Body(name, mass, orbital_radius, velocity, self)
            for body in self.body_list:
                print(body.calc_KE())

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
