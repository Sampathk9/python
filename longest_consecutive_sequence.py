#!/usr/bin/env python3
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Approach: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

# DSA Concept: Hashing (using a set to store unique elements and check for consecutive numbers efficiently)
# Visual
# Given - [100, 4, 200, 1, 3, 2]
# Set - {100, 4, 200, 1, 3, 2}
# Check if num - 1 is not in set, then it's the start of a sequence
# For num = 1, check if 0 is in set (not in set), then check for 2, 3, 4 in set (all in set), so current streak is 4

# 100 → 99 not present → start → length 1
# 4 → 3 present → skip
# 1 → 0 not present → start → count 1,2,3,4 → length 4
# Example with your input [100, 4, 200, 1, 3, 2]:

# 100 → 99 not in set → count: 100 (length 1)
# 4 → 3 in set → skip
# 200 → 199 not in set → count: 200 (length 1)
# 1 → 0 not in set → start → count: 1, 2, 3, 4 (length 4) ✓ longest
# 3 → 2 in set → skip
# 2 → 1 in set → skip
# Result: 4 (the sequence [1, 2, 3, 4])
# The beauty of using a set is O(1) lookup (in operator), so order doesn't matter—it's all about membership checking!
def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums) # Create a set of numbers for O(1) lookups - {100, 4, 200, 1, 3, 2}
    longest_streak = 0 # Initialize longest streak to 0

    for num in num_set: # Iterate through each number in the set - 100, 4, 200, 1, 3, 2
        if num - 1 not in num_set: # Check if the previous number is not in the set, indicating the start of a sequence
            current_num = num 
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    input_nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive(input_nums)
    print(f"Length of the longest consecutive sequence: {result}")