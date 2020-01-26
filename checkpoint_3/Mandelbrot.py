from numba import jit, jitclass
import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot(object):
    def __init__(self, dimensions, ranges, max_iter):
        self.width, self.height = dimensions
        x_min, x_max, y_min, y_max = ranges
        self.max_iter = max_iter

        self.grid = np.zeros((self.width, self.height))
        self.ys = np.linspace(y_min, y_max, self.height)
        self.xs = np.linspace(x_min, x_max, self.width)

    def run(self):
        self.generate_grid()
        self.plot()

    def plot(self):
        # plt.contour(xxs, yys, self.grid, colors="red", extend="both")

        # get coordinate matrices from coordinate vectors
        # xxs, yys = np.meshgrid(self.xs, self.ys)
        # Create a pseudocolor plot with a non-regular rectangular grid.
        # plt.pcolormesh(xxs, yys, self.grid)

        plt.imshow(self.grid, cmap='hot')
        # plt.xlabel("x")
        # plt.ylabel("y")
        plt.show()

    def generate_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x, y] = mandelbrot(
                    self.xs[x] + self.ys[y] * 1j, self.max_iter)


@jit
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return n
    return 0
