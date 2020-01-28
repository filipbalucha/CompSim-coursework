from Fractal import Fractal


class Mandelbrot(Fractal):
    def __init__(self, dimensions, ranges, max_iter):
        super().__init__(dimensions, ranges, max_iter, self.mandelbrot)

    def mandelbrot(self, c):
        z = c
        for n in range(self.max_iter):
            z = z**2 + c
            if abs(z) > 2:
                return n
        return 0
