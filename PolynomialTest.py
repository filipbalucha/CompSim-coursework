from Polynomial import Polynomial


class PolynomialTest(object):
    def run(self):
        poly_a = Polynomial([2, 4, -1, 6])
        poly_b = Polynomial([-1, -3, 4.5])

        print(f"The order of {poly_a} is: {poly_a.order()}")
        print(f"The sum of {poly_a} and {poly_b} is: {poly_a + poly_b}")
        print(f"The first derivative of {poly_a} is: {poly_a.derivative()}")
        print(
            f"The antiderivative of {poly_a.derivative()} is: {poly_a.derivative().antiderivative(2)}")


if __name__ == "__main__":
    test = PolynomialTest()
    test.run()
