from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, dimensions, ranges, max_iter, c):
        super().__init__(dimensions, ranges, max_iter, self.julia)
        self.c = c

    def julia(self, c):
        z = c
        for n in range(self.max_iter):
            z = z**2 + self.c
            if abs(z) > 2:
                return n
        return 0
