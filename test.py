from main import factorial
import math

def main():
    x = 10
    return math.factorial(x) != factorial(x)
    
if __name__ == '__main__':
    exit(main())