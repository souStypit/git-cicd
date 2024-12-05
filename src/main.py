"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from numpy import exp, sqrt, pi


def factorial(n: int):
    """Calculates the sum of two numbers.

    Examples:
        add(4.0, 2.0)
        6.0
        add(4, 2)
        6.0

    Args:
        a: first number
        b: second number

    Returns:
        sum of the first and the second number
    """
    
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def del_nan_vals(darray: list):
    return [0 if el is None else el for el in darray]

def gauss(x: float, loc=0, scale=1):
    nu = loc
    sigma = scale
    return exp(-((x - nu)**2)/(2 * sigma ** 2)) / (sqrt(2 * pi * sigma ** 2))
