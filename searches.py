#!/usr/bin/env python3

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search (requires sorted array)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3

    # Test Linear Search
    result = linear_search(arr, target)
    if result != -1:
        print(f"Linear Search: Found {target} at index {result}.")
    else:
        print(f"Linear Search: {target} not found in the array.")

    # Test Binary Search
    result = binary_search(arr, target)
    if result != -1:
        print(f"Binary Search: Found {target} at index {result}.")
    else:
        print(f"Binary Search: {target} not found in the array.")