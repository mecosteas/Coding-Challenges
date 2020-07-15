"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Examples:

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

def find_index(sorted_list, target):
    # keep track of start and end index points, this is how we will "half" the array
    s = 0
    e = len(sorted_list) - 1
    while e >= s:
        p = (s + e) // 2
        # if number at pivot is == target, return pivot index
        if sorted_list[p] == target:
            return p
        # if num > target, look at the left half
        elif sorted_list[p] > target:
            e = p - 1
            t = p
        # if num < target, look at right half
        else:
            s = p + 1
            t = p + 1
    # print(f'num would be at index: {t}')
    return t


a = [1, 3, 5, 6]
print(find_index(a, 5))  # 2
print(find_index(a, 2))  # 1
print(find_index(a, 7))  # 4
print(find_index(a, 0))  # 0
print(find_index(a, 1))  # 0
print(find_index(a, 3))  # 1
print(find_index(a, 6))  # 3
print(find_index(a, 4))  # 2