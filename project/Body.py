from math import sqrt as sqrt
import numpy as np

GRAV_CONST = 6.67408 * 10e-11
ZERO_ACC = [0, 0]


class Body:

    # TODO: is the simulation parameter necessary?
    def __init__(self, name, mass, orbital_radius, velocity, simulation):
        self.name = name
        self.mass = mass
        self.velocity = np.array([0, velocity])
        self.simulation = simulation
        self.position = np.array((orbital_radius, 0))
        self.current_acceleration = np.array(ZERO_ACC)
        self.previous_acceleration = np.array(ZERO_ACC)
        self.color = "red"  # TODO: introduce more colors

    def update_position(self, timestep):
        self.position = self.position + self.velocity * timestep + 1/6 * \
            (4 * self.current_acceleration -
             self.previous_acceleration) * timestep ** 2

    def update_velocity(self, timestep):
        # update acceleration
        next_acceleration = self.simulation.calc_acceleration(self)

        self.velocity = self.velocity + 1/6 * \
            (2 * next_acceleration + 5 * self.current_acceleration -
             self.previous_acceleration) * timestep

        self.previous_acceleration = self.current_acceleration
        self.current_acceleration = next_acceleration

    def calc_KE(self):
        return self.mass * np.linalg.norm(self.velocity) ** 2 / 2

    def check_orbital_period(self):
        pass
