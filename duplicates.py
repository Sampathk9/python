#!/usr/bin/env python3
def has_duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 2]
    if has_duplicate(numbers):
        print("The list contains duplicates.")
    else:
        print("The list does not contain duplicates.")