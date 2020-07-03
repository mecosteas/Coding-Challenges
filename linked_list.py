class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        print('New linked list created.')
        self.head = None

    def append_end(self, val):
        if not self.head:
            self.head = Node(val)
            print(f'Appended {val} to the end.')
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
            print(f'Appended {val} to the end.')

    def append_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        print(f'Appended {val} to the front.')

    def print(self):
        curr = self.head
        print('List:', end=" ")
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print('List is empty. Nothing to remove.')
        else:
            # If there's only the head, delete the head
            if not self.head.next:
                print(f'Removing {self.head.data}')
                last_node_val = self.head.data
                self.head = None
                return last_node_val
            else:
                # Starting from head, look one node ahead. If node ahead is empty, then the last one is the next one.
                # "Delete" the last node by changing reference to the empty node after the last one.
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                last_node_val = curr.next.data
                curr.next = curr.next.next
                print(f'Removed {last_node_val} from the end.')
                return last_node_val

    def remove(self, val):
        if self.is_empty():
            print('List is empty. Nothing to remove.')
        else:
            if self.head.data == val:
                # if the head is the value to remove and it's the only node in list, remove head
                if not self.head.next:
                    print(f'Removed {val}, which was at the head.')
                    self.head = None
                # if the head is the value to remove and there is a next node, make the next node the head
                else:
                    print(f'Removed {val}, which was at the head.')
                    self.head = self.head.next
            else:
                # at this point we know the head isn't the one to be removed
                curr = self.head
                while curr.next.data != val:
                    curr = curr.next
                # when the next value is the value to be removed, skip that node and reference the one after
                curr.next = curr.next.next
                print(f'Removed {val} from the list.')

    def clear(self):
        self.head = None
        print('List cleared.')


def reverse_linked_list(ll):
    print('\nReversing linked list...')
    new_ll = MyLinkedList()
    while not ll.is_empty():
        new_ll.append_end(ll.pop())
    return new_ll

# def reverse_linked_list(ll):
#     while ll

# Main
ll = MyLinkedList()
ll.append_end(1)
ll.append_end(2)
ll.append_end(3)
ll.append_front(0)
ll.print()

reversed_ll = reverse_linked_list(ll)
reversed_ll.print()