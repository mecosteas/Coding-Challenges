# O(n) time | O(1) space
def find_pivot_index(input_list):
    # We have a start, end, pivot, and min_index. Start and min_index begin at first element
    s = min_index = 0
    e = len(input_list) - 1
    # while the start and end don't meet or pass each other, we iterate
    while s < e:
        # pivot is calculated depending on the number of elements between our endpoints
        # if even, pivot is half way between endpoints + 1 (to get the second middle number)
        # this is crucial to our algorithm because if we were to pick the first middle element,
        # our start point and pivot would always equal each other at a certain point and this
        # would create an infinite loop
        p = ((e + s) // 2) + 1 if ((e - s) + 1) % 2 == 0 else (e + s) // 2
        # if pivot value < min value, this means that anything to the right of p will be greater than
        # its value because we know they're in order. At this point, we could have found the minimum
        # index, but we still have more values to the left that could possibly be smaller.
        if input_list[p] < input_list[min_index]:
            # So to check the left side, we move the end point to where p is and update min_index
            min_index = p
            e = p
        # if pivot value >= min value, then we know we should check the right half to find where the
        # array was rotated at since that's the only possible place we could find the min value
        else:
            s = p
    return min_index


ll = [11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [4, 5, 6, 7, 0, 1, 2]
l2 = [1, 2, 4, 5, 6, 7]
l3 = [12, 14, 17, 19, 20, 21, 7, 8, 9]
l4 = [1, 2, 3, 4]
l5 = [5, 6, 7, 0, 1, 2, 3]
print(find_pivot_index(ll))
print(find_pivot_index(l))
print(find_pivot_index(l2))
print(find_pivot_index(l3))
print(find_pivot_index(l4))
print(find_pivot_index(l5))