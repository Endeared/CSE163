# Ross Hamey
# CSE163 - P6.8
# 10/22/2023
# https://github.com/Endeared

def printAll(seq):
    # adding print to trace function arg
    print(seq)
    # rest of code stays the same
    if seq:
        print(seq[0])
        printAll(seq[1:])

def main():
    # test for empty list
    seq = []
    printAll(seq)
    # test for filled list
    seq = [1, 2, 3]
    printAll(seq)
    # test for string
    seq = "abc"
    printAll(seq)
    # test for tuple
    seq = (1, 2, 3)
    printAll(seq)

if __name__ == "__main__":
    main()