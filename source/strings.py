#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    matches = find_index(text, pattern)

    if len(pattern) == 0:
        return True
    elif len(pattern) > len(text):
        return False
    elif matches != None:
        return True
    else: 
        return False



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    # if len(pattern) == 0:
    #     return False
    # for i in range(len(text) - len(pattern) + 1):
    #     # checking the first index to pattern str
    #     if text[i] == pattern[0]:             
    #         is_match = True
    #         # Check if the indices match pattern
    #         for j in range(1, len(pattern)):  
    #            if text[i + j] != pattern[j]:  
    #                is_match = False
    #                i += 1
    #                break
    #         if is_match == True:         
    #             return i
    # return None

    matches = find_all_indexes(text, pattern)
    if len(matches) > 0:
        return matches[0]

    return None




def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []
    pattern_len = len(pattern)
    if pattern_len == 0:     
        for i in range(len(text)):
            indexes.append(i)
        return indexes
    for i in range(len(text) - pattern_len + 1):
        is_match = True
        for j in range(pattern_len):
            if pattern[j] != text[i + j]:
                is_match = False
        if is_match:
            indexes.append(i)
    return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
