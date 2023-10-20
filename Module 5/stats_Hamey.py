# Ross Hamey
# CSE163 - P5.1
# 10/16/2023
# https://github.com/Endeared

def median(nums):
    # if no entries, return 0
    if len(nums) == 0:
        return 0
    else:
        # otherwise, sort the list and grab the length
        nums.sort()
        length_nums = len(nums)

        # if our list has an even number of entries, we need to find the
        # two middle entries and average the two of them, then return that
        if length_nums % 2 == 0:
            lower = nums[length_nums // 2]
            higher = nums[length_nums // 2 - 1]
            result = (lower + higher) / 2
            return result
        # otherwise, we grab the entry at the index of the length divided by
        # 2 (floor division) - which will be the middle entry, then return it
        else:
            median = nums[length_nums // 2]
            return median
    
def mode(nums):
    # if no entries, return 0
    if len(nums) == 0:
        return 0
    else:
        # set a highest num and highest_count var to 0
        highest = 0
        highest_count = 0

        # iterate through all nums, grabbing the count of #each num. 
        # if that count is greater than our highest_count, we store
        # that as our highest num and set our new highest_count and return it
        for num in nums:
            if nums.count(num) > highest_count:
                highest = num
                highest_count = nums.count(num)
        return highest


def mean(nums):
    # if no entries, return 0
    if len(nums) == 0:
        return 0
    else:
        # otherwise, set a total var to 0
        total = 0

        # iterate through all nums and add them to our total var
        for num in nums:
            total += num
        # then divide the total by the length of the list and return it
        result = total / len(nums)
        return result
    
def main():
    lyst = [3, 1, 7, 1, 4, 10]
    print(lyst)
    print(f'Mode: {mode(lyst)}')
    print(f'Median: {median(lyst)}')
    print(f'Mean: {mean(lyst)}')

main()

