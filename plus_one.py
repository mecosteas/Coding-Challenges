"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


# Function to convert the array to an integer
def array_to_int(arr):
    integer = 0
    pow = 0
    last_element = len(arr) - 1
    while last_element >= 0:
        # Ex: [1,2,3] = 3 * 10**0 + 2 * 10**1 + 3 * 10**2 = 123
        integer += arr[last_element] * (10 ** pow)
        pow += 1
        last_element -= 1
    return integer


# Function to convert integer to array
def int_to_array(num):
    # string_num = str(num)
    # for digit in string_num:
    #     arr.append(int(digit))
    # Using list comprehension:
    arr = [int(digit) for digit in str(num)]
    return arr


# Solution 1 is O(n). More specifically O(n + n) where n is the number of digits in the array
def plus_one(arr):
    num = array_to_int(arr)
    num += 1
    arr = int_to_array(num)
    return arr


print('Solution 1')
l = [1, 2, 3]
l2 = [4, 3, 2, 1]
print(plus_one(l))
print(plus_one(l2))

print('\nSolution 2')
# Another solution: O(n) where n is the number of 9's in a row from right to left
def plus_one2(arr):
    # if the last element is NOT a 9, simply add 1 and return list
    if arr[-1] != 9:
        arr[-1] += 1
        return arr
    # otherwise, check from right to left while the value is 9 and we haven't gone out of bounds
    else:
        i = len(arr) - 1
        while arr[i] == 9 and i >= 0:
            arr[i] = 0
            i -= 1
        # If we exited the while loop it's because we either went out of bounds or found a non-nine value
        # if we went out of bounds, then insert a 1 at the beginning of the array
        if i < 0:
            return [1].extend(arr)
        # if we didn't go out of bounds, then we must have found a non-nine, so simply add 1 and return the array
        else:
            arr[i] += 1
            return arr


print(plus_one2(l))
print(plus_one2(l2))
