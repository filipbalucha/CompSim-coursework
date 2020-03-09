from math import sqrt as sqrt


class Body(object):
    GRAV_CONST = 6.67408 * 10e-11

    def __init__(self, name, mass, orbital_radius, velocity):
        self.name = name
        self.mass = mass
        self.velocity = velocity
        self.position = (orbital_radius, 0)
        initial_acceleration = get_initial_acceleration(mass, orbital_radius)
        self.current_acceleration = initial_acceleration
        self.previous_acceleration = initial_acceleration
        self.color = "red"  # TODO: introduce more colors

    def get_initial_acceleration(self, mass, radius):
        return (GRAV_CONST * mass / radius**2, 0)

    def get_initial_velocity(self, mass, radius):
        return (sqrt(GRAV_CONST * mass / radius), 0)
