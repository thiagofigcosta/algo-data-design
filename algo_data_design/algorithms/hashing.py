def hash_triple(number):
    number = ((number >> 16) ^ number) * 0x45d9f3b
    number = ((number >> 16) ^ number) * 0x45d9f3b
    number = (number >> 16) ^ number
    return number


def hash_multiplication(number):
    number = (number ^ 61) ^ (number >> 16)
    number = number + (number << 3)
    number = number ^ (number >> 4)
    number = number * 0x27d4eb2d
    number = number ^ (number >> 15)
    return number


def hash_64_bits(number):
    number = (~number) + (number << 21)
    number = number ^ (number >> 24)
    number = (number + (number << 3)) + (number << 8)
    number = number ^ (number >> 14)
    number = (number + (number << 2)) + (number << 4)
    number = number ^ (number >> 28)
    number = number + (number << 31)
    return number


def hash_7_shifts(number):
    number -= (number << 6)
    number ^= (number >> 17)
    number -= (number << 9)
    number ^= (number << 4)
    number -= (number << 3)
    number ^= (number << 10)
    number ^= (number >> 15)
    return number


def hash_6_shifts(number):
    number = (number + 0x7ed55d16) + (number << 12)
    number = (number ^ 0xc761c23c) ^ (number >> 19)
    number = (number + 0x165667b1) + (number << 5)
    number = (number + 0xd3a2646c) ^ (number << 9)
    number = (number + 0xfd7046c5) + (number << 3)
    number = (number ^ 0xb55a4f09) ^ (number >> 16)
    return number


def hash_6_shifts_low_bits(number):
    number ^= (number >> 10)
    number += (number << 3)
    number ^= (number >> 6)
    number += ~(number << 11)
    number ^= (number >> 16)
    return number


def hash_5_shifts(number):
    number = (number + 0x479ab41d) + (number << 8)
    number = (number ^ 0xe4aa10ce) ^ (number >> 5)
    number = (number + 0x9942f0a6) - (number << 14)
    number = (number ^ 0x5aedd67d) ^ (number >> 3)
    number = (number + 0x17bea992) + (number << 7)
    return number


def hash_python(number):
    number = hash(number)
    return number
