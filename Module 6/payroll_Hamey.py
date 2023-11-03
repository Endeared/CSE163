# Ross Hamey
# CSE163 - Module 6, Mini Project 2
# 10/22/2023
# https://github.com/Endeared

# recording: https://youtu.be/whCvQGhb1R8
# (i always try to record projects / longer
# assignments for future reference)

# match_employees function, which matches data based on employee ids from our
# input text files
def match_employees():
    # creating empty lists for later use
    employees, timeclock, final_data = [], [], []

    # opening both files, reading them into our empty lists from earlier using
    # splitlines (rather than readlines, so we dont have \n at the end of our last
    # val), then closing files
    with open('personnel.txt', 'r') as emp:
        employees = emp.read().splitlines()
    with open('timeclock.txt', 'r') as tc:
        timeclock = tc.read().splitlines()
    emp.close()
    tc.close()

    # iterating over our employees list
    for employee in employees:
        # grabbing each value for a single employee into a list and creating empty dict
        employee_data = employee.split(',')
        employee_dict = {}

        # iterating over our timeclock list
        for clock in timeclock:
            # grabbing each value for a single timeclock line into a list
            clock_data = clock.split(',')

            # if our ids match, we create an employee dict with all relevant data
            if employee_data[0] == clock_data[0]:
                employee_dict = {
                    'name': employee_data[1],
                    'hours': int(clock_data[1]),
                    'wage': float(employee_data[2]),
                    'id': employee_data[0],
                    'shift': clock_data[2]
                }
                # then we append that dict to our earlier list and break out of
                # our for clock in timeclock loop
                final_data.append(employee_dict)
                break

    # once weve gone through all employees, return our final_data list which should now
    # be filled with employee data
    return final_data

# calculate_payroll func, which takes in our data returned from match_employees
def calculate_payroll(data):
    # create empty payroll list
    payroll = []

    # iterate over all employees
    for employee in data:
        # initialize each key-value to a variable for ease of access
        hours = employee['hours']
        shift = employee['shift']
        wage = employee['wage']
        id = employee['id']
        name = employee['name']

        # if they worked 3rd shift, increase wage by 1
        if shift == '3':
            wage += 1
        
        # if they worked overtime
        if hours > 40:
            # grab regular time + overtime, add and leave 2 decimal places
            regular_time = 40 * wage
            overtime = (hours - 40) * wage * 1.5
            gross_pay = overtime + regular_time
            gross_pay_final = "%.2f" % gross_pay
        # if they didnt work overtime
        else:
            # grab all time, leave 2 decimal places
            gross_pay = hours * wage
            gross_pay_final = "%.2f" % gross_pay
        
        # append relevant employee data + gross pay to a new dict
        employee_payroll_final = {
            'id': id,
            'name': name,
            'gross_pay': gross_pay_final
        }
        # append that dict to our payroll list from earlier
        payroll.append(employee_payroll_final)
    
    # once weve gone through each employee, return our payroll list
    return payroll

# write_payroll function, which takes our list from our calculate_payroll function
def write_payroll(data):
    # create a new file named payroll.txt
    with open('payroll.txt', 'w') as pr:
        # go over each employee, write their id + name + gross pay in order on each
        # line
        for employee in data:
            pr.write(f"{employee['id']},{employee['name']},{employee['gross_pay']}")
            pr.write('\n')
    # close our file
    pr.close()


def main():
    data = match_employees()
    payroll = calculate_payroll(data)
    write_payroll(payroll)
    input()

if __name__ == "__main__":
    main()