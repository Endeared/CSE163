# Ross Hamey
# CSE163 - P3.7
# 10/1/2023
# https://github.com/Endeared

# starter code was only minimally modified, didnt change
# var names

# assigning vars
theSum = 0.0
count = 0
data = input("Enter a number or press Enter to quit: ")

# repeatedly prompt user for input, then convert to float /
# iterate count / add to sum
while data != "":
    count += 1
    number = float(data)
    theSum += number
    data = input("Enter a number or press Enter to quit: ")

# print sum and average
print("\nThe sum is", theSum)
print(f'The average is {theSum / count}')