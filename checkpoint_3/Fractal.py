import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


class Fractal(object):
    def __init__(self, dimensions, ranges, max_iter, function):
        self.width, self.height = dimensions
        self.x_min, self.x_max, self.y_min, self.y_max = ranges
        self.max_iter = max_iter

        # initiate an empty array
        self.grid = np.zeros((self.width, self.height))

        # return evenly spaced numbers from y_min to y_max; the number of these numbers is equal to the height in pixels
        self.ys = np.linspace(self.y_min, self.y_max, self.height)
        self.xs = np.linspace(self.x_min, self.x_max, self.width)

        # function used in fractal generation
        self.function = function

    def run(self):
        self.generate_grid()
        self.plot()

    def generate_grid(self):
        print("Calculating...")
        # run fractal function on every pixel
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x, y] = self.function(
                    self.xs[x] + self.ys[y] * 1j)

    def plot(self):
        print("Plotting...")
        # transpose grid to for regular x- and y-axis orientation
        # set colour theme
        # set range of values for ticks
        plt.imshow(self.grid.T, cmap='inferno', extent=[
            self.x_min, self.x_max, self.y_min, self.y_max])
        # set axis labels
        plt.xlabel("Re(C)")
        plt.ylabel("Im(C)")
        # store output in a PNG
        plt.savefig(f"./out/fractal {datetime.now()}.png")
        # display output
        plt.show()
