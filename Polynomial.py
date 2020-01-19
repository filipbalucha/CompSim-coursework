from numpy import trim_zeros
from itertools import zip_longest


class Polynomial(object):
    _coefficients = []  # coefficients are not accessible to the outside world

    def __init__(self, coefficients):
        self._coefficients = coefficients

    def order(self):
        """Calculates the order of the polynomial

        Returns:
            int -- the order of the polynomial
        """
        trimmed_list = trim_zeros(self._coefficients, 'b')
        # the n-th non-zero coefficient corresponds to (n-1)th power
        return len(trimmed_list) - 1

    def __add__(self, polynomial):
        """Adds two polynomials together

        Arguments:
            polynomial {Polynomial} -- the polynomial to be added to the current instance

        Returns:
            Polynomial -- the sum of the two polynomials
        """
        # Your code should include the case where the polynomials being added are of different order
        c1 = self._coefficients
        c2 = polynomial._coefficients
        coefficients = list(map(sum, zip_longest(c1, c2, fillvalue=0)))
        return Polynomial(coefficients)

    def derivative(self):
        """Calculates the derivative of the polynomial

        Returns:
            Polynomial -- the derivative of the polynomial
        """
        # make a copy of the values so as not to modify the actual values
        coefficients = self._coefficients.copy()
        for (i, coefficient) in enumerate(coefficients):
            # the index corresponds to the power, e.g. on the 0th position is the constant, with x^0
            coefficients[i] *= i
        # constant (i.e. the leftmost coefficient) is removed as its derivative is 0
        coefficients = coefficients[1:]
        return Polynomial(coefficients)

    def antiderivative(self, constant):
        """Calculates the indefinite integral of the polynomial

        Arguments:
            constant {double} -- constant of integration

        Returns:
            Polynomial -- the indefinite integral of the polynomial
        """
        # make a copy of the values so as not to modify the actual values
        coefficients = self._coefficients.copy()
        for (i, coefficient) in enumerate(coefficients):
            if i+1 != 0:
                coefficients[i] *= 1/(i+1)

        # +C, added to the left as this is where the constant resides in our representation of a polynomial
        coefficients.insert(0, constant)
        return Polynomial(coefficients)

    def __str__(self):
        """
        Returns:
            String -- a sensible String representation of the polynomial
        """
        def term(coefficient, power):
            if coefficient == 0:
                return ""
            if power == 0:  # a constant, so no x
                return str(coefficient)
            if coefficient > 0:
                if coefficient == 1:
                    return f" + x^{power}"
                return f" + {str(coefficient)}*x^{power}"
            # here coefficient is negative
            if coefficient == -1:
                return f" - x^{power}"
            return f" - {str(abs(coefficient))}*x^{power}"
        return f"P(x) = {''.join([term(coefficient, i) for (i, coefficient) in enumerate(self._coefficients)])}"

    # TODO: add term class - coefficient, power
