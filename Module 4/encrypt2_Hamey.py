# Ross Hamey
# CSE163 - P4.3
# 10/8/2023
# https://github.com/Endeared

"""
File: encrypt.py
Project 4.3

Encypts a text file.  The inputs are the names of
the input file and the output file and the distance value.
The encrypted code is witten to a new file.
"""

file_in = input("Enter the input file name: ")
file_out = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))
code = ""

input_file = open(file_in, "r")
all_text = input_file.read()
input_file.close()

for char in all_text:
    char_ascii = ord(char)
    char_ascii += int(distance)
    code += chr(char_ascii)

output_file = open(file_out, "w")
output_file.write(code)
output_file.close()
