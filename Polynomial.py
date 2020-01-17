from numpy import trim_zeros
from itertools import zip_longest


class Polynomial(object):
    __coefficients = []  # coefficients are not accessible to the outside world

    def __init__(self, coefficients):
        self.__coefficients = coefficients

    def get_coefficients(self):
        return self.__coefficients

    def order(self):  # calculate and return the order of the polynomial
        trimmed_list = trim_zeros(self.get_coefficients(), 'b')
        # the n-th non-zero coefficient corresponds to (n-1)th power
        return len(trimmed_list) - 1

    def __add__(self, polynomial):
        # Add another polynomial to this polynomial and return a new polynomial.
        # Your code should include the case where the polynomials being added are of different order
        c1 = self.get_coefficients()
        c2 = polynomial.get_coefficients()
        coefficients = list(map(sum, zip_longest(c1, c2, fillvalue=0)))
        return Polynomial(coefficients)

    # calculate the derivative of the polynomial and return the result as a new polynomial
    def derivative(self):
        coefficients = self.get_coefficients().copy()
        for (i, coefficient) in enumerate(coefficients):
            # the index corresponds to the power, e.g. on the 0th position is the constant, with x^0
            coefficients[i] *= i
        # constant (i.e. the leftmost coefficient) is removed as its derivative is 0
        coefficients = coefficients[1:]
        return Polynomial(coefficients)

    def antiderivative(self, constant):
        # calculate the indefinite integral of the polynomial and return the result as a new polynomial
        coefficients = self.get_coefficients().copy()
        for (i, coefficient) in enumerate(coefficients):
            if i+1 != 0:
                coefficients[i] *= 1/(i+1)

        # +C, added to the left as this is where the constant resides in our representation of a polynomial
        coefficients.insert(0, constant)
        return Polynomial(coefficients)

    def __str__(self):
        # Print a sensible String representation of the polynomial
        # e.g.: P(x) = a0 + a1x + a2x^2 + .... + anx^n

        def term(coefficient, power):
            if power == 0:  # a constant, so no x
                return str(coefficient)
            if coefficient >= 0:
                if coefficient == 1:
                    return f" + x^{power}"
                return f" + {str(coefficient)}*x^{power}"
            # here coefficient is negative
            if coefficient == -1:
                return f" - x^{power}"
            return f" - {str(abs(coefficient))}*x^{power}"
        return ''.join([term(coefficient, i) for (i, coefficient) in enumerate(self.get_coefficients())])

    # TODO: add term class - coefficient, power
