#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """ Check if the input is palindrome using iterative method """
    # TODO1: fix the ValueError
    # TODO2: edge case input has whitespace and puncutation
        # if text !== str:
        #         raise ValueError('Please input a string')
        # else:
        #         return text.lower()
    text = text.lower()
    text = ''.join(e for e in text if e.isalnum())
#     print(text)
#     TODO3: find to work this line out
#     clean_text = str.maketrans(string.ascii_lowercase, string.ascii_uppercase, string.whitespace + string.punctuation)
#     this part works dont touch
    reversed_text = text[::-1]
    if reversed_text == text:
        print('palindrome')
        return True    
    else:
        print('not palindrome')
        return False

            


def is_palindrome_recursive(text, left=None, right=None):
    """ Check if the input is palindrome using recursive method """
    if left == None and right == None:
        left = 0
        right = len(text) - 1

    if left >= right:
        return True
    elif text[left] != text[right]:
        return False
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
