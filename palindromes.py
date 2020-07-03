# O(n) time, O(n) space where n is the size of the string
def isPalindrome(the_string):
# reverse the string and check if the string == reversed string
  reversed = the_string[::-1]  # O(n)
  if the_string == reversed:    # O(1) assuming it uses hash code to compare.
    return 1
  return 0

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

#  Roughly O(n^3)
def find_longest_palindromic_substring(s):  # if s is itself a palindrome, does that count?
    n = len(s)
    #  Strings of length 2 or are always palindromic, and length 0 are obviously nothing
    if n <= 2:
        return s

    window = n  # start at the full string's length (n - 1 could work if we don't want to consider whole string)
    while window > 1:  # O(w)
        start = 0
        end = start + window
        while end <= (n):  # n instead of n - 1 because of the way array splicing works. O(n - window)
            # print(s[start:end], start, end)
            sub = s[start:end]
            if isPalindrome(sub):  # O(n)
                return sub
            start += 1
            end += 1
        window -= 1



s = 'babad'
s1 = "cbbd"
s3 = "al"
s4 = ""
# print(find_longest_palindromic_substring(s))
# print(find_longest_palindromic_substring(s1))
# print(find_longest_palindromic_substring(s3))
# print(find_longest_palindromic_substring(s4))


# O(n^2) time, O(n) space which is our growing string length
# The high level explanation of this algorithm would be that the helper is like an "expander" that expands the search
# beginning at a starting point, and the for loop provides that point. The for loop says, "start expanding at 0, then
# 1, 2, 3, etc. Each time trying to find the largest palindrome". The helper function says, "i'll expand to try to find
# the longest function, just tell me where to start expanding left and right from". Then we check if the palindrome
# found by the helper is larger than the previous one. We do this check twice to make sure we cover every possible
# expansion window possible which is achieved by checking "odd" and "even" starting positions.
def longestPalindrome(s):
    res = ""
    #  We're going to check the entire string using windows of increasing size
    for i in range(len(s)):
        # odd case, like "aba"
        # in odd case we pass in the same i for l and r because we have to start in the middle and expand to the l and r
        # by 1 and check if those values are equal each time
        tmp = helper(s, i, i)
        # if the result of that is larger than what we had previously (we begin with length 0), then we update the
        # largest palindrome
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        # for even case we pass in i and i + 1 for l and r because we need to begin at the middle two values in our
        # window and expand l and r by one. each time we check if they are equal
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res


# get the longest palindrome, l, r are the middle indexes of the window
# from inner to outer
def helper(s, l, r):
    # the first two checks help us stay within bounds, the third is to make sure we're looking at a palindrome
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    # l + 1 because we either exited the loop because the values at l and r weren't equal, which means the previous
    # check was in fact equal, so we want to pass in the previous position--OR the left index went out of bound and we
    # need to use an in-bound index. The reason why we don't need to do r - 1 is because array splicing is exclusive
    # on the right bound.
    return s[l + 1:r]

print(longestPalindrome("abbabaaba"))