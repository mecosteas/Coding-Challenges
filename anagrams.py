def is_anagram(a, b):
    # if lengths are different, then they're not anagrams by definition
    if len(a) is not len(b):
        return False
    # initiate an array with 256 zeroes to represent the frequency of ASCII characters
    arr = 256*[0]
    for i in range(len(a)):
        # since both strings are the same length at this point, we increase the value of our array element by one at the
        # index corresponding to the ASCII character value of the first string
        arr[ord(a[i])] += 1
        # for the second string, we decrease the value of the element at the corresponding ASCII character value
        arr[ord(b[i])] -= 1
    # in the end, if the string is truly an anagram of the other, then the array should contain only 0s
    # if any of the elements are True (not False; not 0), then b is not an anagram of a.
    if any(arr):
        return False
    else:
        return True

print(is_anagram('cinema', 'iceman')) # true
print(is_anagram('batman', 'btanma')) # true
print(is_anagram('batman', 'bat')) # false