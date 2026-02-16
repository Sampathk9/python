#!/usr/bin/env python3
# Given - nums = [1,2,3,4]
# Output - [24, 12, 8, 6]
# Explanation - 24 = 2*3*4, 12 = 1*3*4, 8 = 1*2*4, 6 = 1*2*3
# For each index i,
# multiply all numbers except nums[i]

# Approach 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def product_of_array_brute_force(nums):
    n = len(nums)
    result = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                result[i] *= nums[j]
    return result

# Approach 2: Using Left and Right Products
# Time Complexity: O(n)
# Space Complexity: O(n) for the result array and O(1) for the left and right products

# DSA Concept: Prefix and Suffix Products
# Prefix multiplication
# Suffix multiplication
# Avoiding nested loops
# answer = (product of left side) × (product of right side)

def product_of_array(nums):
    """Return an array where each element is the product of all other elements."""
    n = len(nums)
    if n == 0:
        return []
    
    # Initialize the result array with 1s
    result = [1] * n
    
    # Calculate the product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
    
    # Calculate the product of all elements to the right of each index
    right_product = 1

    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    result = product_of_array(numbers)
    print(f"Product of array except self: {result}")


# product_of_array works
# Given - nums = [1,2,3,4]
# We take 2 passes through the array:
# 1. First pass (left products):
# Left products:
# Given nums = [1, 2, 3, 4]
# - result[0] = 1 (no elements to the left)
# - result[1] = 1 * nums[0] = 1 * 1 = 1
# - result[2] = 1 * nums[0] * nums[1] = 1 * 1 * 2 = 2
# - result[3] = 1 * nums[0] * nums[1] * nums[2] = 1 * 1 * 2 * 3 = 6
# Result after first pass:
# [1, 1, 2, 6]
# 2. Second pass (right products):
# Right products:
# Given nums = [1, 2, 3, 4]
# - result[3] = 6 * 1 (no elements to the right) = 6
# - result[2] = 2 * nums[3] = 2 * 4 = 8
# - result[1] = 1 * nums[2] * nums[3] = 1 * 3 * 4 = 12
# - result[0] = 1 * nums[1] * nums[2] * nums[3] = 1 * 2 * 3 * 4 = 24
# Result after second pass:
# [24, 12, 8, 6]