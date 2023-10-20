# Ross Hamey
# CSE163 - P5.2
# 10/16/2023
# https://github.com/Endeared

# grabbing file name and creating empty list
file_name = input("Enter the input file name: ")
file_lines = []

# opening file and assigning the lines as a list to our file_lines var,
# since .splitlines() returns a list
with open(file_name, "r") as file:
    file_lines = file.read().splitlines()

# setting up our loop
stop_loop = False

# while loop that runs until stop_loop is set to True
while not stop_loop:
    # at the start, we print out the number of lines and prompt the user
    # for a line number to check
    print(f'The file has {len(file_lines)} lines.')
    response = input('Enter a line number [0 to quit]: ')

    # if their response is 0, we end the loop
    if response == '0':
        stop_loop = True
    # otherwise, we set their response as an index and check if the index is valid
    else:
        index = int(response) - 1
        # if index is invalid, we print an error
        if index < 0 or index + 1 > len(file_lines):
            print(f'ERROR: line number must be less than {len(file_lines)}.')
        # otherwise, we grab the data at that index and print it
        else:
            data = file_lines[index]
            print(f'{response} : {data}')