#!/usr/bin/env python3
""" Without Enumerate """
nums = [10, 20, 30]

for i in range(len(nums)):
    print(i, nums[i])

""" With Enumerate """
nums = [10, 20, 30]

for index, value in enumerate(nums):
    print(index, value)

# Step 1: Simple loop
nums = [2, 7, 11, 15]

for num in nums:
    end = ', ' if num != nums[-1] else '\n'
    print(num, end=end)

# Step 2: Index + value
for i, num in enumerate(nums):
    print(i, num)

# step 3: Dictionary Basics
seen = {}

seen[2] = 0
seen[7] = 1

print(seen)
