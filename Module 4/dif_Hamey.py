# Ross Hamey
# CSE163 - P4.10
# 10/8/2023
# https://github.com/Endeared

"""
File: dif.py
Project 4.10

Deterines whether or not the contents of two text
files are the same.  Outputs "Yes" if that is the
case or "No" and the first two lines that differ if
that is not the case.
"""

file_one = input("Enter the first file name: ")
file_two = input("Enter the second file name: ")

file_one = open(file_one, "r")
file_two = open(file_two, "r")

files_identical = True
one_mismatch = ""
two_mismatch = ""

while files_identical:
    line_data_one = file_one.readline()
    line_data_two = file_two.readline()
    if not line_data_one or not line_data_two:
        break
    if line_data_one != line_data_two:
        files_identical = False
        one_mismatch = line_data_one
        two_mismatch = line_data_two

if files_identical == True:
    print("Yes")
else:
    print("No")
    print(one_mismatch)
    print(two_mismatch)

file_one.close()
file_two.close()