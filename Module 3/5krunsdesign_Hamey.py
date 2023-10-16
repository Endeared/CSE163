'''
Ross Hamey
CSE163 - Mini Project 1
9/22/2023
https://github.com/Endeared

This program prompts the user for a series of 5K run times (in minutes),
and calculates various data regarding their times to output back to the
user. I implemented two possible solutions for this - but the first
solution (without a list) is the solution I will use for my outputs.

vod: https://youtu.be/Ccx22OUISDQ
(i try to record assignments i work on as
a benchmark / for my own future reference)
'''


# first method - without a list => this function is being called at the end of the file
def runs_without_list():

    # our initial variables - we need a boolean for our while loop, and 
    # then set two variables to 0 to increment our count and add to our total sum
    finished_input = False
    total_minutes = 0
    count = 0

    while not finished_input:

        # try-except incase input isn't a valid int
        try:
            # grabbing user input
            time = input('Please enter a whole number time in minutes for a 5K run (press enter to end): ')

            # if our input isn't blank, we try to cast the input to an int and increment count 
            # + add our int input to our total count. if it fails to cast, we will run into an error
            if time != '':
                time = int(time)
                count += 1
                total_minutes += time
            # otherwise, the input is blank, so we end our while loop
            else:
                finished_input = True
        # if input is not a valid int, show a prompt accordingly and restart while loop
        except Exception as error:
            print('Invalid input!')
            continue

    # calculating our average minutes per run and average minutes spent per km
    average_minutes = round(total_minutes / count, 2)
    average_minutes_per_km = round(total_minutes / count / 5, 2)

    # finally, print statement to display results.
    print(f'''
    You ran for {count} days for a total of {total_minutes} minutes.
    Your average minutes per run was {average_minutes} minutes, while your average minutes per kilometer was {average_minutes_per_km} minutes/km.
    ''')
    input()


# second alternative method - with a list
def runs_with_list():
    finished_input = False
    time_data = []

    while not finished_input:

        # try-except incase input isn't a valid int
        try:
            # grabbing user input
            time = input('Please enter a whole number time in minutes for a 5K run (press enter to end): ')

            # if our input isn't blank, we try to cast the input to an int and append our 
            # input to our list. if the input fails to cast, we will run into an error
            if time != '':
                time = int(time)
                time_data.append(time)
            # otherwise, the input is blank, so we end our while loop
            else:
                finished_input = True
        # if input is not a valid int, show a prompt accordingly and restart while loop
        except Exception as error:
            print('Invalid input!')
            continue

    # getting num of inputs by calling len() on our list, then getting sum of inputs by calling sum() on our list. 
    # lastly, we calculate the average minutes of each run and average minutes spent per km ran
    count = len(time_data)
    total_minutes = sum(time_data)
    average_minutes = round(total_minutes / count, 2)
    average_minutes_per_km = round(total_minutes / count / 5, 2)

    # finally, print statement to display results.
    print(f'''
    You ran for {count} days for a total of {total_minutes} minutes.
    Your average minutes per run was {average_minutes} minutes, while your average minutes per kilometer was {average_minutes_per_km} minutes/km.
    ''')

# calling our first method / function here
runs_without_list()
