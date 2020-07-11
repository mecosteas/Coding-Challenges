class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, data):
        # if head is empty
        if not self.head:
            # make new node the head
            self.head = Node(data)
            self.tail = self.head
        else:
            # otherwise
            new_node = Node(data)
            # start at head
            curr = self.head
            # keep checking if there's a next
            while curr.next:
                # update curr to the next while it exists
                curr = curr.next
            # once there's no next, attach the new node by referencing to it with next
            curr.next = new_node
            # make the new node's previous reference the current node
            curr.next.prev = curr
            self.tail = curr.next

# this function doesn't work for adding to an empty list, use add to end for that, and then you can use this
    def add_to_start(self, data):
        # create new node
        new_node = Node(data)
        # reference next node as the head [new -> head -> next]
        new_node.next = self.head
        # reference prev node as the new node [<- new <- head <- next]
        self.head.prev = new_node
        # make new head the new node [head -> next -> next]
        self.head = new_node

    def get_tail(self):
        return self.tail.data

    def get_tail_node(self):
        return self.tail

    def get_head(self):
        return self.head.data

    def print(self):
        if not self.head:
            return print('Nothing to print')
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def reverse(self):
        # swap head and tail
        self.head, self.tail = self.tail, self.head
        # establish start point at head
        curr = self.head
        # swap prev and next
        curr.next, curr.prev = curr.prev, curr.next
        # while next node exists
        while curr.next:
            # move on to next node
            curr = curr.next
            # and swap next and previous references
            curr.next, curr.prev = curr.prev, curr.next

    def remove(self, data):
        # if we need to remove the head and there is no other element
        if self.head.data == data and not self.head.next:
            self.head = None
        # if we need to remove the head and there is at least one more element in list
        elif self.head.data == data and self.head.next:
            # take prev reference to it away [<- head <- next] to [head.prev <- next]
            self.head.next.prev = self.head.prev  # same as head.prev which is same as None
            # curr.next = None
            self.head = self.head.next
        # if we're removing the tail
        elif self.tail.data == data:
            # move the tail back one node
            self.tail = self.tail.prev
            # dereference the new tail's references so they don't point at the old tail node
            self.tail.next = self.tail.next.next
        # if we're removing anything in between the head and the tail
        else:
            # start a reference point at the head
            curr = self.head
            # while there is a next node
            while curr.next:
                # move to the next node
                curr = curr.next
                # see if it contains the target value
                if curr.data == data:
                    # make previous node's next reference skip current node
                    curr.prev.next = curr.next
                    # and don't forget to make the next node's previous reference skip current node
                    curr.next.prev = curr.prev


def reverse_dll(dll):
    curr = dll.get_tail_node()
    reversed_dll = DoubleLinkedList()
    while curr.prev:
        reversed_dll.add_to_end(curr.data)
        curr = curr.prev
    reversed_dll.add_to_end(curr.data)
    return reversed_dll


dll = DoubleLinkedList()
dll.add_to_end(1)
dll.add_to_end(2)
dll.add_to_end(3)
dll.add_to_end(4)
dll.print()
dll.remove(4)
dll.print()

# Test get_head() and get_tail()
# print('head', dll.get_head(), 'tail', dll.get_tail())

# Test two reverse functions
# reversed_dll = reverse_dll(dll)
# reversed_dll.print()
# dll.reverse()
# dll.print()

# Test add_to_start()
# dll.add_to_start(0)
# dll.print()
# # print('head', dll.get_head(), 'tail', dll.get_tail())
