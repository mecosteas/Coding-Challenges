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
    # check to see if target is at edges or beyond edges
    # it might be a sloppy way of doing it, but it simplifies the logic for dealing with these
    # endpoint cases in my opinion.
    if sorted_list[s] == target or target < sorted_list[s]:
        return s
    elif sorted_list[e] == target:
        return e
    elif target > sorted_list[e]:
        return e + 1
    # stop when the distance between the end points is <= 1 (when they're neighbors)
    while e - s > 1:
        p = (s + e) // 2
        # if number at pivot is == target, return pivot index
        if sorted_list[p] == target:
            return p
        # if num > target, look at the left half
        elif sorted_list[p] > target:
            e = p
            t = p
        # if num < target, look at right half
        else:
            s = p
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
