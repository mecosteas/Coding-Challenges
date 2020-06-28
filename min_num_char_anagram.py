"""
Minimum Characters required to make a String Palindromic
You are given a string. The only operation allowed is to insert characters in the beginning of the string. Return the number of characters that are needed to be inserted to make the string a palindrome string


Examples:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
"""
#  I think this algorithm is O(n*m) where n is the length of the string (since we need to reverse it each time we
#  check the while loop condition. although each iteration n reduces by 1) and m is the number of times we'll need
#  to delete.
#  We could improve it by saving the reversed list in a different variable so we only have to do it once, then
#  after popping the list we also remove the first element in the reversed list. (our string is a stack and our
#  reversed list is a queue). I think this would make it an O(n) time since popping a stack and removing from a
#  queue are both O(1)
def min_char_to_make_palindrome_by_deletion(s):
    deletions = 0
    s = list(s)
    # check if it's a palindrome
    while s != s[::-1]:
    # if not, delete last char, then check again
        s.pop()
        deletions += 1
    # the number of deletions will equal the number of min chars
    return deletions

#  The time complexity would be O(n^2) because of the while loop and because of the string concatenation
def min_char_to_make_palindrome_by_pointers_and_insertion(s):
    beginning = 0
    end = len(s) - 1
    counter = 0
    while beginning != end:
        # print(beginning, end, s[beginning], s[end])
        if s[beginning] != s[end]:
            s = s[end] + s
            beginning += 1
            counter += 1
            continue
        beginning += 1
        end -= 1
    return counter

s = 'AACECAAAA'
# print(min_char_to_make_palindrome_by_deletion(s))
print(min_char_to_make_palindrome_by_deletion(s))
print(min_char_to_make_palindrome_by_pointers_and_insertion(s))