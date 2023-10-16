# Ross Hamey
# CSE163 - P4.4
# 10/8/2023
# https://github.com/Endeared

octal_integer = "0o"
octal_integer += input("Enter a string of octal digits: ")
plain_integer = int(octal_integer, 8)
print(f'The integer value is {plain_integer}')