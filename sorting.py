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
# print(bubble_sort(arr))
# print(bubble_sort(arr2))
# print(bubble_sort(arr3))


# We can make a binary search tree and add a list of numbers to it in O(n) time
# Then we can print them in order in O(n) time. So we could technically sort it in O(n)
# But it would take O(n) space if everything is done iteratively.
# I tried returning a list from the in_order_traversal but it's quite complicated with the recursive way. Perhaps
# doing it iteratively would be the way to go if we want to make this work.
class TreeNode:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, data):
        # if root hasn't been initialized
        if not self.data:
            self.data = data
        else:
            # begin with root
            root = self
            # we'll keep going until we end up finding an empty node either on the left or right side
            while True:
                # if data is less than the current root's data
                if data < root.data:
                    # check if a left subtree exists
                    if root.left:
                        # if so, move to that subtree so we can keep checking if the data is less than the root
                        root = root.left
                    else:
                        # if not, add the data to the left root node
                        root.left = TreeNode(data)
                        break
                # if the data is greater than the current root's data
                else:
                    # check if a right subtree exists
                    if root.right:
                        # if so, move to that subtree
                        root = root.right
                    else:
                        # if not, add the data to the right subtree's root
                        root.right = TreeNode(data)
                        break
        # not necessary but helps so we can chain this function
        return self

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data, end=' ')
        if self.right:
            self.right.in_order_traversal()

    def add_list(self, l):
        for item in l:
            self.add(item)

# bst = TreeNode(1)
# bst.add(2).add(0).add(5).add(3).add(4)
# # in_order_traversal(bst)
# bst.in_order_traversal()
# bst_from_list = TreeNode()
# bst_from_list.add_list(arr3)
# print()
# bst_from_list.in_order_traversal()