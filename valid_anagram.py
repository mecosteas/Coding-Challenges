"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase letters.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution?
"""


# One way to solve this is to realize that the order of the letters don't matter. This means we can change their
# position if it helps us. Sorting would give us an O(n log(n)) time complexity
def validate_anagram_by_sorting(s, t):
    # First, if lengths don't match, then this cannot possibly be an anagram
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t


print('Validate by sorting', validate_anagram_by_sorting('anagram', 'nagaram'))
print('Validate by sorting', validate_anagram_by_sorting('rat', 'car'))

# Another way would be to make a frequency tables and compare letter counts (frequencies)
# This is done in O(n) time
def validate_anagram_by_letter_frequency(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for letter in s:
        if letter in s_dict:
            s_dict[letter] += 1
        else:
            s_dict[letter] = 1
    for letter in t:
        if letter in t_dict:
            t_dict[letter] += 1
        else:
            t_dict[letter] = 1
    for letter, frequency in s_dict.items():
        if letter not in t_dict:
            return False
        elif s_dict[letter] != t_dict[letter]:
            return False
    return True

print('Validate by letter frequencies:', validate_anagram_by_letter_frequency('anagram', 'nagaram'))
print('Validate by letter frequencies:', validate_anagram_by_sorting('rat', 'car'))

# Using counters
from collections import Counter
def validate_anagram_with_counter(s, t):
    s_counter = Counter(s)
    t_counter = Counter(t)
    for key in s_counter:
        if s_counter.get(key) != t_counter.get(key):
            print('test', t_counter.get('t'))
            return False
    return True

# print('Validate by letter frequencies:', validate_anagram_with_counter('anagram', 'nagaram'))
print('Validate by letter frequencies:', validate_anagram_with_counter('rat', 'car'))