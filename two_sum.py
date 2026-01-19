#!/usr/bin/env python3

def two_sums(nums, target):
    """Return indices of the two numbers that add up to target."""
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], index)
        num_to_index[num] = index
    return None

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target_value = 9
    result = two_sums(numbers, target_value)
    if result:
        print(f"Indices of numbers that add up to {target_value}: {result}")
    else:
        print("No two numbers add up to the target value.")
