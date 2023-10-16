# Ross Hamey
# CSE163 - P3.7
# 10/1/2023
# https://github.com/Endeared

# grab data points to start with
starting_salary = float(input("Enter the starting salary: "))
annual_increase = input("Enter the annual % increase: ")
years = input("Enter the number of years: ")

# print header
print("\nYear   Salary")
print("-------------")

# iterate and print salary for each year after increase
for i in range(int(years)):
    print(f'{i + 1}    {starting_salary:.2f}')
    starting_salary *= 1 + float(annual_increase) / 100

