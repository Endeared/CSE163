# Ross Hamey
# CSE163 - P3.1
# 9/24/2023
# https://github.com/Endeared

# grabbing sides
first = input("Enter the first side: ")
second = input("Enter the second side: ")
third = input("Enter the third side: ")

# checking if equilateral
if first == second and second == third:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")