class BST:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Average: O(Log n) time, O(1) space
    # Worst: O(n), time, O(1) space
    def add(self, data):
        curr_node = self
        while True:
            # if value we are trying to insert is < current vallue, check left subtree
            if data < curr_node.data:
                # if there is a node on the left, then let's move there
                if curr_node.left:
                    curr_node = curr_node.left
                # if there is not, then insert and leave loop
                else:
                    curr_node.left = BST(data)
                    break
            # else, this means we should look at the right subtree. This also means that if the value is the same,
            # then we will attach the duplicate value to the right.
            else:
                # if there is a node on the right, let's move there
                if curr_node.right:
                    curr_node = curr_node.right
                # if there is not, then insert and leave loop
                else:
                    curr_node.right = BST(data)
                    break

        # so we can chain insertions. not needed
        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right
            else:
                return True
        return False

    def delete(self, value):
        # self = self
        print('the root:')
        in_order_traversal(self)
        # base case is that the root is empty
        # if not self:
        #     print('no root')
        #     # maybe self = None. maybe we don't even need this
        #     return None
        # if value is smaller, look into left subtree
        if value < self.data:
            print(f'value {value} < root.data {self.data}')
            self.left.delete(value)
            print('the root:')
            in_order_traversal(self)
        # if value is bigger, look into right subtree
        elif value > self.data:
            print(f'value {value} > root.data {self.data}')
            self.right.delete(value)
            print('the root:')
            in_order_traversal(self)
        # if it's equal
        else:
            print(f'value {value} = root.data {self.data}')
            # case 1: root to delete has no children
            if not self.left and not self.right:
                print('no children')
                # update root to none. maybe self = None?
                # root = None
                self = None
                # del self
                # print(self)
                print('the root:')
                in_order_traversal(self)
            # case 2: root to delete has two children
            elif self.left and self.right:
                print('both children')
                # find it's right subtree's min value, replace with root's value, then delete the min node
                successor = self.right.get_min_value() # we want the value not the node
                print(f'successor: {successor}')
                self.data = successor # careful with nodes and node.data here
                self.right.delete(successor)
                print('the root:')
                in_order_traversal(self)
            # case 3: root to delete has one child
            else:
                print('one child')
                # if root.left:
                #     self = root.left
                # else:
                #     self = root.right
                self = self.left if self.left else self.right
                # return root.left if root.left else root.right
                # if it has a left child, then replace root with it
                # if it has a right child, then replace root with it
                print('the root:')
                in_order_traversal(self)
        # returning is optional
        return self


    def get_min_value(self):
        root = self
        while root.left:
            root = root.left
        return root.data

    # def in_order_traversal(tree):
    #     if tree:
    #         # visit left subtree first
    #         in_order_traversal(tree.left)
    #         # on returning from the deepest recursive call, we'll be at the very bottom left of tree, which will be the
    #         # smallest value in the entire tree due to the nature of the BST, so we print it
    #         print(tree.data)
    #         # then we move to the right side of these sub trees, performing the same operations. Checking the lower left
    #         # nodes and moving to the lower right nodes
    #         in_order_traversal(tree.right)

def in_order_traversal(tree):
    if tree:
        in_order_traversal(tree.left)
        print(tree.data)
        in_order_traversal(tree.right)

def post_order_traversal(tree):
    if tree:
        post_order_traversal(tree.left)
        post_order_traversal(tree.right)
        print(tree.data)

def pre_order_traversal(tree):
    if tree:
        print(tree.data)
        post_order_traversal(tree.left)
        post_order_traversal(tree.right)


def in_order_traversal_iterative(tree):
    myStack = []
    result = []

    # while the stack is not empty or the tree is not empty
    while myStack or tree:
        # only one of these two things will be called
        # if there is a tree
        if tree:
            # append it to the stack
            myStack.append(tree)
            # move on to the left one (to follow in order traversal)
            tree = tree.left
        # otherwise, if there is no tree
        else:
            # print the node popped from the top of the stack (making sure we save it)
            current = myStack.pop()
            result.append(current.data)
            # move on to right side of tree
            tree = current.right

    print(result)
    return result


# Function to find maximum value node in subtree rooted at ptr
def maximumKey(ptr):

	while ptr.right:
		ptr = ptr.right

	return ptr


# Function to delete node from a BST
def deleteNode(root, key):

    # base case: key found not in tree
    if root is None:
        return root

    # if given key is less than the root node, recur for left subtree
    if key < root.data:
        root.left = deleteNode(root.left, key)

    # if given key is more than the root node, recur for right subtree
    elif key > root.data:
        root.right = deleteNode(root.right, key)

    # key found
    else:

        # Case 1: node to be deleted has no children (it is a leaf node)
        if root.left is None and root.right is None:
            # update root to None
            return None

        # Case 2: node to be deleted has two children
        elif root.left and root.right:
            # find its in-order predecessor node
            predecessor = maximumKey(root.left)

            # Copy the value of predecessor to current node
            root.data = predecessor.data

            # recursively delete the predecessor. Note that the
            # predecessor will have at-most one child (left child)
            root.left = deleteNode(root.left, predecessor.data)

        # Case 3: node to be deleted has only one child
        else:
            # find child node
            child = root.left if root.left else root.right
            root = child

    # return root

def validate_bst(tree):
    in_order_arr = in_order_traversal_iterative(tree)
    for i in range(len(in_order_arr) - 1):
        if in_order_arr[i] > in_order_arr[i + 1]:
            return False
    return True

def validate_bst_2(tree):
    myStack = []

    # while the stack is not empty or the tree is not empty
    while myStack or tree:
        # only one of these two things will be called
        # if there is a tree
        if tree:
            # append it to the stack
            myStack.append(tree)
            # move on to the left one (to follow in order traversal)
            # check if left (child) is less than tree (parent)
            if tree.left and tree.left.data > tree.data:
                return False
            tree = tree.left
        # otherwise, if there is no tree
        else:
            # print the node popped from the top of the stack (making sure we save it)
            current = myStack.pop()
            print(current.data, end=" ")
            # move on to right side of tree
            # check if right (child) is greater than current (parent)
            if current.right and current.right.data < current.data:
                return False
            tree = current.right
    return True

# main
my_bst = BST(15).add(10).add(20).add(8).add(12).add(25)
in_order_traversal(my_bst)  # prints them in order
print(validate_bst_2(my_bst))
# # post_order_traversal(my_bst)
# # pre_order_traversal(my_bst)
# # print('is 10 in the tree?', my_bst.contains(10))
# # print('is 100 in the tree?', my_bst.contains(100))
# # root = deleteNode(my_bst, 4)
# # in_order_traversal(root)
# print()
# my_bst.delete(20)
# in_order_traversal(my_bst)