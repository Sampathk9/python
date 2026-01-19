#!/usr/bin/env python3
""" Requirement: Reverse a given string. """
"""
Strings are immutable in Python, meaning you cannot change them in place.
To reverse a string, we can convert it to a list (which is mutable),
perform the reversal, and then convert it back to a string.
"""
def reverse_string(s):
    left, right = 0, len(s) - 1
    s = list(s)

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)
