import unittest

test = unittest.TestCase()


def info():
    print("Sum of Two Integers")
    print("Compute the sum of two integers without using the + and - operators")
    print('\t50, 1 -> 51')
    print('\t7, 6 -> 13')
    print('\t-5, 5 -> 0')
    print('\t-5, -5 -> -10')


def _invalid_number_to_bin(num, cache=None):  # not valid solution because uses - and +
    negative = num < 0
    num = abs(num)
    if cache is None:
        cache = {}
    power = 1
    if power not in cache:
        cache[0] = 1
        cache[1] = 2
    while cache[power] < num:
        power += 1
        if power not in cache:
            cache[power] = 2 ** power
    # I could use log2 to compute the power, but I wouldn't have a cache using this approach, and this way is faster
    binary_length = power
    binary_number = [0] * binary_length
    while num > 0 and power >= 0:
        if num >= cache[power]:
            binary_number[power] = -1 if negative else 1
            num -= cache[power]
        power -= 1
    return binary_number


def number_to_bin(num):
    num = abs(num)
    binary_number = []
    while num > 0:
        binary_number.append(1 if num & 1 > 0 else 0)
        num = num >> 1
    return binary_number


def sum_bit(a_bit, b_bit, carry=0):
    if a_bit == 0 and b_bit == 0:
        return 0, max(0, carry)
    elif (a_bit == 1 and b_bit == 0) or (a_bit == 0 and b_bit == 1):
        return 1, max(0, carry)
    else:  # a_bit==1 and b_bit == 1
        return 0, 1  # don't need max, the result is always 1


def sum_bin(a_bin, b_bin):
    ab_max_length = max(len(a_bin), len(b_bin))
    ab_bin = [0] * ab_max_length
    ab_bin.append(0)  # to avoid adding 1 to max_length
    ab_max_length = len(ab_bin)
    carry = 0
    for i in range(ab_max_length):
        a_bit = 0
        b_bit = 0
        if i < len(a_bin):
            a_bit = a_bin[i]
        if i < len(b_bin):
            b_bit = b_bin[i]
        ab_bit, carry = sum_bit(a_bit, b_bit, carry)
        if carry > 0:
            ab_bit, carry = sum_bit(ab_bit, carry)
        ab_bin[i] = ab_bit

    return ab_bin


def diff_bit(a_bit, b_bit, borrow=0):
    if a_bit == 0 and b_bit == 0:
        return 0, max(0, borrow)
    elif a_bit == 1 and b_bit == 0:
        return 1, max(0, borrow)
    elif a_bit == 0 and b_bit == 1:
        return 1, 1  # don't need max, the result is always 1
    else:  # a_bit==1 and b_bit == 1
        return 0, max(0, borrow)


def diff_bin(a_bin, b_bin):
    ab_max_length = max(len(a_bin), len(b_bin))
    ab_bin = [0] * ab_max_length
    borrow = 0
    for i in range(ab_max_length):
        a_bit = 0
        b_bit = 0
        if i < len(a_bin):
            a_bit = a_bin[i]
        if i < len(b_bin):
            b_bit = b_bin[i]
        ab_bit, borrow = sum_bit(a_bit, b_bit, borrow)
        if borrow > 0:
            ab_bit, borrow = sum_bit(ab_bit, borrow)
        ab_bin[i] = ab_bit

    return ab_bin


def bin_to_number(ab_bin):
    num = 0
    for i, bit in enumerate(ab_bin):
        num = num | bit << i
    return num


def run(a, b):
    # Time complexity: # O(log(n)), where n is the number
    # Space complexity: O(log(n))
    a_bin = number_to_bin(a)
    b_bin = number_to_bin(b)

    if a >= 0 and b >= 0:
        ab_bin = sum_bin(a_bin, b_bin)
        negative_signal = False
    elif (a > 0 and b < 0) or (a < 0 and b > 0):
        if abs(a) < abs(b):
            tmp = a_bin
            a_bin = b_bin
            b_bin = tmp
        ab_bin = diff_bin(a_bin, b_bin)
        negative_signal = (a < 0 and abs(a) > abs(b)) or (b < 0 and abs(b) > abs(a))
    else:  # a<0 and b<0
        ab_bin = sum_bin(a_bin, b_bin)
        negative_signal = True
    ab = bin_to_number(ab_bin)
    if negative_signal:
        return -ab
    else:
        return ab


def main():
    info()
    print(number_to_bin(45))
    print(number_to_bin(19))
    test.assertEqual(51, run(50, 1))
    test.assertEqual(13, run(7, 6))
    test.assertEqual(0, run(-5, 5))
    test.assertEqual(-10, run(-5, -5))
    test.assertEqual(45, run(50, -5))
    test.assertEqual(-45, run(5, -50))
    test.assertEqual(-45, run(-50, 5))
    test.assertEqual(45, run(-5, 50))
    test.assertEqual(62, run(31, 31))
    print('All tests passed')


if __name__ == "__main__":
    main()
