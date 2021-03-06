#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if not self.list.head:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue (head of the LL).
        Running time: O(1) – Why? >>> back of the queue can be accessed via LL head, no need to traverse"""
        self.list.prepend(item)
        # self.list.size += 1


    def front(self):
        """Return the item at the front (tail of the LL) of this queue without removing it,
        or None if this queue is empty."""
        if not self.list.head:
            return None
        else:
            return self.list.tail.data


    def dequeue(self):
        """Remove and return the item at the front of this queue (tail of the LL),
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? >>> front of the queue is tail of the LL, can be accessed via tail.data"""
        if not self.list.head:
            raise ValueError('The queue is empty')
        else:
            front_data = self.list.tail.data
            self.list.delete(front_data)
            return front_data


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if not self.list:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue.""" 
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? >>> we can use insert func """
        self.list.insert(0, item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if not self.list:
            return None
        else:
            return self.list[-1]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? >>> we can access the front of the queue with arr[index]"""
        if not self.list:
            raise ValueError('The queue is empty')
        else:
            return self.list.pop()


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
