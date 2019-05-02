#!python
from hashtable import HashTable
class Set(object):

    def __init__(self, elements=None):
        self.hashtable = HashTable()
        self.size = 0
        

    def contains(self, element):
        """Returns a boolean indicating whether element is in this set"""
        #TODO: write test
        if not self.hashtable:
            raise ValueError('Empty Hashtable')
        else:
            self.hashtable.contains(element)

    def add(self, element):
        """Adds element to this set, if not present already"""
        pass
    
    def remove(self, element):
        """Removes element from this set, if present, or else raise KeyError"""
        pass

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


    
