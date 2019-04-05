#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z] >> check ascii decoding
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    power = 0
    hex_offset = 87
    powered_arr = []
    letter_value = string.ascii_lowercase
    digits = digits.lower()
    # reverse iteration of the input
    for index in range(len(digits)-1, -1, -1):
        value = digits[index]
        if value in letter_value:
            # translating to hex value
            bit = ord(value) - hex_offset
        elif value.isnumeric(): 
            bit = int(value)    
        else:
            print("error")
            raise ValueError('Error! Please enter base between 2-36')
        # key formula
        powered_bit = bit * (base ** power)
        power += 1
        powered_arr.append(powered_bit)
        base_to_decimal = sum(powered_arr)
    return base_to_decimal


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    bit = 0
    hex_offset = 87
    encoded_base10 = ''
    # loop until the result of 
    while number != 0:  
        bit = number % base
        number = number // base
        if base < 2 or base > 36:
            raise ValueError('Error! Please enter base between 2-36')
        elif bit > 9:
            # translating to hex value and adding to final string
            encoded_base10 += str(chr(bit + hex_offset))
        else:
            encoded_base10 += str(bit)
    # returning reversed string
    return encoded_base10[::-1]
  

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    if base1 == base2:
        return digits
    else:
        decoded_digits = decode(digits, base1)
        return encode(decoded_digits, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
