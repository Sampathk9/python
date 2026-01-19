#!/usr/bin/env python3
from collections import Counter

def find_first_unique(text):
    """Find the first character that appears only once in the text."""
    char_count = Counter(text)
    for char in text:
        if char_count[char] == 1:
            return char
    return None

if __name__ == "__main__":
    test_string = "swiss"
    result = find_first_unique(test_string)
    if result:
        print(f"First unique character in '{test_string}': {result}")
    else:
        print("No unique characters found")
