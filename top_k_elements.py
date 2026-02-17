#!/usr/bin/env python3
# Given an array of integers, return the k most frequent elements.
# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Approach: Hash Map + Heap
# Time Complexity: O(n log k) - Building the frequency map takes O(n), and maintaining a heap of size k takes O(log k) for each of the n elements.
# Space Complexity: O(n) - The frequency map can have up to n entries in the worst case (when all elements are unique).
# DSA Concept: Hashing (using a dictionary to count frequencies) and Heaps (using a min-heap to keep track of the top k elements based on their frequencies).
# Visual
# Given - [1,1,1,2,2,3], k = 2
# Frequency Map - {1: 3, 2: 2, 3: 1}
# Min-Heap - [(3, 1), (2, 2)] → After processing all elements, the heap contains the top k elements based on frequency. 
import heapq

def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (-freq, num))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result
