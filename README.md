# Python Code Repository

This repository contains Python code examples and scripts for learning and development purposes.

## Contents

- `unique.py` - Script to iterate through characters in a string
- `first_unique_character.py` - Find the first unique character in a string
- `1.py` - Python example
- `2.py` - Python example

## Usage

Run any Python script directly:
```bash
python3 script_name.py
```

Or make the script executable and run it:
```bash
chmod +x script_name.py
./script_name.py
```

## Data Structures

### List (Dynamic Array)
```python
arr = [1, 2, 3]
```
**Use when:** Ordered data, index access, iteration, two pointers, sliding window

| Operation       | Time   |
|-----------------|--------|
| Access          | O(1)   |
| Append          | O(1)   |
| Insert (middle) | O(n)   |

---

### Dictionary (HashMap)
```python
d = {}
```
**Use when:** Frequency counting, fast lookup, mapping key → value, complement search (Two Sum)

| Operation | Time |
|-----------|------|
| Insert    | O(1) |
| Lookup    | O(1) |

---

### Set (HashSet)
```python
s = set()
```
**Use when:** Fast existence check, remove duplicates, longest consecutive sequence

| Operation | Time |
|-----------|------|
| Add       | O(1) |
| Check     | O(1) |

---

### Heap (Priority Queue)
```python
import heapq
```
Default = Min Heap

**Use when:** Need Top K, Kth largest, streaming median, always need smallest/largest quickly

| Operation | Time     |
|-----------|----------|
| Push      | O(log n) |
| Pop       | O(log n) |

---

### Stack
Python doesn’t have a built-in stack, use list:
```python
stack = []
```
**Use when:** Parentheses validation, DFS, monotonic stack, undo/backtracking

---

### Queue (for BFS)
```python
from collections import deque
q = deque()
```
**Use when:** Level order traversal, BFS, shortest path

---

### Recursion
**Used for:** DFS, trees, backtracking
**Be careful:** Stack depth, base condition

---

## Algorithms

### HashMap Pattern
**Trigger words:** Frequency, count, duplicate, complement
**Examples:** Two Sum, Valid Anagram, Top K Frequent

### Sliding Window
**Trigger words:** Longest substring, subarray, continuous segment, window size
**Examples:** Longest Substring Without Repeat, Min Window Substring

### Two Pointers
**Trigger words:** Sorted array, pair sum, palindrome
**Examples:** Container With Most Water, 3Sum

### Stack
**Trigger words:** Parentheses, next greater, temperature warmer day, histogram
**Examples:** Valid Parentheses, Daily Temperatures

### DFS / BFS
**Trigger words:** Islands, connected components, tree traversal, graph cycle
**Examples:** Number of Islands, Course Schedule

### Binary Search
**Trigger words:** Sorted, find target, search range
**Examples:** Binary Search, Search Rotated Array

### Heap
**Trigger words:** Top K, Kth largest, merge K lists, real-time priority