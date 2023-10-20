# Ross Hamey
# CSE163 - P5.7
# 10/16/2023
# https://github.com/Endeared

# grabbing text file name, creating empty list
file_input = input("Enter the input file name: ")
all_words = []

with open(file_input, "r") as file:
    # opening file and reading each word into a list by calling .split(),
    # then sorting the list
    all_words = file.read().split()
    all_words.sort()

# iterating over every word in the list and printing it
for word in all_words:
    print(word)