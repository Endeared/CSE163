# Ross Hamey
# CSE163 - P4.1
# 10/8/2023
# https://github.com/Endeared

message = input("Enter a message: ")
distance = input("Enter the distance value: ")
final_string = ""

for char in message:
    char_ascii = ord(char)
    char_ascii += int(distance)
    final_string += chr(char_ascii)

print()
print(final_string)