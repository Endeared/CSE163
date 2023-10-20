# Ross Hamey
# CSE163 - P5.5
# 10/16/2023
# https://github.com/Endeared

# our lookup table - could have done a for loop to make this, but wanted it explicit
lookup_table = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

def repToDecimal(str, base):
    # setting our initial final var to 0
    final = 0

    # iterating over all characters in our string, setting the char to uppercase
    # then getting its value from our lookup table. then, we multiply our base by
    # our existing final sum, and add our new value to it, then set it to final
    for char in str:
        char = char.upper()
        num = lookup_table[char]
        final = base * final + num

    # lastly, return final
    return final


# A main for testing your program
def main():
    """Tests the function."""
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))

# The entry point for program execution
if __name__ == "__main__":
    main()