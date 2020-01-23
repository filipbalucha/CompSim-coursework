from Term import Term


class Polynomial(object):
    def __init__(self, **kwargs):
        """
        Arguments:
            {[float]} -- a list of numbers that correspond to coefficients
            {[Term]}
        """
        if "coefficients" in kwargs:
            # each term's power corresponds to its position in the list of coefficients
            # e.g. the constant is the leftmost elemenent, so its index is 0, and 0 is also the power of the constant term
            self._terms = [Term(coefficient, int(power))
                           for (power, coefficient) in enumerate(kwargs["coefficients"])]
        elif "terms" in kwargs:
            self._terms = kwargs["terms"]
        else:
            self._terms = []

    def order(self):
        """Calculates the order of the polynomial

        Returns:
            int -- the order of the polynomial
        """
        max_power = 0  # if p(x) = 0, we have a polynomial of degree 0
        for term in self._terms:
            if term._coefficient != 0:
                max_power = term._power
        return max_power

    def __add__(poly_a, poly_b):
        """Adds two polynomials together

        Arguments:
            poly_a {Polynomial}
            poly_b {Polynomial} -- the polynomial to be added to poly_a

        Returns:
            Polynomial -- the sum of the two polynomials
        """
        terms_a = poly_a._terms
        terms_b = poly_b._terms

        terms_sum = [
            term_a + term_b for (term_a, term_b) in zip(terms_a, terms_b)]

        # If the polynomials being added are of different order:
        if poly_a.order() > poly_b.order():
            n = len(terms_b)
            leftover_terms = terms_a[n:]
            terms_sum.extend(leftover_terms)
        elif poly_a.order() < poly_b.order():
            n = len(terms_a)
            leftover_terms = terms_b[n:]
            terms_sum.extend(leftover_terms)
        return Polynomial(terms=terms_sum)

    def derivative(self):
        """Calculates the derivative of the polynomial

        Returns:
            Polynomial -- the derivative of the polynomial
        """
        # constant (i.e. the leftmost coefficient) is removed as its derivative is 0
        terms = self._terms[1:]

        # the derivative of a polynomial is equal to the sum of the derivatives of its terms
        # so we differentiate each term respectively
        terms_derivatives = [term.derivative() for term in terms]
        return Polynomial(terms=terms_derivatives)

    def antiderivative(self, constant):
        """Calculates the indefinite integral of the polynomial

        Arguments:
            constant {float} -- constant of integration

        Returns:
            Polynomial -- the indefinite integral of the polynomial
        """
        # make a copy of the values so as not to modify the actual values
        terms_antiderivatives = [term.antiderivative() for term in self._terms]

        # add constant C to the left as per our representation of a polynomial
        terms_antiderivatives.insert(0, constant)
        return Polynomial(terms=terms_antiderivatives)

    def __str__(self):
        """ Pretty prints the polynomial

        Returns:
            String -- a string representation of the polynomial
        """
        terms_str = ' '.join(str(term) for term in self._terms)
        if not terms_str:
            return "P(x) = 0"
        # remove plus at the beginning
        elif terms_str[:2] == " +":
            return f"P(x) = {terms_str[2:]}"
        return f"P(x) = {terms_str}"
