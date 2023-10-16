# Ross Hamey
# CSE163 - P3.2
# 9/24/2023
# https://github.com/Endeared

# grabbing tirangle sides
first = int(input("Enter the first side: "))
second = int(input("Enter the second side: "))
third = int(input("Enter the third side: "))

# sorting sides, since in pythagorean theorem our
# c side should always be the largest
sides = [first, second, third]
sides.sort()

# checking if pythagorean theorem holds
if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")