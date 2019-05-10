#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """return the index of a wanted item implementing linear search"""
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """return the index of a wanted item implementing linear recursive search"""
    # PSEUDOCODE for SPD activity:

    # check for base cases:
    # 1. if array is empty
    # 2. if the index is greated than the length
    # 3. entered index is what we are looking for >> return the index
    # if none of the above call the func recursively
    
    # base case1 array is empty
    if len(array) == 0:
        return None
    # base case2 
    elif index >= len(array):
        return None
    # base case3 initial index is a position of what we are looking for
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)



def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """return the index of a wanted item implementing binary iterative search"""
    # declaring left and right edges of the array
    left = 0
    right = len(array) -1

    while left <= right:
        # declaring midpoint index
        mid_index = (left + right) // 2
        
        if array[left] == item:
            return left
        # check if item in the midpoint is what we need
        elif array[mid_index] == item:
            return mid_index
        # if midpoint item is greater than wanted item, shift midpoint
        elif array[mid_index] < item:
            left = mid_index + 1
        else:
            right = mid_index - 1

 
    

def binary_search_recursive(array, item, left=None, right=None):
    """return the index of a wanted item implementing binary recursive search"""
    # declaring left and right edges of the array
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    elif left == None or right == None:
        raise ValueError("Set value for left and right")

    # declaring midpoint index
    mid_index = (left + right) // 2
    if left > right:
        return None
    elif array[mid_index] == item:
        return mid_index
    elif array[mid_index] > item:
        return binary_search_recursive(array, item, left, mid_index - 1)
    else:
        return binary_search_recursive(array, item, mid_index + 1, right)

    
