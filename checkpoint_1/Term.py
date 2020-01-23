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
        # coefficient_part = self.coefficient_str()
        # if the coefficient is equal to its integer value, we rid the decimals for a neater representation
        # otherwise we print the coefficient accurate to 2 decimal places

        coefficient_part = f"{int(self._coefficient):+g}" if (
            self._coefficient == int(self._coefficient)) else f"{self._coefficient:+.2f}"
        # avoid x^1
        power_part = "x" if self._power == 1 else f"x^{self._power}"

        if self._coefficient == 0:
            return ""
        if self._power == 0:  # a constant, so no x
            return coefficient_part
        return f"{coefficient_part}*{power_part}"
