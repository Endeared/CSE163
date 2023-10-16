# Ross Hamey
# CSE163 - P4.8
# 10/8/2023
# https://github.com/Endeared

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

input_file = open(input_file, "r")
output_file = open(output_file, "w")

input_data = input_file.read()
output_file.write(input_data)

input_file.close()
output_file.close()