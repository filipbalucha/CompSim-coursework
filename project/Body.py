from math import sqrt as sqrt
import numpy as np

GRAV_CONST = 6.67408 * 10e-11
SOLAR_MASS = 1988500e24


class Body:

    # TODO: is the simulation parameter necessary?
    def __init__(self, name, mass, orbital_radius, simulation):
        self.name = name
        self.mass = mass
        self.simulation = simulation
        self.position = np.array((orbital_radius, 0))

        vel = sqrt(GRAV_CONST*SOLAR_MASS /
                   orbital_radius) if orbital_radius != 0 else 0
        self.velocity = np.array(
            (0, vel))
        # TODO: should bodies store patch details; should this export patches?

    def update_position(self, timestep):
        self.position = self.position + self.velocity * timestep + 1/6 * \
            (4 * self.current_acceleration -
             self.previous_acceleration) * timestep ** 2

    def update_velocity(self, timestep, next_acceleration):
        self.velocity = self.velocity + 1/6 * \
            (2 * next_acceleration + 5 * self.current_acceleration -
             self.previous_acceleration) * timestep

        self.previous_acceleration = self.current_acceleration
        self.current_acceleration = next_acceleration

    def calc_KE(self):
        return self.mass * np.linalg.norm(self.velocity) ** 2 / 2

    def check_orbital_period(self):
        pass

    def __str__(self):
        return f"Planet: {self.name} \n \tMass: {self.mass} \n \tVelocity: {self.velocity} \n \tCurrent acceleration: {self.current_acceleration}"
