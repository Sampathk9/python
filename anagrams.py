#!/usr/bin/env python3

# Requirement: Check if two strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# For example, "listen" and "silent" are anagrams.
# Eat, Tea and Ate are also anagrams, ignoring case and spaces.

# Given String ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Approach: Sort the characters of each string and use the sorted string as a key in a dictionary to group anagrams together.

# DSA Concept: Hashing (using a dictionary to group anagrams), Sorting (sorting the characters of the strings to create a unique key for anagrams)
# Anagrams share same sorted characters

# Approach 1: Sort the characters of each string and use the sorted string as a key in a dictionary to group anagrams together.
def group_anagrams(strs):
    anagram_dict = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = []
        anagram_dict[sorted_s].append(s)
    return list(anagram_dict.values())

if __name__ == "__main__":
    input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_strings)
    print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Complexity Analysis:
# Time Complexity: O(n * k log k), where n is the number of strings and k is the maximum length of a string. Sorting each string takes O(k log k) time, and we do this for n strings.
# Space Complexity: O(n * k), where n is the number of strings and k is the maximum length of a string. In the worst case, all strings are anagrams of each other, and we store all n strings in the dictionary.