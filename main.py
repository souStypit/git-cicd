from numpy import exp, sqrt, pi

def factorial(n: int):
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
    

if __name__ == '__main__':
    print(del_nan_vals([10, 20, 30, None]) == [10, 20, 30, 0])
    print(round(gauss(0.09), 4) == 0.3973)