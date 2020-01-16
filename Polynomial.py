class Polynomial(object):
    _coefficients = []

    def __init__(self, coefficients):
        self._coefficients = coefficients

    def order(self):  # calculate and return the order of the polynomial
        return

    def add(self, polynomial):
      # Add another polynomial to this polynomial and return a new polynomial.
      # Your code should include the case where the polynomials being added are of different order
        return

    # calculate the derivative of the polynomial and return the result as a new polynomial
    def derivative(self):
        return

    def antiderivative(self, constant):
      # calculate the indefinite integral of the polynomial and return the result as a new polynomial
        return

    def show(self):
        # Print a sensible String representation of the polynomial
        # e.g.: P(x) = a0 + a1x + a2x^2 + .... + anx^n
        return
