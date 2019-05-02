#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.hashtable = HashTable()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)


    def contains(self, element):
        """Returns a boolean indicating whether element is in this set
        Time Complexity: O(1) >> hashtable lookup is a const operation on average case
        Space Complexity: O(1) >> accessing data
        """
        #TODO: write test
        if not self.hashtable:
            raise ValueError('Empty Hashtable')
        else:
            return self.hashtable.contains(element)

    def add(self, element):
        """Adds element to this set, if not present already
        Time Complexity: O(1) >> set method of hastable is const time
        Space Complexity: O(1) >> one new space is created for new element
        """
        if self.contains(element) is True:
            return element
        else:
            self.hashtable.set(element, None)
            self.size += 1
    
    def remove(self, element):
        """Removes element from this set, if present, or else raise KeyError
        Time Complexity: O(1) >> delete method of hastable is const time
        Space Complexity: O(1) >> removing the element is const time, no need to traverse
        """
        if self.contains(element) is False:
            raise KeyError('Element does not exist')
        else:
            self.hashtable.delete(element)
            self.size -= 1

    def union(self, other_set):
        """Returns a new set that is the union of this set and other_set"""
        pass

    def intersection(self, other_set):
        """Returns a new set that is the intersection of this set and other_set"""
        pass
    
    def difference(self, other_set):
        """Returns a new set that is the difference of this set and other_set"""
        pass
    
    def is_subset(self, other_set):
        """Returns a boolean indicating whether other_set is a subset of this set"""
        pass


if __name__ == '__main__':
    pass


    
