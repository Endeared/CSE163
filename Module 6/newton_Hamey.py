# Ross Hamey
# CSE163 - P6.1
# 10/22/2023
# https://github.com/Endeared

# math import + set tolerance
import math
tolerance = 0.000001

def newton(input):
    # set our estimate, otherwise we will get an error in
    # our while loop
    estimate = 1.0
    while True:
        # repeatedly calculate estimate + difference until difference is
        # less than or equal to our tolerance
        estimate = (estimate + input / estimate) / 2
        difference = abs(input - estimate ** 2)
        if difference <= tolerance:
            break
    # lastly, return estimate
    return estimate

def main():
    # sentinel bool for our lop
    end = False

    while not end:
        # repeatedly ask user for input
        x = input("Enter a positive number: ")
        # if input isn't blank, we try to cast it to a float and
        # print our results
        if x != "":
            x = float(x)
            print("The program's estimate is", newton(x))
            print("Python's estimate is", math.sqrt(x))
        # otherwise, we end our loop
        else:
            end = True

if __name__ == "__main__":
    main()