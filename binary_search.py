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