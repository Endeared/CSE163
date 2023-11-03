# Ross Hamey
# CSE163 - P6.2
# 10/22/2023
# https://github.com/Endeared

# math import
import math

# Initialize the tolerance
TOLERANCE = 0.000001

def newton(x, estimate=1.0):
    """Returns the square root of x."""
    # Perform the successive approximations
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, estimate)

def main():
    """Allows the user to obtain square roots."""
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()