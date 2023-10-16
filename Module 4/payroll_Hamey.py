# Ross Hamey
# CSE163 - P4.12
# 10/8/2023
# https://github.com/Endeared

input_file = input("Enter the input file name: ")
input_file_data = open(input_file, "r")

print("Name         Hours    Total Pay")
for line in input_file_data:
    line = line.split()
    name = line[0]
    hours = int(line[1])
    pay_rate = float(line[2])
    total_pay = hours * pay_rate
    print(f'{name:<13}{hours:<8}{total_pay:>7.2f}')