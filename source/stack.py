#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if self.list.head is None:
            return True
        else:
            return False


    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(n) >>> We have to traverse through the LL to reach the tail"""
        self.list.append(item)
        self.list.size += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.list.head is not None:
            return self.list.tail.data
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – Why? >>> we have to traverse the LL to reach the tail.data"""
        # TODO: Remove and return top item, if any, BUG FIX here
        if self.list.head is None:
            raise ValueError('The stack is empty')
        else:
            top_data = self.list.tail.data
            self.list.size -= 1
            return self.list.delete(top_data)

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if not self.list:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? >>> we can access the end of the array without traversing it"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.list:
            return None
        else:
            return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? >>> we can access the last item with list index"""
        
        if not self.list:
            raise ValueError('The Stack is empty')
        else:
            return self.list.pop(-1)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
