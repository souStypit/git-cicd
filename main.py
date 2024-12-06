from numpy import exp, sqrt, pi


def factorial(n: int):
    """Counts factorial of 'n'

    Args:
        n (int): Inputed number

    Returns:
        int: Factorial of n
    """
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


def del_nan_vals(darray: list):
    """Changes NaN values with 0

    Args:
        darray (list): Inputed list

    Returns:
        list: An array with changed NaN values
    """
    return [0 if el is None else el for el in darray]


def gauss(x: float, nu=0, sigma=1):
    """Calculates gauss distribution in x

    Args:
        x (float): Point
        nu (float): Mean
        sigma (float): Sigma

    Returns:
        float: Gauss(x)
    """
    return exp(-((x - nu)**2)/(2 * sigma ** 2)) / (sqrt(2 * pi * sigma ** 2))
