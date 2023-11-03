# Ross Hamey
# CSE163 - P6.9
# 10/22/2023
# https://github.com/Endeared

def read_nums(filename):
    # opening file from filename
    file = open(filename, 'r')
    # splitting file into list of strings, create empty list
    data = file.read().split()
    nums = []

    # append each string in data as an int to our list
    for item in data:
        nums.append(int(item))

    # return our list
    return nums

def calculate_average(nums):
    # define total, add each num in nums to total
    total = 0
    for num in nums:
        total += num
    
    # calculate avg and return it
    average = total / len(nums)
    return average

def main():
    # prompt for filename, then call other functions
    filename = input('Enter the input file name: ')
    nums = read_nums(filename)
    average = calculate_average(nums)
    # print final result
    print(f'The average is {average}')

if __name__ == "__main__":
    main()