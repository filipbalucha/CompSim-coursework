from Mandelbrot import Mandelbrot


class MandelbrotTest(object):
    def run(self):
        width, height = (300, 300)
        x_min, x_max, y_min, y_max = (-2, 2, -2, 2)
        max_iter = 255
        # x_min = -2
        # x_max = 2
        # y_min = -2
        # y_max = 2
        mandelbrot = Mandelbrot(
            (width, height), (x_min, x_max, y_min, y_max), max_iter)
        # mandelbrot = Mandelbrot(width, height, x_min,
        # x_max, y_min, y_max, max_iter)
        mandelbrot.run()


if __name__ == "__main__":
    test = MandelbrotTest()
    test.run()
