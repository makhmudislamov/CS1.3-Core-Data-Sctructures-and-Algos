#!python

from st import Set
import unittest

class SetTest(unittest.TestCase):
    pass

    def test_add(self, element):
        """Adds element to this set, if not present already"""
        pass
    
    def test_remove(self, element):
        """Removes element from this set, if present, or else raise KeyError"""
        pass

    def test_union(self, other_set):
        """Returns a new set that is the union of this set and other_set"""
        pass

    def test_intersection(self, other_set):
        """Returns a new set that is the intersection of this set and other_set"""
        pass
    
    def test_difference(self, other_set):
        """Returns a new set that is the difference of this set and other_set"""
        pass
    
    def test_is_subset(self, other_set):
        """Returns a boolean indicating whether other_set is a subset of this set"""
        pass


if __name__ == '__main__':
    # unittest.main()
    pass
