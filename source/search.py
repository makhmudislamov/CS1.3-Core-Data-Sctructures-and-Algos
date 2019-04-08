#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    
    # PSEUDOCODE
    # if first item is what Im looking for
        # return its position
    # else, iterate throught the rest of the item:
        # if item is found
            # return its positon
        # else
            # return not found
    if len(array) == 0:
        return None
    if array[index] == item:
        return index

    for index in array:
        if array[index] == item:
            return index
        else:
            return None
    # EDGE CASE:
    # if array is empty
        # return not found and print "array is empty"


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):

    # declaring left and right edges of the array
    left = 0
    right = len(array) -1

    while left <= right:
        # declaring midpoint index
        mid_index = (left + right) // 2
        # check if item in the midpoint is what we need
        if array[mid_index] == item:
            return mid_index
        # if midpoint item is greater than wanted item, shift midpoint
        elif array[mid_index] > item:
            left = mid_index + 1
        else:
            right = mid_index - 1


def binary_search_recursive(array, item, left=None, right=None):
    # declaring left and right edges of the array
    left = 0
    right = len(array) - 1

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

    
