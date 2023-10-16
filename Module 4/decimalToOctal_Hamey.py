# Ross Hamey
# CSE163 - P4.4
# 10/8/2023
# https://github.com/Endeared

decimal_integer = int(input("Enter a decimal integer: "))
octal_integer = str(oct(decimal_integer))
octal_integer = octal_integer.replace("0o", "")
print(f'The octal representation is {octal_integer}')