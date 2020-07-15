#  Pass in an array, a target value, a left index, and a right index
#  O(log n) time, O(log n) space
def binary_search_recursive(arr, val, l, r):
    # This is our base case due to the fact that l keeps moving right when our target is greater than mid,
    # and r keeps moving left when our target is less than mid. Eventually r and l will meet each other,
    # and that's where our target value will be
    if r >= l:
        # calculate the middle value
        mid = (l + r) // 2
        # if the value at the mid index is > target value, look at elements to the left half
        if arr[mid] > val:
            return binary_search_recursive(arr, val, l, mid - 1)
        # if the value at the mid index is < target value, look at elements to the left half
        elif arr[mid] < val:
            return binary_search_recursive(arr, val, mid + 1, r)
        else:
            return arr[mid]
    else:
        return 'not found'

#  O(log n) time, O(1) space
def binary_search_iterative(arr, val, l, r):
    while r >= l:
        mid = (l + r) // 2
        if arr[mid] > val:
            r = mid - 1
        elif arr[mid] < val:
            l = mid + 1
        else:
            return arr[mid]
    return 'not found'


arr = [1, 2, 3, 4, 5]
# arr = [1]
val = 1
print('Recursive result:', binary_search_recursive(arr, val, 0, len(arr) - 1))
print('Iterative result:', binary_search_iterative(arr, val, 0, len(arr) - 1))


"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example:
Given [5, 7, 7, 8, 8, 10]
and target value 8,
return [3, 4].
"""


def search_for_range(array, target):
    left = binary_search_left_boundary(array, target)
    right = binary_search_right_boundary(array, target)
    return [left, right]


def binary_search_left_boundary(array, target):
    s = 0
    e = len(array) - 1
    while s <= e:
        p = (e + s) // 2
        if array[p] < target:
            s = p + 1
        elif array[p] > target:
            e = p - 1
        # array[p] == target and p-1 > 0 and array[p-1] < target
        # means we found a left boundary
        else:
            if p - 1 >= 0:
                # if left neighbor is less, than we must be at the left boundary
                if array[p - 1] < target:
                    return p
                # if it's sorted, technically, there cannot be a case where the left num is > current
                elif array[p - 1] > target:
                    return 'that is weird. this should not happen'
                else:
                    # if left neightbor is equal, search left side
                    e = p - 1
            # if we're at beginning of array, then this has to be the left boundary
            else:
                return p
    return -1


def binary_search_right_boundary(array, target):
    s = 0
    e = len(array) - 1
    while s <= e:
        p = (e + s) // 2
        if array[p] < target:
            s = p + 1
        elif array[p] > target:
            e = p - 1
        # array[p] == target and p-1 > 0 and array[p-1] < target
        # means we found a left boundary
        else:
            if p + 1 <= len(array) - 1:
                # if right neighbor is greater, then we must be at the left boundary
                if array[p + 1] > target:
                    return p
                # if it's sorted, technically, there cannot be a case where the left num is > current
                elif array[p + 1] < target:
                    return 'that is weird. this should not happen'
                else:
                    # if right neightbor is equal, search right side
                    s = p + 1
            # if we're at end of array, then this has to be the right boundary
            else:
                return p
    return -1


arr = [8, 8]
# print(binary_search_left_boundary(arr, 8))
# print(binary_search_right_boundary(arr, 8))
print(search_for_range(arr, 8))
