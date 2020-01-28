from Mandelbrot import Mandelbrot
from Julia import Julia


class FractalTest(object):
    def __init__(self, *args):
        self.args = args

    def run_mandelbrot(self):
        mandelbrot = Mandelbrot(*self.args)
        mandelbrot.run()

    def run_julia(self, constant):
        julia = Julia(*self.args, constant)
        julia.run()


if __name__ == "__main__":
    julia_constants = {
        "one": -1,
        "two": 0.5,
        "dendrite": -1j,
        "rabbit": -0.1+0.8j,
        "dragon": 0.36+0.1j
    }
    width = 500
    height = 500
    max_iter = 255
    x_min, x_max, y_min, y_max = (-2.0, 2.0, -1.5, 1.5)
    test = FractalTest((width, height), (x_min, x_max, y_min, y_max), max_iter)

    # x_min, x_max, y_min, y_max = (-2.025, 0.6, -1.125, 1.125)
    # test.run_mandelbrot()

    test.run_julia(julia_constants["dragon"])
