# Ross Hamey
# CSE163 - P2.10
# 9/17/2023
# https://github.com/Endeared

hourly_wage = float(input("Enter the wage: "))
hours_worked = float(input("Enter the regular hours: "))
overtime_hours = float(input("Enter the overtime hours: "))

total_pay = (hours_worked * hourly_wage) + (overtime_hours * hourly_wage * 1.5)
print(f'The total weekly pay is ${total_pay}')