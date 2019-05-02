#!python

from my_set import Set
import unittest

class SetTest(unittest.TestCase):
    
    def test_init(self):
        # s = Set()
        # assert s
        pass

    def test_contains(self):
        s = Set(['A', 'B', 'C'])
        assert s.size == 3
        assert s.contains('A') is True
        assert s.contains('B') 
        assert s.contains('C') 
        assert s.contains('D') is False



    def test_add(self):
        """Adds element to this set, if not present already"""
        s = Set([13])
        assert s.size == 1  
        assert s.contains(13) is True
        

    
    def test_remove(self):
        """Removes element from this set, if present, or else raise KeyError"""
        s = Set([12, 13, 14])
        assert s.size == 3
        s.remove(12)
        assert s.size == 2
        assert s.contains(12) is False  


    def test_union(self):
        """Returns a new set that is the union of this set and other_set"""
        pass

    def test_intersection(self):
        """Returns a new set that is the intersection of this set and other_set"""
        pass
    
    def test_difference(self):
        """Returns a new set that is the difference of this set and other_set"""
        pass
    
    def test_is_subset(self):
        """Returns a boolean indicating whether other_set is a subset of this set"""
        pass


if __name__ == '__main__':
    unittest.main()
    # pass
