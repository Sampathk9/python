#!/usr/bin/env python3
from collections import Counter

def find_first_unique(text):
    """Find the first character that appears only once in the text."""
    char_count = Counter(text)
    for char in text:
        if char_count[char] == 1:
            return char
    return None

# __name__ is a special variable in Python that represents the name of the module.
# When a module is run directly, __name__ is set to "__main__".
# This allows us to run some code only when the module is executed directly,
# and not when it is imported by another module.
# This is useful for testing or demonstrating functionality.
# Here, we use it to test the find_first_unique function.
if __name__ == "__main__":
    test_string = "swiss"
    result = find_first_unique(test_string)
    if result:
        print(f"First unique character in '{test_string}': {result}")
    else:
        print("No unique characters found")
