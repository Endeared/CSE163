# Ross Hamey
# CSE163 - P6.5
# 10/22/2023
# https://github.com/Endeared

def isSorted(my_list):
    # take in a list - if list is empty or only has one item, it is sorted
    # by default
    if len(my_list) == 0 or len(my_list) == 1:
        return True
    # otherwise, iterate over list and grab side-by-side values
    else:
        for i in range(len(my_list) - 1):
            val_one = my_list[i]
            val_two = my_list[i + 1]

            # compare values - if out of order, return false
            if val_one > val_two:
                return False
        # otherwise, return true
        return True

def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))

if __name__ == "__main__":
    main()