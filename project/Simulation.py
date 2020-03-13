from Body import Body
from pandas import read_csv
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

GRAV_CONST = 6.67408 * 10e-11


class Simulation:
    def __init__(self, file_name, timestep, num_iterations):
        self.file_name = file_name
        self.timestep = timestep
        self.num_iterations = num_iterations
        self.body_list = []
        self.patch_list = []
        self.animation_data = [[]]
        self.read_input_data()
        self.initialise_body_values()

    def read_input_data(self):
        # TODO: add actual size representations to CSV
        with open(self.file_name) as csv_file:
            df = read_csv(csv_file)
            for row in df.itertuples():
                body = Body(*row[1:-1], self)
                self.body_list.append(body)
                # TODO: add name to these values
                self.animation_data[-1].append(body.position)
                self.patch_list.append(
                    Circle(xy=body.position, radius=10e9, color=row[-1], animated=True))

    def initialise_body_values(self):
        # acc and vel
        for body in self.body_list:
            initial_acceleration = self.calc_acceleration(body)
            body.previous_acceleration = initial_acceleration
            body.current_acceleration = initial_acceleration
        pass

    def run_simulation(self):
        for _ in range(self.num_iterations):
            self.step_forward()
        self.animation()

    def step_forward(self):
        # update positions
        self.animation_data.append([])
        for body in self.body_list:
            body.update_position(self.timestep)
        for body in self.body_list:
            next_acc = self.calc_acceleration(body)
            body.update_velocity(self.timestep, next_acc)
            self.animation_data[-1].append(body.position)

        # TODO: calculate energy

    def calc_acceleration(self, b):
        next_acceleration = np.zeros(2)
        for body in self.body_list:
            if body == b:
                continue
            r = b.position - body.position
            next_acceleration += body.mass / norm(r)**3 * r
        return -GRAV_CONST * next_acceleration

    def calc_total_energy(self):
        pass

    # Animation

    def init(self):
        return self.patch_list

    def update_display(self, i):
        for patch, xy in zip(self.patch_list, self.animation_data[i]):
            patch.center = xy
        return self.patch_list

    def animation(self):

        fig = plt.figure()
        ax = plt.axes()

        for patch in self.patch_list:
            ax.add_patch(patch)

        # TODO: make dynamic
        DIM = 250e9
        ax.set_ylim(-DIM, DIM)
        ax.set_xlim(-DIM, DIM)
        plt.grid(True)
        plt.title("The Solar System")
        plt.xlabel("X")
        plt.ylabel("Y")

        anim = FuncAnimation(fig, self.update_display, init_func=self.init,
                             frames=self.num_iterations, repeat=False, interval=1, blit=True)
        plt.show()
