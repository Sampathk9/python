#!/usr/bin/env python3
s = "swiss"

# for ch in s:
#     print(ch)


def unique_characters(s):
    if not s:
        return None

    freq ={}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    
    return None
print(unique_characters(s)) # w