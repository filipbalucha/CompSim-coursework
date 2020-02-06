from matplotlib import animation
import matplotlib.patches as patches
import numpy as np
from random import random
import matplotlib.pyplot as plt
from math import ceil, floor


class TrafficSimulation(object):
    def __init__(self, size):
        self.size = size

    def plot(self, density_from, density_to, num_samples):
        """Plots steady state average speed against car density

        Arguments:
            density_from {float} - minimum car density
            density_to {float} - maximum car density
            num_samples {int} -- number of evenly-spaced density values to take from the density interval
        """

        x_axis = np.linspace(density_from, density_to, num_samples)
        y_axis = np.vectorize(self.ss_avg_speed)(x_axis)

        plt.scatter(x_axis, y_axis, marker='o', s=1)
        plt.grid(True)
        plt.title("Steady state speed against car density")
        plt.xlabel("Car density")
        plt.ylabel("Average speed in steady state")

        # format x-axis ticks
        step = 0.1  # tick every 10%
        # display first multiple of 10 smaller than range start
        density_from_rounded = floor(density_from*10)/10
        # display first multiple of 10 greater than range end
        density_to_rounded = ceil(density_to*10)/10
        x_ticks = np.arange(density_from_rounded,
                            density_to_rounded+step, step)
        x_labels = [f"{int(round(val*100))}%" for val in x_ticks]
        plt.xticks(x_ticks, x_labels)

        plt.show()

    def ss_avg_speed(self, density):
        """Calculates steady state average speed given car density
        """
        # print(f"Calculating avg. speed for {int(density*100)}%")
        print(f"Calculating avg. speed for {density*100:.2f}%")
        arr = self._road_array(density)
        num_cars = int(density * self.size)
        # shuffle the array in place to simulate random distribution of cars in traffic
        np.random.shuffle(arr)
        avg_speed_last = -1
        avg_speed = 0
        # while average speed is changing
        while(avg_speed != avg_speed_last):
            arr, num_moved = self.traffic_step(arr)
            avg_speed_last = avg_speed
            avg_speed = num_moved/num_cars
        # reached steady state average speed
        return avg_speed

    def traffic_step(self, arr):
        """Performs a single traffic step

        Arguments:
            arr {[int]} -- an array of 1s and 0s where 1 represents a car and 0 an empty road segment

        Returns:
            [int] -- the array after the traffic step
            int -- the number of cars that moved during the traffic step
        """
        new_arr = np.empty(arr.size)
        num_moved = 0
        for i, has_car in enumerate(arr):
            next_full = arr[(i+1) % arr.size]
            previous_full = arr[(i-1) % arr.size]
            if has_car:
                # move only if the next road segment is free
                if next_full:
                    new_arr[i] = 1
                else:
                    new_arr[i] = 0
                    num_moved += 1
            else:
                # a car can come only if the previous road segment is occupied
                # we do not increment num_moved here as this would result in double-counting the cars that moved
                if previous_full:
                    new_arr[i] = 1
                else:
                    new_arr[i] = 0
        return new_arr, num_moved

    def _road_array(self, density):
        """Returns an array that represents the road using 1s and 0s where 1 represents a car and 0 an empty road segment

        Arguments:
            density {float} -- car density

        Returns:
            [int] -- a numpy array
        """
        num_cars = int(density * self.size)
        num_empty = self.size - num_cars
        # create an array of integers where one represents a segment which has a car
        arr = np.array([0] * num_empty + [1] * num_cars)
        # shuffle the array in place to simulate random distribution of cars in traffic
        np.random.shuffle(arr)
        return arr

    def _print_road(self, cars):
        BAR = "---".join("|" * (len(cars)+1))
        CONTENT = "| " + \
            " | ".join(["C" if has_car else " " for has_car in cars]) + " |"
        print(BAR)
        print(CONTENT)
        print(BAR)
        print()

    def animate(self, density, num_iterations):
        """Prints a sensible representation of the road to the console for the given number of iterations

        Arguments:
            density {float} -- car density
            num_iterations {int} -- number of iterations
        """

        arr = self._road_array(density)

        for _ in range(num_iterations):
            self._print_road(arr)
            arr, _ = self.traffic_step(arr)
