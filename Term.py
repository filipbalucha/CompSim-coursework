class Term(object):
    def __init__(self, coefficient, power):
        self._coefficient = coefficient
        self._power = power

    def __add__(term_a, term_b):
        """Adds two terms together

        Arguments:
            term_a {Term}
            term_b {Term} -- the term to be added to term_a

        Returns:
            Term -- the sum of the two terms
        """
        coefficient = term_a._coefficient + term_b._coefficient
        # our representation ensures that the powers of two terms being added
        # is equal, so exception handling is not necessary
        power = term_a._power
        return Term(coefficient, power)

    def derivative(self):
        """Calculates the derivative of the term

        Returns:
            Term -- the derivative of the term
        """
        coefficient = self._coefficient * self._power
        power = self._power - 1
        return Term(coefficient, power)

    def antiderivative(self):
        """Calculates the indefinite integral of the term

        Returns:
            Term -- the indefinite integral of the term
        """
        coefficient = self._coefficient / (self._power+1)
        power = self._power + 1
        return Term(coefficient, power)

    def __str__(self):
        """Pretty prints a term

        Returns:
            String -- a string representation of the term
        """
        def coefficient_str(coefficient):
            # we cast floats to ints if they are equal for a neater representation
            if coefficient == int(coefficient):
                return str(int(coefficient))
            # otherwise we print the coefficient to 2 decimal places
            return f"{self._coefficient:.2f}"

        coefficient = self._coefficient
        power = self._power

        if coefficient == 0:
            return ""
        if power == 0:  # a constant, so no x
            return coefficient_str(coefficient)
        if coefficient > 0:
            if coefficient == 1.0:
                return f" + x^{power}"
            return f" + {coefficient_str(coefficient)}*x^{power}"
        # now coefficient is surely negative
        if coefficient == -1.0:
            return f" - x^{power}"
        return f" - {coefficient_str(abs(coefficient))}*x^{power}"
