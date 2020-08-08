"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
characters of the given string. If there are more than one possible results, return the longest word with the smallest
lexicographical order. If there is no possible result, return the empty string.
"""
"""
Given a string and a dictionary, find the longest entry in the dictionary that can be created by deleting characters from the string.

Example:
string = "batman", dictionary = ["bat", "aman", "antman"]

longest_anagram(string, dictionary) = "aman"
"""

# O(n^2) Time
def find_longest_word(s, d):
    longest = ''
    # check each word in dictionary
    for word in d: # O(n) where n is words in dictionary
        # compare lengths, if same, then compare alphabetical order
        if (-len(word), word) < (-len(longest), longest):
            # iterate through each letter in the string. IMPORTANT!!! We use an iterator instead of simply s because
            # this will allow us to sort of "pop" the letter off the iterator each time we check against it. So that not
            # only are we checking if the letter exists in the word, we are also checking the frequency of the letter
            # IMPORTANT!!! The iterator is checked in order.
            it = iter(s)
            # return True if all values are true in the generator returned from the expression
            # if all characters in the string are in the dictionary word (a subsequence exists)
            if all(c in it for c in word): # O(n) where n is the character in the word
                longest = word
    return longest

s = 'batman'
d = ["bat", "aman", "antman", "namtab"]

print(find_longest_word(s, d))
