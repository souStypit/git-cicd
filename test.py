from main import factorial
import math

def tests():
    try:
        assert math.factorial(10) == factorial(10)
        assert math.factorial(12) == factorial(12)
        assert math.factorial(15) == factorial(15)
    except AssertionError as ae:
        return 1
    return 0
def main():
    return tests()
    
if __name__ == '__main__':
    exit(main())