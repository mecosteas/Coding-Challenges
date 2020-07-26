# O(n^2) Time | O(1) Space
def bubble_sort(arr):
    # we need to iterate at most n times
    for i in range(len(arr)):
        # we are comparing at most n - 1 times
        # we help it a bit by saying, "after we sort one number, we don't have to check all the way to the end anymore"
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



arr = [10,1,3,4,5,2,6,7,9,8]
arr2 = [10,9,8,7,6,5,4,3,2,1]
arr3 = [10,1,2,3,4,5,6,7,8,9]
arr4 = [1]
arr5 = []
# print(bubble_sort(arr))
# print(bubble_sort(arr2))
# print(bubble_sort(arr3))
# print(bubble_sort(arr4))
# print(bubble_sort(arr5))

# Not as good in Space as other algorithms, but it is consistent. Meaning worse and best cases are the same Time.
# This is the best way to sort Linked Lists
# O(n log n) Time | O(n) Space
def merge_sort(arr):
    # while array has more than one element, we need to bisect it
    if len(arr) > 1:
        # save left and right bisections separately
        # note that each of these bisections will already be sorted
        left_arr = merge_sort(arr[:len(arr) // 2])
        right_arr = merge_sort((arr[len(arr) // 2 : len(arr)]))
        left_index = 0
        right_index = 0
        new_arr = []
        # when we insert an element from left bisection, we'll move the left index up. same logic for right side
        # we are comparing the smallest elements in each array, and moving up the index accordingly to check the
        # second smallest, then third smallest, and so on
        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                new_arr.append(left_arr[left_index])
                left_index += 1
            else:
                new_arr.append(right_arr[right_index])
                right_index += 1
        # Once one of the indices goes out of bounds, we know we've "emptied" one array, so we simply extend the other
        if left_index >= len(left_arr):
            new_arr.extend(right_arr[right_index:])
        else:
            new_arr.extend(left_arr[left_index:])
        # return the sorted bisection
        return new_arr
    # otherwise, return the array of length 1
    else:
        return arr

# print(merge_sort(arr))
# print(merge_sort(arr2))
# print(merge_sort(arr3))
# print(merge_sort(arr4))
# print(merge_sort(arr5))


def is_sorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# it sorts, just doesn't give correct number of min operations
# I messed up, the task said delete APPEND. There should be no insertions. Oh well, I think this sorting algo is
# pretty cool anyway. Initially I had it right, where I was only appending. It can easily be turned back to that, but
# I like that this does it in less operations since we're looking at both min and max values.
# O(n^2) Time | O(n) Space... worse than bubble sort T_T
def da_sort(arr, ops=0):
    if not is_sorted(arr): # O(n)
        print('arr', arr)

        # if the min_index is already at the beginning, then it's already sorted, check the rest of the array
        min_index = arr.index(min(arr)) # O(n)
        max_index = arr.index(max(arr))
        if min_index == 0:
            print('min index is 0, already sorted at beginning, do not increase ops')
            min_num = arr.pop(min_index) # O(n)
            arr, ops = da_sort(arr, ops)
            arr.insert(0, min_num)
            print('after reinserting min where it was... arr: ', arr)
        # if the max_index is already at the end, then it's already sorted, check the rest of the array
        elif max_index == len(arr) - 1:
            print(f'max index is at {len(arr) - 1}, already sorted at end, do not increase ops')
            max_num = arr.pop(max_index)
            arr, ops = da_sort(arr, ops)
            arr.append(max_num)
            print('after reappending max where it was... arr: ', arr)
        # if the min_index is before max_index, then sort the max_num by inserting at the end
        elif min_index < max_index:
            print('max index is after min index, sort max')
            max_num = arr.pop(max_index)
            arr, ops = da_sort(arr, ops)
            arr.append(max_num)
            print('after append inserting max at the end... arr: ', arr, end=' ==> ')
            ops += 1
            print('increase ops', ops - 1, 'to', ops)
        # if the min_index is after the max_index, then sort the min_num by inserting at beginning
        elif min_index > max_index:
            print('min index is after max index, sort min')
            min_num = arr.pop(min_index)
            arr, ops = da_sort(arr, ops)
            arr.insert(0, min_num)
            print('after inserting min at the beginning... arr: ', arr, end=' ==> ')
            ops += 1
            print('increase ops', ops - 1, 'to', ops)
    return arr, ops

# print(da_sort([5,3,4,6,2,7,1]))


"""
You work at a sorting factory. You sort things. One day, your boss comes in to tell you there's a new ball shipment. There are three kinds of balls: red, white, and blue. You've been charged with the task of sorting these balls. Unfortunately, your boss won't let you take your lunch break until you've finished sorting the balls, so you want to do it quickly.

Instructions:
Create an algorithm that will sort an array of n elements, each element either red, white or blue. The integers 0, 1, 2, will represent red, white, and blue, respectively. Perform this sorting in-place, using constant space. Your solution should complete this in O(n) time, any longer and you'll miss your lunch break!

Example:
[0, 1, 0, 1, 2, 1] --> [0, 0, 1, 1, 2]

Extra Challenge:
The boss is threatening to replace your job with a very efficient sorting robot, provided you don't perform better than it would. Luckily for you, the robot requires taking two passes over the array to sort the elements. You're not sure, but you think there might be a way to sort the elements that requires taking only one pass over the array, thus handily out-performing the robot.

Original Platform:  https://leetcode.com/problems/sort-colors/ 
"""
# the white pointer serves as a categorizer. We don't know what the color is until the
# white pointer looks at it. It is then decided what to swap it with
def color_sort(nums):
  white = 0
  red = 0
  blue = len(nums) - 1
  while white <= blue:
    # if white points to red ball
    if nums[white] == 0:
      # swap white and red and increment white and red pointers
      nums[white], nums[red] = nums[red], nums[white]
      white += 1
      red += 1
    # if white points to white ball, increment white pointer
    elif nums[white] == 1:
      white += 1
    # if white points to blue
    else:
       # swap blue ball with the uncategorized ball (pointed by blue), decrease blue ptr
       nums[white], nums[blue] = nums[blue], nums[white]
       blue -= 1
  return nums

colors1 = [0,1,2,0,2,2,2,1,1,0,2,1]
print(color_sort(colors1))