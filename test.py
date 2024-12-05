from main import factorial, del_nan_vals, gauss
import math


def tests():
    try:
        assert math.factorial(10) == factorial(10)
        assert math.factorial(12) == factorial(12)
        assert math.factorial(15) == factorial(15)
        
        assert del_nan_vals([10, 20, 30, None]) == [10, 20, 30, 0]
        assert del_nan_vals([10, None, 30, None]) == [10, 0, 30, 0]
        assert del_nan_vals([None, 20, 30, None]) == [0, 20, 30, 0]
        
        assert round(gauss(0.09), 4) == 0.3973
        assert round(gauss(0.19), 4) == 0.3918
        assert round(gauss(0.29), 4) == 0.3825 
    except AssertionError as ae:
        print("Tests are failed")
        return 1
    print("Tests are completed")
    return 0


def main():
    return tests()


if __name__ == "__main__":
    exit(main())
