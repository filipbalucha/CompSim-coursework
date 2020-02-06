from matplotlib import animation
from matplotlib.patches import Rectangle
import numpy as np
from random import random, randrange
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

        # format plot
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
        print(f"Calculating avg. speed for {density*100:.2f}%")
        arr = self._road_array(density)
        num_cars = int(density * self.size)
        avg_speed_last = -1
        avg_speed = 0

        # while average speed is changing
        while(avg_speed != avg_speed_last):
            arr, num_moved = self.traffic_step(arr)
            avg_speed_last = avg_speed
            avg_speed = num_moved/num_cars

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
            prev_full = arr[(i-1) % arr.size]
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
                if prev_full:
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

    def animate(self, density, num_iterations):
        # TODO: finish

        arr = self._road_array(density)

        def init():
            nonlocal patches
            for patch in patches:
                ax.add_patch(patch)
            return patches

        def animate(i):
            nonlocal patches
            ps_new = [None] * len(patches)

            # traffic step
            for i, patch in enumerate(patches):
                has_car = patch.get_visible()

                next_idx = (i+1) % len(patches)
                next_patch = patches[next_idx]
                next_full = next_patch.get_visible()

                prev_idx = (i-1) % len(patches)
                prev_patch = patches[prev_idx]
                prev_full = prev_patch.get_visible()

                if has_car:
                    # move only if the next road segment is free
                    if next_full:
                        ps_new[i] = patch
                    else:
                        # swap positions with next element, which is invisible as it does not contain a car
                        patch.set_x((patch.get_x() + 1) % len(patches))
                        ps_new[(i+1) % len(patches)] = patch
                        ps_new[i] = next_patch
                else:
                    # a car can come only if the previous road segment is occupied
                    # we do not increment num_moved here as this would result in double-counting the cars that moved
                    if prev_full:
                        # swap positions with previous element, which is invisible as it does not contain a car
                        patch.set_x((patch.get_x() - 1) % len(patches))
                        ps_new[(i-1) % len(patches)] = patch
                        ps_new[i] = prev_patch
                    else:
                        ps_new[i] = patch
            patches = ps_new
            return patches

        # plotting
        fig = plt.figure(figsize=(15, 3))

        # configure axes
        ax = plt.axes()
        ax.set_ylim(-1, 1)
        ax.set_xlim(0, self.size+1)
        ax.grid()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        arr = self._road_array(density)

        # Initialise patches
        p_width = 0.4
        p_height = 1
        patches = [Rectangle((x+1-p_width/2, -p_height/2),
                             p_width,
                             p_height,
                             fc=f"#{randrange(0x1000000):06x}",
                             animated=True,
                             visible=has_car)
                   for x, has_car in enumerate(arr)]

        #
        anim = animation.FuncAnimation(fig, animate,
                                       init_func=init,
                                       interval=500,
                                       frames=num_iterations,
                                       blit=True,
                                       repeat=False)
        plt.show()
